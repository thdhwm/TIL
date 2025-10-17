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

# #############################################################################################################################
# 기본 코드

class Node:    # Trie의 각 노드를 나타내는 클래스, 문자와 그 자식 노드들, 그리고 단어의 끝 여부를 저장

    def __init__(self):    # 새로운 노드를 생성할 때 호출되며, 자식 노드와 단어 끝 여부를 초기화
        self.children = {}  # 자식 노드 dict, 이 딕셔너리는 키로 문자(char)를, 값으로 해당 문자를 루트로 하는 자식 노드(Node 객체) 저장
        self.is_end_of_word = False  # 현재 노드가 단어의 끝인지 나타내는 플래그


class Trie:    # Trie 자료구조를 나타내는 Trie 클래스, 단어 삽입, 검색, 접두사 확인 기능

    def __init__(self):    # 빈 루트 노드를 생성

        self.root = Node()    # 루트 노드를 생성
        # Trie의 시작점으로, 어떤 문자도 대표하지 않는 빈 노드, 모든 단어는 이 루트에서 시작해 분기


    def insert(self, word):    # Trie에 단어를 삽입하는 메서드
    # 주어진 단어를 문자 단위로 분해하여 Trie에 삽입, 각 문자는 노드에 저장되며, 마지막 문자에서 단어의 끝을 표시

        node = self.root     # 현재 노드를 루트 노드로 설정
        for char in word:    # 단어의 각 문자를 순회
            if char not in node.children:       # 현재 문자에 해당하는 자식 노드가 없으면 새 노드 생성
                node.children[char] = Node()    # 생성한 새 노드를 현재 노드의 children 딕셔너리에 추가

            node = node.children[char]          # 다음 문자를 처리하기 위해 현재 노드를 자식 노드로 갱신

        node.is_end_of_word = True        # 단어의 모든 문자를 처리한 후, 마지막 노드의 is_end_of_word를 True로 설정


    def search(self, word):    # Trie에서 단어가 존재하는지 확인하는 메서드

        node = self.root     # 현재 노드를 루트 노드로 설정

        for char in word:    # 단어의 각 문자를 순회
            if char not in node.children:    # 현재 노드의 children 딕셔너리에 문자가 없으면
                return False                 # 단어가 Trie에 존재하지 않으므로 False를 반환

            node = node.children[char]       # 다음 문자를 처리하기 위해 현재 노드를 자식 노드로 갱신

        return node.is_end_of_word           # 모든 문자를 확인한 후, 마지막 노드의 is_end_of_word 값이 True면 단어가 존재


    def starts_with(self, prefix):    # Trie에 주어진 접두사로 시작하는 단어가 있는지 확인하는 메서드

        node = self.root              # search와 동일

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True                  # 다른점은 접두사만 채크하기 때문에 is_end_of_word 확인 필요 없음
    
# ################################################################################################
# 추가 학습
# class 없이 dict로 구현해보기