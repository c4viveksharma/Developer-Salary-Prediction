import streamlit as st
import pickle
import numpy as np





def load_model():
    with open('saved_steps.pkl' , 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary prediction")

    st.write("""### We need some information to predict the salary""")
    countries =(
        "United States of America",
        "United Kingdom of Great Britain and Northern Ireland",
        "India",
        "Germany",
        "Canada",
        "France",
        "Australia",
        "Spain",
        "Italy",
        "Netherlands")

    education  = (
        'Bachelor’s degree (B.A., B.S., B.Eng., etc.)',
        'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
        'Some college/university study without earning a degree',
        'Other doctoral degree (Ph.D., Ed.D., etc.)', 'Something else',
        'Primary/elementary school', 'Associate degree (A.A., A.S., etc.)',
        'Professional degree (JD, MD, etc.)',
        'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)'
)

    country = st.selectbox("Country",countries, index=0)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0,50,3)

    ok = st.button("Calculate Salary")
    if ok is True:
        X = np.array([[country, education, experience]])
        X[:,0] = le_country.transform(X[:,0])
        X[:,1] = le_education.transform(X[:,1])
        X=X.astype(float)

        salary = regressor_loaded.predict(X)
        
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

