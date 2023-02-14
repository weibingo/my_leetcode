#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        lenm = max(lena, lenb)
        addOne = 0
        c=[]
        for i in range (lenm-1, -1, -1):
            aa,bb = 0,0
            lena = lena -1
            lenb = lenb -1
            if (lena >= 0):
                aa = int(a[lena])
            if (lenb >= 0):
                bb = int(b[lenb])
            cc = aa + bb + addOne
            if (cc == 2):
                addOne = 1
                cc = 0
            c.insert(i, str(cc))
        if (addOne > 0):
            c.insert(0, str(addOne))
        return ''.join(c)  

        
# @lc code=end

