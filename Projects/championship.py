import json

championship = {}
s = ""
p = ""
print("Welcome!\nFollow the instructions.")

while True:
    s = input("Insert a team (quit for exit): ")
    if s == "quit":
        break
    if s != s.title():
        s = s.title()


    while True:
        p =input("Insert Score: ")
        try:
            val = int(p)
            if int(p) < 0:
                print("INSERT A POSITIVE NUMBER!")
                continue
            break
        except ValueError:
            print("INSERT A POSITIVE NUMBER!")
    p=int(p)


    classifica[s] = p
    with open('Championship.json', 'w') as f:
        f.write(json.dumps(championship, default=str))
print(championship)
