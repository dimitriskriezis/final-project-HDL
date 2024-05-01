import os
from collections import defaultdict
import yaml

THIS_SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
RESULTS_DIR = os.path.join(THIS_SCRIPT_DIR, "example_designs", "eyeriss_like", "outputs")

models = ["VGG01", "VGG02"]

energies = defaultdict(lambda:0)
areas = defaultdict(lambda:0)

for layer in os.listdir(RESULTS_DIR):
    if layer.startswith(".ipynb"):
        continue
    ## COLLECT ENERGY 
    model = layer.split("_")[0]
    file = os.path.join(RESULTS_DIR, layer, "timeloop-mapper.stats.txt")
    energy = open(file, "r").read().split("-------------")[-1].split("\n")[4]
    energy_value = float(energy.split(" ")[1])
    energies[model] += energy_value

    ## COLLECT AREA
    if areas[model]:
        continue
    art_file = os.path.join(RESULTS_DIR, layer, "timeloop-mapper.ART_summary.yaml")
    data = yaml.load(open(art_file, 'r'), Loader=yaml.SafeLoader)
    for elt in data["ART_summary"]["table_summary"]:
        areas[model] += elt["area"]    

print(energies)
print(areas)
    