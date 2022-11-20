#User function Template for python3

class Solution:
    def changeBits(self, N):
        p = 0
        while N >= (2**p):
           p += 1
        return (2**p-N-1, 2**p-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans = ob.changeBits(N)
        
        print(ans[0],ans[1])
# } Driver Code Ends