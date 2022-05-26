
import streamlit as st

from problem_generator.main.Questions import Question


st.title('Gerador de Lista de Exercícios')
gen = st.button('Gerar')

if gen:
    st.markdown('### Questão 1')
    q1 = Question(template_path='src/templates/mruv')
    st.write(q1.question_with_values)

    st.markdown('### Questão 2')
    q2 = Question(template_path='src/templates/mruv')
    st.write(q2.question_with_values)

    st.markdown('### Questão 3')
    q3 = Question(template_path='src/templates/mruv')
    st.write(q3.question_with_values)
