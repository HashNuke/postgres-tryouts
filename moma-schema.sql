CREATE TABLE IF NOT EXISTS artworks(
  id SERIAL PRIMARY KEY,
  title TEXT,
  artist_id INTEGER,
  painting_date DATE,
  classification TEXT,
  department TEXT,
  date_acquired TEXT,
  width NUMERIC(8,2),
  height NUMERIC(8,2),
  website_url TEXT,
  thumbnail_url TEXT
);

CREATE TABLE IF NOT EXISTS artists(
  id SERIAL PRIMARY KEY,
  name TEXT,
  bio TEXT,
  nationality TEXT,
  gender TEXT,
  ulan TEXT
);
