from itertools import accumulate


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        def valid_string(s: str) -> bool:
            vowels = {'u', 'e', 'o', 'a', 'i'}
            return {s[0],s[-1]} <= vowels
        processed_words = map(valid_string, words)
        pref = list(accumulate(processed_words, initial=0))
        return [pref[end+1] - pref[start] for start, end in queries]

if __name__ == '__main__':
    assert Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], 
                                   queries = [[0,2],[1,4],[1,1]]) == [2,3,0], Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
    assert Solution().vowelStrings(words = ["a","e","i"], 
                                   queries = [[0,2],[0,1],[2,2]]) == [3,2,1], Solution().vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])