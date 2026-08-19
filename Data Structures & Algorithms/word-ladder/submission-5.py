class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        set_words = set(wordList)
        if endWord not in set_words: return 0
        len_word = len(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, level = queue.popleft()
            level += 1
            for i in range(len_word):
                for c in string.ascii_lowercase:
                    if word[i] == c: continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord: return level
                    if new_word in set_words: 
                        set_words.remove(new_word)
                        queue.append((new_word, level))
        return 0