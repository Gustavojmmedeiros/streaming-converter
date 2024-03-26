import json
import pytest

from streaming_converter.apis.models import Song
from streaming_converter.apis.navigation import get_value_by_path_list
from streaming_converter.apis.youtube.parsers import (
    get_continuation_token,
    get_songs_to_parse,
    parse_songs,
)
from streaming_converter.apis.youtube.paths import (
    SONGS_TO_PARSE,
    SONGS_TO_PARSE_CONTINUATION,
)


def test_get_continuation_token_success():
    with open("tests/apis/youtube/responses/get_songs_first_resp.json") as f:
        data = json.load(f)
    assert get_continuation_token(data) == "TESTCONTINUATIONTOKEN"


def test_get_continuation_token_fail():
    data = {"Lorem": "Ipsum"}
    assert get_continuation_token(data) is None


@pytest.mark.parametrize(
    "test_file_name, is_continuation, expected",
    [
        ("get_songs_first_resp.json", False, 2),
        ("get_songs_first_resp.json", True, None),
        ("get_songs_continuation.json", True, 3),
        ("get_songs_continuation.json", False, None),
    ],
)
def test_get_songs_to_parse(test_file_name, is_continuation, expected):
    with open("tests/apis/youtube/responses/" + test_file_name) as f:
        data = json.load(f)
    result = get_songs_to_parse(data, is_continuation)
    assert result is None if expected is None else len(result) == expected


@pytest.mark.parametrize(
    "test_file_name, is_continuation, expected",
    [
        (
            "get_songs_first_resp.json",
            False,
            [
                Song("SONG1_ID", "SONG1_NAME", "SONG1_ALBUM", "SONG1_ARTIST"),
                Song("SONG2_ID", "SONG2_NAME", "SONG2_ALBUM", "SONG2_ARTIST"),
            ],
        ),
        (
            "get_songs_continuation.json",
            True,
            [
                Song("SONG1_ID", "SONG1_NAME", "SONG1_ALBUM", "SONG1_ARTIST"),
                Song("SONG2_ID", "SONG2_NAME", "SONG2_ALBUM", "SONG2_ARTIST"),
                Song("SONG3_ID", "SONG3_NAME", "SONG3_ALBUM", "SONG3_ARTIST"),
            ],
        ),
    ],
)
def test_parse_songs(test_file_name, is_continuation, expected):
    with open("tests/apis/youtube/responses/" + test_file_name) as f:
        data = json.load(f)

    if is_continuation:
        to_parse = get_value_by_path_list(SONGS_TO_PARSE_CONTINUATION, data)
    else:
        to_parse = get_value_by_path_list(SONGS_TO_PARSE, data)

    assert parse_songs(to_parse) == expected
