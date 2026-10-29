require "json"
require "net/http"
require "uri"

module Crawlora
  module Bo3
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"bo3-economy-baseline": {"bodyParam": null, "bodyRequired": false, "id": "bo3-economy-baseline", "method": "GET", "params": [], "path": "/bo3/economy-baseline", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bo3-forum": {"bodyParam": null, "bodyRequired": false, "id": "bo3-forum", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Forum category id from bo3-forum-categories, for example 4", "in": "query", "minimum": 1, "name": "category", "type": "integer"}, {"description": "Order; one of activity, newest, comments, rating; defaults to activity", "enum": ["activity", "newest", "comments", "rating"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/forum", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"enum": ["activity", "newest", "comments", "rating"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-forum-categories": {"bodyParam": null, "bodyRequired": false, "id": "bo3-forum-categories", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/forum-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-match": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match", "method": "GET", "params": [{"description": "Match slug from bo3-match-history, for example vitality-vs-natus-vincere-27-10-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}], "path": "/bo3/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-match-games": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-games", "method": "GET", "params": [{"description": "Numeric BO3 match id (the id of a bo3-match-history row)", "in": "query", "minimum": 1, "name": "match_id", "required": true, "type": "integer", "x-example": 132243}], "path": "/bo3/match-games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-match-history": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-history", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Match status; one of finished, defwin, upcoming, current, canceled, postponed; defaults to finished and defwin together", "enum": ["finished", "defwin", "upcoming", "current", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"description": "Tournament tier; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "First start day, YYYY-MM-DD (UTC, inclusive)", "in": "query", "name": "from", "type": "string", "x-example": "2026-10-01"}, {"description": "Last start day, YYYY-MM-DD (UTC, inclusive)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-27"}, {"description": "Order by start time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/match-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"enum": ["finished", "defwin", "upcoming", "current", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-match-players": {"bodyParam": null, "bodyRequired": false, "id": "bo3-match-players", "method": "GET", "params": [{"description": "Match slug from bo3-match-history, for example vitality-vs-natus-vincere-27-10-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}], "path": "/bo3/match-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-news-categories": {"bodyParam": null, "bodyRequired": false, "id": "bo3-news-categories", "method": "GET", "params": [], "path": "/bo3/news-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bo3-news-feed": {"bodyParam": null, "bodyRequired": false, "id": "bo3-news-feed", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb, games (general gaming news); defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb", "games"], "in": "query", "name": "game", "type": "string"}, {"description": "Editorial section; one of news, article, wiki, predictions, reviews (game reviews, game=games only); defaults to news", "enum": ["news", "article", "wiki", "predictions", "reviews"], "in": "query", "name": "section", "type": "string"}, {"description": "Tag slug such as team-liquid or pgl-masters-bucharest-2026 (team, player, tournament or topic tag); an unknown tag returns an empty list", "in": "query", "name": "tag", "type": "string", "x-example": "team-liquid"}, {"description": "Language of the items; one of en, ru, pt, es, de, fr, tr, pl, id, vi, ja, ko, ua, ms, tl, da; defaults to en", "enum": ["en", "ru", "pt", "es", "de", "fr", "tr", "pl", "id", "vi", "ja", "ko", "ua", "ms", "tl", "da"], "in": "query", "name": "locale", "type": "string"}, {"description": "Category id from bo3-news-categories, for example 38 (Predictions)", "in": "query", "minimum": 1, "name": "category", "type": "integer"}, {"description": "Order by publish time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/news-feed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb", "games"], "in": "query", "name": "game", "type": "string"}, {"enum": ["news", "article", "wiki", "predictions", "reviews"], "in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "tag", "type": "string"}, {"enum": ["en", "ru", "pt", "es", "de", "fr", "tr", "pl", "id", "vi", "ja", "ko", "ua", "ms", "tl", "da"], "in": "query", "name": "locale", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Game the player must belong to; one of cs2, valorant, lol, dota2, r6siege, mlbb", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-player-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-leaderboard", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Tournament tier of the games counted; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "Stat to rank by; one of rating, kd, kills, damage, assists, headshots, games, rounds; defaults to rating", "enum": ["rating", "kd", "kills", "damage", "assists", "headshots", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"description": "Direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/player-leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["rating", "kd", "kills", "damage", "assists", "headshots", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player-recent-matches": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-recent-matches", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Opposing team slug, for example mouz-cs2", "in": "query", "name": "opponent", "type": "string"}, {"description": "Tournament slug from bo3-tournaments", "in": "query", "name": "tournament", "type": "string"}, {"default": 10, "description": "Newest matches to return, 1 to 30, default 10", "in": "query", "maximum": 30, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/player-recent-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-player-stats": {"bodyParam": null, "bodyRequired": false, "id": "bo3-player-stats", "method": "GET", "params": [{"description": "Player slug, for example donk", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "donk"}, {"description": "Statistics view; one of general, maps, accuracy; defaults to general", "enum": ["general", "maps", "accuracy"], "in": "query", "name": "kind", "type": "string"}, {"description": "First day, YYYY-MM-DD; defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD; defaults to today (UTC)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}], "path": "/bo3/player-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["general", "maps", "accuracy"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-records": {"bodyParam": null, "bodyRequired": false, "id": "bo3-records", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); unscoped default is six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); unscoped default is today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Record type such as game_player_headshots or game_round_player_clutch; the types present are listed in the response", "in": "query", "name": "record_type", "type": "string"}, {"description": "Match slug to scope the records to one match", "in": "query", "name": "match", "type": "string", "x-example": "vitality-vs-natus-vincere-27-10-2026"}, {"description": "Tournament slug to scope the records to one tournament", "in": "query", "name": "tournament", "type": "string", "x-example": "pgl-masters-bucharest-2026"}, {"description": "Team slug to scope the records to one team", "in": "query", "name": "team", "type": "string", "x-example": "vitality"}, {"description": "Player slug to scope the records to one player", "in": "query", "name": "player", "type": "string", "x-example": "donk"}, {"description": "Order by game time; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"in": "query", "name": "record_type", "type": "string"}, {"in": "query", "name": "match", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "team", "type": "string"}, {"in": "query", "name": "player", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Game the team must belong to; one of cs2, valorant, lol, dota2, r6siege, mlbb", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-team-prize-money": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-prize-money", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/team-prize-money", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-ranking-dates": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-ranking-dates", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/team-ranking-dates", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-team-rankings": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-rankings", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Region label for the game as listed by bo3-team-ranking-dates, for example Europe; omit for worldwide", "in": "query", "name": "region", "type": "string"}, {"description": "Ranking day, YYYY-MM-DD; defaults to the latest", "in": "query", "name": "date", "type": "string", "x-example": "2026-10-05"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 30", "in": "query", "maximum": 100, "minimum": 1, "name": "per_page", "type": "integer"}], "path": "/bo3/team-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "per_page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-recent-matches": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-recent-matches", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Opposing team slug for head-to-head matches, for example natus-vincere", "in": "query", "name": "opponent", "type": "string"}, {"description": "Tournament slug from bo3-tournaments", "in": "query", "name": "tournament", "type": "string"}, {"default": 10, "description": "Newest matches to return, 1 to 30, default 10", "in": "query", "maximum": 30, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/team-recent-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-team-stats": {"bodyParam": null, "bodyRequired": false, "id": "bo3-team-stats", "method": "GET", "params": [{"description": "Team slug, for example vitality", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "vitality"}, {"description": "Statistics view; one of general, advanced, accuracy, economy, map-pool; defaults to general", "enum": ["general", "advanced", "accuracy", "economy", "map-pool"], "in": "query", "name": "kind", "type": "string"}, {"description": "First day, YYYY-MM-DD; defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD; defaults to today (UTC)", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}], "path": "/bo3/team-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["general", "advanced", "accuracy", "economy", "map-pool"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament", "method": "GET", "params": [{"description": "Tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}, {"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "path": "/bo3/tournament", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-map-pool": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-map-pool", "method": "GET", "params": [{"description": "CS2 tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-map-pool", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-mvps": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-mvps", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to every game", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/tournament-mvps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-squads": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-squads", "method": "GET", "params": [{"description": "CS2 tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-squads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournament-stages": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournament-stages", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament slug from bo3-tournaments, for example pgl-masters-bucharest-2026", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "pgl-masters-bucharest-2026"}], "path": "/bo3/tournament-stages", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bo3-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "bo3-tournaments", "method": "GET", "params": [{"description": "Game; one of cs2, valorant, lol, dota2, r6siege, mlbb; defaults to cs2", "enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament status; one of current, upcoming, finished, canceled, postponed", "enum": ["current", "upcoming", "finished", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"description": "Tournament tier; one of s, a, b, c, d", "enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"description": "Event type; one of lan, online", "enum": ["lan", "online"], "in": "query", "name": "event_type", "type": "string"}, {"description": "Order; one of newest, oldest, prize; defaults to newest", "enum": ["newest", "oldest", "prize"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "valorant", "lol", "dota2", "r6siege", "mlbb"], "in": "query", "name": "game", "type": "string"}, {"enum": ["current", "upcoming", "finished", "canceled", "postponed"], "in": "query", "name": "status", "type": "string"}, {"enum": ["s", "a", "b", "c", "d"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["lan", "online"], "in": "query", "name": "event_type", "type": "string"}, {"enum": ["newest", "oldest", "prize"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-transfers": {"bodyParam": null, "bodyRequired": false, "id": "bo3-transfers", "method": "GET", "params": [{"description": "BO3 team id; transfers into or out of this team", "in": "query", "minimum": 1, "name": "team_id", "type": "integer"}, {"description": "BO3 player id; this person's transfers", "in": "query", "minimum": 1, "name": "player_id", "type": "integer"}, {"description": "Transfer action; one of join, change, leave", "enum": ["join", "change", "leave"], "in": "query", "name": "action", "type": "string"}, {"description": "Role; one of player, coach", "enum": ["player", "coach"], "in": "query", "name": "role", "type": "string"}, {"description": "Order by date; one of newest, oldest; defaults to newest", "enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "type": "integer"}, {"in": "query", "name": "player_id", "type": "integer"}, {"enum": ["join", "change", "leave"], "in": "query", "name": "action", "type": "string"}, {"enum": ["player", "coach"], "in": "query", "name": "role", "type": "string"}, {"enum": ["newest", "oldest"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bo3-valorant-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "bo3-valorant-leaderboard", "method": "GET", "params": [{"description": "First day, YYYY-MM-DD (UTC); defaults to six months before to", "in": "query", "name": "from", "type": "string", "x-example": "2026-04-28"}, {"description": "Last day, YYYY-MM-DD (UTC); defaults to today", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-28"}, {"description": "Stat to rank by; one of acs, kills, deaths, damage, assists, first_kills, clutches, first_duels, games, rounds; defaults to acs", "enum": ["acs", "kills", "deaths", "damage", "assists", "first_kills", "clutches", "first_duels", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"description": "Direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"description": "Zero-based offset; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/bo3/valorant-leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["acs", "kills", "deaths", "damage", "assists", "first_kills", "clutches", "first_duels", "games", "rounds"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["bo3-economy-baseline", "bo3-forum", "bo3-forum-categories", "bo3-match", "bo3-match-games", "bo3-match-history", "bo3-match-players", "bo3-news-categories", "bo3-news-feed", "bo3-player", "bo3-player-leaderboard", "bo3-player-recent-matches", "bo3-player-stats", "bo3-records", "bo3-team", "bo3-team-prize-money", "bo3-team-ranking-dates", "bo3-team-rankings", "bo3-team-recent-matches", "bo3-team-stats", "bo3-tournament", "bo3-tournament-map-pool", "bo3-tournament-mvps", "bo3-tournament-squads", "bo3-tournament-stages", "bo3-tournaments", "bo3-transfers", "bo3-valorant-leaderboard"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-bo3-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('economy_baseline') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-economy-baseline', params, response_type: response_type)
      end
      define_method('forum') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-forum', params, response_type: response_type)
      end
      define_method('forum_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-forum-categories', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-match', params, response_type: response_type)
      end
      define_method('match_games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-match-games', params, response_type: response_type)
      end
      define_method('match_history') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-match-history', params, response_type: response_type)
      end
      define_method('match_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-match-players', params, response_type: response_type)
      end
      define_method('news_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-news-categories', params, response_type: response_type)
      end
      define_method('news_feed') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-news-feed', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-player', params, response_type: response_type)
      end
      define_method('player_leaderboard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-player-leaderboard', params, response_type: response_type)
      end
      define_method('player_recent_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-player-recent-matches', params, response_type: response_type)
      end
      define_method('player_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-player-stats', params, response_type: response_type)
      end
      define_method('records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-records', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team', params, response_type: response_type)
      end
      define_method('team_prize_money') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team-prize-money', params, response_type: response_type)
      end
      define_method('team_ranking_dates') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team-ranking-dates', params, response_type: response_type)
      end
      define_method('team_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team-rankings', params, response_type: response_type)
      end
      define_method('team_recent_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team-recent-matches', params, response_type: response_type)
      end
      define_method('team_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-team-stats', params, response_type: response_type)
      end
      define_method('tournament') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournament', params, response_type: response_type)
      end
      define_method('tournament_map_pool') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournament-map-pool', params, response_type: response_type)
      end
      define_method('tournament_mvps') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournament-mvps', params, response_type: response_type)
      end
      define_method('tournament_squads') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournament-squads', params, response_type: response_type)
      end
      define_method('tournament_stages') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournament-stages', params, response_type: response_type)
      end
      define_method('tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-tournaments', params, response_type: response_type)
      end
      define_method('transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-transfers', params, response_type: response_type)
      end
      define_method('valorant_leaderboard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bo3-valorant-leaderboard', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
