import warnings

warnings.filterwarnings("ignore")

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq


model = ChatGroq(model="llama3-8b-8192",api_key='')

template = """
You're an AI Translator.
You translate texts in different languages as per the user's wish.

Question: {question}

Answer:

"""

prompt = PromptTemplate(template = template, input_variables=['question'])

while True:
    user_inp = input('Ask the Translator ->')

    if user_inp.lower() == 'stop':
        break
    chain = LLMChain(llm = model, prompt = prompt)
    print(chain.run(user_inp))
