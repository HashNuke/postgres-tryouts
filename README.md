# postgres-tryouts





```
# Create the database for the rest of the adventure
psql -c 'create database tryouts'
```

### To prepare the Product Hunt dataset

* The Product Hunt dataset can be downloaded [here](https://data.world/producthunt/product-hunt-research).
* Look for the `PostsForExploration.csv` file to download.
* Run the script below to convert the CSV into insert statements

```
python producthunt.py PostsForExploration.csv > producthunt.sql
psql -D tryouts producthunt-schema.sql
psql -D tryouts producthunt.sql
```

### To prepare the MoMA dataset

This is the data set of Artists and Artworks by Museum of Modern Art available on GitHub.

In order to download this dataset, please ensure that you have the following installed:

* [Git](https://git-scm.com/)
* [Git Large File Storage](https://git-lfs.github.com/)

After Git LFS is installed, ensure to run `git lfs install` command to install Git LFS for your computer user account before cloning the dataset below.

```
# To install Git LFS for your user account
git lfs install

# Download the MoMA dataset
git clone git@github.com:MuseumofModernArt/collection.git
mv collection moma-collection

# Load the schema for the dataset into the database
psql -D tryouts moma-schema.sql
python moma-artists.py > moma-artists.sql
python moma-artworks.py > moma-artworks.sql
psql -D tryouts moma-artists.sql
psql -D tryouts moma-artworks.sql
```
