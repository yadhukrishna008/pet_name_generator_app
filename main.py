import langchain_helper as lch
import streamlit as st


st.title("PET NAME GENERATOR")

my_pet_type= st.sidebar.selectbox(label="Which animal is your Pet?", options=('cow', 'dog', 'cat', 'hamster', 'rabbit', 'parrot'))

my_pet_color= st.sidebar.text_area(label=f"What colour is your {my_pet_type}?", max_chars=25)

if my_pet_color:
    response= lch.generate_pet_name(my_animal=my_pet_type, my_animal_color=my_pet_color)
    st.text(response)

