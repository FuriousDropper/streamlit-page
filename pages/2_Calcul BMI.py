import streamlit as st

st.title("Calcul your Body Mass Index(BMI)")
col1, col2 = st.columns(2)

with col1:
  st.header("Insert your weight[kg]")
  wh = st.number_input("")
with col2:
  st.header("Insert your height[m2]")
  h = st.number_input("", key="key2", value=1.00)


if h < 1:
  calcul = "No height insert"
  st.subheader(f"Your BMI is: {calcul}")
else:
  calcul = round(wh / h, 2)
  st.header(calcul)
  if int(calcul) < 18.5:
    BMI = "underweight"
  elif int(calcul) >= 18.5 and int(calcul) <= 25:
    BMI = "normal build"
  elif int(calcul) > 25 and int(calcul) <= 30:
    BMI = "overweight"
  elif int(calcul) > 30 and int(calcul) <= 35:
    BMI = "moderate obesity"
  elif int(calcul) > 35 and int(calcul) <= 40:
    BMI = "severe obesity"
  elif int(calcul) > 40:
    BMI = "morbid obesity"
  st.subheader(f"Your BMI is: {calcul}, and it corresponds to {BMI}")