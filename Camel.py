import string


tag = "fun with words"

banner = "*" * len(tag)

print(banner)
print(tag)
print(banner)


phrase = input("Please enter a phrase or sentence: ")

##TODO add verification for phrase.

words = phrase.split()

newWords = []

for x, word in enumerate(words):

    if x == 0:

        wordTemp = word.lower()
        newWords.append(wordTemp)

    else:
        wordTemp = string.capwords(word) ## Found this import off Stack overflow.
        newWords.append(wordTemp)

finalString = "".join(newWords)

print (finalString)
