class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for _ in range(n)]
        top=0
        bottom=n-1
        left=0
        right=n-1

        num=1
        while top<=bottom and left<=right:

            for i in range(left,right+1):
                mat[top][i]=num
                num+=1
            top+=1

            for j in range(top,bottom+1):
                mat[j][right]=num
                num+=1
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    mat[bottom][i]=num
                    num+=1
                bottom-=1
            
            if left<=right:
                for j in range(bottom,top-1,-1):
                    mat[j][left]=num
                    num+=1
                left+=1
            
        return mat
                        
        