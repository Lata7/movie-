# Python program to 
# demonstrate creation of an
# assistant using wolf ram API
#Test.py

import wolframalpha
  
# Taking input from user
question = input('Question: ')
  
# App id obtained by the above steps
app_id = 'X23UR3-2T49GWKKVT'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)
  
# Stores the response from the top ratings dataframe
question = df_top5()
res = client.query(question)
  
# Includes only text from the response
# Display for all movies
answer = next(res.results).text
  
print(answer)
