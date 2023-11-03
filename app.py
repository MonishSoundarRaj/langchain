import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_party.linkedin import scarpe_linkedin
from third_party.linkedin_lookup_agent import person_lookup

load_dotenv()

def main(name: str) -> str:
     summary_template = """
          given the Linkedin information {information} about a person from I want you to create:
          1. a short summary
          2. two interesting facts about them
     """

     summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

     llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

     chain = LLMChain(llm=llm, prompt=summary_prompt_template)
     linkedin_profile_url = person_lookup(person_name=name)
     linkedin_data = scarpe_linkedin(Linkedin_url=linkedin_profile_url)

     data_dict=linkedin_data.json()
     data_dict_copy = data_dict.copy()

     for i, v in data_dict_copy.items():
          
          if v is ["", [], None]:
               data_dict_copy.pop(i)
     data_dict_copy.pop("people_also_viewed")
     data_dict_copy.pop("certifications")
               
     result = chain.run(information=linkedin_data)
     
     return result

if __name__ == "__main__":
     result = main("Monish Soundar Raj UNCC")
     print(result)