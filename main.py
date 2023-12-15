import gradio as gr
from gtts import gTTS
import playsound
import os
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

#Input de texto para entendimento da entrada do usuário via terminal
def input_text():
    while True:
        try:
            text = input("O que você gostaria de dizer ?").lower().strip()
            return text
        except:
            exit("Não fui capaz de compreender sua fala, poderia repeti-lá por favor ?")


#Leitura do texto e transformação em um output de aúdio.
def output(text):
    convert_text_to_speech = gTTS(text=text, lang = 'pt-BR')
    convert_text_to_speech.save("output.mp3")
    playsound.playsound("output.mp3")

def __main__():
    print("Olá, tudo bem ? Serei seu sistema responsável por transcrever seus textos em um formato de aúdio")
    input_register = input_text()
    if input_register:
        print("Texto reconhecido:", input_register)
        output(input_register)
    else:
        print("Error")
        exit()

if __name__ == "__main__":
    __main__()