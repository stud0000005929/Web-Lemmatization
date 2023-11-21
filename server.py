import pandas as pd
import streamlit as st

st.set_page_config(layout="centered")

st.title('Программаня инженерия')

text = st.text_area('Введите строку:')
words = text.split()

df = pd.DataFrame({'Words': words})

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    if st.button('Вывести резуьтат'):
        st.success('Yay!')
        st.dataframe(df)
        output_csv = df.to_csv(index=False)
        st.download_button(label='Download CSV', data=output_csv, file_name='output_file.csv', mime='text/csv')

with col3:
    st.write(' ')


