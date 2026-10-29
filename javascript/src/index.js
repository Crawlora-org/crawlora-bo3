import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class BO3Client extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-bo3-js/0.1.0" });
    this["economyBaseline"] = (...args) => this.request("bo3-economy-baseline", ...args);
    this["forum"] = (...args) => this.request("bo3-forum", ...args);
    this["forumCategories"] = (...args) => this.request("bo3-forum-categories", ...args);
    this["match"] = (...args) => this.request("bo3-match", ...args);
    this["matchGames"] = (...args) => this.request("bo3-match-games", ...args);
    this["matchHistory"] = (...args) => this.request("bo3-match-history", ...args);
    this["matchPlayers"] = (...args) => this.request("bo3-match-players", ...args);
    this["newsCategories"] = (...args) => this.request("bo3-news-categories", ...args);
    this["newsFeed"] = (...args) => this.request("bo3-news-feed", ...args);
    this["player"] = (...args) => this.request("bo3-player", ...args);
    this["playerLeaderboard"] = (...args) => this.request("bo3-player-leaderboard", ...args);
    this["playerRecentMatches"] = (...args) => this.request("bo3-player-recent-matches", ...args);
    this["playerStats"] = (...args) => this.request("bo3-player-stats", ...args);
    this["records"] = (...args) => this.request("bo3-records", ...args);
    this["team"] = (...args) => this.request("bo3-team", ...args);
    this["teamPrizeMoney"] = (...args) => this.request("bo3-team-prize-money", ...args);
    this["teamRankingDates"] = (...args) => this.request("bo3-team-ranking-dates", ...args);
    this["teamRankings"] = (...args) => this.request("bo3-team-rankings", ...args);
    this["teamRecentMatches"] = (...args) => this.request("bo3-team-recent-matches", ...args);
    this["teamStats"] = (...args) => this.request("bo3-team-stats", ...args);
    this["tournament"] = (...args) => this.request("bo3-tournament", ...args);
    this["tournamentMapPool"] = (...args) => this.request("bo3-tournament-map-pool", ...args);
    this["tournamentMvps"] = (...args) => this.request("bo3-tournament-mvps", ...args);
    this["tournamentSquads"] = (...args) => this.request("bo3-tournament-squads", ...args);
    this["tournamentStages"] = (...args) => this.request("bo3-tournament-stages", ...args);
    this["tournaments"] = (...args) => this.request("bo3-tournaments", ...args);
    this["transfers"] = (...args) => this.request("bo3-transfers", ...args);
    this["valorantLeaderboard"] = (...args) => this.request("bo3-valorant-leaderboard", ...args);
  }
}

export { BO3Client as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default BO3Client;
