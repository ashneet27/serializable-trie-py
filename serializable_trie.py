from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.isValidWord: bool = False
        self.wordsWithPrefix: int = 0
        self.children: dict[str, TrieNode] = {}


class Trie:
    def __init__(self, words: list[str] = []) -> None:
        self.root: TrieNode = TrieNode()
        self.totalWords = 0
        for word in words:
            self.insertWord(word)

    @classmethod
    def fromListOfWords(cls, words: list[str]) -> Trie:
        return cls(words)

    @classmethod
    def fromSerializedTrie(serializedTrie: str) -> Trie:
        pass

    def insertWord(self, word: str) -> None:
        curNode = self.root
        for c in word:
            curNode.wordsWithPrefix += 1
            if c in curNode.children:
                curNode = curNode.children[c]
            else:
                curNode.children[c] = TrieNode()
                curNode = curNode.children[c]
        curNode.wordsWithPrefix += 1
        curNode.isValidWord = True
        self.totalWords += 1

    def findWord(self, word: str) -> bool:
        return self.wordsWithPrefix(word, prefixShouldBeWord=True) > 0

    def wordsWithPrefix(self, prefix: str, prefixShouldBeWord: bool = False) -> int:
        curNode = self.root
        for c in prefix:
            if c in curNode.children:
                curNode = curNode.children[c]
            else:
                return False
        if prefixShouldBeWord == False or curNode.isValidWord:
            return curNode.wordsWithPrefix
        return 0

    def dfsRecursiveAndStoreInList(
        self, curNode: TrieNode, storingList: list[str], prefix: str = ""
    ) -> None:
        if curNode.isValidWord == True:
            storingList.append(prefix)

        for c in curNode.children:
            prefix += c
            self.dfsRecursiveAndStoreInList(curNode.children[c], storingList, prefix)
            prefix = prefix[:-1]

    def toListOfWords(self) -> list[str]:
        words = []
        self.dfsRecursiveAndStoreInList(self.root, words)
        return words


if __name__ == "__main__":
    trie = Trie.fromListOfWords(["hello", "chat", "chips", "chip"])
    print(trie.toListOfWords())
