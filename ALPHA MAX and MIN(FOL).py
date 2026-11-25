
def MAX(node, alpha, beta, name):
    if isinstance(node, int):
        return node

    value = float('-inf')

    for i, child in enumerate(node):
        value = max(value, MIN(child, alpha, beta, name + str(i + 1)))
        alpha = max(alpha, value)

        if alpha >= beta:
            print("Pruned at MAX:", node[i + 1:])
            break

    print(name, "(MAX) =", value)
    return value


def MIN(node, alpha, beta, name):
    if isinstance(node, int):
        return node

    value = float('inf')

    for i, child in enumerate(node):
        value = min(value, MAX(child, alpha, beta, name + str(i + 1)))
        beta = min(beta, value)

        if alpha >= beta:
            print("Pruned at MIN:", node[i + 1:])
            break

    print(name, "(MIN) =", value)
    return value


tree = [
    [[10, 9], [14, 18]],
    [[5, 4], [50, 3]]
]

result = MAX(tree, float('-inf'), float('inf'), "Root")

print("\nRoot Node Value =", result)
