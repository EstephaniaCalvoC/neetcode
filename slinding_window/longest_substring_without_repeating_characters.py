from typing import List


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0 
    
    aux_set = set()
    l = 0
    r = 1
    max_length = 1

    while r < len(s):
        if r - l == 1 and s[l] == s[r]:
            l += 1
            r += 1
            continue
        elif r - l == 1 and s[l] != s[r]:
            aux_set = {s[l]}

        if s[r] not in aux_set:
            aux_set.add(s[r])
            length = r - l + 1 
            max_length =  max_length if max_length > length else length
            r += 1
        else:
            while s[l] != s[r]:
                aux_set.remove(s[l])
                l += 1
            l += 1
            r += 1

    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("zxyzxyz")) # 3
    print(lengthOfLongestSubstring("zxyzxyzabcdfg")) # 9
    print(lengthOfLongestSubstring("xxxxx")) # 1

