from datasets import load_dataset

dataset = load_dataset("Mahesh2841/Agriculture")

data = dataset["train"]

print("Total rows:", len(data))
print(data[0])