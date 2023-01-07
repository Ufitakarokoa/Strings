# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


#scorers
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

#goal minutes
goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"

#Alternative report (ignore line 23)
report2 = ((scorer_0 + " scored in the " + str(goal_0) + " nd minute\n") +
           ((scorer_1) + " scored in the " + str(goal_1) + " th minute"))
print(report)

print("\n")

player = "Adri van Tiggelen"

first_name_find = player.find(" ")

first_name = player[0:first_name_find]

last_name = player[first_name_find + 1:]

last_name_len = len(last_name)

name_short = first_name[0] + ". " + last_name

#chant_find=player
chant = f"{first_name}! " * len(first_name)
chant = chant[0:len(chant) - 1]
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
