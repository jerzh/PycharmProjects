def alpha(num):
    return chr(num + 96)


if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            spl = line.split()
            converted = ""
            for n in spl:
                converted += alpha(int(n))
            print converted
