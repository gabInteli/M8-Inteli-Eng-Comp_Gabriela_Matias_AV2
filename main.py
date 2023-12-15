from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import gradio as gr

# load the document and split it into chunks
loader = TextLoader("context.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """From now on you are Grace Hopper, a safety professional in the engineering area, you understand equipment, tools and PPE for the areas of Civil, Mechanical, Mechatronics, Electrical, Electronic and Computer Engineering. Additionally

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="mistral")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

# system_message = response[]
#     messages.append(system_message)

#     engine = pyttsx3.init()
#     engine.say(system_message['content'])
#     engine.runAndWait()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = ""
        for s in chain.stream(message):
            bot_message += s
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

