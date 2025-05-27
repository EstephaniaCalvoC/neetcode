from typing import List

def maxArea(heights: List[int]) -> int:
    """
    Input: height = [1,7,2,5,4,7,3,6]
    Output: 36
    """
    max_area = 0

    l = 0
    r = len(heights) - 1

    while l < r:
        base = (r - l)
        height = min(heights[l], heights[r])
        area = base * height

        max_area = area if area > max_area else max_area

        # minum height is left
        l += 1 if heights[l] == height and heights[l] <= height + 1 else 0

        # minum height is rigth
        r -= 1 if heights[r] == height and heights[r] <= height + 1 else 0
        
    return max_area


if __name__ == "__main__":
    print(maxArea([1,7,2,5,4,7,3,6])) # 36
    print(maxArea([2,2,2])) #4 
    print(maxArea([1,2,4,3])) #4
    