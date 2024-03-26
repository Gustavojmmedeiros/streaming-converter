# Base Path for Listing Songs Information
LIST_SONGS_BASE = [
    "contents",
    "singleColumnBrowseResultsRenderer",
    "tabs",
    0,
    "tabRenderer",
    "content",
    "sectionListRenderer",
    "contents",
    0,
    "musicPlaylistShelfRenderer",
]

# These paths contains the contents of the songs mixed with some rendering from
# youtube. For the first request and for the continuations (pagination)
SONGS_TO_PARSE = LIST_SONGS_BASE + ["contents"]
SONGS_TO_PARSE_CONTINUATION = [
    "continuationContents",
    "musicPlaylistShelfContinuation",
    "contents",
]

# The first level before getting information about the songs
SONGS_BASE = ["musicResponsiveListItemRenderer", "flexColumns"]

# Common path to get information about the songs
SONG_INFO_BASE_PATH = [
    "musicResponsiveListItemFlexColumnRenderer",
    "text",
    "runs",
    0,
]
SONG_ID_SUFFIX = ["navigationEndpoint", "browseEndpoint", "browseId"]
SONG_NAME_ALBUM_ARTIST_SUFFIX = ["text"]

# Paths used to get the information about the songs
SONG_ID_PATH = [1] + SONG_INFO_BASE_PATH + SONG_ID_SUFFIX
SONG_NAME_PATH = [0] + SONG_INFO_BASE_PATH + SONG_NAME_ALBUM_ARTIST_SUFFIX
SONG_ARTIST_PATH = [1] + SONG_INFO_BASE_PATH + SONG_NAME_ALBUM_ARTIST_SUFFIX
SONG_ALBUM_PATH = [2] + SONG_INFO_BASE_PATH + SONG_NAME_ALBUM_ARTIST_SUFFIX

# Path to the continuation token (pagination)
CONTINUATION_TOKEN_PATH = LIST_SONGS_BASE + [
    "continuations",
    0,
    "nextContinuationData",
    "continuation",
]
