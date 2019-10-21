lines = [el.split("\t") for el in open("../results/results_5000/.predictions","r").read().split("\n")]
lines = ["\t".join(line[:-1]) for line in lines if line[-1] == "True"]
open("../results/results_5000/results.tsv", "w+").write("\n".join(lines))