"""
A parse tree is just a binary tree used to represent real world constructions like a sentence or a math expression.
We use a stack to keep track of the parent node as we descend, as the binary tree is not capable of this on it's own.
"""

from .stack import Stack
from .binary_tree import BinaryTree


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fplist:
        if i == '(':
            current_tree.insertLeft('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.setRootVal(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.setRootVal(i)
            current_tree.insertRight('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.get_left_child())
        res2 = postordereval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def printexp(tree):
    s_val = ""
    if tree:
        s_val = '(' + printexp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + printexp(tree.get_right_child()) + ')'
    return s_val


inString = "( ( 10 + 5 ) * 3 )"
print(inString)
pt = build_parse_tree(inString)
pt.postorder()

print(preorder(pt))
print(postorder(pt))
print(inorder(pt))

print(printexp(pt))
