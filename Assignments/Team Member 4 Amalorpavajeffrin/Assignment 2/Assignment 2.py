import random
from tempfile import tempdir 
#Assign temperature as temp and Humidity as humidity
temp = random.randint(18,28)
humidity =random.randint(45,70)
#use while condition loop to perform the task
while temp >=18 and 28>= temp:
    if (temp> 22 and 28 > temp)and ( humidity > 55 and 70 > humidity):
        print("The temperature is high 'alert'.")
        break
    elif (temp> 22 and 28 > temp)and ( humidity > 40 and 60 > humidity):
        print("The temperature is normal.")
    elif(temp> 18 and 23 > temp)and ( humidity > 45 and 65 > humidity):
        print("The temperature is low")
    else:
        print("Input proper convention.")
    
    temp = random.randint(18,28)
    humidity =random.randint(45,70)

    
    

          

         