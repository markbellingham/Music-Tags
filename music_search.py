"""Program to output tags from music files."""

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
# from mutagen.mp3 import EasyMP3 as MP3


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


def main():
    """Main controller."""
    # Specify the root directory
    path = "/home/mark/Music/"

    # List of the filetypes that are supported by the program
    # ext = ('.mp3', '.ogg', '.flac')

    '''
    Search the filesystem. For each file found, check if the extension is
    on the supported list. If it is, create a full filename including
    the path and
    '''
    for root, subdir, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root, filename)
            if filename.endswith('.mp3'):
                print("mp3 - " + filename)
                try:
                    audio = MP3(filename)
                    artist(audio, filename) or \
                        album_artist(audio, filename) or \
                        album(audio, filename) or \
                        trackno(audio, filename) or \
                        trackna(audio, filename) or \
                        length(audio, filename) or \
                        genre(audio, filename) or \
                        year(audio, filename)
                except Exception as error:
                    print("mp3 - " + filename)
                    print(error)
                finally:
                    print()
            elif filename.endswith('.flac'):
                try:
                    audio = FLAC(filename)
                    print("flac title: ", audio['title'][0])
                    print("flac artist: ", audio['artist'][0])
                    print("flac album: ", audio['album'][0])
                    print("track number: ", audio['tracknumber'][0])
                    print("genre: ", audio['genre'][0])
                    print("duration: ", audio.info.length)
                    print("flac album artist: ", audio['albumartist'][0])
                except Exception as error:
                    print("error - ", error)
                finally:
                    print()


main()
