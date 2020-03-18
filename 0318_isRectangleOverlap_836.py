# ——————题目
# 836. 矩形重叠
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
#
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
#
# 给出两个矩形，判断它们是否重叠并返回结果。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rectangle-overlap
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

''''''
'''self'''
# 注意坐标系，y轴坐标轴是向上的，不是image里向下的。
def isRectangleOverlap(rec1, rec2) -> bool:
    x1,y1,x2,y2 = rec1[0],rec1[1],rec1[2],rec1[3]
    _x1,_y1,_x2,_y2 = rec2[0],rec2[1],rec2[2],rec2[3]
    if x2 <= _x1 or _x2 <= x1 or y2 <= _y1 or _y2 <= y1:
        return False
    else:
        # 题目没要求求面积，这里直接返回True也可以。
        x_left = max(x1, _x1)
        x_right = min(x2, _x2)
        y_top = min(y2, _y2)
        y_bottom = max(y1, _y1)
        area = (x_right - x_left) * (y_top - y_bottom)
        print(area)
        return (area > 0)


if __name__ == "__main__":
    isOver = isRectangleOverlap([0,0,2,2], [1,1,3,3])
    print(isOver)


