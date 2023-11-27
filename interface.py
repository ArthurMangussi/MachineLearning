import streamlit as st
import joblib
from ClassificadorOdonto.bib import bibtex, vancouver, apa, logo1, logo2

st.set_page_config(page_title='Homepage',
                   page_icon=":tooth:",
                   layout="wide")


# Layout SideBar
st.sidebar.title('Reference')
ref = st.sidebar.radio("How to cite this article:", ["Bibtex", "Vancouver", "APA"], horizontal=True)

# Citation
if ref == "Bibtex":
    st.sidebar.markdown(bibtex, unsafe_allow_html=True)

elif ref == "Vancouver":
    st.sidebar.markdown(vancouver, unsafe_allow_html=True)
else:
    st.sidebar.markdown(apa, unsafe_allow_html=True)

st.sidebar.divider()
c1,c2 = st.sidebar.columns([2,2])

c1.image(logo1)
c2.image(logo2)

# Menu principal
st.title("Prediction of Periodontal Therapy Response")

form = st.form(key="input",clear_on_submit=True)
form.write("Enter patient information:")

c1, c2 = form.columns([1,1])
c1.markdown("**General Information**")
num_teeth = c1.number_input("Number of teeth", min_value=0, max_value=32)
age = c1.number_input("Age", min_value=0, max_value=110)
gender = c1.selectbox("Gender", ["Male", "Female"])
omega3 = c1.selectbox("Omega-3 and Aspirin", ["Yes", "No"])

c2.markdown("**Clinical parameters**")
ps = c2.number_input("PD")
nic = c2.number_input("CAL")
ip = c2.number_input("PI")
ss = c2.number_input("BoP")
hba1c = c2.number_input("HbA1c")

button = form.form_submit_button("Submit", help="Only press the Submit button if all information has been filled in")

# Carregando o modelo Random Forest
rf = joblib.load("ClassificadorOdonto/random_forest.joblib")

if button:
    if omega3 == "Yes":
        omega3_binario = 1
    elif omega3 == "No":
        omega3_binario = 0  

    if gender == "Male":
        gender_binario = 1
    elif gender == "Female":
        gender_binario = 0         
    
    features = [[omega3_binario, gender_binario, age, num_teeth, hba1c, ss, ip, ps, nic]]
    resultado = rf.predict(features)
    proba = rf.predict_proba(features)

    if resultado[0] == 0:
        resposta = "Pacient will not achieve endpoint"
        prob = proba[0][0]
    else:
        resposta = "Pacient will achieve endpoint"
        prob = proba[0][1]

    st.info(f"Prediction: {resposta} with probability of {prob*100:.4f} %")

with st.expander("**Instructions**"):
    st.write("Age: Enter the patient's age")
    st.write("Ômega 3 and Aspirin: Yes, if patient will use Ômega 3 and Aspirin")
    st.write("Gender: Enter the gender of the patient")
    st.write("Number of teeth: Enter the patient's number of teeth")
    st.write("HbA1c: Enter the patient's glycated hemoglobin. You may type the HbA1c level")
    st.write("BoP: Enter the patient's BoP. You may type the BoP level")
    st.write("PI: Enter the patient's PI. You may type the PI level")
    st.write("PD: Enter the patient's PD. You may type the PD level")
    st.write("CAL: Enter the patient's CAL. You may type the CAL level")