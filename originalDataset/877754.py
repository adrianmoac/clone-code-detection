S = raw_input()

val = int(S)

if len(S) >= 2:
    for sep in xrange(1, len(S)):
        val += int(S[:sep]) + int(S[sep:])

if len(S) >= 3:
    for sep1 in xrange(1, len(S)-1):
        for sep2 in xrange(sep1 + 1, len(S)):
            val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:])

if len(S) >= 4:
    for sep1 in xrange(1, len(S)-2):
        for sep2 in xrange(sep1 + 1, len(S)-1):
            for sep3 in xrange(sep2 + 1, len(S)):
                val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:])

if len(S) >= 5:
    for sep1 in xrange(1, len(S)-3):
        for sep2 in xrange(sep1 + 1, len(S)-2):
            for sep3 in xrange(sep2 + 1, len(S)-1):
                for sep4 in xrange(sep3 + 1, len(S)):
                    val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:])

if len(S) >= 6:
    for sep1 in xrange(1, len(S)-4):
        for sep2 in xrange(sep1 + 1, len(S)-3):
            for sep3 in xrange(sep2 + 1, len(S)-2):
                for sep4 in xrange(sep3 + 1, len(S)-1):
                    for sep5 in xrange(sep4 + 1, len(S)):
                        val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:sep5]) + int(S[sep5:])

if len(S) >= 7:
    for sep1 in xrange(1, len(S)-5):
        for sep2 in xrange(sep1 + 1, len(S)-4):
            for sep3 in xrange(sep2 + 1, len(S)-3):
                for sep4 in xrange(sep3 + 1, len(S)-2):
                    for sep5 in xrange(sep4 + 1, len(S)-1):
                        for sep6 in xrange(sep5 + 1, len(S)):
                            val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:sep5]) + int(S[sep5:sep6]) + int(S[sep6:])

if len(S) >= 8:
    for sep1 in xrange(1, len(S)-6):
        for sep2 in xrange(sep1 + 1, len(S)-5):
            for sep3 in xrange(sep2 + 1, len(S)-4):
                for sep4 in xrange(sep3 + 1, len(S)-3):
                    for sep5 in xrange(sep4 + 1, len(S)-2):
                        for sep6 in xrange(sep5 + 1, len(S)-1):
                            for sep7 in xrange(sep6 + 1, len(S)):
                                val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:sep5]) + int(S[sep5:sep6]) + int(S[sep6:sep7]) + int(S[sep7:])

if len(S) >= 9:
    for sep1 in xrange(1, len(S)-7):
        for sep2 in xrange(sep1 + 1, len(S)-6):
            for sep3 in xrange(sep2 + 1, len(S)-5):
                for sep4 in xrange(sep3 + 1, len(S)-4):
                    for sep5 in xrange(sep4 + 1, len(S)-3):
                        for sep6 in xrange(sep5 + 1, len(S)-2):
                            for sep7 in xrange(sep6 + 1, len(S)-1):
                                for sep8 in xrange(sep7 + 1, len(S)):
                                    val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:sep5]) + int(S[sep5:sep6]) + int(S[sep6:sep7]) + int(S[sep7:sep8]) + int(S[sep8:])

if len(S) >= 10:
    for sep1 in xrange(1, len(S)-8):
        for sep2 in xrange(sep1 + 1, len(S)-7):
            for sep3 in xrange(sep2 + 1, len(S)-6):
                for sep4 in xrange(sep3 + 1, len(S)-5):
                    for sep5 in xrange(sep4 + 1, len(S)-4):
                        for sep6 in xrange(sep5 + 1, len(S)-3):
                            for sep7 in xrange(sep6 + 1, len(S)-2):
                                for sep8 in xrange(sep7 + 1, len(S)-1):
                                    for sep9 in xrange(sep8 + 1, len(S)):
                                        val += int(S[:sep1]) + int(S[sep1:sep2]) + int(S[sep2:sep3]) + int(S[sep3:sep4]) + int(S[sep4:sep5]) + int(S[sep5:sep6]) + int(S[sep6:sep7]) + int(S[sep7:sep8]) + int(S[sep8:sep9]) + int(S[sep9:])

print val