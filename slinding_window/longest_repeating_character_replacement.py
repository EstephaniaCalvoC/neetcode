from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    l = 0
    max_length = 0
    max_freq = 0
    counters = defaultdict(int)

    for r in range(len(s)):
        freq = counters[s[r]] + 1
        counters[s[r]] = freq
        max_freq = max(freq, max_freq)

        while r - l + 1 - max_freq > k:
            counters[s[l]] -= 1
            l += 1
        
        max_length = max(max_length, (r - l + 1))

    return max_length


if __name__ == "__main__":
    print(characterReplacement('XYYX', 2)) # 4
    print(characterReplacement('AAXYYYYYY', 2)) # 8
    print(characterReplacement('AAABABB', 1)) # 5
    print(characterReplacement('UFYAAABABB', 1)) # 5
    print(characterReplacement('XYYXUAAABABB', 1)) # 5
