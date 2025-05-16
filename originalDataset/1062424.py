import math

class Gathering:

    def is_possible(self, t):

        
        dist = t / self.points[0][2]
        x_l  = self.points[0][0] - dist
        x_h  = self.points[0][0] + dist
        y_l  = self.points[0][1] - dist
        y_h  = self.points[0][1] + dist

        for i in range(1, self.n):

            dist        = t / self.points[i][2]
            current_x_l = self.points[i][0] - dist
            current_x_h = self.points[i][0] + dist

           
            if current_x_l > x_h or current_x_h < x_l:
                return False

           
            x_l = max(x_l, current_x_l)
            x_h = min(x_h, current_x_h)

        for i in range(1, self.n):

            dist        = t / self.points[i][2]
            current_y_l = self.points[i][1] - dist
            current_y_h = self.points[i][1] + dist

            
            if current_y_l > y_h or current_y_h < y_l:
                return False

            
            y_l = max(y_l, current_y_l)
            y_h = min(y_h, current_y_h)

        return True

    def gather(self, n, points):

        self.n      = n
        self.points = points

        start = -1
        end   = pow(10, 9)
        mid   = (start+end) / 2.0

        for _ in range(100):

            if self.is_possible(mid):
                end = mid
            else:
                start = mid

            mid = (start+end) / 2.0

        print mid

if __name__ == "__main__":

    n = int(raw_input())
    points = [[float(j) for j in raw_input().split()] for i in range(n)]

    arc = Gathering()
    arc.gather(n, points)
