import os
from dotenv import load_dotenv
from chromadb.config import Settings

load_dotenv()


greeting = ["hi", "hello", "hello!", "hey" , "hi buddy", "good morning", "good afternoon", "good evening"]
name_check = ["what is your name", "can you tell your name", "your name please", "can you please tell your name"]
change_name = ["can you change your name", "please change your name to", "can you please change your name", 
               "can you update your name to", "change your name to" ,"this is your name"]

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)
