import json
import pytest
from unittest.mock import patch
from streaming_converter.apis.youtube.api import YoutubeAPI


# NEXT
@patch("streaming_converter.apis.http_request.req")
def test_playlist_list_songs(mock_req):
    f1 = open("tests/apis/youtube/responses/get_songs_first_resp.json")
    f2 = open("tests/apis/youtube/responses/get_songs_continuation.json")

    side_effect = [True, json.load(f1), json.load(f2)]

    api = YoutubeAPI("TEST_AUTH_TOKEN", "TEST_COOKIE")
    is_ok, response = api.playlist_list_songs("TEST_PLAYLIST_ID")

    print(is_ok, response)

    f1.close()
    f2.close()

    pass
