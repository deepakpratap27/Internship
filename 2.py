
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        i = 0
        j = 0
        result, sum1, sum2 = 0,0,0
        
        while i<m and j<n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                sum2 += arr2[j]
                j+=1
            else:
                result += max(sum1,sum2)+arr1[i]
                sum1 = 0
                sum2 = 0
                i+=1
                j+=1
                
        while i<m:
            sum1+=arr1[i]
            i+=1
        while j<n:
            sum2+=arr2[j]
            j+=1
            
        result+= max(sum1,sum2)
        return result
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        print(Solution().maxSumPath(arr1, arr2, m, n))
