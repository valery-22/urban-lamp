# TODO: Define a list of temperatures
temperatures = [16, 14, 20, 22, 15, 36]
# TODO: Write a loop to go through each temperature in the list
for temp in temperatures:
    # TODO: Add an 'if' statement to check if the temperature is over a really hot threshold
    if temp > 30:
        # TODO: Print a message for being really hot and then exit the loop
        print("The temperature it's too high!")
        break
    # TODO: Add an 'elif' condition before the general temperature message to check if it's too cold
    elif temp <= 18:
        # TODO: For temperatures that are too cold, print a specific message and skip to the next one
        print("The temperature is cold ")
        continue
    # TODO: Print a message saying the temperature is nice for all other cases
    else:
     print("It's a nice weather outside.")