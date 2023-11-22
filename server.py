import pandas as pd
import streamlit as st
import model


if __name__ == '__main__':
    model_name = 'ru_core_news_md'
    nlp = model.init_model(model_name)

    st.set_page_config(layout='centered')

    st.title('Web-Lemmatization ' + model_name)

    text = st.text_area('Введите строку:')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        if st.button('Вывести резуьтат'):
            doc = nlp(text)

            dfLemma = pd.DataFrame({'text': [token.text for token in doc],
                                    'pos': [token.pos_ for token in doc],
                                    'dep': [token.dep_ for token in doc]})

            st.success('success!!!')
            st.dataframe(dfLemma)
            output_csv = dfLemma.to_csv(index=False)
            st.download_button(label='Download CSV', data=output_csv, file_name='output_file.csv', mime='text/csv')

    with col3:
        st.write(' ')