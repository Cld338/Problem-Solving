def main():
    X, Y = map(int, input().split())
    
    Z = Y * 100 // X
    if Z >= 99:
        print(-1)
    else:
        Z += 1
        A = X * Z - 100 * Y
        B = 100 - Z
        if A % B == 0:
            print(A // B)
        else:
            print(A // B + 1)

if __name__ == "__main__":
    main()
