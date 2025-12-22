import json

import requests
import streamlit as st

st.title("API de Predicción del Modelo Iris")

st.write(
    "Ingresa las características de la flor de iris para obtener una predicción de su especie."
)

sepal_length = st.slider("Longitud del sépalo (cm)", 0.0, 10.0, 5.0)
sepal_width = st.slider("Ancho del sépalo (cm)", 0.0, 10.0, 3.0)
petal_length = st.slider("Longitud del pétalo (cm)", 0.0, 10.0, 4.0)
petal_width = st.slider("Ancho del pétalo (cm)", 0.0, 10.0, 1.0)

if st.button("Obtener Predicción"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    payload = {"features": features}

    api_url = "http://localhost:5000/predict"

    try:
        response = requests.post(
            api_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == 200:
            prediction_result = response.json().get("prediction")
            species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
            predicted_species = species_map.get(prediction_result, "Desconocida")
            st.success(f"La predicción es: **{predicted_species}**")
        else:
            st.error(f"Error en la petición: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"No se pudo conectar con la API. Error: {e}")
