class Solution:
    def num_swaps(self, a, b):

        if len(a) != len(b):
            return -1

        letter_dict = {}
        for char in a:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1

        for char in b:
            if char in letter_dict:
                letter_dict[char] -= 1
            else:
                letter_dict[char] = -1

        num_swaps = sum(abs(x) for x in letter_dict.values())/2

        return num_swaps

a = "abb"
b = "cbb"

sol = Solution()
print(sol.num_swaps(a,b))
