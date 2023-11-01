word = str(input("Please enter a word\n"))
number = int(input("Please enter an number\n"))
if len(word[number:]) >= 3:
    word = word + word
else:
    word = word[0:2] + word[0:2]
if word.count("e") >= 3:
    word = word.replace("e","a")
else:
    word = word.replace("e","c")
print(word)