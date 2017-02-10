
#
# f = open("words.txt")
# randomWord = f.readline()
# while randomWord != "":
#     print(randomWord)
#     randomWord = f.readline()

# f = open("words.txt")
# for word in f:
#     wordList = word.strip()
#     print(wordList)

array = []
with open("words.txt", "r") as f:
  for line in f:
    array.append(line.strip())

print(array)

file = open("test.txt", "w")
for item in array:
  file.write("%s\n" % item)