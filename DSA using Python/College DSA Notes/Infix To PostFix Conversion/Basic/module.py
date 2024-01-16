import re 
PRECEDENCE = {
    '^':4,
    '*':3,
    '/':3,
    '+':2,
    '-':2,
    '(':1,
}

def infixToPostfix(expr):
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])",expr)
    stack = []
    postfix = []

    for token in tokens:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()
        else:
            while stack and (PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

expressions = [ '4*2+5*(2+1)/2','4^2+5(2+1)/2','A*(B+C)/D']
for expr in expressions:
    print(infixToPostfix(expr))