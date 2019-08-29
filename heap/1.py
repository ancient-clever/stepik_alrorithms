import heapq


def main():
    n = int(input())
    h = []
    for i in range(n):
        cmd = input()
        if 'ExtractMax' in cmd:
            res = heapq.heappop(h)
            print(-res)
        else:
            operation, number = cmd.split()
            heapq.heappush(h, -int(number))


if __name__ == "__main__":
    main()
