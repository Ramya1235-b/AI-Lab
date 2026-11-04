
# First Order Logic - Unification Algorithm
# Taking expressions as user input

import re

# Variables start with lowercase letters
def is_variable(x):
    return isinstance(x, str) and x[0].islower()


# Parse input expression
def parse_expression(expression):
    tokens = re.findall(r'[A-Za-z_][A-Za-z_0-9]*|[(),]', expression)
    position = 0

    def parse_term():
        nonlocal position

        if position >= len(tokens):
            raise ValueError("Invalid expression")

        name = tokens[position]
        position += 1

        # Check whether it is a function/predicate
        if position < len(tokens) and tokens[position] == '(':
            position += 1
            arguments = []

            if position < len(tokens) and tokens[position] != ')':
                while True:
                    arguments.append(parse_term())

                    if position < len(tokens) and tokens[position] == ',':
                        position += 1
                    else:
                        break

            if position >= len(tokens) or tokens[position] != ')':
                raise ValueError("Missing closing bracket")

            position += 1
            return (name, *arguments)

        return name

    result = parse_term()

    if position != len(tokens):
        raise ValueError("Invalid expression")

    if not isinstance(result, tuple):
        raise ValueError("Expression must contain a predicate")

    return result


# Apply substitutions
def apply_substitution(term, substitution):
    if isinstance(term, str):
        while term in substitution:
            term = substitution[term]
        return term

    return (
        term[0],
        *[apply_substitution(arg, substitution)
          for arg in term[1:]]
    )


# Occurs check
def occurs_check(variable, term, substitution):
    term = apply_substitution(term, substitution)

    if variable == term:
        return True

    if isinstance(term, tuple):
        return any(
            occurs_check(variable, arg, substitution)
            for arg in term[1:]
        )

    return False


# Unify variable
def unify_variable(variable, term, substitution):

    if variable in substitution:
        return unify(substitution[variable], term, substitution)

    if isinstance(term, str) and term in substitution:
        return unify(variable, substitution[term], substitution)

    if occurs_check(variable, term, substitution):
        return None

    substitution[variable] = term
    return substitution


# Main Unification Algorithm
def unify(x, y, substitution=None):

    if substitution is None:
        substitution = {}

    x = apply_substitution(x, substitution)
    y = apply_substitution(y, substitution)

    if x == y:
        return substitution

    if isinstance(x, str) and is_variable(x):
        return unify_variable(x, y, substitution)

    if isinstance(y, str) and is_variable(y):
        return unify_variable(y, x, substitution)

    if isinstance(x, tuple) and isinstance(y, tuple):

        # Check predicate/function names
        if x[0] != y[0]:
            return None

        # Check number of arguments
        if len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


# Display expression
def display(term):
    if isinstance(term, tuple):
        return term[0] + "(" + ", ".join(
            display(arg) for arg in term[1:]
        ) + ")"
    return term


# Main program
print("FIRST ORDER LOGIC - UNIFICATION")
print("--------------------------------")

try:
    expr1 = input("Enter first expression: ")
    expr2 = input("Enter second expression: ")

    exp1 = parse_expression(expr1)
    exp2 = parse_expression(expr2)

    print("\nExpression 1:", display(exp1))
    print("Expression 2:", display(exp2))

    result = unify(exp1, exp2)

    if result is not None:
        print("\nUnification Successful!")
        print("Substitution:")

        for variable, value in result.items():
            print(variable, "=", display(value))

        print("\nUnified Expression:")
        print(display(apply_substitution(exp1, result)))

    else:
        print("\nUnification Failed!")
        print("No valid substitution exists.")

except ValueError as error:
    print("Invalid input:", error)
