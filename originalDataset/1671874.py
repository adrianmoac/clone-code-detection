

def main():
    N = int(input())
    Ds = [list(map(int, input().split())) for i in range(N)]
    Q = int(input())
    Ps = [int(input()) for i in range(Q)]

    scores_from_top_left = {}

    for height in range(1, N + 1):
        for width in range(1, N + 1):

            key = str(height) + ',' + str(width)

            if height == 1 and width == 1:
                scores_from_top_left[key] = Ds[0][0]
                continue

            if height == 1:
                base_key = str(height) + ',' + str(width - 1)
                scores_from_top_left[key] = scores_from_top_left[base_key] + Ds[0][width - 1]
                continue

            if width == 1:
                base_key = str(height - 1) + ',' + str(width)
                scores_from_top_left[key] = scores_from_top_left[base_key] + Ds[height - 1][0]
                continue

            base_key1 = str(height) + ',' + str(width - 1)
            base_key2 = str(height - 1) + ',' + str(width)
            base_key3 = str(height - 1) + ',' + str(width - 1)
            val = 0
            val += scores_from_top_left[base_key1]
            val += scores_from_top_left[base_key2]
            val -= scores_from_top_left[base_key3]
            val += Ds[height - 1][width - 1]
            scores_from_top_left[key] = val

    #OK
    #print(scores_from_top_left)

    max_scores = {}

    for height in range(1, N + 1):
        for width in range(1, N + 1):

            key = height * width
            max_score = 0

            for y in range(height, N + 1):
                for x in range(width,N + 1):
                    score = 0

                    if y == height and x == width:
                        score = scores_from_top_left[str(y) + ',' + str(x)]
                    elif y == height:
                        val1 = scores_from_top_left[str(y) + ',' + str(x)]
                        val2 = scores_from_top_left[str(y) + ',' + str(x - width)]
                        score = val1 - val2

                    elif x == width:
                        val1 = scores_from_top_left[str(y) + ',' + str(x)]
                        val2 = scores_from_top_left[str(y - height) + ',' + str(x)]
                        score = val1 - val2
                    else:

                        base_key = str(y) + ',' + str(x)
                        base_key1 = str(y - height) + ',' + str(x)
                        base_key2 = str(y) + ',' + str(x - width)
                        base_key3 = str(y - height) + ',' + str(x - width)

                        score = scores_from_top_left[base_key]
                        score -= scores_from_top_left[base_key1]
                        score -= scores_from_top_left[base_key2]
                        score += scores_from_top_left[base_key3]

                    if score > max_score:
                        max_score = score

            if key not in max_scores:

                max_scores[key] = max_score
            else:
                if max_scores[key] < max_score:
                    max_scores[key] = max_score

    #print(max_scores)
    for i in range(Q):

        max_score = 0

        for j in range(1, Ps[i] + 1):
            if j not in max_scores.keys():
                continue
            if max_scores[j] > max_score:
                max_score = max_scores[j]
        print(max_score)




if __name__ == '__main__':
    main()
