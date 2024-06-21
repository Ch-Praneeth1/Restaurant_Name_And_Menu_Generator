from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.chains import SequentialChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
# HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN
# HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",model_kwargs={'temperature':1})

openAi_Api_Key = os.getenv("openai_api_key")
os.environ['OPENAI_API_KEY'] = openAi_Api_Key
llm = OpenAI(model_name="gpt-3.5-turbo-0125",temperature=0.7,api_key = "sk-proj-RfQ5e7HGTRrB9CtbpFnAT3BlbkFJxFlFpR1zx2FrPVME27jg")

def generateRestaurantNameAndMenu(cuisine):
    

    prompt = PromptTemplate(
        input_variables = ["cuisine"],
        template = "I want to open a restaurant for {cuisine} food. suggest a fancy name for this."
    )
    chain1 = LLMChain(llm=llm,prompt=prompt,output_key="resturant_name")

    prompt2 = PromptTemplate(
        input_variables = ["resturant_name"],
        template = "Suggest some menu items for {resturant_name}. Return it as a comma seperated string"
    )
    chain2 = LLMChain(llm=llm,prompt=prompt2,output_key='menu_items')


    Sequential_Chain = SequentialChain(chains=[chain1,chain2],
                                       input_variables=["cuisine"],
                                       output_variables=['resturant_name','menu_items']
    )
    response = Sequential_Chain({'cuisine':cuisine})
    return response

if __name__ == "__main__":
    cuisine = 'indian'
    print(generateRestaurantNameAndMenu(cuisine))