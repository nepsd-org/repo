def add(a: int, b: int):
    return a + b


if __name__ == "__main__":
    a, b = list(map(int,input().split()))
    print(add(a, b))