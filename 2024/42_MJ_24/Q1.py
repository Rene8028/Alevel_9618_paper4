WordArray = []
NumberWords = []

def ReadWords(filename):
    global WordArray
    global NumberWords
    File = open(filename, "r")
    Fdata = File.read().strip()
    File.close()
    WordArray = Fdata.split()
    NumberWords = len(WordArray)
    play()

def play():
    global WordArray
    global NumberWords
    print("Main word:", WordArray[0])
    print("Number of answers:", NumberWords - 1)
    Uinput = ""
    points = 0
    WordArray[0] = ""
    while Uinput != "no":
        correct = False
        Uinput = input("Enter words of 3 or more letters:").lower()
        if Uinput != "no":
            for i in range(NumberWords):
                if Uinput == WordArray[i]:
                    correct = True
                    points = points + 1
                    WordArray[i] = ""
            if correct:
                print("Correct answer")
            else:
                print("Wrong answer")
            print("You have ", points , "correct answers")
    print("You got ", (points / (NumberWords - 1)) * 100, "% correct answers")
    print("Words you didn't gets:")
    for words in WordArray:
        if words:
            print(words)


select = input("Please enter easy, medium or hard for difficulty:").lower()
if select == "easy":
    ReadWords("Easy.txt")
elif select == "medium":
    ReadWords("Medium.txt")
elif select == "hard":
    ReadWords("Hard.txt")
        
