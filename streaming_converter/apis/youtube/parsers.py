import structlog

from streaming_converter.apis.navigation import get_value_by_path_list
from streaming_converter.apis.models import Song
from streaming_converter.apis.youtube.paths import (
    SONGS_TO_PARSE,
    SONGS_TO_PARSE_CONTINUATION,
    SONGS_BASE,
    CONTINUATION_TOKEN_PATH,
    SONG_ID_PATH,
    SONG_NAME_PATH,
    SONG_ALBUM_PATH,
    SONG_ARTIST_PATH,
)


log = structlog.get_logger(__name__)


def parse_songs(to_parse: dict) -> list[Song]:
    """Parse the json information from the Youtube List API and transform
    on a song

    Args:
        to_parse (dict):
            Subset of the response from the list songs API that contains the
            song information.

    Returns:
        list[Song]: List of songs on the playlist
    """

    songs = []
    for s in to_parse:
        song_info = get_value_by_path_list(SONGS_BASE, s)
        songs.append(
            Song(
                id=get_value_by_path_list(SONG_ID_PATH, song_info),
                name=get_value_by_path_list(SONG_NAME_PATH, song_info),
                album=get_value_by_path_list(SONG_ALBUM_PATH, song_info),
                artist=get_value_by_path_list(SONG_ARTIST_PATH, song_info),
            )
        )

    log.debug(f"Parsed {len(to_parse)} songs")

    return songs


def get_songs_to_parse(data: dict, is_continuation: bool) -> list[dict]:
    """Get the path of the list where the songs information are stored based
    if it is a continuation or not. A continuation is how Youtube API handles
    pagination, this is, each page different from the first is a continuation
    and the paths from the dict are different.

    Args:
        data (dict): Response from the list music endpoint of the API
        is_continuation (bool): False if it is the first page

    Returns:
        list[dict]: List of dicts that contains song information
    """

    if is_continuation:
        return get_value_by_path_list(SONGS_TO_PARSE_CONTINUATION, data)
    else:
        return get_value_by_path_list(SONGS_TO_PARSE, data)


def get_continuation_token(data: dict) -> str:
    """Get the continuation token from a request into Youtube API. A
    continuation token exists if there is more content to fetch from the
    request. Its the way Youtube do pagination

    Args:
        data (dict): Response from the list music endpoint of the API

    Returns:
        str: Continuation token
    """

    return get_value_by_path_list(CONTINUATION_TOKEN_PATH, data)
