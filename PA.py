# Python program to 
# demonstrate creation of an
# assistant using wolf ram API
#PA.py

import wolframalpha
import pandas as pd
import matplotlib.pyplot as plt

# Taking input from user
question = input('Question:')
  
# App id obtained by the above steps
app_id = 'X23UR3-2T49GWKKVT'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)
  
# Stores the response from 
# wolf ram alpha
res = client.query(question)
  
# =============================================================================
# for pod in res.pods:
#      pass
#  
# for pod in res.pods:
#      for sub in pod.subpods:
#          print(sub.plaintext)
# =============================================================================
         

answer = next(res.results).text
  
print(answer)



df = pd.DataFrame(
    {
     'Actor': ['Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith','Will Smith'],
     'Movie Name':['Where the Day Takes You', 'Made in America','Six Degrees of Separation','Bad Boys','Independence Day','Men in Black','Enemy of the State','Wild Wild West','Welcome to Hollywood','The Legend of Bagger Vance','Ali','Men in Black II','Bad Boys II','Jersey Girl','I Robot','Shark Tale','Hitch','The Pursuit of Happyness','I Am Legend','Hancock'],
     'Movie ID':['0105810','0107478','0108149','0112442','0116629','0119654','0120660','0120891','0169376','0146984','0248667','0120912','0172156','0300051','0343818','0307453','0386588','0454921','0480249','0448157'],
     'Movie Rating':['6.5','5','6.8','6.8','7','7.3','7.3','4.9','4.9','6.7','6.7','6.1','6.6','6.2','7.1','6','6.6','8','7.2','6.4']
     }
    )

print(df)

df.plot(kind='scatter',x='Movie Name',y='Movie Rating',color='red')
df.nsmallest(n=5, columns=['Movie Rating'])
plt.show()

