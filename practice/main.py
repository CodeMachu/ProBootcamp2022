def main():
    y = 10
    z = 0

    for x in range(100):
        y = int(y * 1.27)
        z += y
        print(f"{x}: {z}")

main()
