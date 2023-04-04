class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'},
            10: {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
            100: {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'},
            1000: {1: 'M'}
        }

        i = 1
        ans = []
        while num:
            sym = num % 10
            num //= 10
            if sym < 4:
                ans.append(sym * symbols[i][1])
            elif sym == 4:
                ans.append(symbols[i][4])
            elif sym == 5:
                ans.append(symbols[i][5])
            elif sym < 9:
                ans.append(symbols[i][5] + (sym - 5) * symbols[i][1])
            elif sym == 9:
                ans.append(symbols[i][9])
            i *= 10

        return ''.join(ans[::-1])

    def intToRoman_leetcode_solution(self, num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"],
                         [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman


solution = Solution()

assert solution.intToRoman(10) == 'X'
assert solution.intToRoman(58) == 'LVIII'
assert solution.intToRoman(1994) == 'MCMXCIV'

assert solution.intToRoman_leetcode_solution(10) == 'X'
assert solution.intToRoman_leetcode_solution(58) == 'LVIII'
assert solution.intToRoman_leetcode_solution(1994) == 'MCMXCIV'
