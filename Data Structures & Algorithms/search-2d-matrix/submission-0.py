class Solution:
    def searchrow(self,row:List[int],target:int) -> bool:
            left=0
            right=len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    left=mid+1
                elif row[mid]>target:
                    right=mid-1
            return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            row=matrix[mid]
            if row[0]<=target<=row[-1]:
                return self.searchrow(row,target)
            if row[0]>target:
                right=mid-1
            if row[-1]<target:
                left=mid+1
        return False

