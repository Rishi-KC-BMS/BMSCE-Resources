tree = [
    [[10, 9], [14, 18]],
    [[5, 4], [50, 3]]
]


def minimax(node, alpha, beta, is_max):

    if isinstance(node, int):
        return node, {"name": str(node), "children": []}

    children = []

    if is_max:
        best = float('-inf')
        name = "MAX"
    else:
        best = float('inf')
        name = "MIN"

    for i, child in enumerate(node):

        value, info = minimax(child, alpha, beta, not is_max)
        children.append(info)

        if is_max:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)

        if alpha >= beta:
            for remaining in node[i + 1:]:
                children.append({
                    "name": "PRUNED " + str(remaining),
                    "children": [],
                    "pruned": True
                })
            break

    return best, {
        "name": name + " (" + str(best) + ")",
        "children": children
    }

def print_tree(node, prefix="", last=True):

    connector = "`-- " if last else "|-- "
    print(prefix + connector + node["name"])

    if "children" in node:
        children = node["children"]

        for i in range(len(children)):
            new_prefix = prefix + ("    " if last else "|   ")

            print_tree(
                children[i],
                new_prefix,
                i == len(children) - 1
            )

result, root = minimax(
    tree,
    float('-inf'),
    float('inf'),
    True
)

print("\nMINIMAX TREE WITH ALPHA-BETA PRUNING\n")

print(root["name"])

for i, child in enumerate(root["children"]):
    print_tree(child, "", i == len(root["children"]) - 1)

print("\nOptimal Value:", result)

#Output
# MINIMAX TREE WITH ALPHA-BETA PRUNING

# MAX (10)
# |-- MIN (10)
# |   |-- MAX (10)
# |   |   |-- 10
# |   |   `-- 9
# |   `-- MAX (14)
# |       |-- 14
# |       `-- PRUNED 18
# `-- MIN (5)
#     |-- MAX (5)
#     |   |-- 5
#     |   `-- 4
#     `-- PRUNED [50, 3]

# Optimal Value: 10

