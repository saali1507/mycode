#!usr/bin/env python3

"""Alta3 Challenge | Shalese C
    Old Macdonald"""

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    NE_animals= farms[0]["agriculture"]
    W_animals= farms[1]["agriculture"]
    SE_animals= farms[2]["agriculture"]

    for x in NE_animals:
        print(x)
    choice= input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(x)

    yuck= ["carrots", "celery"]

    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in yuck:
                    print(ag_item)

main()
