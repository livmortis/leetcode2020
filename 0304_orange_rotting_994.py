import collections

# ——————题目
# 994. 腐烂的橘子
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotting-oranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


''' self  '''
def orangesRotting(grid) -> int:
    height = len(grid)
    width = len(grid[0])
    hasFresh = False
    hasRotting = False
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                hasFresh = True
            if grid[y][x] == 2:
                hasRotting = True
            if hasRotting and hasFresh:
                break
        else:
            continue
        break

    if not hasFresh:
        return 0
    if not hasRotting:
        return -1
    num = 0
    while hasFresh:
        changed = False
        hasFresh = False
        print(grid)
        tempAxisList = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    continue
                if grid[y][x] == 2:
                    tempAxisList.append([y,x])
                    changed = True
        print("tempaxislist " + str(tempAxisList))
        for axis in tempAxisList:
            y = axis[0]
            x = axis[1]
            if x+1 < width and grid[y][x+1] == 1:
                grid[y][x+1] += 1
            if x-1 >= 0 and grid[y][x-1] == 1 :
                grid[y][x-1] += 1
            if y+1 < height and grid[y+1][x] == 1:
                grid[y+1][x] += 1
            if y-1 >= 0 and grid[y-1][x] == 1:
                grid[y-1][x] += 1

        if changed:
            num += 1

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    hasFresh = True
                    print("fresh y is " + str(y))
                    print("fresh x is " + str(x))
                    break
            else:
                continue
            break
        if num > 999:
            return -1
        print("num is " + str(num))

    return num


''' official  官方解法 '''
def orangesRotting2(self, grid):
    R, C = len(grid), len(grid[0])

    # queue - all starting cells with rotting oranges
    # 借鉴一、双端队列数据结构的使用。  collections.deque()
    #        使得while循环有了更好的终止方法————队列里元素删完的时候 popleft()。
    #        即，自己代码是以“不再有1的元素为止”，这里是以“所有2的元素已经都腐蚀过周围了为止”。 解决了可能最终也会包含有1的元素无法腐蚀，从而循环无法终止的情况。
    queue = collections.deque()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r, c, 0))

    def neighbors(r, c):
        for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    d = 0
    while queue:
        r, c, d = queue.popleft()   #每次循环删队列元素
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr, nc, d + 1))

    # 借鉴二、1、any()函数，参数是列表或元组，对列表所有元素进行且运算。
    # 2、in操作符，判断某数是否存在于列表中，返回一个bool值。
    # 3、(for in) 生成器表达式，遍历每一行
    if any(1 in row for row in grid):
        return -1
    return d




if __name__ == "__main__":
    a = orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    # a = orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    # a = orangesRotting([[0,2]])
    # a = orangesRotting([[1]])
    # a = orangesRotting([[1,0,1,0,0,1,1,0],[1,1,2,0,1,2,1,1],[1,2,2,0,1,2,0,2],[1,1,1,0,1,0,1,1],[0,2,1,0,1,1,1,2],[0,2,1,0,1,0,0,0],[2,0,1,2,1,0,1,1],[0,1,2,0,0,2,2,0],[2,2,1,0,1,0,2,0]]
# )

    print(a)

