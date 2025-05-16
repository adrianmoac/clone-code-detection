import sys
sys.setrecursionlimit(100000)

def set_enable_goal(cur_node, back_paths, enable_goal):
    if cur_node in back_paths:
        for next_node in back_paths[cur_node]:
            if enable_goal[next_node - 1] == 0:
                enable_goal[next_node - 1] = 1
                set_enable_goal(next_node, back_paths, enable_goal)


N, M = map(int, input().split())
MIN = float('-inf')
INF_LIMIT = -MIN

back_paths = {}
all_paths = {}
for i in range(M):
    a, b, c = map(int, input().split())
    if a in all_paths:
        all_paths[a].append((b, c))
    else:
        all_paths[a] = [(b, c)]

    if b in back_paths:
        back_paths[b].append(a)
    else:
        back_paths[b] = [a]


# path cut
enable_goal= [0 for i in range(N)]
enable_goal[N - 1] = 1
set_enable_goal(N, back_paths, enable_goal)

for a, paths in all_paths.items():
    if not enable_goal[a - 1]:
        all_paths[a] = []
    else:
        valid_paths = []
        for b, c in paths:
            if enable_goal[b - 1]:
                valid_paths.append((b, c))
        all_paths[a] = valid_paths


scores = [MIN for i in range(N)]
scores[0] = 0

is_inf = False
for n in range(N):
    for a in all_paths.keys():
        for b, c in all_paths[a]:
            scores[b - 1] = max(scores[b - 1], scores[a - 1] + c)

# loop check
if not is_inf:
    prev_score = scores[N - 1]
    for a in all_paths.keys():
        for b, c in all_paths[a]:
            scores[b - 1] = max(scores[b - 1], scores[a - 1] + c)
    if prev_score != scores[N - 1]:
        is_inf = True


if is_inf:
    print('inf')
else:
    print(scores[N - 1])