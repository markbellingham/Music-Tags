"""Program to output tags from music files."""

import os
import mutagen
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
# from mutagen.mp3 import EasyMP3 as MP3


def artist(audio, filename):
    """Print the Artist name."""
    try:
        print("Artist: %s" % audio['TPE1'].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def album(audio, filename):
    """Print the Album name."""
    try:
        print("Album: %s" % audio['TALB'].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def trackno(audio, filename):
    """Print the Track #."""
    try:
        print("Track #: %s" % audio['TRCK'].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def trackna(audio, filename):
    """Print the track name."""
    try:
        print("Track: %s" % audio["TIT2"].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def length(audio, filename):
    """Print the length."""
    try:
        print("Length: %s" % audio['TLEN'].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def year(audio, filename):
    """Print the Year."""
    try:
        print("Release Year: %s" % audio["TDRC"].text[0])
    except Exception as error:
        print("filename: " + filename)
        print(error)


def main():
    """Main controller."""
    # Specify the root directory
    path = "/home/mark/Music/"
    # This version selects the user's home directory for the root
    # path = expanduser("~")

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
            audio = mutagen.File(filename)
            if filename.endswith('.mp3'):
                try:
                    artist(audio, filename) or \
                        album(audio, filename) or \
                        trackno(audio, filename) or \
                        trackna(audio, filename) or \
                        length(audio, filename) or \
                        year(audio, filename)
                except Exception as error:
                    print("mp3 - " + filename)
                    print(error)
                finally:
                    print()
            elif filename.endswith('.flac'):
                print("flac - " + filename)
                print()


main()
