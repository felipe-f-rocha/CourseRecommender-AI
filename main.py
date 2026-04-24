import streamlit as st
import backend as b

st.set_page_config(page_title="CourseRecommender AI", layout="centered")

st.title("Descubra cursos ideais para você")


with st.form(key="infos", clear_on_submit=True, enter_to_submit=False):
    st.write("Preencha as informações")

    # Input das informações

    area = st.text_input("Área de interesse: ", placeholder='Digite sua área de interesse')
    nivel = st.number_input(label='Digite o seu nível de 0 a 10: ', min_value=0, max_value=10)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

if submitted:
    cursos = b.formar_prompt(area, nivel)

    st.write(f'Cursos de {area.title()} para nivel {nivel}')

    for curso in cursos:
        container = st.container(border=True, horizontal=True, width=700)
        container.text(curso['Nome do Curso'])
        container.badge(curso['Plataforma'], color="green")
        container.text(curso['Por que é ideal'],text_alignment="left")
        container.caption('É gratuito?\n',text_alignment="left")
        container.caption(curso['É gratuito'],text_alignment="left")
        container.link_button("Começar agora", f"{curso['Link']}", type="primary")
