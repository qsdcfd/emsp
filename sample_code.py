import streamlit as st
import pandas as pd
import numpy as np

#정산 파일
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

#비교 파일
uploaded_files = st.file_uploader("Choose the file")
if uploaded_files is not None:
    # To read file as bytes:
    bytes_datas = uploaded_files.getvalue()
    st.write(bytes_datas)

    # To convert to a string based IO:
    stringios= StringIO(uploaded_files.getvalue().decode("utf-8"))
    st.write(stringios)

    # To read file as string:
    string_datas = stringios.read()
    st.write(string_datas)

    # Can be used wherever a "file-like" object is accepted:
    dataframes= pd.read_csv(uploaded_files)
    st.write(dataframes)


# 파일 두  개 비교하는 코드
# Text files

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

st.download_button('Download CSV', text_contents, 'texts.csv')
st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

#with open('myfile.csv') as f:
#   st.download_button('Download CSV', f)  # Defaults to 'text/plain'

# ---
# Binary files

#binary_contents = b'whatever'

# Different ways to use the API

#st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

#with open('myfile.zip', 'rb') as f:
#   st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'

# You can also grab the return value of the button,
# just like with any other button.

#if st.download_button(...):
#   st.write('Thanks for downloading!')

