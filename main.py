from importlib.metadata import version
from dotenv import load_dotenv
from langchain_core import __version__ as core_version
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()


print(f"langchain-core version: {core_version}")
print(f"langgraph version: {version('langgraph')}")
print(f"langchain-groq version: {version('langchain-groq')}")
print(f"langchain-google-genai version: {version('langchain-google-genai')}\n")



def main():

    # Test Gemini
    #llm_genai = ChatGoogleGenerativeAI(
    #    model="gemini-2.0-flash",
    #    temperature=0)
    #response_genai = llm_genai.invoke("Say 'setup complete!' in one word")
    #print(f"Response from Gemini: {response_genai.content}\n")
    
    llm_reasoning = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0.6
)
    
    # Test Groq
    llm_llama = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    response_llama = llm_llama.invoke("Say 'setup complete!' in one word")
    print(f"Response from llama: {response_llama.content}")
    
    llm_fast = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

    print("Setup complete!")


if __name__ == "__main__":
    main()
