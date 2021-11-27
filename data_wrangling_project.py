import pandas as pd
import matplotlib.pyplot as plt
""""
Mini-Project: Data Wrangling and Transformation with Pandas

Working with tabular data is a necessity for anyone with enterprises having a majority of their data in relational databases and flat files. 
This mini-project is adopted from the excellent tutorial on pandas by Brandon Rhodes which you have watched earlier in the Data Wrangling Unit. 
In this mini-project, we will be looking at some interesting data based on movie data from the IMDB.

This assignment should help you reinforce the concepts you learnt in the curriculum for Data Wrangling and sharpen your skills in using Pandas. Good Luck!"""

# Taking a look at the Movies dataset
# This data shows the movies based on their title and the year of release
movies = pd.read_csv('https://raw.githubusercontent.com/springboard-curriculum/mec-mini-projects/master/mec-5.3.10-data-wranging-with-pandas-mini-project/titles.csv')

print('INFO OF THE MOVIE DATASET:\n',movies.info())
print('HEAD OF THE MOVIE DATASET:\n',movies.head(10))

# Taking a look at the Cast dataset

# This data shows the cast (actors, actresses, supporting roles) for each movie

# The attribute n basically tells the importance of the cast role, lower the number, more important the role.
# Supporting cast usually don't have any value for n
cast = pd.read_csv(r'C:\Users\chukw\PycharmProjects\.ipynb_checkpoints\cast.csv')
cast.dropna(axis=0,how ='all', inplace=True)
cast.reset_index(inplace=True, drop=True)
print('INFO OF CAST\n',cast.info(),'\n')
print('HEAD OF CAST\n',cast.head(20), '\n')

# Taking a look at the Release dataset
# This data shows details of when each movie was release in each country with the release date
release_dates = pd.read_csv('https://raw.githubusercontent.com/springboard-curriculum/mec-mini-projects/master/mec-5.3.10-data-wranging-with-pandas-mini-project/release_dates.csv', parse_dates=['date'], infer_datetime_format=True)
print('INFO OF RELEASE DATES:''\n',release_dates.info())
print('HEAD OF RELEASE DATES',release_dates.head(10))

# Section I - Basic Querying, Filtering and Transformations
# What is the total number of movies?
print('Length of movies:''\n',len(movies))
# List all Batman movies ever made
batman_df = movies[movies.title == 'Batman']
print('length of Batman Movies:''\n', len(batman_df))

# List all Batman movies ever made - the right approach
batman_df = movies[movies.title.str.contains('Batman', case=False)]
print('Length of Batman Movies:''\n', len(batman_df))
print('head of batman_df:''\n',batman_df.head(10))

# Display the top 15 Batman movies in the order they were released
print('Display the top 15 Batman movies in the order they were released''\n',batman_df.sort_values(by=['year'], ascending=True).iloc[:15])

# Section I - Q1 : List all the 'Harry Potter' movies from the most recent to the earliest
harry_potter_df = movies[movies.title.str.contains('Harry Potter', case= False)].sort_values('year',ascending=False)
print('List all the Harry Potter movies from the most recent to the earliest:',harry_potter_df)

# How many movies were made in the year 2017?
print("How many movies were made in the year 2017:",len(movies[movies.year == 2017]))

# Section I - Q2 : How many movies were made in the year 2015?
print("How many movies were made in the year 2015:",len(movies[movies['year']==2015]))

# Section I - Q3 : How many movies were made from 2000 till 2018?

# You can chain multiple conditions using OR (|) as well as AND (&) depending on the condition
year_2000_to_2018 = [year for year in range(2000,2018)]
type(year_2000_to_2018)

print(len(movies[movies.year.isin(year_2000_to_2018)]))

# Section I - Q4: How many movies are titled "Hamlet"?
print('How many movies are titled Hamlet:',len(movies[movies['title'].str.contains('Hamlet',case=False)]))
print("How many movies are titled Hamlet:",len(movies[movies['title'].isin(['Hamlet'])]))

