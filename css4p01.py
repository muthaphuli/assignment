#question 1

%%time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users/winston/Documents/coding_summer/assignemt'
df = pd.read_csv('movie_dataset.csv')
df.head()

columns_to_dropna = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year',
                     'Runtime_(Minutes)', 'Rating', 'Votes', 'Revenue_(Millions)', 'Metascore']
df = df.dropna(subset=columns_to_dropna)

len(df)
df.sort_values(by='Rating',ascending=False, inplace=True)

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]['Title'].iloc[0]

print(f"The highest-rated movie in the dataset is: {highest_rated_movie}")

#question 2
average_revenue = df['Revenue_(Millions)'].mean()

print(f"The average revenue of all movies in the dataset is: {average_revenue:.2f}")

#Question 3

movies_2015_to_2017 = df[df['Year'].between(2015, 2017, inclusive=True)]
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue (Millions)'].mean()

print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017:.2f}")

#Question 4

movies_2016 = df[df['Year'] == 2016]
number_of_movies_2016 = len(movies_2016)
print(number_of_movies_2016)

#quesion 5

nolan_movies = df[df['Director'] == 'Christopher Nolan']
number_of_nolan_movies = len(nolan_movies)

print(f"The number of movies directed by Christopher Nolan is: {number_of_nolan_movies}")

#question 6

count_rows = (df['Rating'] >= 8.0).sum()
print(count_rows)

#question 7

nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan = nolan_movies['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan}")

#Question 8

average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}")

#question 9
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

#question 10
all_actors = df['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]
print(f"The most common actor in all the movies is: {most_common_actor}")

#question 11

df['Genres'] = df['Genre'].str.split(',')
all_genres = [genre for genres in df['Genres'] for genre in genres]
unique_genres = set(all_genres)
print("Number of unique genres:", len(unique_genres))
print("Unique genres:", unique_genres)

#Question 12
numerical_features = df.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numerical_features.corr()
print(correlation_matrix)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

