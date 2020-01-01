# mat = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
# mat = [
#     [0, -1, 1],
#     [1, 1, 0],
#     [0, 1, -1]
# ]

mat = [
    [1, 1, 1, -1, 1, 1],
    [1, 1, 0, 1],
    [0, 1, -1, 1]
]


def matrix_get(node):
    return mat[node[0]][node[1]]


def get_neighbours(node, direction):
    neighbours = []
    if direction == "down":
        if node[0] < len(mat) - 1:
            right_node = (node[0] + 1, node[1])
            if matrix_get(right_node) != -1:
                neighbours.append(right_node)

        if node[1] < len(mat[0]) - 1:
            bottom_node = (node[0], node[1] + 1)
            if matrix_get(bottom_node) != -1:
                neighbours.append(bottom_node)
    else:
        if node[0] > 0:
            left_node = (node[0] - 1, node[1])
            if matrix_get(left_node) != -1:
                neighbours.append(left_node)

        if node[1] > 0:
            top_node = (node[0], node[1] - 1)
            if matrix_get(top_node) != -1:
                neighbours.append(top_node)

    return neighbours


def find_all_costs(direction):
    stack = []
    costs = dict()
    max_diamonds = dict(diamonds=0)

    min_node = (0, 0)
    max_node = (len(mat) - 1, len(mat[0]) - 1)

    if matrix_get(min_node) == -1 or matrix_get(max_node) == -1:
        return dict(diamonds=0, paths=[])

    if direction == "down":
        stack.append(min_node)
        last_node = max_node
    else:
        stack.append(max_node)
        last_node = min_node

    while len(stack) > 0:
        node = stack.pop()
        neighbours = get_neighbours(node, direction)

        node_value = costs.get(node, dict())
        diamonds = node_value.get("diamonds", 0)
        paths = node_value.get("paths", [node])

        for n in neighbours:
            costs[n] = dict(diamonds=diamonds+matrix_get(n), paths=paths + [n])
            stack.append(n)

        if diamonds > max_diamonds.get("diamonds") and node == last_node:
            max_diamonds = dict(diamonds=diamonds, paths=paths)

    return max_diamonds


def find_max_diamonds():

    top_max_diamonds = find_all_costs("down")
    # print("Down Max", top_max_diamonds)

    # print("Mat: Before", mat)
    for node in top_max_diamonds["paths"]:
        mat[node[0]][node[1]] = 0

    # print("Mat: After", mat)
    bottom_max_diamonds = find_all_costs("up")
    # print("Up Max", bottom_max_diamonds)

    return top_max_diamonds.get("diamonds") + bottom_max_diamonds.get("diamonds")


if __name__ == '__main__':
    max_diamonds = find_max_diamonds()
    print("Max Diamonds", max_diamonds)
