import random
from medicines import drugs_list
import string


def get_drug():
    i = random.randint(0, len(drugs_list) -1)
    drug = drugs_list[i]
    return drug
    #return drug.name.upper()
    

def hangman():
    drug = get_drug()
    drug_name = drug.name.upper()
    drug_type = drug.type.upper()
    drug_url = drug.url
    # drug = get_valid_drug(drugs)
    drug_letters = set(drug_name) #letters in the drug
    alphabet = set(string.ascii_uppercase) #setting the letters to uppercase
    used_letters = set() #what the user has guessed

    lives = 10

    #getting user input
    while len(drug_letters)> 0 and lives> 0:
        #letters used
        #' '.join(['a', 'b', 'cd']) --> 'a d cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W _ R D)
        drug_list = [letter if letter in used_letters else '_' for letter in drug_name]
        print ('Guess a drug. Generic names only.')
        print ('Your clue is: ' + drug_type)
        print ('Current drug: ', ' '.join(drug_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in drug_letters:
                drug_letters.remove(user_letter)
                print ('')

            else:
                lives = lives-1 #takes a life if wrong
                print ('\nYour letter', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print ('\nYou have already used that character. Please try again.')

        else:
            print('\nInvalid character. Please try again.')
    
    #gets here when len(word_letter) == 0 OR when lives == 0
    if lives == 0:
        print ('You died, sorry. The drug was', drug_name)
    else:
        print('You guessed the drug', drug_name, 'Yay!!')
        print ('To learn more about this drug follow the link: ' + drug_url)

if __name__ == '__main__':
    hangman()
