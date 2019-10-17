def main():
    f = {}
    g = ""
    i = input("Write what do you want: ")
    for b in i:
        if b.isalpha():
            g = g + b

    for p in g:
        try:
            f[p] = f[p] + 1
        except Exception:
            f[p] = 1
    print(f)


main()
