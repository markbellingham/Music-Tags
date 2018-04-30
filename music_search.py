"""Program to output tags from music files."""


import os
import database as db
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
import music_tag_list_mp3 as mtl_mp3
import music_tag_list_flac as mtl_flac


'''
Notes:
The program generates lists for artist, album_artist, album and tracks.
Once tables have been created, the primary key for artist, album_artist and
genre can replace their name in the albums and tracks tables. The printout from
the script should first be checked for errors and duplicates of the artists.
'''


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
    This will hold the list of albums, artists and genres so that separate
    tables can be created without duplicates.
    '''
    albums = []
    artists = []
    genres = []
    track = []

    genre_sql = "INSERT INTO genres (genre) VALUES (%s)"
    artist_sql = "INSERT INTO artists (artist) VALUES (%s)"
    album_sql = "INSERT INTO albums (artist, album_artist, title, genre, year, image) VALUES (%s, %s, %s, %s, %s, %s)"
    track_sql = "INSERT INTO tracks (track_no, track_name, album_title, duration, filename) VALUES (%s, %s, %s, %s, %s)"
    album_data = []
    track_data = []

    'Supported filetypes'
    ext = ('mp3', 'flac', 'ogg')

    '''
    Search the filesystem. For each audio file found, create a full filename
    including the path and pass it to the relevant decoder to extract the tags.
    '''
    for root, subdir, files in os.walk(path):
        for filename in files:
            full_filename = os.path.join(root, filename)
            if filename.endswith(tuple(ext)):
                at = get_tag_values(full_filename)
                image = (str(root) + "/folder.jpg")
                if at['artist'] not in artists:
                    artists.append(at['artist'])
                if at['album_artist'] not in artists:
                    artists.append(at['album_artist'])
                if at['genre'] not in genres:
                    genres.append(at['genre'])
                if at['album'] not in albums:
                    albums.append(at['album'])
                    album = [at['artist'], at['album_artist'], at['album'], at['genre'], str(at['year']), image]
                    album_data.append(album)
                track = [at['trackno'], at['trackna'], at['album'], at['duration'], str(full_filename)]
                track_data.append(track)

    db.insert_many(genre_sql, genres)
    db.insert_many(artist_sql, artists)
    db.insert_many(album_sql, album_data)
    # n = 1
    # for values in track_data:
    #     print(n, values)
    #     n = n + 1
    db.insert_many(track_sql, track_data)

    # with open('music_db.sql', 'w') as f:
    #     f.write(sql + '\n')
    #     for x in album_data:
    #         f.write('("' + '","'.join(x) + '"),\n')
    #     f.write('\n')
    #     for x in artists:
    #         f.write(x + '\n')
    #     f.write('\n')
    #     for x in genres:
    #         f.write(x + '\n')
    #     f.write('\n')
    #     for x in track_data:
    #         f.write('("' + '","'.join(x) + '"),\n')
    # f.close()


main()
