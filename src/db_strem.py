import streamlit as st
import app_db

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'UPDATE RECORD BY ID'))
