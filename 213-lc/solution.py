class Solution:
    def rob(self, nums: List[int]) -> int:
        return None


if __name__ == "__main__":
    input1 = [2,3,2]
    input2 = [1,2,3,1]
    input3 = [1,2,3]
    solution = Solution()
    response1 = solution.rob(input1)
    response2 = solution.rob(input2)
    response3 = solution.rob(input3)

    assert response1 == 3
    assert response2 == 4
    assert response3 == 3

