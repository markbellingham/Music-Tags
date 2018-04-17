"""Functions for flac files."""


def artist(audio, filename):
    """Print the artist name."""
    try:
        print("flac artist: ", audio['artist'][0])
    except Exception as error:
        print(error, " - Artist not found")


def album(audio, filename):
    """Print the album name."""
    try:
        print("flac album: ", audio['album'][0])
    except Exception as error:
        print(error, " - Album not found")


def album_artist(audio, filename):
    """Print the album artist name."""
    try:
        print("flac album artist: ", audio['albumartist'][0])
    except Exception as error:
        print(error, " - Album artist not found")


def trackna(audio, filename):
    """Print the track name."""
    try:
        print("flac track: ", audio['title'][0])
    except Exception as error:
        print(error, " - Track name not found")


def trackno(audio, filename):
    """Print the track number."""
    try:
        print("flac track #: ", audio['tracknumber'][0])
    except Exception as error:
        print(error, " - Track # not found")


def genre(audio, filename):
    """Print the genre."""
    try:
        print("genre: ", audio['genre'][0])
    except Exception as error:
        print(error, " - Genre not found")


def duration(audio, filename):
    """Print the duration."""
    try:
        duration = audio.info.length
        duration = int(round(duration))
        str_duration = '{}m{:02d}s'.format(*divmod(duration, 60))
        print("duration: ", str_duration)
    except Exception as error:
        print(error, " - Duration not found")


def year(audio, filename):
    """Print the year."""
    try:
        print("Release year: ", audio['date'][0])
    except Exception as error:
        print(error, " - Year not found")
