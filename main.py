import streamlit as st
from services import recommendation_service
from presentation import error_handler

st.set_page_config(page_title="CourseRecommender AI", layout="centered")

st.title("Descubra cursos ideais para você")

with st.form(key="infos", clear_on_submit=True, enter_to_submit=False):
    st.write("Preencha as informações")

    # Input das informações

    area = st.text_input("Área de interesse: ", placeholder='Digite sua área de interesse')
    escolaridade = st.selectbox(label='Selecione a sua escolaridade: ',
                         options=("Ensino Fundamental",
                                  "Ensino Médio",
                                  "Curso Técnico / Profissionalizante",
                                  "Graduação",
                                  "Pós Graduação"
                                  ))

    level = st.selectbox(label='Selecione o nível do curso desejado: ',
                         options=("Iniciante",
                                  "Intermediário",
                                  "Avançado",
                                  "Profissional"
                                  ))

    submitted = st.form_submit_button("Submit")

if submitted:
    try:
        cursos = recommendation_service.recommend(area, escolaridade, level)
    except Exception as e:
        mensagem = error_handler.get_message(e)
        st.error(mensagem)


    else:
        st.write(f'Cursos de {area.title()} para nivel {level}')
        for curso in cursos:
            container = st.container(border=True, horizontal=True, width=700)
            container.text(curso['Nome do Curso'])
            container.badge(curso['Plataforma'], color="green")
            container.text(curso['Por que é ideal'], text_alignment="left")
            container.caption('É gratuito?\n', text_alignment="left")
            container.caption(curso['É gratuito'], text_alignment="left")
            container.link_button("Começar agora", f"{curso['Link']}", type="primary")
