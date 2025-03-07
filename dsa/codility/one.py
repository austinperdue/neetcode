# Problem: Valid Expression Transformer
# You are given a string S consisting of characters '(', ')', '[', ']', '{', and '}'. An expression is considered valid if opening brackets are closed by the same type of closing brackets in the correct order.
# You can transform the string by removing any valid pair of adjacent matching brackets (such as "()", "[]", or "{}").
# Write a function:
# Copydef solution(S):
# That, given a string S consisting of N characters, returns any string that:

# Can be obtained from S by repeatedly removing valid pairs of adjacent matching brackets
# Cannot be further transformed

# If there are multiple ways to transform the string, any valid sequence of operations may be chosen.
# Examples:

# Given S = "({[]})", the function may return "" (empty string) because all brackets can be matched and removed.
# Given S = "([)]", the function may return "([)]" because no operation can be applied.
# Given S = "[({})([])]", the function may return "" (empty string).
# Given S = "{[()()]}", the function may return "" (empty string).

# Write an efficient algorithm for the following assumptions:

# The length of string S is within the range [0...100,000]
# String S consists only of the characters '(', ')', '[', ']', '{', and '}'

def solution(S):
    # need to keep removing valid adjacent pairs until no more can be removed
    stack = []

    for char in S:
        if not stack:
            # if the stack is empty, just add the character
            stack.append(char)
        else:
            # check if the current char forms a valid pair with the top of the stack
            top = stack[-1]
            current_pair = top + char

            if (current_pair == "()" or
                current_pair == "[]" or
                current_pair == "{}"):
                # found a valid pair, remove the top of the stack
                stack.pop()
            else:
                # not a valid pair, add the current char to the stack
                stack.append(char)
    return ''.join(stack)

