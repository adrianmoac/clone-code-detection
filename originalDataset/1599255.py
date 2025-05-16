# -*- coding=utf-8 -*-
def convert_lines_to_int(args):
    """ "a b c d e f ..." >> [a, b, c, d, e, f ...]
        args:
            args:text splited by space.
        return:
            list
    """
    return list(map(int, args.split(" ")))

ball_count = int(input())
type_b_robot_point = int(input())
ball_point_x = convert_lines_to_int(input())

class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collect_ball(self, ball_point):
        pass

class RobotA(Robot):
    def __init__(self, x, y):
        self.x = 0
        self.y = y
        self.collect_cost = None

    def collect_ball(self, ball_point):
        self.collect_cost = ball_point * 2

class RobotB(Robot):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collect_cost = None

    def collect_ball(self, ball_point):
        self.collect_cost = (self.x - ball_point) * 2

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


ball_list = [Ball(ball_point_x[count], count + 1) for count in range(ball_count)]
robot_a_list = list()
robot_b_list = list()
for ball in ball_list:
    r = RobotA(ball.x, ball.y)
    r.collect_ball(ball.x)
    robot_a_list.append(r)

    r = RobotB(type_b_robot_point, ball.y)
    r.collect_ball(ball.x)
    robot_b_list.append(r)
# Test
# for r in robot_a_list:
#     print(r.collect_cost)
#
# print("")
#
# for r in robot_b_list:
#     print(r.collect_cost)

# Check!
summary = list()
for i in range(ball_count):
    if robot_a_list[i].collect_cost > robot_b_list[i].collect_cost:
        summary.append(robot_b_list[i].collect_cost)
    else:
        summary.append(robot_a_list[i].collect_cost)

print(sum(summary))