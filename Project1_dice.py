"""Here we are going to make a game dice roller where a user will wait for his/her turn
   then roll the dice and as long as the dice value is not equal to 1 the user will be
   rolling the dice.Once he got 50 points he will be a winner. """

#First we are going to make a dice roller function.
#We also have to import random module so we can get random order of number while rolling a dice.
import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

"""Now going to ask the user about no of players who are going to participate.
   We are using while loop here just to make sure that the number of players are valid.
   if they are not, the system will ask again to write the no of players."""
while True:   
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 to 4")
            
    else:
        print("Unvalid ,try again") 
#Now gonna make  variables for score.
max_score=50
#The "_" is here instead of any variable because we dont want its value to be stored in any variable like "i".
player_scores = [0 for _ in range(players)]
#if the max score of player is less than max score we will keep looping.
while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
        #using the lower function here so that even if user enter "Y" it will still roll the dice.    
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("player",player_idx + 1,"score is:", current_score)
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
        
(max_score) =int(max(player_scores))
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
