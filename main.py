import langchain_helper as lch
import streamlit as st


st.title("PET NAME GENERATOR")

my_pet_type= st.sidebar.selectbox(label="Which animal is your Pet?", options=('cow', 'dog', 'cat', 'hamster', 'rabbit', 'parrot'))

if my_pet_type == 'cow':
    my_pet_color= st.sidebar.text_area(label="What colour is your Cow?", max_chars=25)
elif my_pet_type == 'dog':
    my_pet_color= st.sidebar.text_area(label="What colour is your Dog?", max_chars=25)
elif my_pet_type == 'cat':
    my_pet_color= st.sidebar.text_area(label="What colour is your Cat?", max_chars=25)
elif my_pet_type == 'hamster':
    my_pet_color= st.sidebar.text_area(label="What colour is your Hamster?", max_chars=25)
elif my_pet_type == 'rabbit':
    my_pet_color= st.sidebar.text_area(label="What colour is your Rabbit?", max_chars=25)
elif my_pet_type == 'parrot':
    my_pet_color= st.sidebar.text_area(label="What colour is your Parrot?", max_chars=25)
else:
    print("Random value taken as animal type select option")

if my_pet_color:
    response= lch.generate_pet_name(my_animal=my_pet_type, my_animal_color=my_pet_color)
    st.text(response)

