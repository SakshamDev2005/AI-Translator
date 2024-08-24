# AI-Translator

This project is an AI-based language translator implemented using LangChain and Groq models. The AI module is designed to translate text based on user input, with support for different languages as specified by the user.

# Overview

The AI Translator uses the langchain library to create a conversational model that can translate text into various languages. The ChatGroq model, powered by the "llama3-8b-8192" model, is utilized for natural language processing. The program runs in a loop, continuously taking user input until the user decides to stop.

# Installation

To run this project, you need to have Python installed along with the following dependencies:

langchain
langchain_groq

# Usage
To use the AI Translator, simply run the script:

bash
Copy code
python AI-Agent.py
The program will prompt you to enter text for translation. Type your text and press Enter. The AI will then provide a translation based on the input. To exit the program, type stop.
