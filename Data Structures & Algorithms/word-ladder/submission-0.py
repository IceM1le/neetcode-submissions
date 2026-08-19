class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])    # (слово, уровень)
        len_word = len(beginWord)
        while queue:
            word, level = queue.popleft()
            
            for i in range(len_word):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word == endWord:
                        return level + 1
                    
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, level + 1))
        
        return 0