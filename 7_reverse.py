# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 来源：力扣（LeetCode）

class Solution():
    def reverse(self, x):
        def revesemyself(num):
            l = []
            temp = num
            out = num
            numfianl = 0

            while out != 0:
                temp = out % 10
                out = out // 10
                l.append(temp)
            j = 1
            for i in l:
                numfianl = i * 10 ** (len(l) - j) + numfianl
                j = j + 1
            return numfianl
        if (-2**31) <= x <= (2**31 - 1):
            if x > 0:
                final = revesemyself(x)

            if x < 0:
                x = -x
                final = -revesemyself(x)

            if x == 0:
                final = x

            if (-2**31) <= final <= (2**31 - 1):
                return final
            else:
                return 0

        else:
            return 0


ss = Solution()
s = ss.reverse(1534236469)
print(s)

