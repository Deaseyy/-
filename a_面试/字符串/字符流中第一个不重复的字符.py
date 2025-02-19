"""
# 牛客网
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""


def find_first_unique_char(s):
    hash = {}
    for c in s:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1

    for c in s:
        if hash[c] == 1:
            return c


s = 'google'
print(find_first_unique_char(s))

