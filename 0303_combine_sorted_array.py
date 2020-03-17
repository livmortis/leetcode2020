# ——————题目
# 面试题 10.01. 合并排序的数组
# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
# 初始化 A 和 B 的元素数量分别为 m 和 n。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sorted-merge-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




# ——————关键
# 1、双指针循环法
# 时间复杂度只有O(m+n)，空间复杂度也是O(m+n)

# 2、思路
# 卡点：一旦一个数组全部读取完，指针势必指向数组越界的位置，再去比较两个数组元素就会数组越界。
# 解决：一旦一个数组全部读取完，就没必要再比较了，直接依次读另一个数组元素即可。

# 3、python基础
# 数组直接赋值数组，只是浅复制。需要赋值给数组切片

''''''
''' self  '''
# 双重for循环，弃用。
def merge1( A, m: int, B, n: int) -> None:
    """
    Do not return anything, modify A in-place instead.
    """
    C = []
    marker = -99999
    D = []
    for a in A:
        if a != 0:
            D.append(a)
    A = D
    for b in B:
        print("big for , b is " + str(b))
        for i in range(100):
            if i < len(A):
                a = A[i]
            else:
                a = A[-1]
            print("small for")

            if a <= marker and i < len(A):
                print("continue 2")
                continue
            print("a is " + str(a))
            print("A[-1] is " + str(A[-1]))
            if a <= b and i < len(A):
                C.append(a)
                print("if")
            # 两种情况插入b：   b当前值比a当前值小；a已经循环到最后一位，b还是更大

            else:
                C.append(b)
                marker = b
                print("marker is : "+ str(marker))
                print("else")
                break
        print(C)
        print("  ")
    A = C
    print(A)


''' official  官方解法 '''
def merge2( A, m: int, B, n: int) -> None:
    """
    Do not return anything, modify A in-place instead.
    """
    D = []
    for a in A:
        if a != 0:
            D.append(a)
    A[:] = D

    ai = 0
    bj = 0
    C = []
    if len(A) == 0:
        A[:] = B
        print(A)
        return
    if len(B) == 0:
        print(A)
        return
    # 借鉴一、双指针循环法。 利用指针ai循环A数组，指针bj循环B数组，且只需要一个for循环。
    #       “双指针方法。这一方法将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中。”
    while ai < len(A) or bj < len(B):
        print(ai)
        print(bj)
        print(C)
        # 借鉴二、由插入A数组元素变为插B数组元素，有两种情况： 1、A元素比B元素大；2、A元素已经插完，指针指向最后一位的后一位时。
        #        第二种情况时，再去比较AB元素大小，就会数组越界————一直卡在这里。
        #                       正确做法，只要A指针指向最后一位的后一位，就插B元素，且移动B指针，即可。
        if ai == len(A):
            C.append(B[bj])
            bj += 1
        elif bj == len(B):
            C.append(A[ai])
            ai += 1
        elif  A[ai] <= B[bj]:
            C.append(A[ai])
            ai += 1
            continue
        # if A[ai] > B[bj]:
        else:
            C.append(B[bj])
            bj += 1
            continue
    # 借鉴三、赋值给A必须赋值给A的切片A[:]，才能真正改变A的值。
    A[:] = C
    print(A)


if __name__ == "__main__":
    # merge1([1,2,3,0,0], 3, [2,5,6],3)
    # merge2([1,2,3,0,0], 3, [2,5,6],3)
    # merge2([1,2,3,0,0], 3, [],0)
    merge2([2,3,4], 3, [1,2],0)