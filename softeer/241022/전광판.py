import sys

light = {
    "0" : '1111110',
    "1" : '0110000',
    "2" : '1101101',
    "3" : '1111001',
    "4" : '0110011',
    "5" : '1011011',
    "6" : '1011111',
    "7" : '1110010',
    "8" : '11111111', 
    "9" : '1111011',
    " " : '0000000'
}

T = int(input())
for _ in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    A = (5 - len(A)) * " " + A
    B = (5 - len(B)) * " " + B

    cnt = 0
    for i in range(5):
        for j in range(7):
            cnt += (light[A[i]][j] != light[B[i]][j])

    print(cnt)

    
