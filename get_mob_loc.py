# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_mob_loc(map):
    n = len(map)
    m = len(map[0])

    newlist = []
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                newlist.append([i, j])

    print(newlist)


List = [[1,0,0,2],[3,3,2,1],[2,2,0,1]]
get_mob_loc(List)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
