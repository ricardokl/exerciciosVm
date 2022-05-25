
import streamlit as st

from problem_generator.main.Questions import Question


st.title('Gerador de Lista de Exercícios')
gen = st.button('Gerar')

if gen:
    q1 = Question(template_path='src/templates/mruv')
    st.write(q1.question_with_values)
