from operator import itemgetter


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
        left, right = input().split()
        sections.append([int(left), int(right)])
    points = cross_points(sorted(sections, key=itemgetter(1)))
    print(str(len(points)))
    print(' '.join(str(point) for point in points))


if __name__ == "__main__":
    main()
