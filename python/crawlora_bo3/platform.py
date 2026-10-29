"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class BO3Client(CrawloraClient):
    """Synchronous BO3.gg API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-bo3-python/0.1.0')
        super().__init__(*args, **kwargs)

    def economy_baseline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-economy-baseline', params, response_type=response_type, timeout=timeout, headers=headers)

    def forum(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-forum', params, response_type=response_type, timeout=timeout, headers=headers)

    def forum_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-forum-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-match-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-match-history', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-match-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-news-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-news-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-player-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_recent_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-player-recent-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_prize_money(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team-prize-money', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_ranking_dates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team-ranking-dates', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_recent_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team-recent-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_map_pool(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournament-map-pool', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_mvps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournament-mvps', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_squads(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournament-squads', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_stages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournament-stages', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    def transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    def valorant_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bo3-valorant-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncBO3Client(AsyncCrawloraClient):
    """Asynchronous BO3.gg API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-bo3-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def economy_baseline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-economy-baseline', params, response_type=response_type, timeout=timeout, headers=headers)

    async def forum(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-forum', params, response_type=response_type, timeout=timeout, headers=headers)

    async def forum_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-forum-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-match-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-match-history', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-match-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-news-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-news-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-player-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_recent_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-player-recent-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_prize_money(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team-prize-money', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_ranking_dates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team-ranking-dates', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_recent_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team-recent-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_map_pool(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournament-map-pool', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_mvps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournament-mvps', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_squads(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournament-squads', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_stages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournament-stages', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def valorant_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bo3-valorant-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)
