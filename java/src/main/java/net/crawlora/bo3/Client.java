package net.crawlora.bo3;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the BO3.gg endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 28;
    public static final List<String> OPERATION_IDS = List.of(
            "bo3-economy-baseline",
            "bo3-forum",
            "bo3-forum-categories",
            "bo3-match",
            "bo3-match-games",
            "bo3-match-history",
            "bo3-match-players",
            "bo3-news-categories",
            "bo3-news-feed",
            "bo3-player",
            "bo3-player-leaderboard",
            "bo3-player-recent-matches",
            "bo3-player-stats",
            "bo3-records",
            "bo3-team",
            "bo3-team-prize-money",
            "bo3-team-ranking-dates",
            "bo3-team-rankings",
            "bo3-team-recent-matches",
            "bo3-team-stats",
            "bo3-tournament",
            "bo3-tournament-map-pool",
            "bo3-tournament-mvps",
            "bo3-tournament-squads",
            "bo3-tournament-stages",
            "bo3-tournaments",
            "bo3-transfers",
            "bo3-valorant-leaderboard"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("bo3-economy-baseline", new Operation("bo3-economy-baseline", "GET", "/bo3/economy-baseline", Map.of(), List.of("application/json")));
        operations.put("bo3-forum", new Operation("bo3-forum", "GET", "/bo3/forum", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("category", new Param("category", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("activity", "newest", "comments", "rating"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-forum-categories", new Operation("bo3-forum-categories", "GET", "/bo3/forum-categories", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv"))), List.of("application/json")));
        operations.put("bo3-match", new Operation("bo3-match", "GET", "/bo3/match", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-match-games", new Operation("bo3-match-games", "GET", "/bo3/match-games", Map.ofEntries(Map.entry("match_id", new Param("match_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-match-history", new Operation("bo3-match-history", "GET", "/bo3/match-history", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("finished", "defwin", "upcoming", "current", "canceled", "postponed"), "csv")), Map.entry("tier", new Param("tier", "query", false, "string", List.of("s", "a", "b", "c", "d"), "csv")), Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("newest", "oldest"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-match-players", new Operation("bo3-match-players", "GET", "/bo3/match-players", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-news-categories", new Operation("bo3-news-categories", "GET", "/bo3/news-categories", Map.of(), List.of("application/json")));
        operations.put("bo3-news-feed", new Operation("bo3-news-feed", "GET", "/bo3/news-feed", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb", "games"), "csv")), Map.entry("section", new Param("section", "query", false, "string", List.of("news", "article", "wiki", "predictions", "reviews"), "csv")), Map.entry("tag", new Param("tag", "query", false, "string", List.of(), "csv")), Map.entry("locale", new Param("locale", "query", false, "string", List.of("en", "ru", "pt", "es", "de", "fr", "tr", "pl", "id", "vi", "ja", "ko", "ua", "ms", "tl", "da"), "csv")), Map.entry("category", new Param("category", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("newest", "oldest"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-player", new Operation("bo3-player", "GET", "/bo3/player", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv"))), List.of("application/json")));
        operations.put("bo3-player-leaderboard", new Operation("bo3-player-leaderboard", "GET", "/bo3/player-leaderboard", Map.ofEntries(Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("tier", new Param("tier", "query", false, "string", List.of("s", "a", "b", "c", "d"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("rating", "kd", "kills", "damage", "assists", "headshots", "games", "rounds"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("desc", "asc"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-player-recent-matches", new Operation("bo3-player-recent-matches", "GET", "/bo3/player-recent-matches", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("opponent", new Param("opponent", "query", false, "string", List.of(), "csv")), Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-player-stats", new Operation("bo3-player-stats", "GET", "/bo3/player-stats", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("kind", new Param("kind", "query", false, "string", List.of("general", "maps", "accuracy"), "csv")), Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-records", new Operation("bo3-records", "GET", "/bo3/records", Map.ofEntries(Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("record_type", new Param("record_type", "query", false, "string", List.of(), "csv")), Map.entry("match", new Param("match", "query", false, "string", List.of(), "csv")), Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("team", new Param("team", "query", false, "string", List.of(), "csv")), Map.entry("player", new Param("player", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("newest", "oldest"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-team", new Operation("bo3-team", "GET", "/bo3/team", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv"))), List.of("application/json")));
        operations.put("bo3-team-prize-money", new Operation("bo3-team-prize-money", "GET", "/bo3/team-prize-money", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-team-ranking-dates", new Operation("bo3-team-ranking-dates", "GET", "/bo3/team-ranking-dates", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv"))), List.of("application/json")));
        operations.put("bo3-team-rankings", new Operation("bo3-team-rankings", "GET", "/bo3/team-rankings", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("per_page", new Param("per_page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-team-recent-matches", new Operation("bo3-team-recent-matches", "GET", "/bo3/team-recent-matches", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("opponent", new Param("opponent", "query", false, "string", List.of(), "csv")), Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-team-stats", new Operation("bo3-team-stats", "GET", "/bo3/team-stats", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("kind", new Param("kind", "query", false, "string", List.of("general", "advanced", "accuracy", "economy", "map-pool"), "csv")), Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-tournament", new Operation("bo3-tournament", "GET", "/bo3/tournament", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv"))), List.of("application/json")));
        operations.put("bo3-tournament-map-pool", new Operation("bo3-tournament-map-pool", "GET", "/bo3/tournament-map-pool", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-tournament-mvps", new Operation("bo3-tournament-mvps", "GET", "/bo3/tournament-mvps", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-tournament-squads", new Operation("bo3-tournament-squads", "GET", "/bo3/tournament-squads", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-tournament-stages", new Operation("bo3-tournament-stages", "GET", "/bo3/tournament-stages", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-tournaments", new Operation("bo3-tournaments", "GET", "/bo3/tournaments", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("current", "upcoming", "finished", "canceled", "postponed"), "csv")), Map.entry("tier", new Param("tier", "query", false, "string", List.of("s", "a", "b", "c", "d"), "csv")), Map.entry("event_type", new Param("event_type", "query", false, "string", List.of("lan", "online"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("newest", "oldest", "prize"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-transfers", new Operation("bo3-transfers", "GET", "/bo3/transfers", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv")), Map.entry("player_id", new Param("player_id", "query", false, "integer", List.of(), "csv")), Map.entry("action", new Param("action", "query", false, "string", List.of("join", "change", "leave"), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of("player", "coach"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("newest", "oldest"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bo3-valorant-leaderboard", new Operation("bo3-valorant-leaderboard", "GET", "/bo3/valorant-leaderboard", Map.ofEntries(Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("acs", "kills", "deaths", "damage", "assists", "first_kills", "clutches", "first_duels", "games", "rounds"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("desc", "asc"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown BO3.gg operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object economyBaseline(Map<String, ?> params) { return request("bo3-economy-baseline", params); }
    public Object forum(Map<String, ?> params) { return request("bo3-forum", params); }
    public Object forumCategories(Map<String, ?> params) { return request("bo3-forum-categories", params); }
    public Object match(Map<String, ?> params) { return request("bo3-match", params); }
    public Object matchGames(Map<String, ?> params) { return request("bo3-match-games", params); }
    public Object matchHistory(Map<String, ?> params) { return request("bo3-match-history", params); }
    public Object matchPlayers(Map<String, ?> params) { return request("bo3-match-players", params); }
    public Object newsCategories(Map<String, ?> params) { return request("bo3-news-categories", params); }
    public Object newsFeed(Map<String, ?> params) { return request("bo3-news-feed", params); }
    public Object player(Map<String, ?> params) { return request("bo3-player", params); }
    public Object playerLeaderboard(Map<String, ?> params) { return request("bo3-player-leaderboard", params); }
    public Object playerRecentMatches(Map<String, ?> params) { return request("bo3-player-recent-matches", params); }
    public Object playerStats(Map<String, ?> params) { return request("bo3-player-stats", params); }
    public Object records(Map<String, ?> params) { return request("bo3-records", params); }
    public Object team(Map<String, ?> params) { return request("bo3-team", params); }
    public Object teamPrizeMoney(Map<String, ?> params) { return request("bo3-team-prize-money", params); }
    public Object teamRankingDates(Map<String, ?> params) { return request("bo3-team-ranking-dates", params); }
    public Object teamRankings(Map<String, ?> params) { return request("bo3-team-rankings", params); }
    public Object teamRecentMatches(Map<String, ?> params) { return request("bo3-team-recent-matches", params); }
    public Object teamStats(Map<String, ?> params) { return request("bo3-team-stats", params); }
    public Object tournament(Map<String, ?> params) { return request("bo3-tournament", params); }
    public Object tournamentMapPool(Map<String, ?> params) { return request("bo3-tournament-map-pool", params); }
    public Object tournamentMvps(Map<String, ?> params) { return request("bo3-tournament-mvps", params); }
    public Object tournamentSquads(Map<String, ?> params) { return request("bo3-tournament-squads", params); }
    public Object tournamentStages(Map<String, ?> params) { return request("bo3-tournament-stages", params); }
    public Object tournaments(Map<String, ?> params) { return request("bo3-tournaments", params); }
    public Object transfers(Map<String, ?> params) { return request("bo3-transfers", params); }
    public Object valorantLeaderboard(Map<String, ?> params) { return request("bo3-valorant-leaderboard", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
