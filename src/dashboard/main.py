import streamlit as st

import os
st.write(os.listdir('src'))

import src.dashboard.steps as steps

st.set_page_config(
    page_title='Receitas',
    page_icon='🧶'
)

st.markdown("# Vamos criar sua receita 🧶")
modelo = steps.config_model()
if not modelo.lacking_measurements():
    st.markdown('## Calibrando')
    st.markdown('''
        Para prosseguir com a criação da receita, precisamos calibrar as medidas com os seus pontos.
        Para isso, pegue a linha que pretende usar e sua agulha, e faça um quadrado de pelo menos 5 x 5.
        Meça a largura e a altura da peça final, e informe também o número de pontos e de linhas.
        Opcionalmente, você pode medir quantos centímetros de linha utilizou para fazer a peça, e quanto tempo levou.
    ''')

    st.markdown('### Preencha após concluir a amostra')
    calibration = steps.calibrate()

    if calibration:
        st.write(
            'Largura do ponto: ' +
            str(calibration['column_width'])
        )
        st.write(
            'Altura do ponto: ' +
            str(calibration['row_height'])
        )

        st.markdown('# Receita')
        steps.make_recipe(modelo, calibration)