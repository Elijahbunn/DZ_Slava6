secret_word = input("ведите слова для игры: ")
print("\033[2J")
win = False
all_letters = []
true_letters = []
points = [0,0,0]
counter = 0
players = ["player_one","player_two","player_three"]
while win == False:
    letter = input(f"\n{players[counter%3]} ведите букву:")
    if letter in all_letters:
	    print("Такая буква ведина")        
    elif letter in secret_word:
        print("вы отгадали букву")
        true_letters.append(letter)
        points[counter%3] +=1
    else:
        print("вы не отгадали букву")
    all_letters.append(letter)
    win = True
    for letter in secret_word:
        if letter in true_letters:
            print(letter, end = "")
        else:
            print("*", end = "")
            win = False
    counter +=1
for number in range(3):
    print(f"\n{players[number]} : {points[number]}")