import streamlit as st
from PIL import Image

with open("pokemon.txt", "r") as f:
	pokemon = f.read()

pokemon = pokemon.split("\n")
pokemon.pop()

st.title('Pokemon Explorer')
st.text(f"Browse among {len(pokemon)} Pokemons")

pokemonName = st.selectbox("Select Pokemon", pokemon)

pokemonImage = Image.open(f"./pokemonDataset/{pokemonName}.png")
st.image(pokemonImage)

st.markdown("Created by: Tanveer Singh")
st.markdown("Email: singhtanveer38@yahoo.com")
st.markdown("[Github](https://github.com/singhtanveer38) [LinkedIn](https://www.linkedin.com/in/tanveer-singh-250b02194)")