# ——————题目
# 1160. 拼写单词
# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
# 注意：每次拼写时，chars 中的每个字母都只能用一次。
# 返回词汇表 words 中你掌握的所有单词的 长度之和。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

''''''
''' self 列表法 '''
'''
执行用时：264 ms
内存消耗：13.8 MB
'''
def countCharacters( words, chars: str) :
    num = 0
    for word in words:
        chars_list = [i for i in chars]
        for char_in_word in word:
            if char_in_word in chars_list:
                chars_list.remove(char_in_word)
            else:
                break
        else:
            num += len(word)
    return num




''' official  哈希表法 '''
'''
执行用时 :192 ms, 在所有 Python3 提交中击败了59.39%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.11%的用户
'''

# 借鉴一，collections库中的Counter(可迭代对象)，可以类似倒排列表，返回一个字典，里面每一项是元素:元素个数。
# 借鉴二，words中每个字符属于chars中字符，等价于，words中每个字符的个数，小于chars中该字符的个数。
import collections
def countCharacters2(words, chars: str):
    num = 0
    chars_hash = collections.Counter(chars)
    for word in words:
        word_hash = collections.Counter(word)
        # 借鉴三：for in循环字典，每一项是字典每个元素的key。
        for word_hash_element_key in word_hash:
            if word_hash[word_hash_element_key] <= chars_hash[word_hash_element_key]:
                continue
            else:
                break
        else:
            num += len(word)
    return num



if __name__ == "__main__":
    # num = countCharacters2(["cat","bt","hat","tree"], "atach")
    num = countCharacters2(["hello","world","leetcode"],"welldonehoneyr")
    print(num)