from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelBo3ValorantLeaderboardResponse = TypedDict('ModelBo3ValorantLeaderboardResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'min_games_count': NotRequired[int],
    'offset': NotRequired[int],
    'order': NotRequired[Literal['desc', 'asc']],
    'players': NotRequired[list[ModelBo3ValorantPlayer]],
    'sort': NotRequired[Literal['acs', 'kills', 'deaths', 'damage', 'assists', 'first_kills', 'clutches', 'first_duels', 'games', 'rounds']],
    'source_url': NotRequired[str],
    'to': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBo3ValorantPlayer = TypedDict('ModelBo3ValorantPlayer', {
    'games': NotRequired[int],
    'nickname': NotRequired[str],
    'player_id': NotRequired[int],
    'position': NotRequired[int],
    'rounds': NotRequired[int],
    'slug': NotRequired[str],
    'stats': NotRequired[dict[str, float]],
}, total=False)

ModelBo3TransfersResponse = TypedDict('ModelBo3TransfersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'transfers': NotRequired[list[ModelBo3TransferRow]],
}, total=False)

ModelBo3TransferRow = TypedDict('ModelBo3TransferRow', {
    'action': NotRequired[Literal['join', 'change', 'leave']],
    'action_code': NotRequired[int],
    'compensation': NotRequired[str],
    'date': NotRequired[str],
    'from': NotRequired[ModelBo3TransferTeam],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'is_coach': NotRequired[bool],
    'nickname': NotRequired[str],
    'player_id': NotRequired[int],
    'player_slug': NotRequired[str],
    'source_url': NotRequired[str],
    'to': NotRequired[ModelBo3TransferTeam],
}, total=False)

ModelBo3TransferTeam = TypedDict('ModelBo3TransferTeam', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelBo3TournamentListResponse = TypedDict('ModelBo3TournamentListResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'tournaments': NotRequired[list[ModelBo3TournamentListItem]],
}, total=False)

ModelBo3TournamentListItem = TypedDict('ModelBo3TournamentListItem', {
    'end_date': NotRequired[str],
    'event_type': NotRequired[Literal['lan', 'online']],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'prize_usd': NotRequired[int],
    'slug': NotRequired[str],
    'start_date': NotRequired[str],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'url': NotRequired[str],
}, total=False)

ModelBo3TournamentStagesResponse = TypedDict('ModelBo3TournamentStagesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'stages': NotRequired[list[ModelBo3StageRow]],
}, total=False)

