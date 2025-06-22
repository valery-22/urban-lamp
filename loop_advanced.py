# List of temperatures with mixed weather conditions
temperatures = [32, 18, 21, 28, 35, 19, 22]

for temp in temperatures:
    # TODO: Print "It's really hot." and exit the loop if temperature is above 30
    if temp > 30:
        print("It's really hot.")
        break
    # TODO: Print "It's quite chilly." and skip to the next iteration if temperature is below 20
    elif temp < 20:
        print("It's quite chilly.")
        continue

    print("Lovely weather.")