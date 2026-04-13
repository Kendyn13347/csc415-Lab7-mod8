class Token:
    def __init__(self, kind, value):
        self.kind  = kind 
        self.value = value  

    def __repr__(self):
        return f"Token({self.kind}, {self.value!r})"


def tokenize(text):
    tokens = []
    i = 0
    while i < len(text):
        ch = text[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or (ch == '.' and i + 1 < len(text) and text[i+1].isdigit()):
            j = i
            while j < len(text) and (text[j].isdigit() or text[j] == '.'):
                j += 1
            raw = text[i:j]
            value = float(raw) if '.' in raw else int(raw)
            tokens.append(Token('NUMBER', value))
            i = j
            continue

        if ch.isalpha() or ch == '_':
            j = i
            while j < len(text) and (text[j].isalnum() or text[j] == '_'):
                j += 1
            word = text[i:j].lower()
            if word == 'and':
                tokens.append(Token('AND', 'and'))
            elif word == 'or':
                tokens.append(Token('OR', 'or'))
            elif word == 'not':
                tokens.append(Token('NOT', 'not'))
            elif word == 'true':
                tokens.append(Token('NUMBER', 1))   # treat as 1
            elif word == 'false':
                tokens.append(Token('NUMBER', 0))   # treat as 0
            else:
                raise SyntaxError(f"Unknown identifier: '{word}'")
            i = j
            continue

        two = text[i:i+2]
        if two == '**':
            tokens.append(Token('POW', '**'));  i += 2; continue
        if two == '//':
            tokens.append(Token('FLOORDIV', '//')); i += 2; continue

        simple = {
            '+': 'PLUS', '-': 'MINUS', '*': 'MUL', '/': 'DIV',
            '%': 'MOD',  '(': 'LPAREN', ')': 'RPAREN',
        }
        if ch in simple:
            tokens.append(Token(simple[ch], ch))
            i += 1
            continue

        raise SyntaxError(f"Unexpected character: '{ch}'")

    tokens.append(Token('EOF', None))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos    = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, kind):
        """Consume the current token if it matches 'kind', else raise."""
        tok = self.current()
        if tok.kind != kind:
            raise SyntaxError(f"Expected {kind}, got {tok.kind} ({tok.value!r})")
        self.pos += 1
        return tok

    def peek(self, *kinds):
        """Return True if the current token is one of the given kinds."""
        return self.current().kind in kinds

    def parse(self):
        result = self.expr()
        self.eat('EOF')
        return result

    def expr(self):
        return self.or_expr()

    def or_expr(self):
        left = self.and_expr()
        while self.peek('OR'):
            self.eat('OR')
            if left:
                _ = self.and_expr()
            else:
                left = self.and_expr()
        return left

    def and_expr(self):
        left = self.not_expr()
        while self.peek('AND'):
            self.eat('AND')
            if not left:
                _ = self.not_expr()
            else:
                left = self.not_expr()
        return left

    def not_expr(self):
        if self.peek('NOT'):
            self.eat('NOT')
            return not self.not_expr()
        return self.add_expr()

    def add_expr(self):
        left = self.mul_expr()
        while self.peek('PLUS', 'MINUS'):
            op = self.current().kind
            self.pos += 1
            right = self.mul_expr()
            left = left + right if op == 'PLUS' else left - right
        return left

    def mul_expr(self):
        left = self.unary()
        while self.peek('MUL', 'DIV', 'FLOORDIV', 'MOD'):
            op = self.current().kind
            self.pos += 1
            right = self.unary()
            if   op == 'MUL':      left = left * right
            elif op == 'DIV':      left = left / right     # always true division
            elif op == 'FLOORDIV': left = left // right
            elif op == 'MOD':      left = left % right
        return left

    def unary(self):
        if self.peek('MINUS'):
            self.eat('MINUS')
            return -self.unary()
        return self.power()

    def power(self):
        base = self.primary()
        if self.peek('POW'):
            self.eat('POW')
            exp = self.unary()  
            return base ** exp
        return base

    def primary(self):
        tok = self.current()

        if tok.kind == 'NUMBER':
            self.pos += 1
            return tok.value                 

        if tok.kind == 'LPAREN':
            self.eat('LPAREN')
            val = self.expr()
            self.eat('RPAREN')
            return val

        raise SyntaxError(f"Unexpected token: {tok}")


def smart_convert(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def evaluate(expression: str):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    raw    = parser.parse()
    return smart_convert(raw)

def run_demo():
    test_cases = [
        # Basic arithmetic
        ("3 + 5 * (2 - 1)",        "precedence: * before +"),
        ("10 / 4",                 "true division → float"),
        ("10 // 4",                "floor division → int"),
        ("10 % 3",                 "modulo"),
        ("2 ** 10",                "exponentiation"),
        ("2 ** 3 ** 2",            "right-assoc: 2**(3**2) = 512"),
        ("-3 + 10",                "unary minus"),
        ("(1 + 2) * (3 + 4)",      "nested parentheses"),
        ("1.5 + 2.5",              "float arithmetic → int via smart_convert"),
        ("3.0 * 2",                "mixed int/float"),

        # Type conversion
        ("7 / 2",                  "int / int → float (2 + 3.5)"),
        ("6 / 2",                  "int / int → 3.0 → smart_convert → 3"),
        ("9.0 // 2",               "floor div on float"),

        # Short-circuit logical operators
        ("1 and 2",                "truthy and → returns right"),
        ("0 and 2",                "falsy and → short-circuits, returns 0"),
        ("0 or 5",                 "falsy or → evaluates right, returns 5"),
        ("1 or 5",                 "truthy or → short-circuits, returns 1"),
        ("not 0",                  "not false → True"),
        ("not 1",                  "not true → False"),
        ("1 and 2 and 0 and 99",   "chain and: stops at 0"),
        ("0 or 0 or 7",            "chain or: reaches 7"),

        # Complex combinations
        ("2 + 3 * 4 - 8 / 2",     "mixed ops: 2+12-4 = 10"),
        ("(2 + 3) * (4 - 1) ** 2","parens + power: 5*9=45"),
        ("100 // (3 + 2) % 4",    "floor div then mod"),
    ]

    print("=" * 60)
    print("   Mini Expression Evaluator — Bonus Challenge")
    print("=" * 60)

    for expr, note in test_cases:
        result = evaluate(expr)
        print(f"  {expr:<35}  =>  {str(result):<10}  # {note}")

    print()
    print("=" * 60)
    print("  Interactive Mode (type 'quit' to exit)")
    print("  Operators: + - * / // % **  |  Logical: and or not")
    print("  Grouping:  ( )")
    print("=" * 60)
    while True:
        try:
            user_input = input("  expr> ").strip()
            if user_input.lower() in ('quit', 'exit', 'q'):
                print("  Goodbye!")
                break
            if not user_input:
                continue
            result = evaluate(user_input)
            print(f"  => {result}  (type: {type(result).__name__})")
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    run_demo()