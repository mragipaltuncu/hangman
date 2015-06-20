#!usr/bin/env python3 

import random
import time
import os
import platform


word_list =  '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat 
goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon 
seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

def print_hangman(missed_letters):

  HANGMAN = ['''
  +---+

  |   |      _                                             
            | |                                            
      |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
      |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                         __/ |                      
                               |___/                       
      |

=========''', '''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
      |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                         __/ |                      
                               |___/                       
      |

=========''', '''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  |   |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                         __/ |                      
                               |___/                       
      |

=========''', '''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 /|   |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                         __/ |                      
                               |___/                       
      |

=========''', '''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 /|\  |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                         __/ |                      
                               |___/                       
      |

=========''','''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 /|\  |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
 /    |                         __/ |                      
                               |___/                       
      |

=========''','''
  +---+

  |   |      _                                            
            | |                                            
  O   |     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 /|\  |     | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
 / \  |                         __/ |                      
                               |___/                       
      |

========='''  ]

  print(HANGMAN[len(missed_letters)])


def get_random_word(word_list):
  word = random.choice(word_list)
  return word


def blankify(secret_word,correct_letters):
  blank = "_"*len(secret_word)

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blank = blank[:i] + secret_word[i] + blank[i+1:]

  return blank

def display_game(missed_letters):
  print_hangman(missed_letters)
  print()
  print("Missed Letters : ", missed_letters,"<<")

def display_blank_word(secret_word,correct_letters):
  blank = blankify(secret_word,correct_letters)
  print()
  for letter in blank:
    print(letter,end=" ")

def play_again():
  answer = input("Play again? [Y/N] : ")
  answer = answer.lower()
  answer_bool = answer.startswith("y")
  return answer_bool

def get_guess(guessed_letters):
  alphabet = "abcdefgğhıijklmnoöprsştıijklmnoöpqrştuüvwxyzABCDEFGĞHIİJKLMNOÖPQRŞTUÜVWYZ"
  while True:
    guess = input("Guess a letter : ")
    if guess not in alphabet:
      print("Please only guess a LETTER")
    elif len(guess) != 1:
      print("Please guess only 1 LETTER at time")
    elif guess in guessed_letters:
      print("You have guessed that letter already")
    else:
      return guess

def game_header(missed_letters,state='begin'):
  if state == 'begin':
    commands = {"Linux" : "clear", "Windows" : "cls", "Darwin" : "clear"}
    os.system(commands[platform.system()])
    display_game(missed_letters)


  elif state == 'end':
    commands = {"Linux" : "clear", "Windows" : "cls", "Darwin" : "clear"}
    os.system(commands[platform.system()])
    goodbye_header()  



def man_is_dead(missed_letters):
  if len(missed_letters) >= 6 :
    return True
  else:
    return False

def is_winner(secret_word,correct_letters):
  for i in range(len(secret_word)):
    if secret_word[i] not in correct_letters:
      return False
  return True


secret_word = get_random_word(word_list)
missed_letters = ""
correct_letters = ""



def main(word_list,secret_word,missed_letters,correct_letters):
  
  while True:
    game_header(missed_letters)
    display_blank_word(secret_word,correct_letters)
    print()
    guess = get_guess(missed_letters+correct_letters)
    if guess in secret_word:
      correct_letters = correct_letters + guess
    else:
      missed_letters = missed_letters + guess
    game_header(missed_letters)
    if man_is_dead(missed_letters):
      print("The man is dead")
      print("The secret word is ",secret_word)
      if play_again():
        secret_word = get_random_word(word_list)
        missed_letters = ""
        correct_letters = ""
      else:
        break
    elif is_winner(secret_word,correct_letters):
      print("You win!")
      if play_again():
        secret_word = get_random_word(word_list)
        missed_letters = ""
        correct_letters = ""
      else:
        break
    game_header(missed_letters)

if __name__ == "__main__":
  main(word_list,secret_word,missed_letters,correct_letters)