# ——————题目
# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
''''''
'''self1'''
'''执行结果：超出时间限制'''
def twoSum(nums, target) :
    result = []
    for i, num in enumerate(nums):
        for j, otherNum in enumerate(nums):
            if i == j:
                continue
            if num + otherNum == target :
                result.append(i)
                result.append(j)
                break
        else:
            continue
        break

    return result


'''self2
    失败，列表排序后会丢失索引信息。
'''
def twoSum2(nums, target) :
    # 1、排序nums
    # numsSort = nums
    numsSort = nums.copy()
    numsSort.sort()

    # 2、裁剪nums，去掉大于target的数
    short_nums = []
    for num in numsSort:
        if num <= target:
            short_nums.append(num)
        else:
            break

    # 3、从数组两头分别循环，求和
    length = len(short_nums)
    result = []
    for i, num in enumerate(short_nums):
        for j, otherNum in enumerate(short_nums[::-1]):
            if i == length-1-j:
                continue
            if num + otherNum < target:
                break
            if num + otherNum == target:
                result.append(nums.index(num))
                result.append(nums.index(otherNum))     #出错，如果num和otherNum值相同，index()无法分别得到各自索引。
                return result



'''self3
执行用时 :76 ms, 在所有 Python3 提交中击败了51.55%的用户
内存消耗 :17.9 MB, 在所有 Python3 提交中击败了5.05%的用户

1、排序前变为字典，保留索引信息
2、排序后，原计划将大于target的元素全删掉，后发现元素可能是负数，取消此步。
3、从前开始第一层for，从后开始第二层for，元素之和一旦小于target时，就跳出第二层for继续第一层。节省时间开销。

1、zip()将列表变成{索引:列表元素}字典。
2、sorted()和items()+lambda配合，可将字典按value值排序。
3、items()和list()配合，可将字典变为元素为元祖的列表。list(dict.items())。

'''
def twoSum3(nums, target) :
    # 1、列表转字典，通过zip()函数
    num_dict = dict(zip([i for i in range(len(nums))], nums))

    # 2、字典排序，通过items()，sorted()和lambda
    num_dict_sorted_by_value = dict( sorted(num_dict.items(), key= lambda xzy : xzy[1]) )


    # # 3、裁剪掉大于target的数，字典变为元素为元祖的列表    ----错误!  可能有负数
    # num_shorted = []
    # for elem_tuple in num_dict_sorted_by_value.items():
    #     if elem_tuple[1] <= target:
    #         num_shorted.append(elem_tuple)
    #     else:
    #         break
    # print(num_shorted)


    # 4、字典变列表，从列表两头分别循环，求和
    result = []
    for num in list(num_dict_sorted_by_value.items()):
        for otherNum in list(num_dict_sorted_by_value.items())[::-1]:
            if num[0] == otherNum[0]:
                print("continue")
                continue
            if num[1] + otherNum[1] < target:
                print("second break")
                break
            if num[1] + otherNum[1] == target:
                print("find it")
                result.append(num[0])
                result.append(otherNum[0])
                return result



if __name__ == "__main__":
    # result = twoSum([2, 7, 11, 15], 9)
    # result = twoSum3([2, 7, 11, 15], 9)
    result = twoSum3([-3,4,3,90], 0)
    print(result)
