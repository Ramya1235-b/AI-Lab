
import random
import math

def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                cost += 1

    return cost


def get_random_neighbor(state):
    neighbor = state.copy()
    col = random.randint(0, len(state) - 1)

    row = random.randint(1, len(state))
    while row == neighbor[col]:
        row = random.randint(1, len(state))

    neighbor[col] = row
    return neighbor


def simulated_annealing(initial_state):
    current = initial_state.copy()
    temperature = 100.0
    cooling_rate = 0.95

    print("\nInitial state:", current)
    print("Initial cost:", calculate_cost(current))

    while temperature > 0:
        next_state = get_random_neighbor(current)

        current_cost = calculate_cost(current)
        next_cost = calculate_cost(next_state)

        delta_e = current_cost - next_cost

        # If next state is better, accept it
        if delta_e > 0:
            current = next_state

        # Otherwise, accept it with probability exp(delta_e / T)
        else:
            probability = math.exp(delta_e / temperature)

            if random.random() < probability:
                current = next_state

        print("State:", current,
              "Cost:", calculate_cost(current),
              "Temperature:", round(temperature, 2))

        if calculate_cost(current) == 0:
            break

        temperature *= cooling_rate

    print("\nFinal state:", current)
    print("Final cost:", calculate_cost(current))

    if calculate_cost(current) == 0:
        print("Goal state reached!")
    else:
        print("Goal not reached.")


# Get initial configuration from user
print("Enter row positions of 4 queens (1 to 4):")
initial_state = list(map(int, input().split()))

if len(initial_state) != 4 or any(x < 1 or x > 4 for x in initial_state):
    print("Invalid input! Enter exactly 4 numbers between 1 and 4.")
else:
    simulated_annealing(initial_state)
