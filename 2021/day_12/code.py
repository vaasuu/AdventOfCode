from collections import defaultdict


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def part1(lines):

    edges = defaultdict(set)
    for line in lines:
        source, destination = line.split("-")
        edges[source].add(destination)
        edges[destination].add(source)

    all_paths = set()
    todo = [("start",)]
    while todo:
        path = todo.pop()

        if path[-1] == "end":
            all_paths.add(path)
            continue

        for candidate_path in edges[path[-1]]:
            if not candidate_path.islower() or candidate_path not in path:
                todo.append(path + (candidate_path,))

    return len(all_paths)


def double_small_visit(path):
    lower = [vertex for vertex in path if vertex.islower()]
    is_small_double_visit = len(lower) != len(set(lower))
    return is_small_double_visit


def part2(lines):

    edges = defaultdict(set)
    for line in lines:
        source, destination = line.split("-")
        edges[source].add(destination)
        edges[destination].add(source)

    all_paths = set()
    todo = [("start",)]

    while todo:
        path = todo.pop()

        if path[-1] == "end":
            all_paths.add(path)
            continue

        for candidate_path in edges[path[-1]]:
            if candidate_path == "start":
                continue
            elif candidate_path.isupper() or candidate_path not in path:
                todo.append(path + (candidate_path,))
            elif not double_small_visit(path):
                todo.append(path + (candidate_path,))

    return len(all_paths)


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 10

    part1ans = part1(lines)
    print("part1:", part1ans)

    assert part2(sample_lines) == 36

    part2ans = part2(lines)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
