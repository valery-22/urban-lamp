#List of fruits to include in a fruit salad 
fruits = ['blueberries','strawberries',"'raspberries",'kiwi']
fruit_salad = []
#iterate a while loop over the fruits 
i = 0
while i < len(fruits):
    #add each fruit to the fruit salad 
    fruit = fruits[i]
    print(f"Adding {fruit} to the sald.")
    fruit_salad.append(fruit)
    #increment the counter
    i += 1