# BO3.gg API endpoint reference and client usage

This reference lists all 28 public BO3.gg API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/bo3`, `crawlora-bo3`, and `crawlora-bo3` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape BO3.gg locally; Crawlora is independent from and not endorsed by BO3.gg or its owners.

The package tracks the public API contract revision `sha256:873a7ac103d7bfe056abcdb6d8711a12c34dc8878206f4fb549647432ca16361` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `bo3`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `economyBaseline` | `economy_baseline` | `bo3.economy_baseline` | `GET /bo3/economy-baseline` | — | BO3.gg CS2 economy baseline |
| `forum` | `forum` | `bo3.forum` | `GET /bo3/forum` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `category` (query, optional), `sort` (query, optional; values: `activity`, `newest`, `comments`, `rating`), `offset` (query, optional), `limit` (query, optional) | BO3.gg forum threads with category and sort filters |
| `forumCategories` | `forum_categories` | `bo3.forum_categories` | `GET /bo3/forum-categories` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`) | BO3.gg forum categories |
| `match` | `match` | `bo3.match_` | `GET /bo3/match` | `slug` (query, required) | BO3.gg match detail |
| `matchGames` | `match_games` | `bo3.match_games` | `GET /bo3/match-games` | `match_id` (query, required) | BO3.gg esports match maps with round-by-round results |
| `matchHistory` | `match_history` | `bo3.match_history` | `GET /bo3/match-history` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `status` (query, optional; values: `finished`, `defwin`, `upcoming`, `current`, `canceled`, `postponed`), `tier` (query, optional; values: `s`, `a`, `b`, `c`, `d`), `from` (query, optional), `to` (query, optional), `sort` (query, optional; values: `newest`, `oldest`), `offset` (query, optional), `limit` (query, optional) | BO3.gg esports match history |
| `matchPlayers` | `match_players` | `bo3.match_players` | `GET /bo3/match-players` | `slug` (query, required) | BO3.gg per-player match statistics |
| `newsCategories` | `news_categories` | `bo3.news_categories` | `GET /bo3/news-categories` | — | BO3.gg news categories |
| `newsFeed` | `news_feed` | `bo3.news_feed` | `GET /bo3/news-feed` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`, `games`), `section` (query, optional; values: `news`, `article`, `wiki`, `predictions`, `reviews`), `tag` (query, optional), `locale` (query, optional; values: `en`, `ru`, `pt`, `es`, `de`, `fr`, `tr`, `pl`, `id`, `vi`, `ja`, `ko`, `ua`, `ms`, `tl`, `da`), `category` (query, optional), `sort` (query, optional; values: `newest`, `oldest`), `offset` (query, optional), `limit` (query, optional) | BO3.gg news, articles, wiki and predictions feed |
| `player` | `player` | `bo3.player` | `GET /bo3/player` | `slug` (query, required), `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`) | BO3.gg player profile |
| `playerLeaderboard` | `player_leaderboard` | `bo3.player_leaderboard` | `GET /bo3/player-leaderboard` | `from` (query, optional), `to` (query, optional), `tier` (query, optional; values: `s`, `a`, `b`, `c`, `d`), `sort` (query, optional; values: `rating`, `kd`, `kills`, `damage`, `assists`, `headshots`, `games`, `rounds`), `order` (query, optional; values: `desc`, `asc`), `offset` (query, optional), `limit` (query, optional) | BO3.gg CS2 player leaderboard |
| `playerRecentMatches` | `player_recent_matches` | `bo3.player_recent_matches` | `GET /bo3/player-recent-matches` | `slug` (query, required), `opponent` (query, optional), `tournament` (query, optional), `limit` (query, optional) | BO3.gg player recent matches |
| `playerStats` | `player_stats` | `bo3.player_stats` | `GET /bo3/player-stats` | `slug` (query, required), `kind` (query, optional; values: `general`, `maps`, `accuracy`), `from` (query, optional), `to` (query, optional) | BO3.gg player statistics |
| `records` | `records` | `bo3.records` | `GET /bo3/records` | `from` (query, optional), `to` (query, optional), `record_type` (query, optional), `match` (query, optional), `tournament` (query, optional), `team` (query, optional), `player` (query, optional), `sort` (query, optional; values: `newest`, `oldest`), `offset` (query, optional), `limit` (query, optional) | BO3.gg CS2 records with scope and type filters |
| `team` | `team` | `bo3.team` | `GET /bo3/team` | `slug` (query, required), `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`) | BO3.gg team profile |
| `teamPrizeMoney` | `team_prize_money` | `bo3.team_prize_money` | `GET /bo3/team-prize-money` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `from` (query, optional), `to` (query, optional), `offset` (query, optional), `limit` (query, optional) | BO3.gg team prize money by period |
| `teamRankingDates` | `team_ranking_dates` | `bo3.team_ranking_dates` | `GET /bo3/team-ranking-dates` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`) | BO3.gg official ranking dates and regions |
| `teamRankings` | `team_rankings` | `bo3.team_rankings` | `GET /bo3/team-rankings` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `region` (query, optional), `date` (query, optional), `page` (query, optional), `per_page` (query, optional) | BO3.gg team rankings, current and historical |
| `teamRecentMatches` | `team_recent_matches` | `bo3.team_recent_matches` | `GET /bo3/team-recent-matches` | `slug` (query, required), `opponent` (query, optional), `tournament` (query, optional), `limit` (query, optional) | BO3.gg team recent matches |
| `teamStats` | `team_stats` | `bo3.team_stats` | `GET /bo3/team-stats` | `slug` (query, required), `kind` (query, optional; values: `general`, `advanced`, `accuracy`, `economy`, `map-pool`), `from` (query, optional), `to` (query, optional) | BO3.gg team statistics |
| `tournament` | `tournament` | `bo3.tournament` | `GET /bo3/tournament` | `slug` (query, required), `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`) | BO3.gg tournament detail |
| `tournamentMapPool` | `tournament_map_pool` | `bo3.tournament_map_pool` | `GET /bo3/tournament-map-pool` | `slug` (query, required) | BO3.gg CS2 tournament map pool |
| `tournamentMvps` | `tournament_mvps` | `bo3.tournament_mvps` | `GET /bo3/tournament-mvps` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `offset` (query, optional), `limit` (query, optional) | BO3.gg esports tournament MVPs |
| `tournaments` | `tournaments` | `bo3.tournaments` | `GET /bo3/tournaments` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `status` (query, optional; values: `current`, `upcoming`, `finished`, `canceled`, `postponed`), `tier` (query, optional; values: `s`, `a`, `b`, `c`, `d`), `event_type` (query, optional; values: `lan`, `online`), `sort` (query, optional; values: `newest`, `oldest`, `prize`), `offset` (query, optional), `limit` (query, optional) | BO3.gg tournament list with filters |
| `tournamentSquads` | `tournament_squads` | `bo3.tournament_squads` | `GET /bo3/tournament-squads` | `slug` (query, required) | BO3.gg CS2 tournament squads |
| `tournamentStages` | `tournament_stages` | `bo3.tournament_stages` | `GET /bo3/tournament-stages` | `game` (query, optional; values: `cs2`, `valorant`, `lol`, `dota2`, `r6siege`, `mlbb`), `slug` (query, required) | BO3.gg esports tournament stages |
| `transfers` | `transfers` | `bo3.transfers` | `GET /bo3/transfers` | `team_id` (query, optional), `player_id` (query, optional), `action` (query, optional; values: `join`, `change`, `leave`), `role` (query, optional; values: `player`, `coach`), `sort` (query, optional; values: `newest`, `oldest`), `offset` (query, optional), `limit` (query, optional) | BO3.gg esports transfer feed |
| `valorantLeaderboard` | `valorant_leaderboard` | `bo3.valorant_leaderboard` | `GET /bo3/valorant-leaderboard` | `from` (query, optional), `to` (query, optional), `sort` (query, optional; values: `acs`, `kills`, `deaths`, `damage`, `assists`, `first_kills`, `clutches`, `first_duels`, `games`, `rounds`), `order` (query, optional; values: `desc`, `asc`), `offset` (query, optional), `limit` (query, optional) | BO3.gg Valorant player leaderboard |

## Client forms

- JavaScript: import `BO3Client` (also exported as `Client`) from `@crawlora-org/bo3`; use `new BO3Client({ apiKey })` and `await client.method({ ... })`.
- Python: import `BO3Client` (also exported as `Client`) from `crawlora_bo3`; use `with BO3Client(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBO3Client`, used with `async with` and `await`.
- Rust: add `crawlora-bo3` with Cargo; import `Client` and the generated operation parameter struct, then call `client.bo3.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-bo3/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
