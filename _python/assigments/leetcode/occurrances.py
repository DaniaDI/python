class Solution(object):
    def areOccurrencesEqual(self, s) -> bool:
        result = {}

        # for each char in string if is char found =>+1 else =1
        for char in s:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

        #  first =result[val]=>ex:{'a':2}=>first =2
        first = 0
        for val in result:
            first = result[val]
            break
# first=2 =>if val =first for all val in result then return true else false
        for val in result:
            if result[val] != first:
                return False

        return True
    
sol = Solution()
result=sol.areOccurrencesEqual('aabbcc')
r2=sol.areOccurrencesEqual('abbaabc')
print(result)
print(r2)