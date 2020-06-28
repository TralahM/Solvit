from typing import List  # , Int  # , Dict, Tuple


class Expression:
    def __init__(self, variables: List, total: int):
        self.variables = [v.upper() for v in variables]
        self.total = total

    def __repr__(self):
        return "+".join(self.variables) + "=" + str(self.total)


class Relation:
    pass


LT = Relation()

LTE = Relation()

GT = Relation()

GTE = Relation()

EQ = Relation()

NE = Relation()


def reduce_expr(x1: Expression, x2: Expression):
    i = set(tuple(x1.variables)).difference(set(tuple(x2.variables)))
    j = set(tuple(x2.variables)).difference(set(tuple(x1.variables)))
    x, y = list(i), list(j)
    d = x1.total - x2.total
    print("+".join(x), " = ", "+".join(y), " ", d)


class Inequality:
    def __init__(self, expr1: Expression, expr2: Expression, rel: Relation):
        self.expr1 = expr1
        self.expr2 = expr2
        ...


class Puzzle:
    def __init__(self, expressions: List[Expression]):
        self.expressions = expressions
        self.solution = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "J": 0,
        }

    def __repr__(self):
        return str(
            "\n".join(
                ["+".join(e.variables) + "=" + str(e.total)
                 for e in self.expressions]
            )
        )

    def var_intersects(self, *args):
        if args:
            v = self.var_expressions(args[0])
            for a in args:
                v = v.intersection(self.var_expressions(a))
            return v

    def var_expressions(self, var):
        var = var.upper()
        assert var in self.solution.keys()
        exps = set([e for e in self.expressions if var in e.variables])
        return exps

    def solve(self):
        ...
