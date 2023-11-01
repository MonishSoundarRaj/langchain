from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, AgentType, initialize_agent
from tools.tools import get_profile_url

def person_lookup(person_name: str):
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    
    template = """ given the full name {input} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only a URL
    """
    
    tools = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL"
        )
    ]
    
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template = PromptTemplate(input_variables=['input'], template=template)
    prompt = prompt_template.format_prompt(input=person_name)
    linkedin_profile_url=agent.run(input=prompt)
    
    return linkedin_profile_url

    

