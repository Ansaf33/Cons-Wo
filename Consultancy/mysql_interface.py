import mysql.connector
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


connection = mysql.connector.connect(
  host=os.getenv('mysql_host'),
  user=os.getenv('mysql_user'),
  password=os.getenv('mysql_password'),
  database=os.getenv('mysql_database'),
  port=os.getenv('mysql_port')
)

table = os.getenv('mysql_table')

cursor = connection.cursor()

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
      
      # TO DELETE EXISTING DATA IN THE TABLE
      
      delete_query = """
      DELETE FROM %s;
      """
      data = (table)
      cursor.execute(delete_query,data)
      
      # TO INSERT THE DATA IN THE DF
      
      
      insert_query = """
    
      """
      
      data = ()
      cursor.execute(insert_query,data)
    
        
   
      st.write("Added data to the table.")
    except Exception as e:
      st.write('You have received an error. Do ensure that : ')
      st.write("The data is inserted.")
      print(e)
    
    


  






