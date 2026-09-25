from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lookup = defaultdict(list)
        res = 0
        q = deque()
        visited = set()

        wordList.append(beginWord)

        for word in wordList:
            word_len = len(word)

            for i in range(word_len):
                w = word[:i] + "*" + word[i+1: word_len]
                lookup[w].append(word)
        
        q.append(beginWord)

        print(f"Dict: {lookup}")

        while q:
            q_len = len(q)
            res += 1

            for _ in range(q_len):
                word = q.popleft()
                
                if word in visited:
                    continue
                else:
                    visited.add(word)

                if word == endWord:
                    return res

                for i in range(len(word)):
                    w = word[:i] + "*" + word[i+1: word_len]

                    if len(lookup[w]) > 1:
                        for e in lookup[w]:
                            if e == word:
                                continue

                            q.append(e)

        return 0                   
        
