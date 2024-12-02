import streamlit as st
from src.classes import models

def config_model():
    model_class = st.selectbox(
        'Selecione um modelo para começar',
        options=[
            submodel for submodel in
            models.Model.__subclasses__()
        ],
        format_func=(lambda a: a.__name__)
    )

    if model_class:
        modelo = model_class()
        nedded_measurements = modelo.get_measurements()

        st.write('Configure as seguintes medidas:')
        for k in nedded_measurements.keys():
            required = (
                ' - opcional' if not nedded_measurements[k].required
                else ''
            )
            unit = '(' + nedded_measurements[k].unit + ')'
            v = st.number_input(
                k.capitalize() + ' ' + unit + required
            )
            if v is not None:
                nedded_measurements[k].set_value(v)
                modelo.set_measurements(
                    nedded_measurements
                )
    
    return modelo


def calibrate():
    cols = st.columns(2)
    with cols[0]:
        columns = st.number_input('Número de pontos da peça final')
        width = st.number_input('Largura da peça final (cm)')
        line = st.number_input('Quantidade de linha usada (cm) - opcional')
    with cols[1]:
        rows = st.number_input('Número de linhas da peça final')
        height = st.number_input('Altura da peça final (cm)')
        time = st.number_input('Tempo gasto (min) - opcional')

    if (
        columns > 0 and rows > 0 and
        width > 0 and height > 0
    ):
        column_width = columns/width
        row_height = rows/height

        return {
            'column_width': column_width,
            'row_height': row_height,
            'total_stiches': rows*columns,
            'line': line,
            'time': time
        }
    
def make_recipe(model, calibration):
    recipe, total_stiches = model.make_recipe(calibration)
    st.write(recipe)
    if calibration['line'] > 0:
        line_per_stitch = calibration['line']/calibration['total_stiches']
        expected_line = total_stiches * line_per_stitch
        st.write(f'Espera-se que você vai utilizar {expected_line} cm de linha neste trabalho.')
    if calibration['time'] > 0:
        time_per_stitch = calibration['time']/calibration['total_stiches']
        expected_time = int(total_stiches * time_per_stitch)
        st.write(f'Espera-se que você vai gastar {expected_time} minutos neste trabalho.')