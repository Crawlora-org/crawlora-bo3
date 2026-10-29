package net.crawlora.bo3;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(28, Client.OPERATION_IDS.size());
        assertEquals(List.of("bo3-economy-baseline", "bo3-forum", "bo3-forum-categories", "bo3-match", "bo3-match-games", "bo3-match-history", "bo3-match-players", "bo3-news-categories", "bo3-news-feed", "bo3-player", "bo3-player-leaderboard", "bo3-player-recent-matches", "bo3-player-stats", "bo3-records", "bo3-team", "bo3-team-prize-money", "bo3-team-ranking-dates", "bo3-team-rankings", "bo3-team-recent-matches", "bo3-team-stats", "bo3-tournament", "bo3-tournament-map-pool", "bo3-tournament-mvps", "bo3-tournament-squads", "bo3-tournament-stages", "bo3-tournaments", "bo3-transfers", "bo3-valorant-leaderboard"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("bo3-match", Map.ofEntries(Map.entry("slug", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            // This operation has no path parameters to encode.
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("match", Map.class).invoke(client, Map.ofEntries(Map.entry("slug", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("bo3-economy-baseline", Map.of()));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("bo3-match", Map.ofEntries(Map.entry("slug", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("bo3-match", Map.ofEntries(Map.entry("slug", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("bo3-forum", Map.ofEntries(Map.entry("game", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("bo3-match", Map.ofEntries(Map.entry("slug", "value &/one"))));
    }
}
