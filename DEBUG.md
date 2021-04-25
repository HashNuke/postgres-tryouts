# Debug scripts

Additional scripts to make life easier when debugging.

## Drop everything and repopulate MoMA tables

```
psql -d tryouts -c 'DROP TABLE artworks' && \
psql -d tryouts -c 'DROP TABLE artists' && \
psql -d tryouts -c 'DROP TABLE artist_contributions' && \
psql -d tryouts < moma-schema.sql && \
python3 moma-artists.py moma-collection/Artists.json && \
python3 moma-artworks.py moma-collection/Artworks.json && \
psql -d tryouts < moma-artist-contributions.sql
```

## Drop everything and repopulate Product Hunt Posts table

```
psql -d tryouts -c 'DROP TABLE ph_posts' && \
psql -d tryouts producthunt-schema.sql && \
python producthunt.py PostsForExploration.csv
```