ModelBo3StageRow = TypedDict('ModelBo3StageRow', {
    'end_date': NotRequired[str],
    'format_type': NotRequired[str],
    'hold': NotRequired[bool],
    'id': NotRequired[int],
    'promotion_team_count': NotRequired[int],
    'sequence': NotRequired[int],
    'start_date': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelBo3TournamentSquadsResponse = TypedDict('ModelBo3TournamentSquadsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'squads': NotRequired[list[ModelBo3TournamentSquad]],
}, total=False)

ModelBo3TournamentSquad = TypedDict('ModelBo3TournamentSquad', {
    'logo_url': NotRequired[str],
    'players': NotRequired[list[ModelBo3SquadPlayer]],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
    'team_slug': NotRequired[str],
}, total=False)

ModelBo3SquadPlayer = TypedDict('ModelBo3SquadPlayer', {
    'first_name': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'is_coach': NotRequired[bool],
    'is_standin': NotRequired[bool],
    'last_name': NotRequired[str],
    'nickname': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelBo3TournamentMvpsResponse = TypedDict('ModelBo3TournamentMvpsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'mvps': NotRequired[list[ModelBo3Mvprow]],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBo3Mvprow = TypedDict('ModelBo3Mvprow', {
    'article_url': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'player': NotRequired[ModelBo3PersonRef],
    'team': NotRequired[ModelBo3TransferTeam],
    'tournament': NotRequired[ModelBo3TournamentRef],
    'type': NotRequired[str],
}, total=False)

ModelBo3TournamentRef = TypedDict('ModelBo3TournamentRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'prize_usd': NotRequired[int],
    'slug': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
}, total=False)

ModelBo3PersonRef = TypedDict('ModelBo3PersonRef', {
    'id': NotRequired[int],
    'nickname': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelBo3TournamentMapPoolResponse = TypedDict('ModelBo3TournamentMapPoolResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'maps': NotRequired[list[ModelBo3TournamentMapRow]],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3TournamentMapRow = TypedDict('ModelBo3TournamentMapRow', {
    'banned_maps': NotRequired[int],
    'ct_round_wins': NotRequired[int],
    'ct_win_percent': NotRequired[int],
    'games': NotRequired[int],
    'map': NotRequired[str],
    'picked_maps': NotRequired[int],
    'rounds': NotRequired[int],
    't_round_wins': NotRequired[int],
}, total=False)

ModelBo3TournamentInfo = TypedDict('ModelBo3TournamentInfo', {
    'city': NotRequired[str],
    'country': NotRequired[str],
    'description': NotRequired[str],
    'end_date': NotRequired[str],
    'event_type': NotRequired[Literal['lan', 'online']],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'prize_usd': NotRequired[int],
    'prizes': NotRequired[list[ModelBo3Prize]],
    'region': NotRequired[str],
    'series': NotRequired[str],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'stages': NotRequired[list[ModelBo3TournamentStage]],
    'start_date': NotRequired[str],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'teams': NotRequired[list[ModelBo3TournamentTeam]],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
}, total=False)

ModelBo3TournamentTeam = TypedDict('ModelBo3TournamentTeam', {
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'place': NotRequired[str],
    'prize_usd': NotRequired[int],
    'slug': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelBo3TournamentStage = TypedDict('ModelBo3TournamentStage', {
    'end_date': NotRequired[str],
    'format_type': NotRequired[str],
    'id': NotRequired[int],
    'sequence': NotRequired[int],
    'start_date': NotRequired[str],
    'status': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelBo3Prize = TypedDict('ModelBo3Prize', {
    'place': NotRequired[str],
    'points': NotRequired[int],
    'prize_usd': NotRequired[int],
    'team_id': NotRequired[int],
}, total=False)

ModelBo3StatsResponse = TypedDict('ModelBo3StatsResponse', {
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'id': NotRequired[int],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'rows': NotRequired[list[dict[str, Any]]],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'stats': NotRequired[dict[str, float]],
    'subject': NotRequired[Literal['team', 'player']],
    'to': NotRequired[str],
}, total=False)

ModelBo3RecentMatchesResponse = TypedDict('ModelBo3RecentMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelBo3RecentMatch]],
    'opponent': NotRequired[str],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'subject': NotRequired[Literal['team', 'player']],
    'tournament': NotRequired[str],
}, total=False)

ModelBo3RecentMatch = TypedDict('ModelBo3RecentMatch', {
    'lines': NotRequired[list[ModelBo3RecentLine]],
    'maps': NotRequired[list[ModelBo3RecentMap]],
    'match_slug': NotRequired[str],
    'opponent': NotRequired[ModelBo3TeamRef],
    'rounds': NotRequired[int],
    'started_at': NotRequired[str],
    'tournament_slug': NotRequired[str],
}, total=False)

ModelBo3TeamRef = TypedDict('ModelBo3TeamRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelBo3RecentMap = TypedDict('ModelBo3RecentMap', {
    'game_id': NotRequired[int],
    'game_number': NotRequired[int],
    'map': NotRequired[str],
    'won': NotRequired[bool],
}, total=False)

ModelBo3RecentLine = TypedDict('ModelBo3RecentLine', {
    'accuracy': NotRequired[float],
    'assists': NotRequired[int],
    'avg_kill_cost': NotRequired[float],
    'damage': NotRequired[int],
    'deaths': NotRequired[int],
    'equipment_value': NotRequired[int],
    'first_deaths': NotRequired[int],
    'first_kills': NotRequired[int],
    'headshot_ratio': NotRequired[float],
    'headshots': NotRequired[int],
    'hits': NotRequired[int],
    'kills': NotRequired[int],
    'money_saved': NotRequired[int],
    'multikills': NotRequired[float],
    'nickname': NotRequired[str],
    'player_slug': NotRequired[str],
    'rating': NotRequired[float],
    'shots': NotRequired[int],
    'team_slug': NotRequired[str],
    'trade_deaths': NotRequired[int],
    'trade_kills': NotRequired[int],
}, total=False)

ModelBo3TeamRankingsResponse = TypedDict('ModelBo3TeamRankingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'official': NotRequired[bool],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
    'ranking_date': NotRequired[str],
    'region': NotRequired[str],
    'source': NotRequired[Literal['internal', 'valve_official']],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelBo3RankingRow]],
    'total_pages': NotRequired[int],
    'total_teams': NotRequired[int],
}, total=False)

ModelBo3RankingRow = TypedDict('ModelBo3RankingRow', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'points': NotRequired[float],
    'rank': NotRequired[int],
    'rank_change': NotRequired[int],
    'region': NotRequired[str],
    'roster': NotRequired[list[ModelBo3RankedPlayer]],
    'slug': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelBo3RankedPlayer = TypedDict('ModelBo3RankedPlayer', {
    'country_code': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'nickname': NotRequired[str],
    'rating': NotRequired[float],
    'slug': NotRequired[str],
}, total=False)

ModelBo3TeamRankingDatesResponse = TypedDict('ModelBo3TeamRankingDatesResponse', {
    'count': NotRequired[int],
    'dates': NotRequired[list[str]],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'regions': NotRequired[list[str]],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3TeamPrizeMoneyResponse = TypedDict('ModelBo3TeamPrizeMoneyResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelBo3TeamEarningsRow]],
    'to': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBo3TeamEarningsRow = TypedDict('ModelBo3TeamEarningsRow', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'earnings_usd': NotRequired[int],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'players': NotRequired[list[ModelBo3EarningPlayer]],
    'position': NotRequired[int],
    'region': NotRequired[str],
    'slug': NotRequired[str],
    'team_id': NotRequired[int],
    'tournament_wins': NotRequired[int],
}, total=False)

ModelBo3EarningPlayer = TypedDict('ModelBo3EarningPlayer', {
    'id': NotRequired[int],
    'is_coach': NotRequired[bool],
    'nickname': NotRequired[str],
    'six_month_avg_rating': NotRequired[float],
    'slug': NotRequired[str],
    'total_prize_usd': NotRequired[int],
}, total=False)

ModelBo3TeamInfo = TypedDict('ModelBo3TeamInfo', {
    'achievement_count': NotRequired[int],
    'achievements': NotRequired[list[ModelBo3Achievement]],
    'acronym': NotRequired[str],
    'alternative_names': NotRequired[list[str]],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'established_date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'links': NotRequired[ModelBo3Links],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'rank_change': NotRequired[int],
    'region': NotRequired[str],
    'roster': NotRequired[list[ModelBo3TeamMember]],
    'six_month_earnings_usd': NotRequired[int],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3TeamMember = TypedDict('ModelBo3TeamMember', {
    'birthday': NotRequired[str],
    'first_name': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'last_name': NotRequired[str],
    'nickname': NotRequired[str],
    'six_month_avg_rating': NotRequired[float],
    'slug': NotRequired[str],
}, total=False)

ModelBo3Links = TypedDict('ModelBo3Links', {
    'facebook': NotRequired[str],
    'instagram': NotRequired[str],
    'twitch': NotRequired[str],
    'twitter': NotRequired[str],
    'website': NotRequired[str],
    'youtube': NotRequired[str],
}, total=False)

ModelBo3Achievement = TypedDict('ModelBo3Achievement', {
    'date': NotRequired[str],
    'title': NotRequired[str],
    'tournament_id': NotRequired[int],
    'tournament_name': NotRequired[str],
    'tournament_slug': NotRequired[str],
}, total=False)

ModelBo3RecordsFeedResponse = TypedDict('ModelBo3RecordsFeedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelBo3RecordRow]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'to': NotRequired[str],
    'total': NotRequired[int],
    'types': NotRequired[list[str]],
}, total=False)

ModelBo3RecordRow = TypedDict('ModelBo3RecordRow', {
    'average': NotRequired[float],
    'begin_at': NotRequired[str],
    'country_code': NotRequired[str],
    'detail': NotRequired[str],
    'map': NotRequired[str],
    'match_slug': NotRequired[str],
    'opponents': NotRequired[list[str]],
    'player': NotRequired[ModelBo3PersonRef],
    'round_number': NotRequired[int],
    'series': NotRequired[str],
    'side': NotRequired[Literal['CT', 'T']],
    'team_name': NotRequired[str],
    'type': NotRequired[str],
    'unit': NotRequired[str],
    'value': NotRequired[float],
}, total=False)

ModelBo3LeaderboardResponse = TypedDict('ModelBo3LeaderboardResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'limit': NotRequired[int],
    'min_games_count': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'order': NotRequired[Literal['desc', 'asc']],
    'players': NotRequired[list[ModelBo3TopPlayer]],
    'sort': NotRequired[Literal['rating', 'kd', 'kills', 'damage', 'assists', 'headshots', 'games', 'rounds']],
    'source_url': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'to': NotRequired[str],
}, total=False)

ModelBo3TopPlayer = TypedDict('ModelBo3TopPlayer', {
    'country_code': NotRequired[str],
    'games': NotRequired[int],
    'image_url': NotRequired[str],
    'nickname': NotRequired[str],
    'player_id': NotRequired[int],
    'position': NotRequired[int],
    'rounds': NotRequired[int],
    'slug': NotRequired[str],
    'stats': NotRequired[dict[str, float]],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
}, total=False)

ModelBo3PlayerInfo = TypedDict('ModelBo3PlayerInfo', {
    'achievement_count': NotRequired[int],
    'achievements': NotRequired[list[ModelBo3Achievement]],
    'alternative_names': NotRequired[list[str]],
    'birthday': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'fetched_at': NotRequired[str],
    'first_name': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'is_coach': NotRequired[bool],
    'joined_team_at': NotRequired[str],
    'last_name': NotRequired[str],
    'links': NotRequired[ModelBo3Links],
    'nickname': NotRequired[str],
    'role': NotRequired[str],
    'six_month_avg_rating': NotRequired[float],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelBo3TeamRef],
    'total_prize_usd': NotRequired[int],
}, total=False)

ModelBo3NewsFeedResponse = TypedDict('ModelBo3NewsFeedResponse', {
    'category': NotRequired[int],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelBo3NewsItem]],
    'limit': NotRequired[int],
    'locale': NotRequired[Literal['en', 'ru', 'pt', 'es', 'de', 'fr', 'tr', 'pl', 'id', 'vi', 'ja', 'ko', 'ua', 'ms', 'tl', 'da']],
    'offset': NotRequired[int],
    'section': NotRequired[Literal['news', 'article', 'wiki', 'predictions', 'reviews']],
    'source_url': NotRequired[str],
    'tag': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBo3NewsItem = TypedDict('ModelBo3NewsItem', {
    'author': NotRequired[ModelBo3PersonRef],
    'category': NotRequired[str],
    'category_id': NotRequired[int],
    'description': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'likes': NotRequired[int],
    'pinned': NotRequired[bool],
    'published_at': NotRequired[str],
    'slug': NotRequired[str],
    'tags': NotRequired[list[ModelBo3TagRef]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBo3TagRef = TypedDict('ModelBo3TagRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelBo3NewsCategoriesResponse = TypedDict('ModelBo3NewsCategoriesResponse', {
    'categories': NotRequired[list[ModelBo3FeedCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3FeedCategory = TypedDict('ModelBo3FeedCategory', {
    'id': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelBo3MatchPlayersResponse = TypedDict('ModelBo3MatchPlayersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelBo3MatchPlayerStats]],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3MatchPlayerStats = TypedDict('ModelBo3MatchPlayerStats', {
    'multikills': NotRequired[dict[str, int]],
    'nickname': NotRequired[str],
    'opponent': NotRequired[str],
    'player_id': NotRequired[int],
    'stats': NotRequired[dict[str, float]],
    'team': NotRequired[str],
    'win': NotRequired[bool],
}, total=False)

ModelBo3MatchHistoryResponse = TypedDict('ModelBo3MatchHistoryResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'matches': NotRequired[list[ModelBo3MatchSummary]],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'status': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBo3MatchSummary = TypedDict('ModelBo3MatchSummary', {
    'best_of': NotRequired[int],
    'end_time': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'live_coverage': NotRequired[bool],
    'maps': NotRequired[list[ModelBo3MapRow]],
    'prediction': NotRequired[ModelBo3Prediction],
    'slug': NotRequired[str],
    'stars': NotRequired[int],
    'start_time': NotRequired[str],
    'status': NotRequired[Literal['upcoming', 'current', 'finished', 'defwin', 'canceled', 'postponed']],
    'teams': NotRequired[list[ModelBo3Team]],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'tournament': NotRequired[ModelBo3TournamentRef],
    'url': NotRequired[str],
}, total=False)

ModelBo3Team = TypedDict('ModelBo3Team', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'id': NotRequired[int],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'score': NotRequired[int],
    'slug': NotRequired[str],
    'winner': NotRequired[bool],
}, total=False)

ModelBo3Prediction = TypedDict('ModelBo3Prediction', {
    'team1_score': NotRequired[int],
    'team2_score': NotRequired[int],
    'winner_team_id': NotRequired[int],
}, total=False)

ModelBo3MapRow = TypedDict('ModelBo3MapRow', {
    'begin_at': NotRequired[str],
    'loser_score': NotRequired[int],
    'map': NotRequired[str],
    'number': NotRequired[int],
    'status': NotRequired[Literal['upcoming', 'current', 'finished']],
    'winner_score': NotRequired[int],
    'winner_team_id': NotRequired[int],
    'winner_team_name': NotRequired[str],
}, total=False)

ModelBo3MatchGamesResponse = TypedDict('ModelBo3MatchGamesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelBo3GameRow]],
    'match_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3GameRow = TypedDict('ModelBo3GameRow', {
    'begin_at': NotRequired[str],
    'duration_seconds': NotRequired[float],
    'id': NotRequired[int],
    'loser_name': NotRequired[str],
    'loser_score': NotRequired[int],
    'map': NotRequired[str],
    'number': NotRequired[int],
    'rounds': NotRequired[list[ModelBo3RoundRow]],
    'rounds_count': NotRequired[int],
    'side_results': NotRequired[list[ModelBo3SideResult]],
    'state': NotRequired[str],
    'status': NotRequired[str],
    'winner_name': NotRequired[str],
    'winner_score': NotRequired[int],
}, total=False)

ModelBo3SideResult = TypedDict('ModelBo3SideResult', {
    'loser_name': NotRequired[str],
    'loser_score': NotRequired[int],
    'loser_side': NotRequired[str],
    'order': NotRequired[int],
    'overtime': NotRequired[bool],
    'winner_name': NotRequired[str],
    'winner_score': NotRequired[int],
    'winner_side': NotRequired[str],
}, total=False)

ModelBo3RoundRow = TypedDict('ModelBo3RoundRow', {
    'duration_seconds': NotRequired[float],
    'end_reason': NotRequired[str],
    'loser_score': NotRequired[int],
    'number': NotRequired[int],
    'winner_name': NotRequired[str],
    'winner_score': NotRequired[int],
    'winner_side': NotRequired[str],
}, total=False)

ModelBo3MatchInfo = TypedDict('ModelBo3MatchInfo', {
    'best_of': NotRequired[int],
    'end_time': NotRequired[str],
    'event_type': NotRequired[Literal['lan', 'online']],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[int],
    'insights': NotRequired[list[ModelBo3Insight]],
    'live_coverage': NotRequired[bool],
    'maps': NotRequired[list[ModelBo3MapRow]],
    'prediction': NotRequired[ModelBo3Prediction],
    'round': NotRequired[str],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'stage': NotRequired[str],
    'stars': NotRequired[int],
    'start_time': NotRequired[str],
    'status': NotRequired[Literal['upcoming', 'current', 'finished', 'defwin', 'canceled', 'postponed']],
    'streams': NotRequired[list[ModelBo3Stream]],
    'teams': NotRequired[list[ModelBo3Team]],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'tournament': NotRequired[ModelBo3TournamentRef],
    'url': NotRequired[str],
}, total=False)

ModelBo3Stream = TypedDict('ModelBo3Stream', {
    'language': NotRequired[str],
    'name': NotRequired[str],
    'official': NotRequired[bool],
    'platform': NotRequired[Literal['twitch', 'youtube', 'kick', 'other']],
    'url': NotRequired[str],
    'viewer_count': NotRequired[int],
}, total=False)

ModelBo3Insight = TypedDict('ModelBo3Insight', {
    'facts': NotRequired[list[str]],
    'team': NotRequired[str],
}, total=False)

ModelBo3ForumCategoriesResponse = TypedDict('ModelBo3ForumCategoriesResponse', {
    'categories': NotRequired[list[ModelBo3ForumCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3ForumCategory = TypedDict('ModelBo3ForumCategory', {
    'id': NotRequired[int],
    'slug': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelBo3ForumFeedResponse = TypedDict('ModelBo3ForumFeedResponse', {
    'category': NotRequired[int],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'sort': NotRequired[Literal['activity', 'newest', 'comments', 'rating']],
    'source_url': NotRequired[str],
    'threads': NotRequired[list[ModelBo3ForumThread]],
    'total': NotRequired[int],
}, total=False)

ModelBo3ForumThread = TypedDict('ModelBo3ForumThread', {
    'author': NotRequired[ModelBo3PersonRef],
    'category': NotRequired[str],
    'category_id': NotRequired[int],
    'comments': NotRequired[int],
    'created_at': NotRequired[str],
    'id': NotRequired[int],
    'last_activity_at': NotRequired[str],
    'pinned': NotRequired[bool],
    'rating': NotRequired[int],
    'slug': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelBo3EconomyBaselineResponse = TypedDict('ModelBo3EconomyBaselineResponse', {
    'cells': NotRequired[list[ModelBo3EconomyCell]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelBo3EconomyCell = TypedDict('ModelBo3EconomyCell', {
    'enemy_level': NotRequired[Literal['-1', '0', '1', '2']],
    'rounds': NotRequired[int],
    'team_level': NotRequired[Literal['-1', '0', '1', '2']],
    'win_rate': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

Bo3EconomyBaselineResponse = Any
Bo3EconomyBaselineParams = TypedDict('Bo3EconomyBaselineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

Bo3ForumResponse = Any
Bo3ForumParams = TypedDict('Bo3ForumParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['activity', 'newest', 'comments', 'rating']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ForumCategoriesResponse = Any
Bo3ForumCategoriesParams = TypedDict('Bo3ForumCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3MatchResponse = Any
Bo3MatchParams = TypedDict('Bo3MatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

Bo3MatchGamesResponse = Any
Bo3MatchGamesParams = TypedDict('Bo3MatchGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_id': Required[int],
}, total=False)

Bo3MatchHistoryResponse = Any
Bo3MatchHistoryParams = TypedDict('Bo3MatchHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['finished', 'defwin', 'upcoming', 'current', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3MatchPlayersResponse = Any
Bo3MatchPlayersParams = TypedDict('Bo3MatchPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

Bo3NewsCategoriesResponse = Any
Bo3NewsCategoriesParams = TypedDict('Bo3NewsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

Bo3NewsFeedResponse = Any
Bo3NewsFeedParams = TypedDict('Bo3NewsFeedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb', 'games']],
    'section': NotRequired[Literal['news', 'article', 'wiki', 'predictions', 'reviews']],
    'tag': NotRequired[str],
    'locale': NotRequired[Literal['en', 'ru', 'pt', 'es', 'de', 'fr', 'tr', 'pl', 'id', 'vi', 'ja', 'ko', 'ua', 'ms', 'tl', 'da']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerResponse = Any
Bo3PlayerParams = TypedDict('Bo3PlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3PlayerLeaderboardResponse = Any
Bo3PlayerLeaderboardParams = TypedDict('Bo3PlayerLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'sort': NotRequired[Literal['rating', 'kd', 'kills', 'damage', 'assists', 'headshots', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerRecentMatchesResponse = Any
Bo3PlayerRecentMatchesParams = TypedDict('Bo3PlayerRecentMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerStatsResponse = Any
Bo3PlayerStatsParams = TypedDict('Bo3PlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'maps', 'accuracy']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3RecordsResponse = Any
Bo3RecordsParams = TypedDict('Bo3RecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'record_type': NotRequired[str],
    'match': NotRequired[str],
    'tournament': NotRequired[str],
    'team': NotRequired[str],
    'player': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamResponse = Any
Bo3TeamParams = TypedDict('Bo3TeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamPrizeMoneyResponse = Any
Bo3TeamPrizeMoneyParams = TypedDict('Bo3TeamPrizeMoneyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamRankingDatesResponse = Any
Bo3TeamRankingDatesParams = TypedDict('Bo3TeamRankingDatesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamRankingsResponse = Any
Bo3TeamRankingsParams = TypedDict('Bo3TeamRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'region': NotRequired[str],
    'date': NotRequired[str],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
}, total=False)

Bo3TeamRecentMatchesResponse = Any
Bo3TeamRecentMatchesParams = TypedDict('Bo3TeamRecentMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamStatsResponse = Any
Bo3TeamStatsParams = TypedDict('Bo3TeamStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'advanced', 'accuracy', 'economy', 'map-pool']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3TournamentResponse = Any
Bo3TournamentParams = TypedDict('Bo3TournamentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TournamentMapPoolResponse = Any
Bo3TournamentMapPoolParams = TypedDict('Bo3TournamentMapPoolParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

Bo3TournamentMvpsResponse = Any
Bo3TournamentMvpsParams = TypedDict('Bo3TournamentMvpsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentSquadsResponse = Any
Bo3TournamentSquadsParams = TypedDict('Bo3TournamentSquadsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

Bo3TournamentStagesResponse = Any
Bo3TournamentStagesParams = TypedDict('Bo3TournamentStagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'slug': Required[str],
}, total=False)

Bo3TournamentsResponse = Any
Bo3TournamentsParams = TypedDict('Bo3TournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'event_type': NotRequired[Literal['lan', 'online']],
    'sort': NotRequired[Literal['newest', 'oldest', 'prize']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TransfersResponse = Any
Bo3TransfersParams = TypedDict('Bo3TransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': NotRequired[int],
    'player_id': NotRequired[int],
    'action': NotRequired[Literal['join', 'change', 'leave']],
    'role': NotRequired[Literal['player', 'coach']],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ValorantLeaderboardResponse = Any
Bo3ValorantLeaderboardParams = TypedDict('Bo3ValorantLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['acs', 'kills', 'deaths', 'damage', 'assists', 'first_kills', 'clutches', 'first_duels', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

class Bo3Group:
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineStreamParams]) -> BinaryIO: ...
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineTextResponseParams]) -> str: ...
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineDefaultParams]) -> Bo3EconomyBaselineResponse: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumStreamParams]) -> BinaryIO: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumTextResponseParams]) -> str: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumDefaultParams]) -> Bo3ForumResponse: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesTextResponseParams]) -> str: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesDefaultParams]) -> Bo3ForumCategoriesResponse: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchDefaultParams]) -> Bo3MatchResponse: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesStreamParams]) -> BinaryIO: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesTextResponseParams]) -> str: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesDefaultParams]) -> Bo3MatchGamesResponse: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryTextResponseParams]) -> str: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryDefaultParams]) -> Bo3MatchHistoryResponse: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersTextResponseParams]) -> str: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersDefaultParams]) -> Bo3MatchPlayersResponse: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesTextResponseParams]) -> str: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesDefaultParams]) -> Bo3NewsCategoriesResponse: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedStreamParams]) -> BinaryIO: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedTextResponseParams]) -> str: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedDefaultParams]) -> Bo3NewsFeedResponse: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerDefaultParams]) -> Bo3PlayerResponse: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardTextResponseParams]) -> str: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardDefaultParams]) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesTextResponseParams]) -> str: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesDefaultParams]) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsDefaultParams]) -> Bo3PlayerStatsResponse: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsDefaultParams]) -> Bo3RecordsResponse: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamDefaultParams]) -> Bo3TeamResponse: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyStreamParams]) -> BinaryIO: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyTextResponseParams]) -> str: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyDefaultParams]) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesStreamParams]) -> BinaryIO: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesTextResponseParams]) -> str: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesDefaultParams]) -> Bo3TeamRankingDatesResponse: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsTextResponseParams]) -> str: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsDefaultParams]) -> Bo3TeamRankingsResponse: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesTextResponseParams]) -> str: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesDefaultParams]) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsTextResponseParams]) -> str: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsDefaultParams]) -> Bo3TeamStatsResponse: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentDefaultParams]) -> Bo3TournamentResponse: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolTextResponseParams]) -> str: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolDefaultParams]) -> Bo3TournamentMapPoolResponse: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsTextResponseParams]) -> str: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsDefaultParams]) -> Bo3TournamentMvpsResponse: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsTextResponseParams]) -> str: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsDefaultParams]) -> Bo3TournamentSquadsResponse: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesTextResponseParams]) -> str: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesDefaultParams]) -> Bo3TournamentStagesResponse: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsDefaultParams]) -> Bo3TournamentsResponse: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersStreamParams]) -> BinaryIO: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersTextResponseParams]) -> str: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersDefaultParams]) -> Bo3TransfersResponse: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardTextResponseParams]) -> str: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardDefaultParams]) -> Bo3ValorantLeaderboardResponse: ...

