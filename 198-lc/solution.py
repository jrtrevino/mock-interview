class Solution:
    def rob(self, nums: List[int]) -> int:
        return None


if __name__ == "__main__":
    input1 = [1,2,3,1]
    input2 = [2,7,9,3,1]
    solution = Solution()
    response1 = solution.rob(input1)
    response2 = solution.rob(input2)

    assert response1 == 4
    assert response2 == 12
