import jstyleson as json
import os


#################################################################

def ensure_outputs_exist():
    for file in os.walk(_cwd + f"\\{input_path}\\"):
        try:
            os.mkdir(file[0].replace(input_path, output_path))
        except:
            continue

# these 2 are for looping/replacing through every single key and value in a dict
def dict_replace_value(d, old, new):
    x = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = dict_replace_value(v, old, new)
        elif isinstance(v, list):
            v = list_replace_value(v, old, new)
        elif isinstance(v, str):
            if not old is None and not new is None:
                v = v.replace(old, new)
            v = v.replace("{namespace}",f"{namespace}")
        x[k] = v
    return x

def list_replace_value(l, old, new):
    x = []
    for e in l:
        if isinstance(e, list):
            e = list_replace_value(e, old, new)
        elif isinstance(e, dict):
            e = dict_replace_value(e, old, new)
        elif isinstance(e, str):
            if not old is None and not new is None:
                e = e.replace(old, new)
            e = e.replace("{namespace}",f"{namespace}")
        x.append(e)
    return x

#################################################################


colors = [
    "orange",
    "magenta",
    "light_blue",
    "yellow",
    "lime",
    "pink",
    "gray",
    "light_gray",
    "cyan",
    "purple",
    "blue",
    "brown",
    "green",
    "red",
    "black"
]

namespace = "another_furniture"

cwd = os.getcwd()


process_specific = input("process specific file (or enter to skip): ")
if process_specific != "":
    files_to_process = ["white_" + process_specific + ".json"]
else:
    files_to_process = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f)) and f.startswith("white")]

for file in files_to_process:
    should_process = input("should process file " + file + "? ")
    if should_process == "" or should_process.lower() == "y" or should_process.lower() == "yes":
        f = open(file, "r")
        data = json.loads(f.read())
        for color in colors:
            new_data = dict_replace_value(data, "white", color)
            with open(file.replace("white", color), "w+") as f:
                f.write(json.dumps(new_data, indent=4) + "\n")

