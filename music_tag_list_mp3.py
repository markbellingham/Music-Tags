"""Functions for mp3 files."""


def artist(audio, filename):
    """Print the Artist name."""
    try:
        print("Artist: %s" % audio['TPE1'].text[0])
    except Exception as error:
        print(error, " - Artist not found.")


def album_artist(audio, filename):
    """Print the Album Artist."""
    try:
        print("Album Artist: %s" % audio['TPE2'].text[0])
    except Exception as error:
        print(error, " - Album Artist not found.")


def album(audio, filename):
    """Print the Album name."""
    try:
        print("Album: %s" % audio['TALB'].text[0])
    except Exception as error:
        print(error, " - Album not found.")


def trackno(audio, filename):
    """Print the Track #."""
    try:
        print("Track #: %s" % audio['TRCK'].text[0])
    except Exception as error:
        print(error, " - Track number not found.")


def trackna(audio, filename):
    """Print the track name."""
    try:
        print("Track: %s" % audio["TIT2"].text[0])
    except Exception as error:
        print(error, " - Track name not found.")


def length(audio, filename):
    """Print the length."""
    try:
        print("Length: %s" % audio['TLEN'].text[0])
    except Exception as error:
        print(error, " - Length not found.")


def genre(audio, filename):
    """Print the genre."""
    try:
        print("Genre: %s" % audio['TCON'].text[0])
    except Exception as error:
        print(error, " - Genre not found.")


def year(audio, filename):
    """Print the Year."""
    try:
        print("Release Year: %s" % audio["TDRC"].text[0])
    except Exception as error:
        print(error, " - Year not found.")
