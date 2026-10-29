import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class BO3Client extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  economyBaseline(params?: OperationParamsMap["bo3-economy-baseline"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  forum(params?: OperationParamsMap["bo3-forum"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  forumCategories(params?: OperationParamsMap["bo3-forum-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["bo3-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchGames(params: OperationParamsMap["bo3-match-games"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchHistory(params?: OperationParamsMap["bo3-match-history"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchPlayers(params: OperationParamsMap["bo3-match-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsCategories(params?: OperationParamsMap["bo3-news-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsFeed(params?: OperationParamsMap["bo3-news-feed"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["bo3-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerLeaderboard(params?: OperationParamsMap["bo3-player-leaderboard"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerRecentMatches(params: OperationParamsMap["bo3-player-recent-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStats(params: OperationParamsMap["bo3-player-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  records(params?: OperationParamsMap["bo3-records"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["bo3-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPrizeMoney(params?: OperationParamsMap["bo3-team-prize-money"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamRankingDates(params?: OperationParamsMap["bo3-team-ranking-dates"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamRankings(params?: OperationParamsMap["bo3-team-rankings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamRecentMatches(params: OperationParamsMap["bo3-team-recent-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamStats(params: OperationParamsMap["bo3-team-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournament(params: OperationParamsMap["bo3-tournament"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentMapPool(params: OperationParamsMap["bo3-tournament-map-pool"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentMvps(params?: OperationParamsMap["bo3-tournament-mvps"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentSquads(params: OperationParamsMap["bo3-tournament-squads"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentStages(params: OperationParamsMap["bo3-tournament-stages"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournaments(params?: OperationParamsMap["bo3-tournaments"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  transfers(params?: OperationParamsMap["bo3-transfers"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  valorantLeaderboard(params?: OperationParamsMap["bo3-valorant-leaderboard"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  economyBaseline(params?: OperationParamsMap["bo3-economy-baseline"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  forum(params?: OperationParamsMap["bo3-forum"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  forumCategories(params?: OperationParamsMap["bo3-forum-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["bo3-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchGames(params: OperationParamsMap["bo3-match-games"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchHistory(params?: OperationParamsMap["bo3-match-history"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchPlayers(params: OperationParamsMap["bo3-match-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsCategories(params?: OperationParamsMap["bo3-news-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsFeed(params?: OperationParamsMap["bo3-news-feed"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["bo3-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerLeaderboard(params?: OperationParamsMap["bo3-player-leaderboard"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerRecentMatches(params: OperationParamsMap["bo3-player-recent-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStats(params: OperationParamsMap["bo3-player-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  records(params?: OperationParamsMap["bo3-records"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["bo3-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPrizeMoney(params?: OperationParamsMap["bo3-team-prize-money"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamRankingDates(params?: OperationParamsMap["bo3-team-ranking-dates"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamRankings(params?: OperationParamsMap["bo3-team-rankings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamRecentMatches(params: OperationParamsMap["bo3-team-recent-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamStats(params: OperationParamsMap["bo3-team-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournament(params: OperationParamsMap["bo3-tournament"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentMapPool(params: OperationParamsMap["bo3-tournament-map-pool"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentMvps(params?: OperationParamsMap["bo3-tournament-mvps"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentSquads(params: OperationParamsMap["bo3-tournament-squads"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentStages(params: OperationParamsMap["bo3-tournament-stages"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournaments(params?: OperationParamsMap["bo3-tournaments"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  transfers(params?: OperationParamsMap["bo3-transfers"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  valorantLeaderboard(params?: OperationParamsMap["bo3-valorant-leaderboard"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  economyBaseline(...args: OperationRequestArgs<"bo3-economy-baseline">): Promise<OperationResponseMap["bo3-economy-baseline"]>;
  forum(...args: OperationRequestArgs<"bo3-forum">): Promise<OperationResponseMap["bo3-forum"]>;
  forumCategories(...args: OperationRequestArgs<"bo3-forum-categories">): Promise<OperationResponseMap["bo3-forum-categories"]>;
  match(...args: OperationRequestArgs<"bo3-match">): Promise<OperationResponseMap["bo3-match"]>;
  matchGames(...args: OperationRequestArgs<"bo3-match-games">): Promise<OperationResponseMap["bo3-match-games"]>;
  matchHistory(...args: OperationRequestArgs<"bo3-match-history">): Promise<OperationResponseMap["bo3-match-history"]>;
  matchPlayers(...args: OperationRequestArgs<"bo3-match-players">): Promise<OperationResponseMap["bo3-match-players"]>;
  newsCategories(...args: OperationRequestArgs<"bo3-news-categories">): Promise<OperationResponseMap["bo3-news-categories"]>;
  newsFeed(...args: OperationRequestArgs<"bo3-news-feed">): Promise<OperationResponseMap["bo3-news-feed"]>;
  player(...args: OperationRequestArgs<"bo3-player">): Promise<OperationResponseMap["bo3-player"]>;
  playerLeaderboard(...args: OperationRequestArgs<"bo3-player-leaderboard">): Promise<OperationResponseMap["bo3-player-leaderboard"]>;
  playerRecentMatches(...args: OperationRequestArgs<"bo3-player-recent-matches">): Promise<OperationResponseMap["bo3-player-recent-matches"]>;
  playerStats(...args: OperationRequestArgs<"bo3-player-stats">): Promise<OperationResponseMap["bo3-player-stats"]>;
  records(...args: OperationRequestArgs<"bo3-records">): Promise<OperationResponseMap["bo3-records"]>;
  team(...args: OperationRequestArgs<"bo3-team">): Promise<OperationResponseMap["bo3-team"]>;
  teamPrizeMoney(...args: OperationRequestArgs<"bo3-team-prize-money">): Promise<OperationResponseMap["bo3-team-prize-money"]>;
  teamRankingDates(...args: OperationRequestArgs<"bo3-team-ranking-dates">): Promise<OperationResponseMap["bo3-team-ranking-dates"]>;
  teamRankings(...args: OperationRequestArgs<"bo3-team-rankings">): Promise<OperationResponseMap["bo3-team-rankings"]>;
  teamRecentMatches(...args: OperationRequestArgs<"bo3-team-recent-matches">): Promise<OperationResponseMap["bo3-team-recent-matches"]>;
  teamStats(...args: OperationRequestArgs<"bo3-team-stats">): Promise<OperationResponseMap["bo3-team-stats"]>;
  tournament(...args: OperationRequestArgs<"bo3-tournament">): Promise<OperationResponseMap["bo3-tournament"]>;
  tournamentMapPool(...args: OperationRequestArgs<"bo3-tournament-map-pool">): Promise<OperationResponseMap["bo3-tournament-map-pool"]>;
  tournamentMvps(...args: OperationRequestArgs<"bo3-tournament-mvps">): Promise<OperationResponseMap["bo3-tournament-mvps"]>;
  tournamentSquads(...args: OperationRequestArgs<"bo3-tournament-squads">): Promise<OperationResponseMap["bo3-tournament-squads"]>;
  tournamentStages(...args: OperationRequestArgs<"bo3-tournament-stages">): Promise<OperationResponseMap["bo3-tournament-stages"]>;
  tournaments(...args: OperationRequestArgs<"bo3-tournaments">): Promise<OperationResponseMap["bo3-tournaments"]>;
  transfers(...args: OperationRequestArgs<"bo3-transfers">): Promise<OperationResponseMap["bo3-transfers"]>;
  valorantLeaderboard(...args: OperationRequestArgs<"bo3-valorant-leaderboard">): Promise<OperationResponseMap["bo3-valorant-leaderboard"]>;
}
export { BO3Client as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default BO3Client;
