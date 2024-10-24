import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv;

load_dotenv()


# HANDLE CONNECTION TO MONGODB DATABASE

URL = os.getenv('mongodb_url')
DATABASE_NAME = os.getenv('mongodb_db_name')
COLLECTION_NAME = os.getenv('mongodb_collection_name')
client = MongoClient(URL)
db = client[DATABASE_NAME]
collections = db[COLLECTION_NAME]



# DATA IS SENT THROUGH STREAMLIT TO MONGODB

st.title("Data Uploader")

uploaded_excel_file = st.file_uploader("Choose Excel file to upload",type="xlsx")
uploaded_csv_file = st.file_uploader("Choose CSV file to uplaod", type="csv")


if uploaded_excel_file and uploaded_csv_file:
  st.write("You have uploaded both, remove one format.")

# DEAL WITH EXCEL FILE

else:
  
  if uploaded_excel_file:
    st.write("Parsing Excel sheet.")
    df = pd.read_excel(uploaded_excel_file)
    st.dataframe(df) 
    
  if uploaded_csv_file:
    st.write("Parsing CSV File")
    df = pd.read_csv(uploaded_csv_file,encoding='ISO-8859-1')
    st.dataframe(df)
    
    

  addtoDB = st.button("Add to database")
  
  if addtoDB:
    try:
      data_dictionary = df.to_dict(orient="records")
      collections.delete_many({})
      collections.insert_many(data_dictionary)
      st.write("Added data to collections.")
    except Exception as e:
      print(e)
    
    


  



