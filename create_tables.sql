DROP TABLE tracks;
DROP TABLE albums;
DROP TABLE artists;
DROP TABLE genres;

CREATE TABLE genres (
  genre_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  genre VARCHAR(50)
);

CREATE TABLE artists (
  artist_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  artist VARCHAR(50)
);

CREATE TABLE albums (
  album_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  artist VARCHAR(50),
  album_artist VARCHAR(50),
  title VARCHAR(100),
  genre VARCHAR(50),
  year VARCHAR(20),
  image VARCHAR(150)
);

CREATE TABLE tracks (
  trackId INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  track_no VARCHAR(5),
  track_name VARCHAR(100),
  album_title VARCHAR(100),
  duration VARCHAR(10),
  filename VARCHAR(200)
);

-----------------------------------------------------------------------

ALTER TABLE tracks ADD COLUMN album_id INT(10),
ADD CONSTRAINT fk_album_id FOREIGN KEY (album_id) REFERENCES albums (album_id);

ALTER TABLE albums ADD COLUMN genre_id INT(10),
ADD CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES genres (genre_id);

ALTER TABLE albums ADD COLUMN artist_id INT(10),
ADD CONSTRAINT fk_artist_id FOREIGN KEY (artist_id) REFERENCES artists (artist_id);

-----------------------------------------------------------------------

UPDATE albums JOIN artists ON albums.artist = artists.artist
SET albums.artist_id = artists.artist_id
WHERE albums.artist = artists.artist;

UPDATE albums JOIN genres ON albums.genre = genres.genre
SET albums.genre_id = genres.genre_id
WHERE albums.genre = genres.genre;

-- Checks for duplicates in the albums table
SELECT title
FROM albums
GROUP BY title
HAVING count(*) > 1;
