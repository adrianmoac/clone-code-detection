from collections import defaultdict


def solve(s, l):
    for now in range(1, len(s) + 1):
        now %= len(s)
        pre = now - 1
        nex = (now + 1) % len(s)

        # 整合性のチェック
        if l[pre] is not None and l[nex] is not None:
            if l[now] == 1:
                if s[now] == "o":
                    if l[nex] != l[pre]:
                        return False
                else:
                    if l[nex] == l[pre]:
                        return False
            else:
                if s[now] == "o":
                    if l[nex] == l[pre]:
                        return False
                else:
                    if l[nex] != l[pre]:
                        return False

        # nextを決める
        if l[pre] is not None and l[nex] is None:
            # ひつじ
            if l[now] == 1:
                # 両隣が同じはず
                if s[now] == "o":
                    l[nex] = l[pre]

                # 両隣が違うはず
                else:
                    l[nex] = -1 * l[pre]
            # おおかみ
            else:
                # 両隣が違うはず
                if s[now] == "o":
                    l[nex] = -1 * l[pre]
                # 両隣が同じはず
                else:
                    l[nex] = l[pre]

    return True


def main():
    N = int(input())
    S = input()

    for a, b in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        ans = [None] * N
        ans[0], ans[1] = a, b

        if solve(S, ans):
            print(*["S" if x == 1 else "W" for x in ans], sep="")
            return

    print(-1)


if __name__ == '__main__':
    main()
