import streamlit as st
import datetime

# Título y bienvenida
st.title("🏋️ Rutina de Transformación Corporal - Edwin")
st.write(f"Hola Edwin 👋 Hoy es {datetime.date.today().strftime('%d/%m/%Y')}.")
st.write("Camina, aliméntate bien y sigue tu rutina exprés. ¡Vamos con todo!")

# Navegación
seccion = st.sidebar.selectbox(
    "Navegar a:",
    ["📅 Mi Plan Diario", "💪 Ejercicios Exprés", "🍽️ Mi Menú del Día", "📈 Seguimiento Semanal", "🌙 Tips para Dormir Mejor"]
)

if seccion == "📅 Mi Plan Diario":
    st.header("📅 Plan Diario")
    st.write("**Rutina de hoy:** Rutina A (Flexiones, Sentadillas, Planchas)")
    st.write("**Consejo:** Si dormiste mal, haz solo la caminata y una versión ligera de la rutina.")
    st.write("**Comidas clave:** Rica en proteína, antiinflamatoria y ligera en la noche.")

elif seccion == "💪 Ejercicios Exprés":
    st.header("💪 Rutinas Exprés")
    rutina = st.selectbox("Elige una rutina:", ["Rutina A", "Rutina B", "Rutina C"])

    if rutina == "Rutina A":
        st.markdown("""
        - 10 flexiones  
        - 20 sentadillas  
        - 30 segundos de plancha  
        - 10 fondos en silla  
        - 15 segundos de descanso entre ejercicios (repetir 3 veces)
        """)
    elif rutina == "Rutina B":
        st.markdown("""
        - 12 sentadillas con salto  
        - 10 desplantes por pierna  
        - 15 abdominales  
        - 10 lagartijas diamante  
        - Repetir 3 veces
        """)
    else:
        st.markdown("""
        - 15 puentes de glúteo  
        - 30 segundos de plancha lateral por lado  
        - 20 elevaciones de talones  
        - 10 burpees (lento si estás cansado)  
        - Repetir 2 veces
        """)

elif seccion == "🍽️ Mi Menú del Día":
    st.header("🍽️ Menú del Día")
    st.markdown("""
    **Desayuno:**  
    - 3 claras + 2 huevos completos  
    - 2 tostadas integrales o 1/2 taza de avena  
    - 1 té verde  

    **Almuerzo:**  
    - 120g de pollo o atún  
    - 1 taza de arroz integral o camote  
    - Ensalada con aguacate y limón  

    **Snack:**  
    - Yogur griego + canela  
    - 10 almendras  

    **Cena:**  
    - Omelette de claras con verduras  
    - 1 taza de lentejas o sopa de verduras  
    - Infusión de manzanilla
    """)

elif seccion == "📈 Seguimiento Semanal":
    st.header("📈 Seguimiento Semanal")
    with st.form("seguimiento"):
        semana = st.number_input("Semana número:", min_value=1, max_value=52, step=1)
        cintura = st.number_input("Medida de cintura (cm):", step=0.5)
        energia = st.slider("Nivel de energía (1-10):", 1, 10, 5)
        horas_sueno = st.slider("Horas dormidas (última noche):", 0, 12, 6)
        dormiste_mal = st.checkbox("¿Dormiste mal?")
        submitted = st.form_submit_button("Guardar seguimiento")
        if submitted:
            st.success("¡Seguimiento guardado exitosamente!")

elif seccion == "🌙 Tips para Dormir Mejor":
    st.header("🌙 Tips para Dormir Mejor")
    st.markdown("""
    - Evita pantallas 30 min antes de dormir  
    - Prueba la respiración 4-7-8: inhala 4 seg, retén 7, exhala 8  
    - Cena ligera: sin pan, sin azúcar  
    - Toma manzanilla o leche tibia  
    - Si puedes, una siesta de 15–25 min ayuda a recuperar el día  
    - Alimentos que ayudan: kiwi, plátano, avena, nueces, queso fresco
    """)
