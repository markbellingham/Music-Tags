DROP TABLE albums;

CREATE TABLE albums (
  album_id INT(10) NOT NULL AUTO_INCREMENT,
  artist VARCHAR(50),
  album_artist VARCHAR(50),
  title VARCHAR(100),
  genre VARCHAR(20),
  year VARCHAR(20),
  PRIMARY KEY (album_id)
);
