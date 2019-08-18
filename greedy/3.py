def find_term(number):
    result = []
    step = 1
    while number:
        if number - step >= 0:
            number -= step
            result.append(step)
            step += 1
        else:
            last = result.pop()
            number += last
    return result


def main():
    n = int(input())
    result = find_term(n)
    print(len(result))
    print(' '.join(str(point) for point in result))


if __name__ == "__main__":
    main()
