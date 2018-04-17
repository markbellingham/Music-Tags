"""Functions for mp3 files."""


def artist(audio):
    """Return the Artist name."""
    try:
        return (audio['TPE1'].text[0])
    except Exception:
        return (" ")


def album_artist(audio):
    """Return the Album Artist."""
    try:
        return(audio['TPE2'].text[0])
    except Exception:
        return(" ")


def album(audio):
    """Return the Album name."""
    try:
        return(audio['TALB'].text[0])
    except Exception:
        return(" ")


def trackno(audio):
    """Return the Track #."""
    try:
        return(audio['TRCK'].text[0])
    except Exception:
        return(" ")


def trackna(audio):
    """Return the track name."""
    try:
        return(audio["TIT2"].text[0])
    except Exception:
        return(" ")


def length(audio):
    """Return the length."""
    try:
        duration = audio['TLEN'].text[0]
        duration = round(int(duration) / 1000)
        str_duration = '{}m{:02d}s'.format(*divmod(duration, 60))
        return(str_duration)
    except Exception:
        return(" ")


def genre(audio):
    """Return the genre."""
    try:
        return(audio['TCON'].text[0])
    except Exception:
        return(" ")


def year(audio):
    """Return the Year."""
    try:
        return(audio["TDRC"].text[0])
    except Exception:
        return(" ")