OperationId = Literal[
    'bo3-economy-baseline',
    'bo3-forum',
    'bo3-forum-categories',
    'bo3-match',
    'bo3-match-games',
    'bo3-match-history',
    'bo3-match-players',
    'bo3-news-categories',
    'bo3-news-feed',
    'bo3-player',
    'bo3-player-leaderboard',
    'bo3-player-recent-matches',
    'bo3-player-stats',
    'bo3-records',
    'bo3-team',
    'bo3-team-prize-money',
    'bo3-team-ranking-dates',
    'bo3-team-rankings',
    'bo3-team-recent-matches',
    'bo3-team-stats',
    'bo3-tournament',
    'bo3-tournament-map-pool',
    'bo3-tournament-mvps',
    'bo3-tournament-squads',
    'bo3-tournament-stages',
    'bo3-tournaments',
    'bo3-transfers',
    'bo3-valorant-leaderboard',
]

class CrawloraClient:
    bo3: Bo3Group
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-economy-baseline'],
        params: Bo3EconomyBaselineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3EconomyBaselineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-forum'],
        params: Bo3ForumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ForumResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-forum-categories'],
        params: Bo3ForumCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ForumCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-match'],
        params: Bo3MatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-match-games'],
        params: Bo3MatchGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-match-history'],
        params: Bo3MatchHistoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-match-players'],
        params: Bo3MatchPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-news-categories'],
        params: Bo3NewsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3NewsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-news-feed'],
        params: Bo3NewsFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3NewsFeedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-player'],
        params: Bo3PlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-player-leaderboard'],
        params: Bo3PlayerLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-player-recent-matches'],
        params: Bo3PlayerRecentMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-player-stats'],
        params: Bo3PlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-records'],
        params: Bo3RecordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3RecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team'],
        params: Bo3TeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team-prize-money'],
        params: Bo3TeamPrizeMoneyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team-ranking-dates'],
        params: Bo3TeamRankingDatesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRankingDatesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team-rankings'],
        params: Bo3TeamRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team-recent-matches'],
        params: Bo3TeamRecentMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-team-stats'],
        params: Bo3TeamStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournament'],
        params: Bo3TournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournament-map-pool'],
        params: Bo3TournamentMapPoolParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentMapPoolResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournament-mvps'],
        params: Bo3TournamentMvpsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentMvpsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournament-squads'],
        params: Bo3TournamentSquadsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentSquadsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournament-stages'],
        params: Bo3TournamentStagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentStagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-tournaments'],
        params: Bo3TournamentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-transfers'],
        params: Bo3TransfersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TransfersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bo3-valorant-leaderboard'],
        params: Bo3ValorantLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ValorantLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-economy-baseline'],
        params: Bo3EconomyBaselineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3EconomyBaselineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-forum'],
        params: Bo3ForumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ForumResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-forum-categories'],
        params: Bo3ForumCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ForumCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-match'],
        params: Bo3MatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-match-games'],
        params: Bo3MatchGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-match-history'],
        params: Bo3MatchHistoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-match-players'],
        params: Bo3MatchPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3MatchPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-news-categories'],
        params: Bo3NewsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3NewsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-news-feed'],
        params: Bo3NewsFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3NewsFeedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-player'],
        params: Bo3PlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-player-leaderboard'],
        params: Bo3PlayerLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-player-recent-matches'],
        params: Bo3PlayerRecentMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-player-stats'],
        params: Bo3PlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3PlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-records'],
        params: Bo3RecordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3RecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team'],
        params: Bo3TeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team-prize-money'],
        params: Bo3TeamPrizeMoneyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team-ranking-dates'],
        params: Bo3TeamRankingDatesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRankingDatesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team-rankings'],
        params: Bo3TeamRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team-recent-matches'],
        params: Bo3TeamRecentMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-team-stats'],
        params: Bo3TeamStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TeamStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournament'],
        params: Bo3TournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournament-map-pool'],
        params: Bo3TournamentMapPoolParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentMapPoolResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournament-mvps'],
        params: Bo3TournamentMvpsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentMvpsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournament-squads'],
        params: Bo3TournamentSquadsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentSquadsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournament-stages'],
        params: Bo3TournamentStagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentStagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-tournaments'],
        params: Bo3TournamentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TournamentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-transfers'],
        params: Bo3TransfersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3TransfersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bo3-valorant-leaderboard'],
        params: Bo3ValorantLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Bo3ValorantLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class BO3Client(CrawloraClient):
    def __enter__(self) -> BO3Client: ...
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineStreamParams]) -> BinaryIO: ...
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineTextResponseParams]) -> str: ...
    @overload
    def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineDefaultParams]) -> Bo3EconomyBaselineResponse: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumStreamParams]) -> BinaryIO: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumTextResponseParams]) -> str: ...
    @overload
    def forum(self, **params: Unpack[Bo3ForumDefaultParams]) -> Bo3ForumResponse: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesTextResponseParams]) -> str: ...
    @overload
    def forum_categories(self, **params: Unpack[Bo3ForumCategoriesDefaultParams]) -> Bo3ForumCategoriesResponse: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[Bo3MatchDefaultParams]) -> Bo3MatchResponse: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesStreamParams]) -> BinaryIO: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesTextResponseParams]) -> str: ...
    @overload
    def match_games(self, **params: Unpack[Bo3MatchGamesDefaultParams]) -> Bo3MatchGamesResponse: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryTextResponseParams]) -> str: ...
    @overload
    def match_history(self, **params: Unpack[Bo3MatchHistoryDefaultParams]) -> Bo3MatchHistoryResponse: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersTextResponseParams]) -> str: ...
    @overload
    def match_players(self, **params: Unpack[Bo3MatchPlayersDefaultParams]) -> Bo3MatchPlayersResponse: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesTextResponseParams]) -> str: ...
    @overload
    def news_categories(self, **params: Unpack[Bo3NewsCategoriesDefaultParams]) -> Bo3NewsCategoriesResponse: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedStreamParams]) -> BinaryIO: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedTextResponseParams]) -> str: ...
    @overload
    def news_feed(self, **params: Unpack[Bo3NewsFeedDefaultParams]) -> Bo3NewsFeedResponse: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[Bo3PlayerDefaultParams]) -> Bo3PlayerResponse: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardTextResponseParams]) -> str: ...
    @overload
    def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardDefaultParams]) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesTextResponseParams]) -> str: ...
    @overload
    def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesDefaultParams]) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[Bo3PlayerStatsDefaultParams]) -> Bo3PlayerStatsResponse: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[Bo3RecordsDefaultParams]) -> Bo3RecordsResponse: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[Bo3TeamDefaultParams]) -> Bo3TeamResponse: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyStreamParams]) -> BinaryIO: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyTextResponseParams]) -> str: ...
    @overload
    def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyDefaultParams]) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesStreamParams]) -> BinaryIO: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesTextResponseParams]) -> str: ...
    @overload
    def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesDefaultParams]) -> Bo3TeamRankingDatesResponse: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsTextResponseParams]) -> str: ...
    @overload
    def team_rankings(self, **params: Unpack[Bo3TeamRankingsDefaultParams]) -> Bo3TeamRankingsResponse: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesTextResponseParams]) -> str: ...
    @overload
    def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesDefaultParams]) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsTextResponseParams]) -> str: ...
    @overload
    def team_stats(self, **params: Unpack[Bo3TeamStatsDefaultParams]) -> Bo3TeamStatsResponse: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[Bo3TournamentDefaultParams]) -> Bo3TournamentResponse: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolTextResponseParams]) -> str: ...
    @overload
    def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolDefaultParams]) -> Bo3TournamentMapPoolResponse: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsTextResponseParams]) -> str: ...
    @overload
    def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsDefaultParams]) -> Bo3TournamentMvpsResponse: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsTextResponseParams]) -> str: ...
    @overload
    def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsDefaultParams]) -> Bo3TournamentSquadsResponse: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesTextResponseParams]) -> str: ...
    @overload
    def tournament_stages(self, **params: Unpack[Bo3TournamentStagesDefaultParams]) -> Bo3TournamentStagesResponse: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[Bo3TournamentsDefaultParams]) -> Bo3TournamentsResponse: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersStreamParams]) -> BinaryIO: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersTextResponseParams]) -> str: ...
    @overload
    def transfers(self, **params: Unpack[Bo3TransfersDefaultParams]) -> Bo3TransfersResponse: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardTextResponseParams]) -> str: ...
    @overload
    def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardDefaultParams]) -> Bo3ValorantLeaderboardResponse: ...

