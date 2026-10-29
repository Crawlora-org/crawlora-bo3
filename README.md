# BO3.gg clients for Crawlora

Official Crawlora client packages for the hosted BO3.gg API. Access 28 API endpoints covering Counter-Strike and Valorant matches, teams, players, tournaments, rankings, news, and statistics from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape BO3.gg locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by BO3.gg or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/bo3`](javascript/README.md)
- Python: [`crawlora-bo3`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-bo3`](go.mod)
- Ruby: [`crawlora-bo3`](ruby/README.md)
- Java: [`net.crawlora:crawlora-bo3:0.1.0`](java/README.md)
- PHP: [`crawlora/bo3`](php/README.md)
- Rust: [`crawlora-bo3`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 28 selected public BO3.gg API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/bo3/economy-baseline` | `bo3-economy-baseline` | BO3.gg CS2 economy baseline |
| `GET` | `/bo3/forum` | `bo3-forum` | BO3.gg forum threads with category and sort filters |
| `GET` | `/bo3/forum-categories` | `bo3-forum-categories` | BO3.gg forum categories |
| `GET` | `/bo3/match` | `bo3-match` | BO3.gg match detail |
| `GET` | `/bo3/match-games` | `bo3-match-games` | BO3.gg esports match maps with round-by-round results |
| `GET` | `/bo3/match-history` | `bo3-match-history` | BO3.gg esports match history |
| `GET` | `/bo3/match-players` | `bo3-match-players` | BO3.gg per-player match statistics |
| `GET` | `/bo3/news-categories` | `bo3-news-categories` | BO3.gg news categories |
| `GET` | `/bo3/news-feed` | `bo3-news-feed` | BO3.gg news, articles, wiki and predictions feed |
| `GET` | `/bo3/player` | `bo3-player` | BO3.gg player profile |
| `GET` | `/bo3/player-leaderboard` | `bo3-player-leaderboard` | BO3.gg CS2 player leaderboard |
| `GET` | `/bo3/player-recent-matches` | `bo3-player-recent-matches` | BO3.gg player recent matches |
| `GET` | `/bo3/player-stats` | `bo3-player-stats` | BO3.gg player statistics |
| `GET` | `/bo3/records` | `bo3-records` | BO3.gg CS2 records with scope and type filters |
| `GET` | `/bo3/team` | `bo3-team` | BO3.gg team profile |
| `GET` | `/bo3/team-prize-money` | `bo3-team-prize-money` | BO3.gg team prize money by period |
| `GET` | `/bo3/team-ranking-dates` | `bo3-team-ranking-dates` | BO3.gg official ranking dates and regions |
| `GET` | `/bo3/team-rankings` | `bo3-team-rankings` | BO3.gg team rankings, current and historical |
| `GET` | `/bo3/team-recent-matches` | `bo3-team-recent-matches` | BO3.gg team recent matches |
| `GET` | `/bo3/team-stats` | `bo3-team-stats` | BO3.gg team statistics |
| `GET` | `/bo3/tournament` | `bo3-tournament` | BO3.gg tournament detail |
| `GET` | `/bo3/tournament-map-pool` | `bo3-tournament-map-pool` | BO3.gg CS2 tournament map pool |
| `GET` | `/bo3/tournament-mvps` | `bo3-tournament-mvps` | BO3.gg esports tournament MVPs |
| `GET` | `/bo3/tournament-squads` | `bo3-tournament-squads` | BO3.gg CS2 tournament squads |
| `GET` | `/bo3/tournament-stages` | `bo3-tournament-stages` | BO3.gg esports tournament stages |
| `GET` | `/bo3/tournaments` | `bo3-tournaments` | BO3.gg tournament list with filters |
| `GET` | `/bo3/transfers` | `bo3-transfers` | BO3.gg esports transfer feed |
| `GET` | `/bo3/valorant-leaderboard` | `bo3-valorant-leaderboard` | BO3.gg Valorant player leaderboard |

## License

MIT. See [LICENSE](LICENSE).
