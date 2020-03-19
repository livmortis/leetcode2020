# ——————题目
# 409. 最长回文串
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 注意:
# 假设字符串的长度不会超过 1010。
''''''
'''self'''
import collections
def longestPalindrome(s) -> int:
    result = collections.deque()
    s_list = list(s)
    flag = False
    for i, item in enumerate(s_list):
        # s_list.remove(item)     #遇到问题，list删除了元素，for循环的下一轮出问题。
        # 1、循环列表时，想删除列表中元素，用补0代替。
        s_list[i] = 0
        if item in s_list:
            s_list.remove(item)     #同上面一样循环过程中remove列表，但是是删除当前索引之后的元素，不影响循环。
            result.appendleft(item)
            result.append(item)
        elif not flag:
            result.append(item)         #这里投机取巧，只取一个单独的字符，随便append进来。真正回文字符应该append到正中间。
            flag = True
    return len(result) , result



if __name__ == "__main__":
    # result = longestPalindrome("abccccdd")
    # result = longestPalindrome("ccc")
    # result = longestPalindrome("caba")
    result = longestPalindrome("abadd")
    print(result)