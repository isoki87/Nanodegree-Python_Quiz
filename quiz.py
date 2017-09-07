# First message displayed to the user
def showIntro():
    return "\nWelcome! This quiz will test your knowledge of basic Python and coding techniques!"

# This message is displayed if user input is not understood
def showConfused():
    return "\nI'm sorry, I didn't quite get that. \n"

# Checks if the player typed in an appropriate difficulty, this serves as a saftey check for the chooseProblem() and chooseAnswer() functions
def diffOkay(diff, diff_bank):
    for word in diff_bank:
        if diff.upper() == word:
            return True
    return False

# Based on the difficulty entered (already passed safety check with diffOkay() f(x)), chooses a problem for the player
def chooseProblem(diff):
    if diff.upper() == "EASY":
        return "\nThe '___1___ World' program is one of the most common lessons for beginners to programming. Although for this nanodegree program, we started off with another lesson when we learned ___2___, the basics for building a website. After learning the basics of HTML, we delved briefly into styling our webpage with ___3___. Finally, learned the dynamic language ___4___ and built a Mad-Libs generator using the language.\n"
    elif diff.upper() == "MEDIUM":
        return "\nIn our lessons, we learned that the computer is a stupid but very ___1___ tool that, when given proper instructions, allow us to do a lot of things. Programming languages help us communicate to computers and eliminate the ___2___ of spoken languages, allowing precise instructions to be given to the computers. That said, it is crucial to get the spelling of the ___3___ right, otherwise the program will fail to start, whereas spelling mistakes in our spoken languages will, for the most part, still let others understand us. Sometimes, a program may still compile successfully with a bug, which is why it is important for programmers to learn ___4___ techniques such as running edge test cases to minimize a program's possible bugs.\n"
    else:
        return "\nFrom our lessons, we added some very powerful tools to our arsenal. The while ___1___ in Python allowed us to perform repetitive tasks until certain conditions are satisfied and the ___2___ syntax allows us to make our own functions in our programs. Raw_input allows our program to become more interactive with the user, and it lets us take the user's ___3___ and incorporate that into the program. Of course, this also makes our program more prone to errors since we can no longer predict with certainty what the user will type, so it is very important to code ___4___ in interactive programs to minimize bugs.\n"

# Based on the difficulty entered (already passed safety check with diffOkay() f(x)), chooses the answer set for the appropriate problem
def chooseAnswer(diff):
    if diff.upper() == "EASY":
        return ["Hello", "HTML", "CSS", "Python"]
    elif diff.upper() == "MEDIUM":
        return ["powerful", "ambiguity", "syntax", "debugging"]
    else:
        return ["loop", "def", "input", "defensively"]

# This is the actual game code (18 lines), if the player win, then will return true, otherwise this function will return false
def beginGame(problem, answer, tries):
    wrong_answers = 0
    total_num_ans = 4
    correct_answers = 0
    # The game will loop until the player runs out of 'tries' or if the player guesses all the correct answers
    while wrong_answers < int(tries):
        if(correct_answers == total_num_ans):
            print problem
            return True
        print problem
        attempt = raw_input("\nWhat is the answer for the next blank?  ")
        if (attempt == answer[correct_answers]):
            # Initiates the blank replacement function if an answer matches the attempt
            problem = replaceBlank(answer, correct_answers, problem)
            correct_answers += 1
            print "\nYay! One more blank filled in!\n"
        else:
            wrong_answers += 1
            print "\nOh no! That's not correct, make sure you don't have typos or capitalization errors either! You have " + str(int(tries) - wrong_answers) + " tries left!\n"
    return False

# This function will replace the most current blank space with the answer
def replaceBlank(answer, correct_answers, problem):
    curr_blank = "___" + str(correct_answers + 1) + "___"
    problem = problem.split()
    newList = findAndReplace(curr_blank, answer[correct_answers], problem)
    problem = " ".join(newList)
    return problem

# This function finds a word to be replaced in the input list, and replaces it with the new word, with all the punctuations if applicable
def findAndReplace(replaced, to_replace, word_list):
    newList = []
    for word in word_list:
        if replaced in word:
            word = word.replace(replaced, to_replace)
            newList.append(word)
        else:
            newList.append(word)
    return newList

# If player wins (completed all blanks with tries - wrong_answer > 0), this message will be displayed
def showWinningMessage(difficulty, tries):
    return "\nYou won! You beat the " + difficulty.upper() + " level with " + str(tries) + " tries!\n"

# If player loses (not able to complete the blanks within the chosen number of tries), this message will be displayed with how many tries they attempted
def showLosingMessage(difficulty, tries):
    return "\nBetter luck next time! You couldn't get past the " + difficulty.upper() + " level with " + str(tries) + " tries :(.\n"

# This function will see if the player wants to play the game again
def playAgain():
    # Until the player enters the proper answer, this question will be looped
    while True:
        cont = raw_input("Would you like to play again? (YES or NO)  ").upper()
        if(noTypoDecision(cont)):
            break
        print showConfused()
    if cont == "YES":
        return True
    else:
        return False

# This is a typo check, only a yes or a no will return as True
# A typo will return the player to the "play again?" question so they are not punished by entering the game loop again for a typo
def noTypoDecision(decision):
    if decision == "YES" or decision == "NO":
        return True
    return False

# As per suggestion from Udacity reviewer, I will name the main function main()
def main():
    # This game will continue to loop itself until the player decides to not play again
    while True:
        diffBank = ["EASY", "MEDIUM", "HARD"]
        while True:
            print showIntro()
            difficulty = raw_input("Please type in the difficulty you would like for the quiz (easy, medium, hard):  ")
            tries = raw_input("How many tries would you like to have before the game resets? (Please enter a numerical number)  ")
            if(diffOkay(difficulty, diffBank)):
                break
            print showConfused()
        problem = chooseProblem(difficulty)
        answer = chooseAnswer(difficulty)
        results = beginGame(problem, answer, tries)
        if (results):
            print showWinningMessage(difficulty, tries)
        else:
            print showLosingMessage(difficulty, tries)
        if(playAgain() == False):
            break

# Run main()
if __name__ == "__main__":
    main()