class AsyncBO3Client(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncBO3Client: ...
    bo3: _AsyncBo3Group
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineStreamParams]) -> BinaryIO: ...
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineTextResponseParams]) -> str: ...
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineDefaultParams]) -> Bo3EconomyBaselineResponse: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumStreamParams]) -> BinaryIO: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumTextResponseParams]) -> str: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumDefaultParams]) -> Bo3ForumResponse: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesTextResponseParams]) -> str: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesDefaultParams]) -> Bo3ForumCategoriesResponse: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchDefaultParams]) -> Bo3MatchResponse: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesTextResponseParams]) -> str: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesDefaultParams]) -> Bo3MatchGamesResponse: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryTextResponseParams]) -> str: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryDefaultParams]) -> Bo3MatchHistoryResponse: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersTextResponseParams]) -> str: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersDefaultParams]) -> Bo3MatchPlayersResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesDefaultParams]) -> Bo3NewsCategoriesResponse: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedTextResponseParams]) -> str: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedDefaultParams]) -> Bo3NewsFeedResponse: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerDefaultParams]) -> Bo3PlayerResponse: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardDefaultParams]) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesDefaultParams]) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsDefaultParams]) -> Bo3PlayerStatsResponse: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsDefaultParams]) -> Bo3RecordsResponse: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamDefaultParams]) -> Bo3TeamResponse: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyStreamParams]) -> BinaryIO: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyTextResponseParams]) -> str: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyDefaultParams]) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesTextResponseParams]) -> str: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesDefaultParams]) -> Bo3TeamRankingDatesResponse: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsTextResponseParams]) -> str: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsDefaultParams]) -> Bo3TeamRankingsResponse: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesDefaultParams]) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsTextResponseParams]) -> str: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsDefaultParams]) -> Bo3TeamStatsResponse: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentDefaultParams]) -> Bo3TournamentResponse: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolTextResponseParams]) -> str: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolDefaultParams]) -> Bo3TournamentMapPoolResponse: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsTextResponseParams]) -> str: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsDefaultParams]) -> Bo3TournamentMvpsResponse: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsTextResponseParams]) -> str: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsDefaultParams]) -> Bo3TournamentSquadsResponse: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesTextResponseParams]) -> str: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesDefaultParams]) -> Bo3TournamentStagesResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsDefaultParams]) -> Bo3TournamentsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersDefaultParams]) -> Bo3TransfersResponse: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardDefaultParams]) -> Bo3ValorantLeaderboardResponse: ...

