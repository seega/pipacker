import pickle

with open("all-addr-prefix1") as file_in:
    data = set()
    for line in file_in:
        dline = line.rstrip("\n")
        data.add(dline)
with open("00.pickle", "wb") as f:
    pickle.dump(data, f)
