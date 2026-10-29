<?php

declare(strict_types=1);

namespace Crawlora\Bo3;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'bo3';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 28;
    public const OPERATION_IDS = ["bo3-economy-baseline", "bo3-forum", "bo3-forum-categories", "bo3-match", "bo3-match-games", "bo3-match-history", "bo3-match-players", "bo3-news-categories", "bo3-news-feed", "bo3-player", "bo3-player-leaderboard", "bo3-player-recent-matches", "bo3-player-stats", "bo3-records", "bo3-team", "bo3-team-prize-money", "bo3-team-ranking-dates", "bo3-team-rankings", "bo3-team-recent-matches", "bo3-team-stats", "bo3-tournament", "bo3-tournament-map-pool", "bo3-tournament-mvps", "bo3-tournament-squads", "bo3-tournament-stages", "bo3-tournaments", "bo3-transfers", "bo3-valorant-leaderboard"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"bo3-economy-baseline": {"bodyParam": null, "bodyRequired": false, "id": "bo3-economy-baseline", "method": "GET", "params": [], "path": "/bo3/economy-baseline", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bo3-forum": {"bodyParam": null, "bodyRequired": false, "id": "bo3-forum", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Forum category id from bo3-forum-categories, for example 4", "in": "query", "minimum": 1, "name": "category", "type": "integer"}, {"description": "Order; one of activity, newest, comments, rating; defaults to activity", "enum": ["activity", "newest", "comments", "rating"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/forum", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"enum": ["activity", "newest", "comments", "rating"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-forum-categories": {"bodyParam": null, "bodyRequired": false, "id": "bo3-forum-categories", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/forum-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-match": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match", "method": "GET", "params": [{"description": "Match slug from bo3-match-history, for example vitality-vs-natus-vincere-27-10-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}], "path": "/bo3/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-match-games": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-games", "method": "GET", "params": [{"description": "Numeric BO3 match id (the id of a bo3-match-history row)", "in": "query", "minimum": 1, "name": "match_id", "required": true, "type": "integer", "x-example": 132243}], "path": "/bo3/match-games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-match-history": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-history", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Match status; one of finished, defwin, upcoming, current, canceled, postponed; defaults to finished and defwin together", "enum": ["finished", "defwin", "upcoming", "current", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"description": "Tournament tier; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "First start day, YYYY-MM-DD (UTC, inclusive)", "in": "query", "name": "from", "type": "string", "x-example": "2026-10-01"}, {"description": "Last start day, YYYY-MM-DD (UTC, inclusive)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-27"}, {"description": "Order by start time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/match-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"enum": ["finished", "defwin", "upcoming", "current", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-match-players": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-players", "method": "GET", "params": [{"description": "Match slug from bo3-match-history, for example vitality-vs-natus-vincere-27-10-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}], "path": "/bo3/match-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-news-categories": {"bodyParam": null, "bodyRequired": false, "id": "bo3-news-categories", "method": "GET", "params": [], "path": "/bo3/news-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bo3-news-feed": {"bodyParam": null, "bodyRequired": false, "id": "bo3-news-feed", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb, games (general gaming news); defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb", "games"], "in": "query", "name": "game", "type": "string"}, {"description": "Editorial section; one of news, article, wiki, predictions, reviews (game reviews, game=games only); defaults to news", "enum": ["news", "article", "wiki", "predictions", "reviews"], "in": "query", "name": "section", "type": "string"}, {"description": "Tag slug such as team-liquid or pgl-masters-bucharest-2026 (team, player, tournament or topic tag); an unknown tag returns an empty list", "in": "query", "name": "tag", "type": "string", "x-example": "team-liquid"}, {"description": "Language of the items; one of en, ru, pt, es, de, fr, tr, pl, id, vi, ja, ko, ua, ms, tl, da; defaults to en", "enum": ["en", "ru", "pt", "es", "de", "fr", "tr", "pl", "id", "vi", "ja", "ko", "ua", "ms", "tl", "da"], "in": "query", "name": "locale", "type": "string"}, {"description": "Category id from bo3-news-categories, for example 38 (Predictions)", "in": "query", "minimum": 1, "name": "category", "type": "integer"}, {"description": "Order by publish time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/news-feed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb", "games"], "in": "query", "name": "game", "type": "string"}, {"enum": ["news", "article", "wiki", "predictions", "reviews"], "in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "tag", "type": "string"}, {"enum": ["en", "ru", "pt", "es", "de", "fr", "tr", "pl", "id", "vi", "ja", "ko", "ua", "ms", "tl", "da"], "in": "query", "name": "locale", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Game the player must belong to; one of cs2, valorant, lol, dota2, r6siege, mlbb", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-player-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-leaderboard", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Tournament tier of the games counted; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "Stat to rank by; one of rating, kd, kills, damage, assists, headshots, games, rounds; defaults to rating", "enum": ["rating", "kd", "kills", "damage", "assists", "headshots", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"description": "Direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/player-leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["rating", "kd", "kills", "damage", "assists", "headshots", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player-recent-matches": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-recent-matches", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Opposing team slug, for example mouz-cs2", "in": "query", "name": "opponent", "type": "string"}, {"description": "Tournament slug from bo3-tournaments", "in": "query", "name": "tournament", "type": "string"}, {"default": 10, "description": "Newest matches to return, 1 to 30, default 10", "in": "query", "maximum": 30, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/player-recent-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player-stats": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-stats", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Statistics view; one of general, maps, accuracy; defaults to general", "enum": ["general", "maps", "accuracy"], "in": "query", "name": "kind", "type": "string"}, {"description": "First day, YYYY-MM-DD; defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD; defaults to today (UTC)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}], "path": "/bo3/player-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["general", "maps", "accuracy"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-records": {"bodyParam": null, "bodyRequired": false, "id": "bo3-records", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); unscoped default is six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); unscoped default is today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Record type such as game_player_headshots or game_round_player_clutch; the types present are listed in the response", "in": "query", "name": "record_type", "type": "string"}, {"description": "Match slug to scope the records to one match", "in": "query", "name": "match", "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}, {"description": "Tournament slug to scope the records to one tournament", "in": "query", "name": "tournament", "type": "string", "x-example": "pgl-masters-bucharest-2026"}, {"description": "Team slug to scope the records to one team", "in": "query", "name": "team", "type": "string", "x-example": "vitality"}, {"description": "Player slug to scope the records to one player", "in": "query", "name": "player", "type": "string", "x-example": "donk"}, {"description": "Order by game time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"in": "query", "name": "record_type", "type": "string"}, {"in": "query", "name": "match", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "team", "type": "string"}, {"in": "query", "name": "player", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Game the team must belong to; one of cs2, valorant, lol, dota2, r6siege, mlbb", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-team-prize-money": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-prize-money", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/team-prize-money", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-ranking-dates": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-ranking-dates", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/team-ranking-dates", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-team-rankings": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-rankings", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Region label for the game as listed by bo3-team-ranking-dates, for example Europe; omit for worldwide", "in": "query", "name": "region", "type": "string"}, {"description": "Ranking day, YYYY-MM-DD; defaults to the latest", "in": "query", "name": "date", "type": "string", "x-example": "2026-10-05"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 30", "in": "query", "maximum": 100, "minimum": 1, "name": "per_page", "type": "integer"}], "path": "/bo3/team-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "per_page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-recent-matches": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-recent-matches", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Opposing team slug for head-to-head matches, for example natus-vincere", "in": "query", "name": "opponent", "type": "string"}, {"description": "Tournament slug from bo3-tournaments", "in": "query", "name": "tournament", "type": "string"}, {"default": 10, "description": "Newest matches to return, 1 to 30, default 10", "in": "query", "maximum": 30, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/team-recent-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-stats": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-stats", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Statistics view; one of general, advanced, accuracy, economy, map-pool; defaults to general", "enum": ["general", "advanced", "accuracy", "economy", "map-pool"], "in": "query", "name": "kind", "type": "string"}, {"description": "First day, YYYY-MM-DD; defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD; defaults to today (UTC)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}], "path": "/bo3/team-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["general", "advanced", "accuracy", "economy", "map-pool"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament", "method": "GET", "params": [{"description": "Tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}, {"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/tournament", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-map-pool": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-map-pool", "method": "GET", "params": [{"description": "CS2 tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-map-pool", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-mvps": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-mvps", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to every game", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/tournament-mvps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-squads": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-squads", "method": "GET", "params": [{"description": "CS2 tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-squads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-stages": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-stages", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-stages", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournaments", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament status; one of current, upcoming, finished, canceled, postponed", "enum": ["current", "upcoming", "finished", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"description": "Tournament tier; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "Event type; one of lan, online", "enum": ["lan", "online"], "in": "query", "name": "event_type", "type": "string"}, {"description": "Order; one of newest, oldest, prize; defaults to newest", "enum": ["newest", "oldest", "prize"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"enum": ["current", "upcoming", "finished", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["lan", "online"], "in": "query", "name": "event_type", "type": "string"}, {"enum": ["newest", "oldest", "prize"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-transfers": {"bodyParam": null, "bodyRequired": false, "id": "bo3-transfers", "method": "GET", "params": [{"description": "BO3 team id; transfers into or out of this team", "in": "query", "minimum": 1, "name": "team_id", "type": "integer"}, {"description": "BO3 player id; this person's transfers", "in": "query", "minimum": 1, "name": "player_id", "type": "integer"}, {"description": "Transfer action; one of join, change, leave", "enum": ["join", "change", "leave"], "in": "query", "name": "action", "type": "string"}, {"description": "Role; one of player, coach", "enum": ["player", "coach"], "in": "query", "name": "role", "type": "string"}, {"description": "Order by date; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "type": "integer"}, {"in": "query", "name": "player_id", "type": "integer"}, {"enum": ["join", "change", "leave"], "in": "query", "name": "action", "type": "string"}, {"enum": ["player", "coach"], "in": "query", "name": "role", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-valorant-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "bo3-valorant-leaderboard", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Stat to rank by; one of acs, kills, deaths, damage, assists, first_kills, clutches, first_duels, games, rounds; defaults to acs", "enum": ["acs", "kills", "deaths", "damage", "assists", "first_kills", "clutches", "first_duels", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"description": "Direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/valorant-leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["acs", "kills", "deaths", "damage", "assists", "first_kills", "clutches", "first_duels", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-bo3-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function economy_baseline(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-economy-baseline", $params, $responseType);
    }
    public function forum(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-forum", $params, $responseType);
    }
    public function forum_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-forum-categories", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-match", $params, $responseType);
    }
    public function match_games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-match-games", $params, $responseType);
    }
    public function match_history(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-match-history", $params, $responseType);
    }
    public function match_players(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-match-players", $params, $responseType);
    }
    public function news_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-news-categories", $params, $responseType);
    }
    public function news_feed(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-news-feed", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-player", $params, $responseType);
    }
    public function player_leaderboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-player-leaderboard", $params, $responseType);
    }
    public function player_recent_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-player-recent-matches", $params, $responseType);
    }
    public function player_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-player-stats", $params, $responseType);
    }
    public function records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-records", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team", $params, $responseType);
    }
    public function team_prize_money(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team-prize-money", $params, $responseType);
    }
    public function team_ranking_dates(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team-ranking-dates", $params, $responseType);
    }
    public function team_rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team-rankings", $params, $responseType);
    }
    public function team_recent_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team-recent-matches", $params, $responseType);
    }
    public function team_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-team-stats", $params, $responseType);
    }
    public function tournament(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournament", $params, $responseType);
    }
    public function tournament_map_pool(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournament-map-pool", $params, $responseType);
    }
    public function tournament_mvps(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournament-mvps", $params, $responseType);
    }
    public function tournament_squads(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournament-squads", $params, $responseType);
    }
    public function tournament_stages(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournament-stages", $params, $responseType);
    }
    public function tournaments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-tournaments", $params, $responseType);
    }
    public function transfers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-transfers", $params, $responseType);
    }
    public function valorant_leaderboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("bo3-valorant-leaderboard", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