class _AsyncBo3Group:
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineStreamParams]) -> BinaryIO: ...
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineTextResponseParams]) -> str: ...
    @overload
    async def economy_baseline(self, **params: Unpack[Bo3EconomyBaselineDefaultParams]) -> Bo3EconomyBaselineResponse: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumStreamParams]) -> BinaryIO: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumTextResponseParams]) -> str: ...
    @overload
    async def forum(self, **params: Unpack[Bo3ForumDefaultParams]) -> Bo3ForumResponse: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesTextResponseParams]) -> str: ...
    @overload
    async def forum_categories(self, **params: Unpack[Bo3ForumCategoriesDefaultParams]) -> Bo3ForumCategoriesResponse: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[Bo3MatchDefaultParams]) -> Bo3MatchResponse: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesTextResponseParams]) -> str: ...
    @overload
    async def match_games(self, **params: Unpack[Bo3MatchGamesDefaultParams]) -> Bo3MatchGamesResponse: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryTextResponseParams]) -> str: ...
    @overload
    async def match_history(self, **params: Unpack[Bo3MatchHistoryDefaultParams]) -> Bo3MatchHistoryResponse: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersTextResponseParams]) -> str: ...
    @overload
    async def match_players(self, **params: Unpack[Bo3MatchPlayersDefaultParams]) -> Bo3MatchPlayersResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[Bo3NewsCategoriesDefaultParams]) -> Bo3NewsCategoriesResponse: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedTextResponseParams]) -> str: ...
    @overload
    async def news_feed(self, **params: Unpack[Bo3NewsFeedDefaultParams]) -> Bo3NewsFeedResponse: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[Bo3PlayerDefaultParams]) -> Bo3PlayerResponse: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def player_leaderboard(self, **params: Unpack[Bo3PlayerLeaderboardDefaultParams]) -> Bo3PlayerLeaderboardResponse: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_recent_matches(self, **params: Unpack[Bo3PlayerRecentMatchesDefaultParams]) -> Bo3PlayerRecentMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[Bo3PlayerStatsDefaultParams]) -> Bo3PlayerStatsResponse: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[Bo3RecordsDefaultParams]) -> Bo3RecordsResponse: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[Bo3TeamDefaultParams]) -> Bo3TeamResponse: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyStreamParams]) -> BinaryIO: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyTextResponseParams]) -> str: ...
    @overload
    async def team_prize_money(self, **params: Unpack[Bo3TeamPrizeMoneyDefaultParams]) -> Bo3TeamPrizeMoneyResponse: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesTextResponseParams]) -> str: ...
    @overload
    async def team_ranking_dates(self, **params: Unpack[Bo3TeamRankingDatesDefaultParams]) -> Bo3TeamRankingDatesResponse: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsTextResponseParams]) -> str: ...
    @overload
    async def team_rankings(self, **params: Unpack[Bo3TeamRankingsDefaultParams]) -> Bo3TeamRankingsResponse: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_recent_matches(self, **params: Unpack[Bo3TeamRecentMatchesDefaultParams]) -> Bo3TeamRecentMatchesResponse: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsTextResponseParams]) -> str: ...
    @overload
    async def team_stats(self, **params: Unpack[Bo3TeamStatsDefaultParams]) -> Bo3TeamStatsResponse: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[Bo3TournamentDefaultParams]) -> Bo3TournamentResponse: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolTextResponseParams]) -> str: ...
    @overload
    async def tournament_map_pool(self, **params: Unpack[Bo3TournamentMapPoolDefaultParams]) -> Bo3TournamentMapPoolResponse: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsTextResponseParams]) -> str: ...
    @overload
    async def tournament_mvps(self, **params: Unpack[Bo3TournamentMvpsDefaultParams]) -> Bo3TournamentMvpsResponse: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsTextResponseParams]) -> str: ...
    @overload
    async def tournament_squads(self, **params: Unpack[Bo3TournamentSquadsDefaultParams]) -> Bo3TournamentSquadsResponse: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesTextResponseParams]) -> str: ...
    @overload
    async def tournament_stages(self, **params: Unpack[Bo3TournamentStagesDefaultParams]) -> Bo3TournamentStagesResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[Bo3TournamentsDefaultParams]) -> Bo3TournamentsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[Bo3TransfersDefaultParams]) -> Bo3TransfersResponse: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def valorant_leaderboard(self, **params: Unpack[Bo3ValorantLeaderboardDefaultParams]) -> Bo3ValorantLeaderboardResponse: ...

