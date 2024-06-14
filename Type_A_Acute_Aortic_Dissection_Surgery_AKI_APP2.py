import streamlit as st
import lightgbm as lgb
import numpy as np

# Load the AKI model
aki_model = lgb.Booster(model_file='internalandexternal_aki_model.txt')

# Define mapping dictionaries
ebrantil_mapping = { "without": 0, "with": 1}


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
    
    SCR = st.number_input("Scr (μmol/L)", value=0.0, format="%.2f")
    HR = st.number_input("Heart rate (bpm/min)", value=0, format="%d")
    HB = st.number_input("Hemoglobin (g/L)", value=0, format="%d")
    CKMB = st.number_input("CKMB (ng/ml)", value=0.0, format="%.2f")
    ebrantil = st.selectbox("ebrantil", ["without", "with"])
    CPB_time = st.number_input("Cardiopulmonary bypass time (min)", value=0.0, format="%.2f")
    cadiac_arrest_time = st.number_input("Circulatory arrest time (min)", value=0.0, format="%.2f")
    AST =  st.number_input("AST (U/L)", value=0.0, format="%.2f")
    GLU =  st.number_input("Blood Glucose (mmol/L)", value=0.0, format="%.2f")
    PLT =  st.number_input("PLT (10^9/L)", value=0.0, format="%.2f")

   
    # 根据用户选择从映射字典中获取相应的数字值
    hydragogue_value = hydragogue_mapping[hydragogue]
    ebrantil_value = ebrantil_mapping[ebrantil]
    natriuretic_peptide_value = natriuretic_peptide_mapping[natriuretic_peptide]
    
    # 将特征添加到列表中
    features.extend([SCR, HR, HB, CKMB, ebrantil_value, CPB_time, cadiac_arrest_time, AST, GLU, PLT])
  
    # Create a button to make predictions
    if st.button('Predict AKI Probability'):
        features_array = np.array(features).reshape(1, -1)
        aki_probability = predict_aki_probability(features_array)
        st.write(f'AKI Probability: {aki_probability:.2f}')

if __name__ == '__main__':
    main()
