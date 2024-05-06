import streamlit as st
import lightgbm as lgb
import numpy as np

# Load the AKI model
aki_model = lgb.Booster(model_file='Type_A_Acute_Aortic_Dissection_Surgery_AKI_model.txt')

hydragogue_mapping = {"0-20mg": 0, "20mg": 1, "＞200mg": 2}
ebrantil = {"with": 1, "without": 0}
natriuretic_peptide = {"with": 1, "without": 0}


# Define mapping dictionaries

def predict_aki_probability(features):
    aki_prob = aki_model.predict(features)
    return aki_prob[0]

def main():
    st.title('Morbidity Prediction in Acute Kidney lnjury after Type A Acute Aortic Dissection Surgery')

# User selects which content to display
    selected_content = st.radio("", ("Model Introduction", "AKI Prediction"))

    if selected_content == "Model Introduction":
        st.subheader("Model Introduction")
        st.write("This online platform provides prediction for the probability of acute kidney injury after type a acute aortic dissection surgery using a LightGBMmodel.")
        # Disclaimer
        st.subheader("Disclaimer")
        st.write("The predictions generated by this model are based on historical data and statistical patterns, and they may not be entirely accurate or applicable to every individual.")
        st.write("**For Patients:**")
        st.write("- The predictions presented by this platform are intended for informational purposes only and should not be regarded as a substitute for professional medical advice, diagnosis, or treatment.")
        st.write("- Consult with your healthcare provider for personalized medical guidance and decisions concerning your health.")
        st.write("**For Healthcare Professionals:**")
        st.write("- This platform should be considered as a supplementary tool to aid clinical decision-making and should not be the sole determinant of patient care.")
        st.write("- Clinical judgment and expertise should always take precedence in medical practice.")
        st.write("**For Researchers:**")
        st.write("- While this platform can serve as a valuable resource for research purposes, it is crucial to validate its predictions within your specific clinical context and patient population.")
        st.write("- Ensure that your research adheres to all ethical and regulatory standards.")
        st.write("The creators of this online platform and model disclaim any responsibility for decisions or actions taken based on the predictions provided herein. Please use this tool responsibly and always consider individual patient characteristics and clinical context when making medical decisions.")
        st.write("By utilizing this online platform, you agree to the terms and conditions outlined in this disclaimer.")

    elif selected_content == "AKI Prediction":
        st.subheader("AKI Prediction in Patients Following Type A Acute Aortic Dissection Surgery.")

    # Feature input
    features = []

    st.subheader("AKI Features")

    ventilation_time = st.number_input("Ventilation time (h)", value=0.0, format="%.2f")
    MIN_urine = st.number_input("Urine output_min (ml)", value=0.0, format="%.2f")
    hydragogue = st.selectbox("Diuretics", ["No", "20mg", "＞200mg"])
    SCR = st.number_input("Scr (μmol/L)", value=0.0, format="%.2f")
    HR = st.number_input("Heart rate (bpm/min)", value=0, format="%d")
    UREA = st.number_input("Urea (mmol/L)", value=0.0, format="%.2f")
    natriuretic_peptide = st.selectbox("Natriuretic_peptide", ["with", "without"])
    ebrantil = st.selectbox("ebrantil", ["with", "without"])
    GLU =  st.number_input("Blood Glucose (mmol/L)", value=0.0, format="%.2f")
    MCHC =  st.number_input("MCHC (g/L)", value=0.0, format="%.2f")

    features.extend(['ventilation_time', 'hydragogue', 'SCR', 'MIN_urine', 'HR', 'natriuretic_peptide', 'ebrantil', 'UREA', 'GLU', 'MCHC'])

    # Create a button to make predictions
    if st.button('Predict AKI Probability'):
        features_array = np.array(features).reshape(1, -1)
        aki_probability = predict_aki_probability(features_array)
        st.write(f'AKI Probability: {aki_probability:.2f}')

if __name__ == '__main__':
    main()
