import random

beats = {
    "kamen": ["nuzky", "jesterka"],
    "nuzky": ["papir", "jesterka"],
    "papir": ["kamen", "spock"],
    "jesterka": ["papir", "spock"],
    "spock": ["kamen", "nuzky"],
}

mode = ""
while mode not in ["1", "2", "3"]:
    mode = input("1 normalni, 2 best of five, 3 pocitac vzdy vyhraje: ")

if input("i s jesterkou a spockem? (a/n): ") == "a":
    choices = ["kamen", "nuzky", "papir", "jesterka", "spock"]
else:
    choices = ["kamen", "nuzky", "papir"]

wins = 0
losses = 0
ties = 0

while True:
    player = input("/".join(choices) + " nebo konec: ").lower()

    if player == "konec":
        break
    if player not in choices:
        print("tohle neznam")
        continue

    if mode == "3":
        options = []
        for c in choices:
            if player in beats[c]:
                options.append(c)
        pc = random.choice(options)
    else:
        pc = random.choice(choices)

    print("pocitac:", pc)

    if player == pc:
        print("remiza")
        ties += 1
    elif pc in beats[player]:
        print("vyhral jsi")
        wins += 1
    else:
        print("prohral jsi")
        losses += 1

    if mode == "2" and (wins == 3 or losses == 3):
        break

if mode == "2":
    if wins == 3:
        print("vyhral jsi zapas")
    elif losses == 3:
        print("pocitac vyhral zapas")

print("vyhry:", wins, "prohry:", losses, "remizy:", ties)
