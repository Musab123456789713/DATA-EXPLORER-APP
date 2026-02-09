import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.markdown("""<h1 style='text-align: center;'>DATA EXPLORER</h1>""", unsafe_allow_html=True)
with st.sidebar:
   excel_file = st.file_uploader("Upload your Excel File: ", type="xlsx")
  
if excel_file:
   data = pd.read_excel(excel_file)
   data.dropna(axis=1, inplace=True)
   st.dataframe(data.head())  
  
   with st.sidebar:
       x_col = st.selectbox("SELECT COLUMN A:", data.columns)
       y_col = st.selectbox("SELECT COLUMN B:", data.columns)
      
   if st.button("ðŸŽ¯ GENERATE CHART"):
       x_axis = data[x_col]
       y_axis = pd.to_numeric(data[y_col], errors='coerce') 
       # Optional: remove rows where y is NaN
       mask = y_axis.notna()
       x_axis = x_axis[mask]
       y_axis = y_axis[mask]


       fig, graph = plt.subplots(figsize=(10, 4))
       sns.barplot(x=x_axis, y=y_axis, ax=graph, palette="Set2")
       graph.set(xlabel=None, ylabel=None)
       graph.set_title("CUSTOM BAR CHART")
       st.pyplot(fig)


with st.sidebar:
   st.markdown("""
               <p style='font-family:Arial; font-size: 18px;'> <br> Welcome to Data Explorer App. <br> Upload your Excel file here, select the columns for X and Y axes then
               click on Generate Chart to visualize your data. <br> This web app helps you to quickly explore your dataset in a simple & interactive way.
               <br> Â© 2026 Muhammad Musab AlI
               </p>
               """, unsafe_allow_html=True)


st.markdown("""
           <style>
           .block-container{
               padding-top: 2rem;
           }
           </style>
           """, unsafe_allow_html=True)

