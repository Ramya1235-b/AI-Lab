
from itertools import product

# Knowledge Base:
# Q -> P
# P -> NOT Q
# Q OR R

def implies(a, b):
    return (not a) or b

def knowledge_base(P, Q, R):
    sentence1 = implies(Q, P)
    sentence2 = implies(P, not Q)
    sentence3 = Q or R

    return sentence1 and sentence2 and sentence3

# Queries
def query_R(P, Q, R):
    return R

def query_R_implies_P(P, Q, R):
    return implies(R, P)

def query_Q_implies_R(P, Q, R):
    return implies(Q, R)

# Truth Table Enumeration Algorithm
def tt_entails(query):
    symbols = ['P', 'Q', 'R']

    for values in product([False, True], repeat=3):
        model = dict(zip(symbols, values))

        P = model['P']
        Q = model['Q']
        R = model['R']

        kb = knowledge_base(P, Q, R)

        # Check only models satisfying KB
        if kb and not query(P, Q, R):
            return False

    return True

# Display truth table
print("P Q R | Q->P P->!Q Q|R | KB")

for values in product([True, False], repeat=3):
    P, Q, R = values

    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    kb = knowledge_base(P, Q, R)

    def tf(value):
        return 'T' if value else 'F'

    print(tf(P), tf(Q), tf(R), "|",
          tf(s1), tf(s2), tf(s3), "|", tf(kb))

# Check entailment
print("\nEntailment Results:")

print("KB entails R:",
      tt_entails(query_R))

print("KB entails R -> P:",
      tt_entails(query_R_implies_P))

print("KB entails Q -> R:",
      tt_entails(query_Q_implies_R))
