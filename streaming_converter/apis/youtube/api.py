import json
import structlog
from urllib.parse import urljoin
from streaming_converter.apis.youtube.parsers import (
    parse_songs,
    get_songs_to_parse,
    get_continuation_token,
)
from streaming_converter.apis.models import Song
from streaming_converter.apis.http_request import req

log = structlog.get_logger(__name__)


class YoutubeAPI:
    URL = "https://music.youtube.com/youtubei"
    CLIENT_NAME = "WEB_REMIX"
    CLIENT_VERSION = "1.20240131.01.00"

    def __init__(self, auth_token: str, cookie: str):
        self.auth_token = auth_token
        self.cookie = cookie
        self.token = None

    def search():
        pass

    def user_get_playlists():
        pass

    def playlist_add_song():
        pass

    def playlist_create():
        pass

    def playlist_list_songs(self, playlist_id: str) -> list[Song]:
        # TODO (docs): 100 musics for each page (no limit)

        url = urljoin(self.URL, "v1/browse")
        body = {
            "context": {
                "client": {
                    "clientName": self.CLIENT_NAME,
                    "clientVersion": self.CLIENT_VERSION,
                }
            }
        }
        body["browseId"] = playlist_id

        headers = {
            "Origin": self.URL,
            "Authorization": self.auth_token,
            "Cookie": self.cookie,
        }

        params = {}
        to_parse = []
        is_continuation = False

        while True:
            is_ok, r = req(
                "POST",
                url=url,
                data=json.dumps(body),
                headers=headers,
                params=params,
            )

            print(is_ok, r)
            if not is_ok:
                log.error("Http error on listing songs", message=r.message)
                return None

            response = r.json()

            to_parse.extend(get_songs_to_parse(response, is_continuation))

            ctoken = get_continuation_token(response)
            if not ctoken:
                break

            is_continuation = True
            params = {"ctoken": ctoken, "continuation": ctoken}

        return parse_songs(to_parse)
