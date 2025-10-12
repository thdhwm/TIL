# Trie, Prefix tree -> 문자열 처리, 검색에 특화된 트리 기반 자료 구조
# 자동 완성, 사전 검색, IP 주소 라우팅, 데이터 압축 등의 분야 에서 활용

# 동작 단계
# Trie 의 각 노드는 문자열의 개별 문자를 저장한다.
# 단어를 삽입할 때 각 문자를 순서대로 노드에 저장하고,
# 같은 접두사를 가진 단어는 그 부분을 공유한다.

# ex. 'app', 'apple', 'apply' 라는 3개의 단어를 저장하는 경우
# Trie는 각 문자를 노드로 저장
# 자식 노드는 다음에 올 수 있는 문자를 나타냄
# 첫 번째 레벨에는 a,
# 두 번째에는 p,
# 세 번째에도 p가 배치되며,
# 그 아래에 l,
# 그리고 그 다음에 e와 y가 연결된다.
# a - p - p - l - e
#               - y

class Node:
    def __init__(self):
        self.children = {}  # 자식 노드 dict
        self.is_end_of_word = False  # 단어 끝 여부

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True