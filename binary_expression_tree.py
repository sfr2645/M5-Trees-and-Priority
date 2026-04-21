from stack import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, postfix_expr):
        stack = Stack()
        tokens = postfix_expr.split()

        for token in tokens:
            if token.isdigit():
                node = Node(token)
                stack.push(node)

            elif token in "+-*/":
                node = Node(token)

                if not stack.is_empty():
                    node.right = stack.pop()
                else:
                    raise Exception("Error: Stack empty")

                if not stack.is_empty():
                    node.left = stack.pop()
                else:
                    raise Exception("Error: Stack empty")

                stack.push(node)

            else:
                raise Exception("Unsupported token")

        if not stack.is_empty():
            self.root = stack.pop()
        else:
            raise Exception("Error: No expression tree")

        if not stack.is_empty():
            raise Exception("Error: Unused tokens")

    def evaluate(self):
        return self._evaluate_tree(self.root)

    def _evaluate_tree(self, node):
        if node.left is None and node.right is None:
            return float(node.value)

        x = self._evaluate_tree(node.left)
        y = self._evaluate_tree(node.right)

        if node.value == '+':
            return x + y
        elif node.value == '-':
            return x - y
        elif node.value == '*':
            return x * y
        elif node.value == '/':
            return x / y

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return ""
        if node.left is None and node.right is None:
            return node.value
        return "(" + self._inorder(node.left) + " " + node.value + " " + self._inorder(node.right) + " )"

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return ""
        return (self._postorder(node.left) + " " +
                self._postorder(node.right) + " " +
                node.value).strip()
