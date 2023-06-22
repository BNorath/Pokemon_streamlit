# single page website that returns 100 records from the Pokemon api
# 3 components
    # Component 1 - Make an API call for the first 100 records and display them
    # Component 2 - when a pokemon is selected, display basic information about them
    # Search function - search within the 100 results for a specific pokemon

import streamlit as st
from functions import get_pokemon_list
from functions import get_pokemon_details
from functions import search_pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon/"

st.set_page_config(layout="wide")

st.title("My List of 100 Pokémon")


# Fetch the list of Pokémon
pokemon_list = get_pokemon_list()

col1, col2, col3 = st.columns(3)

# Display the list of Pokemons - component 1
with col1:
    st.write("")
    st.write("Click on a Pokémon to view more details")

for index, pokemon in enumerate(pokemon_list):
    pokemon_name = pokemon["name"].capitalize()
    pokemon_url = pokemon["url"]

    with col1:

        if st.button(f"{index+1} . {pokemon_name}", key=index):
            # Make direct API call to fetch the details of the selected Pokémon
            selected_pokemon_details = get_pokemon_details(pokemon_url)

# Display the Pokemon details of the clicked button in column 2 - component 2
with col2:
    if "selected_pokemon_details" in locals():
        selected_pokemon_name = selected_pokemon_details["name"].capitalize()
        selected_pokemon_image = selected_pokemon_details["sprites"]["front_default"]
        selected_pokemon_weight = selected_pokemon_details["weight"]
        selected_pokemon_height = selected_pokemon_details["height"]
        selected_pokemon_base = selected_pokemon_details["base_experience"]
        selected_pokemon_abilities = selected_pokemon_details["abilities"]

        st.subheader(selected_pokemon_name)
        st.image(selected_pokemon_image, width=150)
        st.write("Weight:", selected_pokemon_weight)
        st.write("Height:", selected_pokemon_height)
        st.write("Base Experience:", selected_pokemon_base)
        st.write("Abilities:")
        for ability in selected_pokemon_abilities:
            ability_name = ability["ability"]["name"].capitalize()
            st.write("-", ability_name)
        #st.write("Base Experience:", pokemon_details["base_experience"])


with col3:
    st.write("")
    # Display the search bar - component 3
    search_query = st.text_input("Search Pokémon by name").lower()

    # Search for a Pokémon
    selected_pokemon = search_pokemon(pokemon_list, search_query)

    if search_query == "":
        st.write("Please type in a Pokémon name.")

    if selected_pokemon:
        # Display Pokemon details
        pokemon_details = get_pokemon_details(selected_pokemon["url"])
        st.subheader(pokemon_details["name"].capitalize())
        st.image(pokemon_details["sprites"]["front_default"], width=150)
        st.write("Weight:", pokemon_details["weight"])
        st.write("Height:", pokemon_details["height"])
        st.write("Base Experience:", pokemon_details["base_experience"])
        st.write("Abilities:")
        for ability in pokemon_details["abilities"]:
            st.write("-", ability["ability"]["name"].capitalize())

    if selected_pokemon not in pokemon_list and search_query != "":
        st.write("This Pokemon is not in the list. Please check your spelling")

