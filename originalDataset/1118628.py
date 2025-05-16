import sys

sys.setrecursionlimit(int(2E5))

SHEEP = True
WOLF = False


def print_tree(tree):
    print(''.join(['S' if e else 'W' for e in tree]))


def calc_next_animal(tree, cur_pos):
    if answer[cur_pos]:
        if tree[cur_pos] == SHEEP:
            return tree[cur_pos - 1]
        else:
            return not tree[cur_pos - 1]
    else:
        if tree[cur_pos] == SHEEP:
            return not tree[cur_pos - 1]
        else:
            return tree[cur_pos - 1]


def calc_prev_animal(tree, cur_pos):
    if answer[cur_pos]:
        if tree[cur_pos] == SHEEP:
            return tree[cur_pos + 1]
        else:
            return not tree[cur_pos + 1]
    else:
        if tree[cur_pos] == SHEEP:
            return not tree[cur_pos + 1]
        else:
            return tree[cur_pos + 1]


def wfs(tree, cur_pos, N):
    tree[cur_pos + 1] = calc_next_animal(tree, cur_pos)
    cur_pos += 1
    if cur_pos == N - 1:
        return tree[0] == calc_next_animal(tree, cur_pos) and tree[cur_pos] == calc_prev_animal(tree, 0)
    else:
        return wfs(tree, cur_pos, N)


if __name__ == '__main__':
    N = int(input())
    answer = [True if i == 'o' else False for i in input().rstrip()]
    aa = [[WOLF, WOLF]
        , [WOLF, SHEEP]
        , [SHEEP, SHEEP]
        , [SHEEP, WOLF]]
    super_list = [0] * int(2E5)
    for a in aa:
        super_list[:2] = a
        if wfs(super_list, 1, N):
            print_tree(super_list[:N])
            break
    else:
        print(-1)