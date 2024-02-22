from typing import List

class Solution:
        def checkIfExist(self, arr: List[int]) -> bool:
            # start beginning of the array
            # compare the anchor to the rest of the array
            # arr[i] == 2 * arr[j]
            for i in range(len(arr)):
                 for j in range(i + 1, len(arr)):
                      if arr[i] == 2 * arr[j]:
                           return True
            
            return False

if __name__ == "__main__":
    input1 = [10,2,5,3]
    input2 = [3,1,7,11]
    solution = Solution()
    response1 = solution.checkIfExist(input1)
    response2 = solution.checkIfExist(input2)

    assert response1 == True
    assert response2 == False
