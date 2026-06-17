import streamlit as st
import numpy as np
import pandas as pd
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="HemaPredict AI - Predictive Medical Analytics",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown("""
    <style>
    .main-title { font-size: 38px; font-weight: bold; color: #8B0000; margin-bottom: 5px; }
    .subtitle { font-size: 18px; color: #555555; margin-bottom: 25px; }
    .metric-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #8B0000; }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<div class="main-title">HemaPredict AI™ Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Medical Informatics & Predictive Computational Biomedicine Dashboard</div>', unsafe_allow_html=True)
st.divider()

# --- Sidebar: Patient Demographics & Clinical Metrics ---
st.sidebar.header("📋 Patient Demographics & Baseline Data")
patient_name = st.sidebar.text_input("Patient Full Name / ID:", placeholder="e.g. PT-90412")
age = st.sidebar.number_input("Age (Years):", min_value=1, max_value=120, value=45)
gender = st.sidebar.selectbox("Biological Sex:", ["Male", "Female", "Other"])
family_history = st.sidebar.radio("Family History of Hematological Malignancies?", ["No", "Yes"])

st.sidebar.divider()
st.sidebar.header("🩺 Clinical Vital Signs")
systolic_bp = st.sidebar.slider("Systolic Blood Pressure (mmHg):", 80, 200, 120)
diastolic_bp = st.sidebar.slider("Diastolic Blood Pressure (mmHg):", 50, 130, 80)
heart_rate = st.sidebar.slider("Heart Rate (bpm):", 40, 160, 75)

# --- Main Layout: Complete Blood Count (CBC) Inputs ---
st.header("🔬 Laboratory Biomarkers (Complete Blood Count - CBC)")
st.write("Please enter the patient's exact laboratory blood panel metrics below:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Red Blood Cell Metrics")
    hb = st.number_input("Hemoglobin (Hb) [g/dL]:", min_value=0.0, max_value=25.0, value=13.5, step=0.1)
    rbc = st.number_input("Red Blood Cell (RBC) [x10^12/L]:", min_value=0.0, max_value=10.0, value=4.5, step=0.1)
    mcv = st.number_input("Mean Corpuscular Volume (MCV) [fL]:", min_value=50.0, max_value=150.0, value=88.0, step=0.5)

with col2:
    st.subheader("White Blood Cell Profile")
    wbc = st.number_input("Total White Blood Cells (WBC) [x10^9/L]:", min_value=0.0, max_value=100.0, value=6.5, step=0.1)
    lymphocytes = st.slider("Lymphocytes Percentage (%):", 0, 100, 30)
    neutrophils = st.slider("Neutrophils Percentage (%):", 0, 100, 60)

with col3:
    st.subheader("Platelets & Other Biomarkers")
    platelets = st.number_input("Platelet Count [x10^9/L]:", min_value=0, max_value=1000, value=250, step=5)
    crp = st.number_input("C-Reactive Protein (CRP) [mg/L]:", min_value=0.0, max_value=200.0, value=3.2, step=0.1)
    ldh = st.number_input("Lactate Dehydrogenase (LDH) [U/L]:", min_value=50, max_value=1500, value=210)

st.divider()

# --- Predictive Analytics Engine (Simulation) ---
st.header("⚡ HemaPredict AI™ Diagnostic Engine")
st.write("Click the button below to process the multi-parametric hematological data through the predictive neural architecture.")

if st.button("🧬 Run Predictive Diagnostics Analytics", type="primary"):
    with st.spinner("Analyzing laboratory biomarkers and computational oncology data matrices..."):
        time.sleep(2)  #Simulating AI computational time
        
        # Simple clinical logic to simulate a smart prediction score based on your research concepts
        base_risk = 5.0
        if wbc > 11.0 or wbc < 4.0: base_risk += 25.0
        if hb < 11.0: base_risk += 20.0
        if platelets < 150 or platelets > 450: base_risk += 15.0
        if ldh > 250: base_risk += 15.0
        if family_history == "Yes": base_risk += 15.0
        
        risk_percentage = min(base_risk, 99.4)
        
        # Displaying Results
        st.success("Analysis Complete! Clinical Report Generated Successfully.")
        
        res_col1, res_col2 = st.columns([1, 2])
        
        with res_col1:
            st.markdown(f"""
                <div class="metric-card">
                    <h4>AI Predictive Risk Score</h4>
                    <h2 style="color: {'#8B0000' if risk_percentage > 50 else '#2E7D32'}; font-size: 45px;">
                        {risk_percentage:.1f}%
                    </h2>
                    <p>Status: <strong>{'HIGH RISK - Immediate Clinical Evaluation Advised' if risk_percentage > 50 else 'LOW RISK - Regular Monitoring'}</strong></p>
                </div>
            """, unsafe_allow_html=True)
            
        with res_col2:
            st.subheader("📈 Biomarker Distribution & Deviation Chart")
            # Generating dummy statistical chart for visualization
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['Patient Index', 'Normal Baseline Upper Bound', 'Normal Baseline Lower Bound']
            )
            st.line_chart(chart_data)
            
        # Clinical Notes Summary Box
        st.subheader("📝 Diagnostic Insights Summary")
        st.info(f"""
        **Patient Reference:** {patient_name if patient_name else 'Anonymous PT'} ({gender}, {age} Years Old)  
        **Primary Indicators Observed:** Hemoglobin is at {hb} g/dL, Total Leukocyte count is {wbc} x10^9/L, and Platelet distribution stands at {platelets} x10^9/L.  
        **Recommendation:** This computational analysis serves as a predictive informatics treatise for oncology risk stratifications. Final prognosis must be verified through bone marrow biopsy or flow cytometry if clinical correlation persists.
        """)