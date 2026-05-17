class Soluation(object):
    def areOccurrencesEqual(self,s)->bool:
        result={}
        self.first=0

        for char in s:
            if char in result:
                result[char]+=1
            else:
                result[char]=1 
                
        for val in result:
            self.first = result[val]
            break
        
        for val in result:
            if result[val]!=self.first:
                return False
        return True

sol =Soluation()
sol1= sol.areOccurrencesEqual('aabbcc')
sol2= sol.areOccurrencesEqual('aabbbcc')
print(sol2)