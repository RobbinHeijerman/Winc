# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
score_1 = "Ruud Gullit"
score_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = score_1 + " " + str(goal_0) + ", " + score_2 + " " + str(goal_1)

report = f"{score_1} scored in the {goal_0}nd minute\n{score_2} scored in the {goal_1}th minute"
#report1 = f"{score_1} scored in the {goal_0}nd minute"
#report2 = f"{score_2} scored in the {goal_1}th minute"
#report = report1 + " " + report2

player = "Ruud Gullit"

first_name = player[:4]

last_name_len = len(player) - player.find("Gullit");

name_short = first_name[:1] + "." + player[4:len(player)]

chant = f"{first_name}! {first_name}! {first_name}! {first_name}!"

good_chant = chant[len(chant)-1:len(chant)] != " "

print(report)