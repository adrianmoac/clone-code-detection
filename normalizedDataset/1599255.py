#-*-coding=utf-8-*-def convert_lines_to_int(args):
    """ "a b c d e f ...">>[a, b, c, d, e, f ...]
        args:
            args:text splited by space.
        return:
            list
    """
    return id0(map(id1, id2.split(" ")))

id3=id1(input())
id4=id1(input())
id5=id6(input())

class id7(id8):
    def id9(id10, id11, id12):
        id10.id11=id11
        id10.id12=id12

    def id13(id10, id14):
        pass

class id15(id7):
    def id9(id10, id11, id12):
        id10.id11=0
        id10.id12=id12
        id10.id16=None

    def id13(id10, id14):
        id10.id16=id14*2

class id17(id7):
    def id9(id10, id11, id12):
        id10.id11=id11
        id10.id12=id12
        id10.id16=None

    def id13(id10, id14):
        id10.id16=(id10.id11-id14)*2

class id18(id8):
    def id9(id10, id11, id12):
        id10.id11=id11
        id10.id12=id12


id19=[id18(id5[id20], id20+1) for id20 in id21(id3)]
id22=id0()
id23=id0()
for id24 in id19:
    id25=id15(id24.id11, id24.id12)
    id25.id13(id24.id11)
    id22.id26(id25)

    id25=id17(id4, id24.id12)
    id25.id13(id24.id11)
    id23.id26(id25)
# Test
# for r in robot_a_list:
#     print(r.collect_cost)
#
# print("")
#
# for r in robot_b_list:
#     print(r.collect_cost)

# Check!summary=list()
for id27 in id21(id3):
    if id22[id27].id16>id23[id27].id16:
        id28.id26(id23[id27].id16)
    else:
        id28.id26(id22[id27].id16)

print(id29(id28))