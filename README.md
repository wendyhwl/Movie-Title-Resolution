# Movie Title Entity Resolution

Practicing data cleaning and basic operations with the provided data.

Simon Fraser University CMPT353 - Summer 2020

## Description
### Objective
With the given [MovieTweetings](https://github.com/sidooms/MovieTweetings) data set, determine the average rating for each movie, ignoring the completely-incorrect movie titles.

### Output
A [CSV file](https://github.com/wendyhwl/Movie-Title-Resolution/blob/main/output.csv) with the following:
* First column: movie title
* Second column: average rating rounded to two decimal places
* Sorted by title, include only movies with ratings in the original data set

### How to run
In terminal:
```bash
python3 average_ratings.py movie_list.txt movie_ratings.csv output.csv
```

## Language

Python3

## Acknowledgement

Assignment created by CMPT353 Professor Greg Baker.

[SFU Academic Integrity](http://www.sfu.ca/students/academicintegrity.html)
