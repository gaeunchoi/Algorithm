M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
nums = list(map(int, input().split()))

state = -1
states = ['normal', 'secret']
if N < M:
    state = 0
else:
    for i in range(0, N-M+1):
        if nums[i:i+M] == secret:
            print(nums[i:i+M])
            state = 1

print(states[state])