import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Monkey", "Hamster", "Snake", "Lizard"))

pet_color = st.sidebar.text_area(label = f"What color is your {animal_type}?", max_chars=20)

if pet_color:
    response = lch.generate_pet_name(animal_type=animal_type, pet_color=pet_color)
    print(response)
    st.text(response["pet_names"])