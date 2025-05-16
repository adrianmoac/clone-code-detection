#!/usr/bin/env python


def read():
    row, col = map(int, raw_input().split())
    b = []
    for i in range(row):
        b.append(raw_input())
    return row, col, b


def work((row, col, b)):
    toPut = [[True for j in range(col)] for i in range(row)]

    for r in range(row):
        for c in range(col):
            if b[r][c] == '#':
                continue
            for (dr, dc) in [(-1, -1), (-1, 0), (-1, 1), \
                             ( 0, -1), ( 0, 0), ( 0, 1), \
                             ( 1, -1), ( 1, 0), ( 1, 1)]:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < row and 0 <= nc < col):
                    continue
                toPut[nr][nc] = False


    putResult = [['.' for j in range(col)] for i in range(row)]
    for r in range(row):
        for c in range(col):
            
            if not toPut[r][c]:
                continue
            
            for (dr, dc) in [(-1, -1), (-1, 0), (-1, 1), \
                             ( 0, -1), ( 0, 0), ( 0, 1), \
                             ( 1, -1), ( 1, 0), ( 1, 1)]:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < row and 0 <= nc < col):
                    continue
                putResult[nr][nc] = '#'

    
    for r in range(row):
        for c in range(col):
            if putResult[r][c] != b[r][c]:
                print 'impossible'
                return

    
    orig = [[] for i in range(row)]
    
    for r in range(row):
        for c in range(col):
            orig[r].append('#' if toPut[r][c] else '.')
    
    print "possible"
    for r in range(row):
        print ''.join(orig[r])


if __name__ == "__main__":
    work(read())
