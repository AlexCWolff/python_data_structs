from stack import Stack, ReverseStack

# Test out our stack class
STACK = Stack()
REVERSE_STACK = ReverseStack()

print(STACK.is_empty)
STACK.push(4)
STACK.push('dog')
print(STACK.peek())
STACK.push(True)
print(STACK.size)
print(STACK.is_empty)
STACK.push(8.4)
print(STACK.pop())
print(STACK.pop())
print(STACK.size)

REVERSE_STACK.push('hello')
REVERSE_STACK.push('true')
print(REVERSE_STACK.pop())


def par_checker(symbol_string):
    """
    Uses a stack to ensure that all parentheses and brackets in a string
    have a closing paran/bracket of the same type in the right place.
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty:
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty:
        return True
    else:
        return False


def matches(open, close):
    """Handle bracket/paran matching."""
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)


print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))


def base_converter(number, base):
    """Converts decimal numbers to any base numbering system up to base 36."""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    remstack = Stack()

    while number > 0:
        rem = number % base
        remstack.push(rem)
        number = number // base

    new_string = ""
    while not remstack.is_empty:
        new_string += digits[remstack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))
print(base_converter(26, 26))


def infix_to_postfix(infix_expr):
    """Convert from infix to postfix expression."""
    # Define the precedence of operators
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    # Create a stack object, postfix output list, and array of the infix expression to work with.
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    # For every item in the infix expression array
    for token in token_list:
        # If it's an alphanumeric character
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            # Append to the output list
            postfix_list.append(token)
        # If it's an opening parentheses
        elif token == '(':
            # Push it to the stack
            op_stack.push(token)
        # If it's a closing parentheses
        elif token == ')':
            # Pop the last item from the stack
            top_token = op_stack.pop()
            # While that item isn't an opening parentheses
            while top_token != '(':
                # Append that item to the output list
                postfix_list.append(top_token)
                # Pop the next item for the loop
                top_token = op_stack.pop()
        # If it is an operator
        else:
            """
            While the stack isn't empty and the precedence of the last item in the stack is
            greater than or equal to the current operator, pop the item from the stack and append it to the output.
            """
            while (not op_stack.is_empty) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            # Put the operator back on the stack.
            op_stack.push(token)

    # While the stack isn't empty
    while not op_stack.is_empty:
        # Pop and append the last item on the stack to the output
        postfix_list.append(op_stack.pop())
    # Return output list as a string.
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def postfix_eval(postfix_expr):
    """Evaluate a postfix expression."""
    # Make a stack and input list
    operand_stack = Stack()
    token_list = postfix_expr.split()

    # For every item in the input
    for token in token_list:
        # If it's a number
        if token in "0123456789":
            # Push it to the stack
            operand_stack.push(int(token))
        # If it's an operator
        else:
            # Pop the last two numbers, do the math on them
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            # Push the results on to the stack
            operand_stack.push(result)
    # Return the results
    return operand_stack.pop()


def do_math(op, op1, op2):
    """Do the actual math operations."""
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfix_eval('7 8 + 3 2 + /'))
