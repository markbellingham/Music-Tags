"""Program to output tags from music files."""

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
import music_tag_list_mp3 as mtl_mp3
import music_tag_list_flac as mtl_flac


def get_tag_values(filename):
    """Function to get the tag values."""
    # Initialise variables
    artist = ""
    album_artist = ""
    album = ""
    trackno = ""
    trackna = ""
    duration = ""
    genre = ""
    year = ""

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

    album_tags = {'artist': artist, 'album_artist': album_artist,
                  'album': album, 'trackno': trackno, 'trackna': trackna,
                  'duration': duration, 'genre': genre, 'year': year}

    return album_tags


def main():
    """Main controller."""
    # Specify the root directory
    path = "/home/mark/Music/"

    '''
    This will hold the list of albums so that
    the tracks do not generate duplicates
    '''
    albums = []

    with open('music_db.sql', 'w') as f:
        sql = "INSERT INTO music\n (artist, album-artist, album, genre, year)\n VALUES\n "
        f.write(sql)

    '''
    Search the filesystem. For each audio file found, create a
        full filename including the path and pass it to the
        relevant decoder to extract the tags
    '''
    for root, subdir, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root, filename)
            at = get_tag_values(filename)
            if at['album'] not in albums:
                albums.append(at['album'])
                with open('music_db.sql', 'a') as f:
                    f.write('("' + at['artist'] + '","' + at['album_artist']
                            + '","' + at['album'] + '","' + at['genre'] + '","'
                            + str(at['year']) + '"),\n')


main()
