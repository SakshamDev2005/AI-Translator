# AI-Translator

This project is an AI-based language translator implemented using LangChain and Groq models. The AI agent is designed to translate text based on user input, with support for different languages as specified by the user.

# Overview

The AI Translator uses the langchain library to create a conversational model that can translate text into various languages. The ChatGroq model, powered by the "llama3-8b-8192" model, is utilized for natural language processing. The program runs in a loop, continuously taking user input until the user decides to stop.

# Note (About Warnings that were shown during the run)

This warning indicates that the way you are importing the PromptTemplate class is outdated. Previously, it was possible to import PromptTemplate directly from the langchain root module, but this is no longer supported.

The LLMChain class, which was used to create a sequence of operations combining prompts and language models, has been deprecated.

The run method, which was previously used to execute a Chain (or LLMChain), has been deprecated.

