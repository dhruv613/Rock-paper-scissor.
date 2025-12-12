import random


class Game:

    def __init__(self):

        self.choices = {1: "rock", 2: "paper", 3: "scissor"}

        self.user_score = 0

        self.comp_score = 0
        self.atempts = 0

    def start_game(self):
        while True:
                try:
                    user = input("Enter your choice Rock, Paper, Scissor: ").lower()
                    user = list(self.choices.keys())[list(self.choices.values()).index(user)]
                except Exception as e:
                    print("Invalid input. Please enter Rock, Paper, or Scissor.")
                    continue

                comp_num = random.randint(1, 3)
                comp = self.choices[comp_num]


                print(f"Computer's choice: {[comp]}")

                if user == comp_num:
                    print("Tie!🤝")
                    self.atempts += 1

                elif (user == 1 and comp_num == 3) or (user == 2 and comp_num == 1) or (user == 3 and comp_num == 2):
                    print("You Win!🥇")   
                    self.user_score += 1
                    self.atempts += 1   
                else:
                    print("You Lose😔")
                    self.comp_score += 1
                    self.atempts += 1

                print(f"Score => You: {self.user_score} | Computer: {self.comp_score}")

                if self.atempts == 5:
                    print("Game Over!")

                    if self.user_score > self.comp_score:
                        print("Congratulations! You won the game!🎉")
                        self.atempts, self.user_score, self.comp_score = 0, 0, 0

                    elif self.user_score < self.comp_score:
                        print("Sorry, you lost the game. Better luck next time!🍀")
                        self.atempts, self.user_score, self.comp_score = 0, 0, 0

                    else:
                        print("The game is a tie!🤝")
                        self.atempts, self.user_score, self.comp_score = 0, 0, 0
                    break

    def reset_game(self):
        while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    self.start_game()
                elif play_again == "no":
                    print("Thanks for playing!🙏")
                    break
                else:
                    print("Invalid input 🤦‍♂️. Please enter 'yes' or 'no'.")


class Player(Game):
    def __init__(self, name=""):
        super().__init__()  
        self.name = name
        
    def get_name(self):
        self.name = input("Enter your name📛: ")
        return self.name

    def start(self):
        name = self.get_name()
        print(f"Welcome {name} to Rock, Paper, Scissor Game!")

        super().start_game()

    def reset(self):
        super().reset_game()




game = Player()
game.start()
game.reset()