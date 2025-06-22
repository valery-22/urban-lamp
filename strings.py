# Given mission name
mission_name = "Sort"

# TODO: Print the first and the last character of the mission name
first_character = mission_name[0]
last_character = mission_name[-1]
print(first_character, last_character)

# TODO: The mission needs a minor update. We aim to change its first letter to 'P' and the last letter to `k`, obtaining the word "Pork".
# Remember, strings in Python are immutable, so you cannot alter them directly.
updated_mission_name = 'P' + mission_name[1:-1] + 'k'
# TODO: Print the updated mission name
print(updated_mission_name)
