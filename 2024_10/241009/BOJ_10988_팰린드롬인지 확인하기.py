input_word = input()
palindrome = 0

pivot = len(input_word) // 2
if len(input_word) % 2 == 0:

    front = input_word[:pivot]
    back = ''.join(reversed(input_word[pivot:]))
    if front == back:
        palindrome = 1
else:
    front = input_word[:pivot]
    back = ''.join(reversed(input_word[pivot+1:]))
    if front == back:
        palindrome = 1

print(palindrome)

# -----------------------------------------------------------------

if ''.join(reversed(input_word)) == input_word:
    print(1)
else:
    print(0)