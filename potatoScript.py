import sys, math, random

consts = {
    "g": 9.82,
    "e": 2.71828,
    "pi": 3.141592
}

varibales = {}


def findBlocks(toks):
    stack = []
    blocks = {}
    index = 0

    for tok in toks:
        if tok == "if":
            stack.append(index)
        elif tok == "end":
            if not stack:
                raise RecursionError(f"Unpaired end at {index+1}")
            
            start = stack.pop()

            blocks[start] = index
        index += 1
    
    return blocks


def op_print(stack, toks):
    if stack:
        print(stack[len(stack)-1])

def op_printN(stack, toks):
    n = stack.pop()
    if n <= len(stack):
        print(stack[int(n-1)])
    else:
        print(f"{int(n)} is outside of stack lenght")

def op_clear(stack, toks):
    stack.clear()

def op_store(stack, toks):
    value = stack.pop()
    name = stack.pop()

    if not isinstance(name, str):
        raise RuntimeError("store expects a name literal")

    varibales[name] = value

def op_load(stack, toks):
    name = stack.pop()

    stack.append(varibales[name])

def op_round(stack, toks):
    number = stack.pop()
    stack.append(round(number))

def op_input(stack, toks):
    if stack and stack[len(stack)-1] in varibales:
        x = input(f"{stack[len(stack)-1]} >")
    else:
        x = input(">")
    try:
        stack.append(float(x))
    except ValueError:
        if x in consts:
            stack.append(float(consts[x]))
        elif x is bool:
            stack.append(bool(x))
        elif x in {"true", "True", "false", "False"}:
            if x in {"true", "True"}:
                stack.append(True)
            else:
                stack.append(False)
        else:
            raise RuntimeError(f"{x} is not a valid input, input only support numeric or boolean inputs")

def op_dump(stack, toks):
    print(f"tokens: {toks}")
    print(f"stack: {stack}")
    print(f"varibales: {varibales}")

def op_stackdump(stack, toks):
    print(f"{stack}")

def op_vardump(stack, toks):
    print(f"{varibales}")

def op_dup(stack, toks):
    x = stack[len(stack)-1]
    stack.append(x)

def op_swap(stack, toks):
    if len(stack) >= 2:
        x = stack.pop()
        y = stack.pop()

        stack.append(x)
        stack.append(y)
    else:
        raise RuntimeError("Not enough items in stack to preforme swap functions")

def op_drop(stack, toks):
    if not stack:
        raise RuntimeError("Cant preforme this action whit a empty stack")
    stack.pop()

def op_isEqual(stack, toks):
    rhs = stack.pop()
    lhs = stack.pop()

    if lhs == rhs:
        stack.append(True)
    else:
        stack.append(False)

def op_isBigger(stack, toks):
    rhs = stack.pop()
    lhs = stack.pop()

    if lhs > rhs:
        stack.append(True)
    else:
        stack.append(False)

def op_isSmaller(stack, toks):
    rhs = stack.pop()
    lhs = stack.pop()

    if lhs < rhs:
        stack.append(True)
    else:
        stack.append(False)

def op_rand(stack, toks):
    end = stack.pop()
    start = stack.pop()

    stack.append(random.uniform(start, end))

def op_randint(stack, toks):
    end = int(stack.pop())
    start = int(stack.pop())

    stack.append(random.randint(start, end)) 


FUNCTIONS = {
    "print" : op_print,
    "print[n]" : op_printN,
    "clear" : op_clear,
    "store" : op_store,
    "load" : op_load,
    "round" : op_round,
    "input" : op_input,
    "dump" : op_dump,
    "stack-dump" : op_stackdump,
    "var-dump" : op_vardump,
    "dup" : op_dup,
    "swap" : op_swap,
    "drop" : op_drop,

    "=" : op_isEqual,
    ">" : op_isBigger,
    "<" : op_isSmaller,

    "rand" : op_rand,
    "randint" : op_randint,
}

def functions(tok, stack, toks):
    if tok.startswith("#"):
        return True
    
    func = FUNCTIONS.get(tok)
    if func:
        func(stack, toks)
        return True
    
    return False

def calc(tok, stack, toks):
    if tok in {"+", "-", "/", "*", "^"}:
        if len(stack) < 2:
            raise RuntimeError("Stack underflow")
        
        rhs = stack.pop()
        lhs = stack.pop()

        ops = {
            "+": lhs + rhs,
            "-": lhs - rhs,
            "/": lhs / rhs,
            "*": lhs * rhs,
            "^": lhs ** rhs
        }

        stack.append(ops[tok])
    elif tok == "!":
        if not stack:
            raise RuntimeError("Stack underflow")
        
        n = stack.pop()
        if n < 0:
            raise RuntimeError("Factorial of negative number")
        
        stack.append(math.factorial(int(n)))

    else:
        if not functions(tok, stack, toks):
            raise RuntimeError(f"Unkown operand: {tok}, at index {toks.index(tok)+1}")
        
    

def ev(s):
    toks = s.split()
    stack = []

    blocks = findBlocks(toks)
    
    index = 0
    try:
        while index < len(toks):
            try:
                stack.append(float(toks[index]))
                index += 1
            except ValueError:
                if toks[index] in consts:
                    stack.append(float(consts[toks[index]]))
                    index += 1
                elif toks[index].startswith("'"):
                    stack.append(toks[index][1:])
                    index += 1
                elif toks[index].startswith("|") and toks[index].endswith("|"):
                    stack.append(toks[index][1:-1])
                    index += 1
                elif toks[index] == "if":
                    check = stack.pop()
                    if check:
                        index += 1
                    else:
                        index = blocks[index]
                elif toks[index] == "end":
                    index += 1
                else:
                    calc(toks[index], stack, toks)
                    index += 1
    
    except RuntimeError as e:
        print(f"PotatoScript ran into a problem: {e}")

filename = sys.argv[1]

if filename.endswith(".ptsc"):
    ev(open(filename).read())
else:
    raise RuntimeError(f"{filename} is not supported, it must be a .ptsc file")