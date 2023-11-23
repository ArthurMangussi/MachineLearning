import streamlit as st
from PIL import Image

ita = Image.open('Images/ita.png')
unifesp = Image.open('Images/unifesp.png')
eistein = Image.open('Images/eistein.png')


st.set_page_config(page_title='Homepage',
                   page_icon=":tooth:",
                   layout="wide")


# Layout SideBar
st.sidebar.title('Reference')
ref = st.sidebar.radio("How to cite this article:", ["Bibtex", "Vancouver", "APA"])

if ref == "Bibtex":
    st.write("Bibtex")

elif ref == "Vancouver":
    st.write("Vancouver")
else:
    st.wirte("APA")

st.sidebar.divider()
c1,c2,c3 = st.sidebar.columns([1,2,1])

c2.image(ita, caption="Instituto Tecnológico de Aeronáutica")
c2.image(unifesp, caption="Universidade Federal de São Paulo")
c2.image(eistein, caption="Hospital Israelita Albert Eistein")

# Menu principal
st.title("Prediction of Periodontal Treatment Response")

form = st.form(key="input",clear_on_submit=True)
form.write("Enter patient information:")

c1, c2 = form.columns([1,1])
c1.markdown("**General Information**")
omega3 = c1.selectbox("Ômega 3 and Aspirin", ["Yes", "No"])
age = c1.number_input("Age", min_value=0, max_value=110)
gender = c1.selectbox("Gender", ["Male", "Female"])
num_teeth = c1.number_input("Number of teeth", min_value=0, max_value=32)
c2.markdown("**Clinical parameters**")
hba1c = c2.number_input("HbA1c")
ss = c2.number_input("BoP")
ip = c2.number_input("PI")
ps = c2.number_input("PD")
nic = c2.number_input("CAL")
button = form.form_submit_button("Submit")

if button:
    st.success("Submited with successful")

with st.expander("**Instructions**"):
    st.write("Age: Enter the age of the patient")
    st.write("Ômega 3 and Aspirin: Yes, if patient used Ômega 3 and Aspirin")
    st.write("Gender: Enter the gender of the patient")
    st.write("Number of teeth: ")
    st.write("HbA1c: ")
    st.write("BoP: ")
    st.write("PI: ")
    st.write("PD: ")
    st.write("CAL: ")