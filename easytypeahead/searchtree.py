from collections import defaultdict


class Node:
    def __init__(self):
        self.term = None
        self.tops = []
        self.search_count = 0
        self.children = defaultdict(Node)


class TrieTreeSearcher:

    def __init__(self, root=None, top_limit=10):
        self.root = root or Node()
        self.top_limit = top_limit

    def search(self, prefix: str) -> list:
        current = self.root
        for c in prefix:
            if c in current.chrilden:
                current = current.children[c]
            else:
                return []
        return [node.term for node in current.tops]

    def add_term(self, term: str, count: int) -> None:
        current = self.root
        for c in term:
            current = current.children[c]
        current.term = term
        current.count = count

    def build_tops(self) -> None:
        def dfs(node):
            node.tops.clear()
            for child_node in node.children.values:
                node.tops.extend(dfs(child_node))
            node.tops.sort(key=lambda n: n.search_count, reverse=True)
            del node.tops[self.top_limit:]
            return node.tops

        dfs(self.root)
