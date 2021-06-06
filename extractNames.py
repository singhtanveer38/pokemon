import os

pokemon = []
for i in os.listdir("./pokemonDataset/"):
	pokemon.append(i.split(".")[0])

with open ("./pokemon.txt", "w") as f:
	for i in pokemon:
		f.write(f"{i}\n") 

print("file saved!!")