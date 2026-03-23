def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count = count + 1
        n = n >> 1
    return count


def main():
    print(countBits(0b001))  # binary literal → 1 set bit
    # or simply: print(countBits(1))

main()