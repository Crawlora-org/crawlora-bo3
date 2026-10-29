# Crawlora BO3.gg API client for Ruby (`crawlora-bo3`)

This Ruby gem calls Crawlora's hosted BO3.gg API at `https://api.crawlora.net/api/v1`. It exposes 28 endpoints covering Counter-Strike and Valorant matches, teams, players, tournaments, rankings, news, and statistics; it does not call or scrape BO3.gg directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-bo3"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/bo3"

client = Crawlora::Bo3::Client.new
result = client.request("bo3-economy-baseline", JSON.parse("{}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 28 API operations.

```ruby
client = Crawlora::Bo3::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported BO3.gg API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-bo3/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-bo3) for account setup, the API operation reference, and release history.
