import streamlit as st

st.title('Calculadora Simple con Streamlit')

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


opcion = st.selectbox(
    "Selecciona tu lenguaje favorito:",
    ["Python", "JavaScript", "C#", "Java", "Go"]
)

st.write("Elegiste:", opcion)


valor1 = st.number_input('Introduce el primer valor:', min_value=0.0, value=10.0)

valor2 = st.number_input('Introduce el segundo valor:', min_value=0.0, value=5.0)

st.write('---') # Separador visual

suma = valor1 + valor2

if st.button('Calcular Suma'):
    st.success(f'El resultado de la suma es: **{suma}**')

st.subheader('Valores Ingresados')
st.write(f'Primer valor: **{valor1}**')
st.write(f'Segundo valor: **{valor2}**')

number = st.slider("Pick a number", 0, 100)