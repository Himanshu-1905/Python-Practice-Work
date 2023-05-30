# The game() function in a program lets a user play a game and returns the score as an integer. YOu need to read a file "highscore.txt" which is either blank or contains the previous High-score . You need to write a program to update the high-score whenever game() breaks the high-score.

def game():
    return 44677

score = game()
with open("highscore.txt") as f:
    highScoreStr = f.read()
    
if highScoreStr=='':
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif int(highScoreStr)<score :
    with open("highscore.txt", "w") as f:
        f.write(str(score)) 