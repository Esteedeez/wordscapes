letters = input("What letters are available?\n")
allWords = []
wordsWithinRange = []
while True:
    try:
        limitNumberOfLetters = input("Would you like to limit the number of letters?")
    except ValueError:
        print("True or False, Try again")
        continue
    else:
        break
if limitNumberOfLetters == "yes":
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            lowerRange = int(input("Lower Range?"))
        except ValueError:
            print("Numbers only plase")
            # better try again... Return to the start of the loop
            continue
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            upperRange = int(input("Upper Range?"))
        except ValueError:
            print("Numbers only plase")
            # better try again... Return to the start of the loop
            continue
        else:
            # age was successfully parsed!
            # we're ready to exit the loop.
            break
else:
    lowerRange = 3
    upperRange = 6

path = "C:/Users/Master/Desktop/Wordscapes/en_US-large.txt"
with open(path) as f:
    data = f.readlines()
for n, line in enumerate(data, 1):
    allWords.append(line.rstrip())
print(len(allWords))
chars = [letters[i:i + 1] for i in range(0, len(letters), 1)]
print(chars)
for word in allWords:
    if len(word) >= lowerRange and len(word) <= upperRange:
        wordsWithinRange.append(word)
    else:
        continue
print(len(wordsWithinRange))
print('cc' in 'check')
# Now need to do pattern matching, see https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
