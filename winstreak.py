import json

with open("winstreak.json", "r") as my_file:
    file = json.load(my_file)
difficult1 = file["difficulty_balance"][0]
difficult2 = file["difficulty_balance"][1]
difficult3 = file["difficulty_balance"][2]
difficult4 = file["difficulty_balance"][3]
difficult5 = file["difficulty_balance"][4]


def count_reward(dif):
    rewards = []
    rewards_dict = {}
    for i in dif["stages"]:
        rewards.append(i["rewards"])
    for i in rewards:
        for k in i:
            if k["id"] not in rewards_dict.keys():
                rewards_dict[k["id"]] = k["amount"]
            else:
                rewards_dict[k["id"]] += k["amount"]
    return rewards_dict


dif1 = count_reward(difficult1)
dif2 = count_reward(difficult2)
dif3 = count_reward(difficult3)
dif4 = count_reward(difficult4)
dif5 = count_reward(difficult5)
print(f"Сложность №1: {dif1}\nСложность №2: {dif2}\nСложность №3: {dif3}\nСложность №4: {dif4}\nСложность №5: {dif5}\n")
