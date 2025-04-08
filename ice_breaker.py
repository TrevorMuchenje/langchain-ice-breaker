import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser

information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman known for his key roles in Tesla, SpaceX, PayPal, OpenAI, Twitter (which he rebranded as X) and America PAC.
Since 2025, he has been a senior advisor to United States president Donald Trump and the de facto head of the Department of Government Efficiency (DOGE). Musk is the wealthiest person
in the world; as of March 2025, Forbes estimates his net worth to be US$345 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada, whose citizenship he had inherited through his mother. He graduated from the University of Pennsylvania
in the U.S. before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company
that later merged to form PayPal, which was acquired by eBay in 2002 for $1.5 billion. That year, Musk also became a U.S. citizen.
"""

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    # llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})
    print(res)
