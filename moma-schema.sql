CREATE TABLE IF NOT EXISTS artworks(
  id SERIAL PRIMARY KEY,
  title TEXT,
  classification TEXT,
  department TEXT,
  date_acquired DATE,
  artwork_year TEXT,
  website_url TEXT,
  thumbnail_url TEXT,
  artist_ids INTEGER[]
);

CREATE TABLE IF NOT EXISTS artist_contributions(
  id SERIAL PRIMARY KEY,
  artist_id INTEGER,
  artwork_id INTEGER
);

CREATE INDEX IF NOT EXISTS artwork_contrib_idx ON artist_contributions(artwork_id);

CREATE TABLE IF NOT EXISTS artists(
  id SERIAL PRIMARY KEY,
  name TEXT,
  bio TEXT,
  nationality TEXT,
  gender TEXT,
  ulan TEXT
);
