# @crawlora-org/bo3 — BO3.gg API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted BO3.gg API.
It exposes 28 API endpoints for Counter-Strike and Valorant matches, teams, players, tournaments, rankings, news, and statistics through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-javascript-homepage). It does not run a browser or scrape BO3.gg locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by BO3.gg or its owners.

## Install

```sh
npm install @crawlora-org/bo3
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { BO3Client } from "@crawlora-org/bo3";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new BO3Client({ apiKey });
const result1 = await client.matchHistory({});
console.log(result1);
const result2 = await client.economyBaseline({});
console.log(result2);
```

The client also exports `Client` as an alias for `BO3Client`. Operation
methods are available directly in camelCase and through the `bo3`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-bo3/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-bo3/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported BO3.gg API endpoints

This package exposes each route below as a direct method and through the `bo3` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-bo3/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
