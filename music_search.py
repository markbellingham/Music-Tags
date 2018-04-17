"""Program to output tags from music files."""

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
import music_tag_list_mp3 as mtl_mp3
import music_tag_list_flac as mtl_flac


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
                try:
                    audio = MP3(filename)
                    mtl_mp3.artist(audio, filename) or \
                        mtl_mp3.album_artist(audio, filename) or \
                        mtl_mp3.album(audio, filename) or \
                        mtl_mp3.trackno(audio, filename) or \
                        mtl_mp3.trackna(audio, filename) or \
                        mtl_mp3.length(audio, filename) or \
                        mtl_mp3.genre(audio, filename) or \
                        mtl_mp3.year(audio, filename)
                except Exception as error:
                    print("mp3 - " + filename)
                    print(error)
                finally:
                    print()
            elif filename.endswith('.flac'):
                try:
                    audio = FLAC(filename)
                    mtl_flac.artist(audio, filename) or \
                        mtl_flac.album_artist(audio, filename) or \
                        mtl_flac.album(audio, filename) or \
                        mtl_flac.trackno(audio, filename) or \
                        mtl_flac.trackna(audio, filename) or \
                        mtl_flac.duration(audio, filename) or \
                        mtl_flac.genre(audio, filename) or \
                        mtl_flac.year(audio, filename)
                except Exception as error:
                    print("error - ", error)
                finally:
                    print()
            elif filename.endswith('.ogg'):
                try:
                    audio = OggVorbis(filename)
                    mtl_flac.artist(audio, filename) or \
                        mtl_flac.album_artist(audio, filename) or \
                        mtl_flac.album(audio, filename) or \
                        mtl_flac.trackno(audio, filename) or \
                        mtl_flac.trackna(audio, filename) or \
                        mtl_flac.duration(audio, filename) or \
                        mtl_flac.genre(audio, filename) or \
                        mtl_flac.year(audio, filename)
                except Exception as error:
                    print("error - ", error)
                finally:
                    print()


main()
