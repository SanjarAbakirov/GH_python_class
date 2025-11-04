from collections import Counter
# str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

sentence = str(input("Enter your sentence: "))
print(sentence.split())
splitedSentece = Counter(sentence.split())
# print(splitedSentece)
dictionary = dict(splitedSentece)
print(dictionary)

# Hello
