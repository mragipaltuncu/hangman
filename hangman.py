import random

word_list = ["mehmet altuncu"]

letter_and_blueprint = []

limbs_left = 4

def create_letter_dash_list(word_list=word_list,letter_and_blueprint=letter_and_blueprint):
	word = random.choice(word_list)
	for char in word:
	    if char != " ":
	        letter_and_blueprint.append([char,"_"])
	    else:
	        letter_and_blueprint.append([char," "])

def print_word_blueprint(letter_and_blueprint=letter_and_blueprint):
	blueprint = ""
	for i in letter_and_blueprint:
   		blueprint += i[1]

	print(blueprint)

def get_player_guess():
	player_guess = input("Guess a letter: ")
	return player_guess

def check_guess(guess,letter_and_blueprint=letter_and_blueprint):
	found = False
	for i in letter_and_blueprint:
		if i[0].lower() == guess.lower():
			i[1] = guess
			found = True

	if not found:
		global limbs_left
		limbs_left -= 1
		print("limbs left : ", limbs_left)
		
def welcome_header():
	welcome_msg = (r"""

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                
                                                                       

*Welcome Friend! Our guy is about to be hanged!
*Sheriff of the town wants you to unlock a secret password.
*Each time you guess a wrong letter, our guy will be closer to death!
*Good luck!
""")
	print(welcome_msg)

create_letter_dash_list()

while limbs_left > 0:
	welcome_header()
	print_word_blueprint()
	guess = get_player_guess()
	check_guess(guess)
