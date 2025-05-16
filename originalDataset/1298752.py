H, W = map(int, input().split())
if H > W:
    tmp = H
    H = W
    W = tmp

if H%3 == 0 or W%3 == 0:
    print(0)
else:
    w1 = W//3
    w2 = w1+1
    rw1 = W - w1
    rw2 = W - w2
    h1 = H//2
    h2 = H - h1
    s11 = H * w1
    s12 = rw1 * h1
    s13 = rw1 * h2
    diff1 = max(abs(s11-s12), abs(s12-s13), abs(s13-s11))
    s21 = H * w2
    s22 = rw2 * h1
    s23 = rw2 * h2
    diff2 = max(abs(s21-s22), abs(s22-s23), abs(s23-s21))
    delta1 = min(diff1, diff2)

    s31 = w1 * H
    s32 = s31
    s33 = (W - 2 * w1) * H
    delta2 = abs(s33 - s31)

    s41 = w2 * H
    s42 = s41
    s43 = (W - 2 * w2) * H
    delta3 = abs(s43 - s41)
    
    tmp = H
    H = W
    W = tmp
    
    w1 = W//3
    w2 = w1+1
    rw1 = W - w1
    rw2 = W - w2
    h1 = H//2
    h2 = H - h1
    s11 = H * w1
    s12 = rw1 * h1
    s13 = rw1 * h2
    diff1 = max(abs(s11-s12), abs(s12-s13), abs(s13-s11))
    s21 = H * w2
    s22 = rw2 * h1
    s23 = rw2 * h2
    diff2 = max(abs(s21-s22), abs(s22-s23), abs(s23-s21))
    delta4 = min(diff1, diff2)

    s31 = w1 * H
    s32 = s31
    s33 = (W - 2 * w1) * H
    delta5 = abs(s33 - s31)

    s41 = w2 * H
    s42 = s41
    s43 = (W - 2 * w2) * H
    delta6 = abs(s43 - s41)    

    print(min(delta1, delta2, delta3, delta4, delta5, delta6))
    
