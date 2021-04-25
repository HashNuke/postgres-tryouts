INSERT INTO artist_contributions (artwork_id, artist_id) (
  SELECT
    id AS artwork_id,
    UNNEST(artist_ids) AS artist_id
  FROM artworks
)
