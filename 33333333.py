from math import factorial as fact
class Solution:

    def posIntSol(self,s):

        r=1
        n=""
        for i in range(len(s)):
            if(s[i]=="+"):
                r+=1
            if(s[i]=="="):
                n=s[i+1:]
                break     
        n=int(n)
        
        if(n-1>=r-1):
            x=fact(n-1)
            y=fact(n-r)
            z=fact(r-1)
            return x//(y*z)
        else:
            return 0
        
        

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.posIntSol(s))