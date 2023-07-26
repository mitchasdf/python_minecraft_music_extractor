
import json
import shutil


# change these 2
username_folder = "mitch"
minecraft_version = "1.18"


# change these 3, if necessary
output_folder = f"C:\\Users\\{username_folder}\\Desktop\\extracted minecraft music\\"
index = f"C:\\Users\\{username_folder}\\AppData\\Roaming\\.minecraft\\assets\\indexes\\{minecraft_version}.json"
hashed_folder = f"C:\\Users\\{username_folder}\\AppData\\Roaming\\.minecraft\\assets\\objects\\"


def hash_file(hash_name):
    return f"{hashed_folder}{hash_name[0:2]}\\{hash_name}"


with open(index, 'rb') as file:
    a = file.read()
    ob = json.loads(a)

if len(ob) == 1:
    ob = ob[list(ob.keys())[0]]

for key in ob:
    if '/music/' in key or '/sounds/records/' in key:
        place = key.rfind('/')
        if place > 0:
            smol_key = key[place+1:]
            target_file = f"{output_folder}{smol_key}"
            print(f"{smol_key} was copied to {target_file}")
            _hash = hash_file(ob[key]['hash'])
            shutil.copy2(_hash, target_file)

