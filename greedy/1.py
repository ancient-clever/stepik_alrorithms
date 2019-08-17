def cross_points(sections):
    points = [sections.pop(0)[1]]
    for left, right in sections:
        if left > points[-1]:
            points.append(right)
    return points


def main():
    n = int(input())
    sections = []
    for r in range(n):
        section = input().split()
        sections.append(section)
    points = cross_points(sections)
    print(str(len(points)))
    print(' '.join(points))


if __name__ == "__main__":
    main()
