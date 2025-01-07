class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        ans = set()
        for w in words:
            for w2 in words:
                if w != w2 and w in w2:
                    ans.add(w)

        return list(i for i in words if i in ans)


if __name__ == '__main__':
    assert Solution().stringMatching(words = ["mass","as","hero","superhero"]) == ["as","hero"], Solution().stringMatching(words = ["mass","as","hero","superhero"])
    assert Solution().stringMatching(words = ["leetcode","et","code"]) == ["et","code"], Solution().stringMatching(words = ["leetcode","et","code"])
    assert Solution().stringMatching(words = ["blue","green","bu"]) == [], Solution().stringMatching(words = ["blue","green","bu"])