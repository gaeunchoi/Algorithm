def solution(s, n):
    big_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small_alpha = list('abcdefghijklmnopqrstuvwxyz')

    result = ''
    for ele in s:
        if ele == ' ':
            result += ' '
        else:
          result += big_alpha[(big_alpha.index(ele) + n) % 26] if ele.isupper() else small_alpha[(small_alpha.index(ele) + n) % 26]
      
    return result

# 아스키코드 이용 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)