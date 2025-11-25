import json
import os

def load_config(env="local"):
    path = os.path.join(os.path.dirname(__file__), f"environments/{env}.json")
    with open(path, "r") as f:
        return json.load(f)
