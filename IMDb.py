# importing the module
import imdb
import matplotlib.pyplot as plt 
# creating instance of IMDb
ia = imdb.IMDb()

#code is the movie id to get movie ratings
code = "0105810 "

# getting the movie with name
search = ia.search_movie('Ali')
  

  
# getting information
movie = ia.get_movie(code)
  
# getting rating of the series
rating = movie.data['rating']

# getting movie year
year = search[0]['year']
  
# printing movie name and year
print(search[0]['title'] + " : " + str(year))
  
# printing the object i.e name
print(movie)
  
# print the rating
print(rating)

df.plot(kind='bar',x='Movie Name',y='Rating')
plt.show()