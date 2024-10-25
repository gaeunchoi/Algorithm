import sys

N = int(input())

scores = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
total_scores = [0] * N

def check_rank(sorted):
    rank = {}
    r = 1
    for s in sorted:
        if s not in rank:
            rank[s] = r
        r += 1
    return rank

for score in scores:
    result = []
    sort_scores  = sorted(score, reverse = True)
    rank_dict = check_rank(sort_scores)

    for i in range(N):
        result.append(rank_dict[score[i]])
        total_scores[i] += score[i]
    print(*result)

total_rank = []
sort_total_scores = sorted(total_scores, reverse=True)
total_rank_dict = check_rank(sort_total_scores)
for score in total_scores:
    total_rank.append(total_rank_dict[score])
print(*total_rank)