import collections

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

MOVES = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

def print_board(state):
    for i in range(0, 9, 3):
        print(list(state[i:i+3]))
    print()

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3

    for move, (dr, dc) in MOVES.items():
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_idx = new_row * 3 + new_col
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

def dfs_8puzzle(initial_state, max_depth=10):
    stack = [(initial_state, 0, [initial_state])]
    visited = set()

    while stack:
        current_state, depth, path = stack.pop()

        if current_state == GOAL_STATE:
            return path

        if depth < max_depth:
            visited.add(current_state)

            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1, path + [neighbor]))

    return None

def dls_recursive(current_state, depth, limit, path, visited):
    if current_state == GOAL_STATE:
        return path

    if depth == limit:
        return "CUTOFF"

    cutoff_occurred = False
    visited.add(current_state)

    for neighbor in get_neighbors(current_state):
        if neighbor not in visited:
            result = dls_recursive(neighbor, depth + 1, limit, path + [neighbor], visited)

            if result == "CUTOFF":
                cutoff_occurred = True
            elif result is not None:
                return result

    visited.remove(current_state)

    return "CUTOFF" if cutoff_occurred else None

def ids_8puzzle(initial_state, max_limit=30):
    for limit in range(max_limit):
        visited = set()
        result = dls_recursive(initial_state, 0, limit, [initial_state], visited)

        if result != "CUTOFF" and result is not None:
            return result
        
    return None

if __name__ == "__main__":
    initial_state = (1, 2, 3,
                     4, 0, 6,
                     7, 5, 8)

    print("Initial State:")
    print_board(initial_state)

    print("DFS Solution:")
    dfs_path = dfs_8puzzle(initial_state, max_depth=15)
    if dfs_path:
        for step_idx, state in enumerate(dfs_path):
            print(f"Step {step_idx}:")
            print_board(state)

    print("IDS Solution:")
    ids_path = ids_8puzzle(initial_state, max_limit=20)
    if ids_path:
        for step_idx, state in enumerate(ids_path):
            print(f"Step {step_idx}:")
            print_board(state)
