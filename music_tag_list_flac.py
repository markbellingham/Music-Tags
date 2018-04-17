"""Functions for flac files."""


def artist(audio):
    """Return the artist name."""
    try:
        return(audio['artist'][0])
    except Exception:
        return(" ")


def album(audio):
    """Return the album name."""
    try:
        return(audio['album'][0])
    except Exception:
        return(" ")


def album_artist(audio):
    """Return the album artist name."""
    try:
        return(audio['albumartist'][0])
    except Exception:
        return(" ")


def trackna(audio):
    """Return the track name."""
    try:
        return(audio['title'][0])
    except Exception:
        return(" ")


def trackno(audio):
    """Return the track number."""
    try:
        return(audio['tracknumber'][0])
    except Exception:
        return(" ")


def genre(audio):
    """Return the genre."""
    try:
        return(audio['genre'][0])
    except Exception:
        return(" ")


def duration(audio):
    """Return the duration."""
    try:
        duration = audio.info.length
        duration = int(round(duration))
        str_duration = '{}m{:02d}s'.format(*divmod(duration, 60))
        return(str_duration)
    except Exception:
        return(" ")


def year(audio):
    """Return the year."""
    try:
        return(audio['date'][0])
    except Exception:
        return(" ")
