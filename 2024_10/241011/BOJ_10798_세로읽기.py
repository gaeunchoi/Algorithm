import sys

text = []
for i in range(5):
    words = sys.stdin.readline().rstrip()
    text.append(words.ljust(15))

for i in range(15):
    for j in range(5):
        if text[j][i] != " ":
            print(text[j][i], end="")
