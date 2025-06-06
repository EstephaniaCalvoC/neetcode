from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    tmp_stack = []

    for i, t in enumerate(temperatures):
        while tmp_stack and tmp_stack[-1][1] < t:
            previous_i = tmp_stack.pop()[0]
            result[previous_i] = i - previous_i
        tmp_stack.append((i, t))
    
    return result




if __name__ == "__main__":
    print(dailyTemperatures([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]
    print(dailyTemperatures([22,21,20])) # [0,0,0]
