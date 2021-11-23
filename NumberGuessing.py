import random
import sqlite3
con = sqlite3.connect('scoreboard.db')
cur = con.cursor()
attempts_list = []
def best_score():
    if len(attempts_list) <= 0:
        print("You don't have best score yet!")
    else:
        print("Currently your best score is {} attempts".format(min(attempts_list)))
pick_number = int(random.randint(1, 20))
print("Welcome to my number guessing game!")
name = input("What is your name? ")
name1 = (name.lower()).capitalize()
play = input("Hi, {}, would you like to play the guessing game? (Yes/No) ".format(name1))
player_attempts = 0
best_score()
while play.lower() == "yes":
    try:
        predict = input("Pick a number between 1 and 20! ")
        if int(predict) < 1 or int(predict) > 20:
            raise ValueError("Your number is not valid, please guess a number within the given range!")
        if int(predict) == pick_number:
            print("Well done, you got it right!")
            player_attempts += 1
            attempts_list.append(player_attempts)
            print("It took you {} attempts".format(player_attempts))
            play_again = input("Would you like to play again? (Yes/No) ")
            player_attempts = 0
            best_score()
            pick_number = int(random.randint(1, 20))
            if play_again.lower() == "no":
                print("That's cool, have a good one!")
                break
        elif int(predict) > pick_number:
            print("It's lower")
            player_attempts += 1
        elif int(predict) < pick_number:
            print("It's higher")
            player_attempts += 1
    except ValueError as error:
        print("That is not valid value, plesase try again!")
        print("({})".format(error))
else:
    print("Thanks for playing!")
cur.execute('CREATE TABLE IF NOT EXISTS result ([player_name] VARCHAR[15], [attempts] INTEGER)')
cur.execute('INSERT INTO result (player_name, attempts) VALUES (?, ?)', (name1, min(attempts_list)))
con.commit()
con.close()
logging.basicConfig(
    level=logging.INFO,
    format='{asctime} {message}',
    style='{',
    filename='mylog.log',
    filemode='w'
)
logging.info("%s played the number guessing game" %name1)