# Section I - Q5: List all movies titled "Hamlet"

#     The movies should only have been released on or after the year 2000
#     Display the movies based on the year they were released (earliest to most recent)
#The movies should only have been released on or after the year 2000
print('List all movies titled Hamlet:',movies[(movies['title'].isin(['Hamlet']))& (movies['year']>=2000)])
# Display the movies based on the year they were released (earliest to most recent)
print('Display the movies based on the year they were released:',movies[(movies['title'].isin(['Hamlet']))& (movies['year']>=2000)].sort_values(by='year',ascending=False))

# Section I - Q6: How many roles in the movie "Inception" are of the supporting cast (extra credits)

#     supporting cast are NOT ranked by an "n" value (NaN)
#     check for how to filter based on nulls
print(cast[cast['title']=='Inception'])

print('How many roles in the movie "Inception" are of the supporting cast\n',len(cast.query('title=="Inception" and n=="Nan"')))

# Section I - Q7: How many roles in the movie "Inception" are of the main cast

#     main cast always have an 'n' value
print('How many roles in the movie "Inception" are of the main cast\n',len(cast.query('title=="Inception" and n!="Nan"')))

# Section I - Q8: Show the top ten cast (actors\actresses) in the movie "Inception"
#     main cast always have an 'n' value
#     remember to sort!

top_ten_cast_of_Inception= cast.query('title=="Inception" and n!="Nan"')
sorted_top_ten_cast_of_Inception=top_ten_cast_of_Inception.sort_values(by='n',ascending=False).iloc[:10]
print('Show the top ten cast (actors or actresses) in the movie Inception:\n',sorted_top_ten_cast_of_Inception['character'])


# Section I - Q9:

# (A) List all movies where there was a character 'Albus Dumbledore'
df_Albus_Dumbledore= cast[cast.character.str.contains('Albus Dumbledore', case=False)]
print(df_Albus_Dumbledore['type'])

# (B) Now modify the above to show only the actors who played the character 'Albus Dumbledore'

#     For Part (B) remember the same actor might play the same role in multiple movies
actors_of_Albus_Dumbledore = cast.query('character=="Albus Dumbledore"')
print(actors_of_Albus_Dumbledore['name'])

# Section I - Q10:

# (A) How many roles has 'Keanu Reeves' played throughout his career?

# (B) List the leading roles that 'Keanu Reeves' played on or after 1999 in order by year.
print(len(cast.query('name=="Keanu Reeves"')))
print(cast.query('name=="Keanu Reeves" and year>=1999').sort_values(by='year',ascending = True))

# Section I - Q11:

# (A) List the total number of actor and actress roles available from 1950 - 1960
total_number_of_actor_and_actress_roles_from_1950_1960 = cast.query('type == ["actor","actress"] and 1950<=year<=1960')
print(len(total_number_of_actor_and_actress_roles_from_1950_1960))

# (B) List the total number of actor and actress roles available from 2007 - 2017
total_number_of_actor_and_actress_roles_from_1950_1960 = cast.query('type == ["actor","actress"] and 2007<=year<=2017')
print(len(total_number_of_actor_and_actress_roles_from_1950_1960))



# Section I - Q12:

# (A) List the total number of leading roles available from 2000 to present
total_number_of_leading_roles_available_from_2000_to_present = cast.query('n!="Nan" and 2000<=year<=2021')
print(len(total_number_of_leading_roles_available_from_2000_to_present))

# (B) List the total number of non-leading roles available from 2000 - present (exclude support cast)
total_number_of_non_leading_roles_available_from_2000_to_present = cast.query('n!="Nan" and 2000<=year<=2021')
print(len(total_number_of_non_leading_roles_available_from_2000_to_present))
# (C) List the total number of support\extra-credit roles available from 2000 - present
total_number_of_support_extra_credit_roles_available_from_2000_to_present = cast.query('n=="Nan" and 2000<=year<=2021')
print(len(total_number_of_leading_roles_available_from_2000_to_present))


