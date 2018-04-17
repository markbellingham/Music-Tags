"""Program to output tags from music files."""

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
import music_tag_list_mp3 as mtl_mp3
import music_tag_list_flac as mtl_flac


def get_tag_values():
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
                audio = MP3(filename)

                artist = mtl_mp3.artist(audio)
                album_artist = mtl_mp3.album_artist(audio)
                album = mtl_mp3.album(audio)
                trackno = mtl_mp3.trackno(audio)
                trackna = mtl_mp3.trackna(audio)
                duration = mtl_mp3.length(audio)
                genre = mtl_mp3.genre(audio)
                year = mtl_mp3.year(audio)

            elif filename.endswith('.flac'):
                audio = FLAC(filename)

                artist = mtl_flac.artist(audio)
                album_artist = mtl_flac.album_artist(audio)
                album = mtl_flac.album(audio)
                trackno = mtl_flac.trackno(audio)
                trackna = mtl_flac.trackna(audio)
                duration = mtl_flac.duration(audio)
                genre = mtl_flac.genre(audio)
                year = mtl_flac.year(audio)

            elif filename.endswith('.ogg'):
                audio = OggVorbis(filename)

                artist = mtl_flac.artist(audio)
                album_artist = mtl_flac.album_artist(audio)
                album = mtl_flac.album(audio)
                trackno = mtl_flac.trackno(audio)
                trackna = mtl_flac.trackna(audio)
                duration = mtl_flac.duration(audio)
                genre = mtl_flac.genre(audio)
                year = mtl_flac.year(audio)


get_tag_values()
