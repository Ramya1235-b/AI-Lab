
# First Order Logic - Resolution

def is_variable(x):
    return x.startswith("?")

def substitute(term, subst):
    while term in subst:
        term = subst[term]
    return term


def unify(a, b, subst):
    a = substitute(a, subst)
    b = substitute(b, subst)

    if a == b:
        return subst

    if is_variable(a):
        subst[a] = b
        return subst

    if is_variable(b):
        subst[b] = a
        return subst

    return None


def standardize(clause, count):
    mapping = {}

    new_clause = []

    for neg, pred, args in clause:
        new_args = []

        for arg in args:
            if is_variable(arg):
                if arg not in mapping:
                    mapping[arg] = arg + "_" + str(count)
                new_args.append(mapping[arg])
            else:
                new_args.append(arg)

        new_clause.append((neg, pred, tuple(new_args)))

    return new_clause


def apply_substitution(literal, subst):
    neg, pred, args = literal

    args = tuple(substitute(x, subst) for x in args)

    return (neg, pred, args)


def resolve(c1, c2, count):
    c1 = standardize(c1, count)
    c2 = standardize(c2, count + 1)

    results = []

    for i, l1 in enumerate(c1):
        for j, l2 in enumerate(c2):

            if (l1[0] != l2[0] and
                l1[1] == l2[1] and
                len(l1[2]) == len(l2[2])):

                subst = {}

                for a, b in zip(l1[2], l2[2]):
                    subst = unify(a, b, subst)

                    if subst is None:
                        break

                if subst is not None:

                    result = [
                        apply_substitution(x, subst)
                        for k, x in enumerate(c1) if k != i
                    ]

                    result += [
                        apply_substitution(x, subst)
                        for k, x in enumerate(c2) if k != j
                    ]

                    result = list(dict.fromkeys(result))

                    results.append(result)

    return results


def display(clause):
    if not clause:
        return "{}"

    result = []

    for neg, pred, args in clause:
        text = pred + "(" + ",".join(args) + ")"

        if neg:
            text = "~" + text

        result.append(text)

    return " OR ".join(result)


# Knowledge Base

KB = [

    # John likes all food
    [(True, "food", ("?x",)),
     (False, "likes", ("John", "?x"))],

    # Apple is food
    [(False, "food", ("Apple",))],

    # Vegetables are food
    [(False, "food", ("Vegetables",))],

    # Anyone who eats and is not killed: food
    [(True, "eats", ("?y", "?z")),
     (False, "killed", ("?y",)),
     (False, "food", ("?z",))],

    # Anil eats peanuts
    [(False, "eats", ("Anil", "Peanuts"))],

    # Anil is alive
    [(False, "alive", ("Anil",))],

    # Harry eats everything Anil eats
    [(True, "eats", ("Anil", "?w")),
     (False, "eats", ("Harry", "?w"))],

    # Alive implies not killed
    [(True, "alive", ("?x",)),
     (True, "killed", ("?x",))],

    # Not killed implies alive
    [(False, "killed", ("?x",)),
     (False, "alive", ("?x",))]
]


# Negation of the query
query = [(True, "likes", ("John", "Peanuts"))]

print("FIRST ORDER LOGIC - RESOLUTION")
print("--------------------------------")

support = [query]
count = 1
proved = False

while support and not proved:

    current = support.pop(0)

    for clause in KB:

        resolvents = resolve(current, clause, count)
        count += 2

        for r in resolvents:

            print("Resolvent:", display(r))

            if len(r) == 0:
                proved = True
                break

            if r not in support:
                support.append(r)

        if proved:
            break

print("--------------------------------")

if proved:
    print("Empty clause found: {}")
    print("Query is PROVED")
    print("John likes peanuts.")
else:
    print("Query could not be proved.")