# Section II - Aggregations, Transformations and Visualizations
# What are the top ten most common movie names of all time?
top_ten = movies.title.value_counts()[:10]
print(top_ten)

# Plot the top ten common movie names of all time
top_ten.plot(kind='barh')
plt.show()

# Section II - Q1: Which years in the 2000s saw the most movies released? (Show top 3)
print(release_dates['year'].value_counts()[:3])

# Section II - Q2: # Plot the total number of films released per-decade (1890, 1900, 1910,....)

#     Hint: Dividing the year and multiplying with a number might give you the decade the year falls into!
#     You might need to sort before plotting

grouping_the_number_of_films_by_decades = cast.groupby((cast['year']//10)*10).sum()
grouping_the_number_of_films_by_decades.plot(kind = 'barh')
plt.show()

# Section II - Q3:

# (A) What are the top 10 most common character names in movie history?
print(cast['name'].value_counts()[:10])

# (B) Who are the top 10 people most often credited as "Herself" in movie history?
her_self_character = cast.query('character =="Herself"')
print(her_self_character['name'].value_counts()[:10])
# (C) Who are the top 10 people most often credited as "Himself" in movie history?

him_self_character = cast.query('character =="Himself"')
print(her_self_character['name'].value_counts()[:10])
# Section II - Q4:

# (A) What are the top 10 most frequent roles that start with the word "Zombie"?
zombie_character = cast.character.str.startswith('Zombie')
print(zombie_character)
print(cast[zombie_character].sort_values(by='character', ascending = False)[:10])


# (B) What are the top 10 most frequent roles that start with the word "Police"?
police_character = cast.character.str.startswith('Police')
print(police_character)
print(cast[police_character].sort_values(by='character', ascending = False)[:10])

#     Hint: The startswith() function might be useful

# Section II - Q5: Plot how many roles 'Keanu Reeves' has played in each year of his career.


# Section II - Q6: Plot the cast positions (n-values) of Keanu Reeve's roles through his career over the years.

# Section II - Q7: Plot the number of "Hamlet" films made by each decade

# Section II - Q8:

# (A) How many leading roles were available to both actors and actresses, in the 1960s (1960-1969)?

# (B) How many leading roles were available to both actors and actresses, in the 2000s (2000-2009)?

#     Hint: A specific value of n might indicate a leading role

# Section II - Q9: List, in order by year, each of the films in which Frank Oz has played more than 1 role.

# Section II - Q10: List each of the characters that Frank Oz has portrayed at least twice

# Section III - Advanced Merging, Querying and Visualizations
# Make a bar plot with the following conditions

#     Frequency of the number of movies with "Christmas" in their title
#     Movies should be such that they are released in the USA.
#     Show the frequency plot by month

christmas = release_dates[(release_dates.title.str.contains('Christmas')) & (release_dates.country == 'USA')]
christmas.date.dt.month.value_counts().sort_index().plot(kind='bar')


# Section III - Q1: Make a bar plot with the following conditions
#     Frequency of the number of movies with "Summer" in their title
#     Movies should be such that they are released in the USA.
#     Show the frequency plot by month

# Section III - Q2: Make a bar plot with the following conditions

#     Frequency of the number of movies with "Action" in their title
#     Movies should be such that they are released in the USA.
#     Show the frequency plot by week

# Section III - Q3: Show all the movies in which Keanu Reeves has played the lead role along with their release date in the USA sorted by the date of release

#     Hint: You might need to join or merge two datasets!

# Section III - Q4: Make a bar plot showing the months in which movies with Keanu Reeves tend to be released in the USA?

# Section III - Q5: Make a bar plot showing the years in which movies with Ian McKellen tend to be released in the USA?