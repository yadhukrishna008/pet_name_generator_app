from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
from utils import my_prompt_template


# load_dotenv()

def generate_pet_name(my_animal, my_animal_color):
    llm= OllamaLLM(
        model="llama3:latest",
        temperature=.7
    )
    
    prompt_templete_name= PromptTemplate(
        input_variables=["animal_type", "animal_color"],
        template= my_prompt_template
    )

    chain= prompt_templete_name | llm | StrOutputParser()

    response = chain.invoke(
        {"animal_type": my_animal, "animal_color": my_animal_color}
    )
    return response



