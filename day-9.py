from typing import List
from collections import deque

def word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    This function finds the length of the shortest transformation sequence from `beginWord` to `endWord`,
    changing one letter at a time, with each intermediate word being in `wordList`.

    :param beginWord: The word to start the transformation.
    :param endWord: The word to end the transformation.
    :param wordList: A list of allowed words for the transformation.
    :return: The length of the shortest transformation sequence. If no such sequence exists, returns 0.
    """
    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Use a set for O(1) look-ups
    queue = deque([(beginWord, 1)])  # Queue for BFS, storing word and sequence length

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length - 1

        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i+1:]

                # Check if the next word is in the word set and not the same as the current word
                if next_word in wordSet and next_word != word:
                    queue.append((next_word, length + 1))
                    wordSet.remove(next_word)  # Remove to prevent revisiting

    return 0

# Example calls
print(word_ladder("and", "ant", ["add", "aid", "and", "ant", "any"]))  # Expected output: 1
print(word_ladder("phone", "phase", ["phone", "phane", "plane", "prane", "prase", "phase"]))  # Expected output: 2
