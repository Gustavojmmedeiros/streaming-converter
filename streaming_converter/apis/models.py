from dataclasses import dataclass


@dataclass()
class Song:
    """Represents a song"""

    id: str
    name: str
    album: str
    artist: str

    def __str__(self):
        return f"{self.artist} - {self.name} [{self.album}]"

    def __eq__(self, other):
        if isinstance(other, Song):
            return (self.name, self.album, self.artist) == (
                other.name,
                other.album,
                other.artist,
            )
