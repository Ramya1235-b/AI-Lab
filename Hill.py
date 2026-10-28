
def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                cost += 1

    return cost


def get_neighbors(state):
    neighbors = []
    n = len(state)

    for col in range(n):
        for row in range(1, n + 1):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors


def hill_climbing(initial_state):
    current = initial_state

    print("\nInitial state:", current)
    print("Initial cost:", calculate_cost(current))

    while True:
        neighbors = get_neighbors(current)
        best = min(neighbors, key=calculate_cost)

        current_cost = calculate_cost(current)
        best_cost = calculate_cost(best)

        print("\nCurrent state:", current)
        print("Current cost:", current_cost)
        print("Best neighbor:", best)
        print("Neighbor cost:", best_cost)

        if best_cost == 0:
            print("\nGoal state reached:", best)
            print("Final cost: 0")
            break

        if best_cost >= current_cost:
            print("\nNo better neighbor found.")
            print("Hill climbing stopped at:", current)
            break

        current = best


# Get user input
print("Enter the row positions of 4 queens (1 to 4).")
print("Enter 4 numbers separated by spaces:")

initial_state = list(map(int, input().split()))

if len(initial_state) != 4 or any(x < 1 or x > 4 for x in initial_state):
    print("Invalid input! Enter exactly 4 numbers between 1 and 4.")
else:
    hill_climbing(initial_state)
