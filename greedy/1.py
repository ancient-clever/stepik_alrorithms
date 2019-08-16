def cross_points(sections):
    # провкряьт лежит ли точка на отрезке
    points = []
    while sections:
        a, b = sections.pop()
        for c, d in sections:
            if a <= c <= b:
                points.append(c)
            elif c <= a <= d:
                points.append(a)

    return points


def main():
    # n = int(input())
    # sections = []
    # for r in range(n):
    #     section = input().split()
    #     sections.append(section)
    # print(cross_points(sections))
    print(cross_points([['1', '3'], ['2', '5']]))


if __name__ == "__main__":
    main()
