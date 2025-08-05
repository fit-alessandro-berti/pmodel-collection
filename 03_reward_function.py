import os
import pm4py
import traceback
import pandas as pd

REFERENCE_POWL_FOLDER = "models/o4-mini/powl"

NEW_POWL_FOLDER = "models/gpt-4.1-mini/powl"


def __read_file(file_path):
    try:
        F = open(file_path, "r")
        contents = F.read()
        F.close()
    except:
        F = open(file_path, "r", encoding="utf-8")
        contents = F.read()
        F.close()
    return contents


def get_footprints(contents):
    dictio = {}
    exec(contents, dictio)
    powl = dictio["root"]
    net, im, fm = pm4py.convert_to_petri_net(powl)
    footprints = pm4py.discover_footprints(powl)
    return powl, footprints


def compute_reward(rpowl, npowl):
    rpowl = rpowl.split("```python")[-1].split("```")[0]
    npowl = npowl.split("```python")[-1].split("```")[0]
    rpowl, rfootprints = get_footprints(rpowl)
    reward_score = 0.0
    try:
        npowl, nfootprints = get_footprints(npowl)
        reward_score += 0.25
        if nfootprints["activities"].issubset(rfootprints["activities"]):
            reward_score += 0.25
            if nfootprints["activities"] == rfootprints["activities"]:
                reward_score += 0.1
            reward_score += 0.4 * pm4py.behavioral_similarity(rpowl, npowl)
    except:
        traceback.print_exc()
    reward_score = -1.0 + 2.0 * reward_score
    return reward_score


def compute_reward_from_files(file_name):
    rpowl_path = os.path.join(REFERENCE_POWL_FOLDER, file_name)
    npowl_path = os.path.join(NEW_POWL_FOLDER, file_name)
    rpowl = __read_file(rpowl_path)
    npowl = __read_file(npowl_path)
    return compute_reward(rpowl, npowl)


if __name__ == "__main__":
    rewards = []
    for index, file_name in enumerate(os.listdir(NEW_POWL_FOLDER)):
        rewards.append({"file_name": file_name, "reward_score": compute_reward_from_files(file_name)})
        if index > 10:
            break

    rewards = pd.DataFrame(rewards)
    rewards.to_csv("stats/reward_gpt-4.1-mini.csv", index=False)