Bo3EconomyBaselineDefaultParams = TypedDict('Bo3EconomyBaselineDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

Bo3EconomyBaselineTextResponseParams = TypedDict('Bo3EconomyBaselineTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

Bo3EconomyBaselineStreamParams = TypedDict('Bo3EconomyBaselineStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

Bo3ForumDefaultParams = TypedDict('Bo3ForumDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['activity', 'newest', 'comments', 'rating']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ForumTextResponseParams = TypedDict('Bo3ForumTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['activity', 'newest', 'comments', 'rating']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ForumStreamParams = TypedDict('Bo3ForumStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['activity', 'newest', 'comments', 'rating']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ForumCategoriesDefaultParams = TypedDict('Bo3ForumCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3ForumCategoriesTextResponseParams = TypedDict('Bo3ForumCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3ForumCategoriesStreamParams = TypedDict('Bo3ForumCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3MatchDefaultParams = TypedDict('Bo3MatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

Bo3MatchTextResponseParams = TypedDict('Bo3MatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

Bo3MatchStreamParams = TypedDict('Bo3MatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

Bo3MatchGamesDefaultParams = TypedDict('Bo3MatchGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_id': Required[int],
}, total=False)

Bo3MatchGamesTextResponseParams = TypedDict('Bo3MatchGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_id': Required[int],
}, total=False)

Bo3MatchGamesStreamParams = TypedDict('Bo3MatchGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_id': Required[int],
}, total=False)

Bo3MatchHistoryDefaultParams = TypedDict('Bo3MatchHistoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['finished', 'defwin', 'upcoming', 'current', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3MatchHistoryTextResponseParams = TypedDict('Bo3MatchHistoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['finished', 'defwin', 'upcoming', 'current', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3MatchHistoryStreamParams = TypedDict('Bo3MatchHistoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['finished', 'defwin', 'upcoming', 'current', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3MatchPlayersDefaultParams = TypedDict('Bo3MatchPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

Bo3MatchPlayersTextResponseParams = TypedDict('Bo3MatchPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

Bo3MatchPlayersStreamParams = TypedDict('Bo3MatchPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

Bo3NewsCategoriesDefaultParams = TypedDict('Bo3NewsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

Bo3NewsCategoriesTextResponseParams = TypedDict('Bo3NewsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

Bo3NewsCategoriesStreamParams = TypedDict('Bo3NewsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

Bo3NewsFeedDefaultParams = TypedDict('Bo3NewsFeedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb', 'games']],
    'section': NotRequired[Literal['news', 'article', 'wiki', 'predictions', 'reviews']],
    'tag': NotRequired[str],
    'locale': NotRequired[Literal['en', 'ru', 'pt', 'es', 'de', 'fr', 'tr', 'pl', 'id', 'vi', 'ja', 'ko', 'ua', 'ms', 'tl', 'da']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3NewsFeedTextResponseParams = TypedDict('Bo3NewsFeedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb', 'games']],
    'section': NotRequired[Literal['news', 'article', 'wiki', 'predictions', 'reviews']],
    'tag': NotRequired[str],
    'locale': NotRequired[Literal['en', 'ru', 'pt', 'es', 'de', 'fr', 'tr', 'pl', 'id', 'vi', 'ja', 'ko', 'ua', 'ms', 'tl', 'da']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3NewsFeedStreamParams = TypedDict('Bo3NewsFeedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb', 'games']],
    'section': NotRequired[Literal['news', 'article', 'wiki', 'predictions', 'reviews']],
    'tag': NotRequired[str],
    'locale': NotRequired[Literal['en', 'ru', 'pt', 'es', 'de', 'fr', 'tr', 'pl', 'id', 'vi', 'ja', 'ko', 'ua', 'ms', 'tl', 'da']],
    'category': NotRequired[int],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerDefaultParams = TypedDict('Bo3PlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3PlayerTextResponseParams = TypedDict('Bo3PlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3PlayerStreamParams = TypedDict('Bo3PlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3PlayerLeaderboardDefaultParams = TypedDict('Bo3PlayerLeaderboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'sort': NotRequired[Literal['rating', 'kd', 'kills', 'damage', 'assists', 'headshots', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerLeaderboardTextResponseParams = TypedDict('Bo3PlayerLeaderboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'sort': NotRequired[Literal['rating', 'kd', 'kills', 'damage', 'assists', 'headshots', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerLeaderboardStreamParams = TypedDict('Bo3PlayerLeaderboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'sort': NotRequired[Literal['rating', 'kd', 'kills', 'damage', 'assists', 'headshots', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerRecentMatchesDefaultParams = TypedDict('Bo3PlayerRecentMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerRecentMatchesTextResponseParams = TypedDict('Bo3PlayerRecentMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerRecentMatchesStreamParams = TypedDict('Bo3PlayerRecentMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3PlayerStatsDefaultParams = TypedDict('Bo3PlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'maps', 'accuracy']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3PlayerStatsTextResponseParams = TypedDict('Bo3PlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'maps', 'accuracy']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3PlayerStatsStreamParams = TypedDict('Bo3PlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'maps', 'accuracy']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3RecordsDefaultParams = TypedDict('Bo3RecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'record_type': NotRequired[str],
    'match': NotRequired[str],
    'tournament': NotRequired[str],
    'team': NotRequired[str],
    'player': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3RecordsTextResponseParams = TypedDict('Bo3RecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'record_type': NotRequired[str],
    'match': NotRequired[str],
    'tournament': NotRequired[str],
    'team': NotRequired[str],
    'player': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3RecordsStreamParams = TypedDict('Bo3RecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'record_type': NotRequired[str],
    'match': NotRequired[str],
    'tournament': NotRequired[str],
    'team': NotRequired[str],
    'player': NotRequired[str],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamDefaultParams = TypedDict('Bo3TeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamTextResponseParams = TypedDict('Bo3TeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamStreamParams = TypedDict('Bo3TeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamPrizeMoneyDefaultParams = TypedDict('Bo3TeamPrizeMoneyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamPrizeMoneyTextResponseParams = TypedDict('Bo3TeamPrizeMoneyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamPrizeMoneyStreamParams = TypedDict('Bo3TeamPrizeMoneyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamRankingDatesDefaultParams = TypedDict('Bo3TeamRankingDatesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamRankingDatesTextResponseParams = TypedDict('Bo3TeamRankingDatesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamRankingDatesStreamParams = TypedDict('Bo3TeamRankingDatesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TeamRankingsDefaultParams = TypedDict('Bo3TeamRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'region': NotRequired[str],
    'date': NotRequired[str],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
}, total=False)

Bo3TeamRankingsTextResponseParams = TypedDict('Bo3TeamRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'region': NotRequired[str],
    'date': NotRequired[str],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
}, total=False)

Bo3TeamRankingsStreamParams = TypedDict('Bo3TeamRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'region': NotRequired[str],
    'date': NotRequired[str],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
}, total=False)

Bo3TeamRecentMatchesDefaultParams = TypedDict('Bo3TeamRecentMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamRecentMatchesTextResponseParams = TypedDict('Bo3TeamRecentMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamRecentMatchesStreamParams = TypedDict('Bo3TeamRecentMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'opponent': NotRequired[str],
    'tournament': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

Bo3TeamStatsDefaultParams = TypedDict('Bo3TeamStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'advanced', 'accuracy', 'economy', 'map-pool']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3TeamStatsTextResponseParams = TypedDict('Bo3TeamStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'advanced', 'accuracy', 'economy', 'map-pool']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3TeamStatsStreamParams = TypedDict('Bo3TeamStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'kind': NotRequired[Literal['general', 'advanced', 'accuracy', 'economy', 'map-pool']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

Bo3TournamentDefaultParams = TypedDict('Bo3TournamentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TournamentTextResponseParams = TypedDict('Bo3TournamentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TournamentStreamParams = TypedDict('Bo3TournamentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
}, total=False)

Bo3TournamentMapPoolDefaultParams = TypedDict('Bo3TournamentMapPoolDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentMapPoolTextResponseParams = TypedDict('Bo3TournamentMapPoolTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentMapPoolStreamParams = TypedDict('Bo3TournamentMapPoolStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentMvpsDefaultParams = TypedDict('Bo3TournamentMvpsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentMvpsTextResponseParams = TypedDict('Bo3TournamentMvpsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentMvpsStreamParams = TypedDict('Bo3TournamentMvpsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentSquadsDefaultParams = TypedDict('Bo3TournamentSquadsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentSquadsTextResponseParams = TypedDict('Bo3TournamentSquadsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentSquadsStreamParams = TypedDict('Bo3TournamentSquadsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

Bo3TournamentStagesDefaultParams = TypedDict('Bo3TournamentStagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'slug': Required[str],
}, total=False)

Bo3TournamentStagesTextResponseParams = TypedDict('Bo3TournamentStagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'slug': Required[str],
}, total=False)

Bo3TournamentStagesStreamParams = TypedDict('Bo3TournamentStagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'slug': Required[str],
}, total=False)

Bo3TournamentsDefaultParams = TypedDict('Bo3TournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'event_type': NotRequired[Literal['lan', 'online']],
    'sort': NotRequired[Literal['newest', 'oldest', 'prize']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentsTextResponseParams = TypedDict('Bo3TournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'event_type': NotRequired[Literal['lan', 'online']],
    'sort': NotRequired[Literal['newest', 'oldest', 'prize']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TournamentsStreamParams = TypedDict('Bo3TournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'valorant', 'lol', 'dota2', 'r6siege', 'mlbb']],
    'status': NotRequired[Literal['current', 'upcoming', 'finished', 'canceled', 'postponed']],
    'tier': NotRequired[Literal['s', 'a', 'b', 'c', 'd']],
    'event_type': NotRequired[Literal['lan', 'online']],
    'sort': NotRequired[Literal['newest', 'oldest', 'prize']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TransfersDefaultParams = TypedDict('Bo3TransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': NotRequired[int],
    'player_id': NotRequired[int],
    'action': NotRequired[Literal['join', 'change', 'leave']],
    'role': NotRequired[Literal['player', 'coach']],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TransfersTextResponseParams = TypedDict('Bo3TransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': NotRequired[int],
    'player_id': NotRequired[int],
    'action': NotRequired[Literal['join', 'change', 'leave']],
    'role': NotRequired[Literal['player', 'coach']],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3TransfersStreamParams = TypedDict('Bo3TransfersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': NotRequired[int],
    'player_id': NotRequired[int],
    'action': NotRequired[Literal['join', 'change', 'leave']],
    'role': NotRequired[Literal['player', 'coach']],
    'sort': NotRequired[Literal['newest', 'oldest']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ValorantLeaderboardDefaultParams = TypedDict('Bo3ValorantLeaderboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['acs', 'kills', 'deaths', 'damage', 'assists', 'first_kills', 'clutches', 'first_duels', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ValorantLeaderboardTextResponseParams = TypedDict('Bo3ValorantLeaderboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['acs', 'kills', 'deaths', 'damage', 'assists', 'first_kills', 'clutches', 'first_duels', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

Bo3ValorantLeaderboardStreamParams = TypedDict('Bo3ValorantLeaderboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'sort': NotRequired[Literal['acs', 'kills', 'deaths', 'damage', 'assists', 'first_kills', 'clutches', 'first_duels', 'games', 'rounds']],
    'order': NotRequired[Literal['desc', 'asc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)
