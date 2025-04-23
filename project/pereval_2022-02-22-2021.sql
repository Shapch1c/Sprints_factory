-- -------------------------------------------------------------
-- Database: pereval
-- -------------------------------------------------------------
-- Таблица пользователей
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  fam VARCHAR(255),
  name VARCHAR(255),
  otc VARCHAR(255),
  phone VARCHAR(20)
);

-- Таблица координат
CREATE TABLE coords (
  id SERIAL PRIMARY KEY,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  height INTEGER NOT NULL
);

-- Таблица перевалов
CREATE TABLE pereval_added (
  id SERIAL PRIMARY KEY,
  beauty_title VARCHAR(255),
  title VARCHAR(255),
  other_titles VARCHAR(255),
  connect VARCHAR(255),
  add_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  user_id INTEGER REFERENCES users(id),
  coord_id INTEGER REFERENCES coords(id),
  level_winter VARCHAR(10),
  level_summer VARCHAR(10),
  level_autumn VARCHAR(10),
  level_spring VARCHAR(10),
  status VARCHAR(20) DEFAULT 'new' CHECK (status IN ('new', 'pending', 'accepted', 'rejected'))
);

-- Таблица изображений
CREATE TABLE images (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  data BYTEA NOT NULL
);

-- Связующая таблица для перевалов и изображений
CREATE TABLE pereval_images (
  pereval_id INTEGER REFERENCES pereval_added(id),
  image_id INTEGER REFERENCES images(id),
  PRIMARY KEY (pereval_id, image_id)
);


