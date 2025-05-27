from typing import List


def group_anagrams_1(strs: List[str]):
    # Time complexity: O(n * k * log(k)), where n is the number of strings and k is the maximum length of a string
    # Space complexity: O(n * k)
    anagrams = {}

    for word in strs:
        sorted_word = tuple(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word]=[word]

    return list(anagrams.values())

def group_anagrams_2(strs: List[str]):
    # Assuming the words only contains a - z characters
    # Time complexity O(n*k) and space complexity of O(n * 26) ->
    anagrams = {}
    l_characters = ord('z') - ord('a') + 1

    for word in strs:
        counter = [0] * l_characters
        for l in word:
            index = ord(l) - ord('a')
            counter[index] += 1

        counter_key = tuple(counter)

        if counter_key in anagrams:
            anagrams[counter_key].append(word)
        else:
            anagrams[counter_key] = [word]
    
    return list(anagrams.values())

def group_anagrams_3(strs: List[str]):
    # TODO: Time complexity O(n * k) using defaultdict
    pass


if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    print(group_anagrams_2(strs)) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
