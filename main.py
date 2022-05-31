
import streamlit as st

from problem_generator.main.Lists import ListOfQuestions


st.title('Gerador de Lista de Exercícios')

theme = st.radio('Tema', ('Movimento Retilíneo Uniforme Variado', 'Movimento Circular Uniforme',))
if theme == 'Movimento Retilíneo Uniforme Variado':
    path = 'src/templates/cinemática/mruv'
else:
    path = 'src/templates/cinemática/mcu'

question_list = ListOfQuestions(path=path, number_of_questions=2)
question_list.generate()
for question in question_list.questions:
    st.markdown(f'<div style="text-align:justify; margin-bottom: 20px;">{question}<br></div>', unsafe_allow_html=True)

generate_list = st.button('Gerar')
if generate_list:
    question_list.generate()
