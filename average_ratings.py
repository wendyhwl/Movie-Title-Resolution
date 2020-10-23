"""
* CMPT353 Exercise 4.1: Movie Title Entity Resolution
* June 12, 2020
"""

import sys
import numpy as np
import pandas as pd
import difflib # for matching similar strings

def match_movie_name(name):
    match = difflib.get_close_matches(name, movies['title'], cutoff=0.6)
    return match

# command line takes the movie title list, movie ratings CSV, and the output CSV filename
mList = sys.argv[1]
mRatings = sys.argv[2]
output = sys.argv[3]

# read the txt file for movie list and rename column
movies = pd.read_csv(mList, sep='\t', dtype=str, header=None)
movies.columns = ['title']

# read the csv file for ratings
ratings = pd.read_csv(mRatings)

ratings_fixed = ratings

# match titles in the rating df with titles in movies df
ratings_fixed['title'] = ratings_fixed['title'].apply(lambda name: match_movie_name(name))

# remove square brackets
ratings_fixed['title'] = ratings_fixed.title.apply(''.join)

# remove the ones with no title matches
ratings_fixed = ratings_fixed[ratings_fixed.title != '']

# group by title and take the average, reset index
ratings_fixed = ratings_fixed.groupby('title').mean().reset_index()

# round ratings to 2 decimal places and merge with movies df
ratings_fixed['rating'] = ratings_fixed['rating'].round(2)
result = movies.merge(ratings_fixed, on='title')
# print(result) # for testing

# save result to output file
result.to_csv(output, index=False)