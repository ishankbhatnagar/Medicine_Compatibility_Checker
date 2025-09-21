import streamlit as st
import google.generativeai as genai
import warnings
import json
import pandas as pd
import re
import os

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("GEMINI_API_KEY not found! Please set it in Streamlit Secrets.")
else:
    genai.configure(api_key=API_KEY)

warnings.filterwarnings('ignore')

model = genai.GenerativeModel("gemini-1.5-flash")

def get_drug_interactions(medications):
    medications_str = ", ".join(medications)
    
    prompt = (
        f"Analyze the following medications together: {medications_str}. "
        "1. For each medication, list potential interactions with the other drugs, side effects, severity (Mild/Moderate/Severe), and short advice. "
        "2. Provide an overall conclusion on whether these medications can be safely taken together, including precautions or monitoring needed. "
        "3. Include references if possible. "
        "Return the response strictly in valid JSON format, without comments or extra text."
    )

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        raw_text = re.sub(r"^```(?:json)?", "", raw_text)
        raw_text = re.sub(r"```$", "", raw_text)

        raw_text = re.sub(r"//.*", "", raw_text)
        raw_text = re.sub(r"/\*.*?\*/", "", raw_text, flags=re.DOTALL)

        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if match:
            json_text = match.group(0)
            try:
                return json.loads(json_text)
            except Exception:
                return {"Error": "Model returned malformed JSON. Raw output:", "RawOutput": raw_text}
        else:
            return {"Error": "No JSON found in model output.", "RawOutput": raw_text}

    except Exception as e:
        return {"Error": f"API call failed: {e}"}

st.sidebar.title("💊 Instructions")
st.sidebar.info(
    "1. Enter medication names separated by commas.\n"
    "2. Click 'Check Interactions'.\n"
    "3. View individual drug interactions and overall advice.\n"
    "4. Download results as JSON if needed."
)

st.markdown("<h1 style='color:#4B0082;'>💊 Medicine Compatibility Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray; font-size:12px;'>- Made by Ishank Bhatnagar</p>", unsafe_allow_html=True)
st.markdown("Check if your medications can be safely taken together and see potential side effects.")

medications_input = st.text_area(
    "Enter the medications (separated by commas):",
    placeholder="e.g., Dolo 650, Paracetamol",
    key="medications_input"
)

if st.button("Check Interactions"):
    if medications_input:
        medications = [med.strip() for med in medications_input.split(",")]

        with st.spinner('Checking interactions...'):
            result = get_drug_interactions(medications)

        if "Error" in result:
            st.error(result["Error"])
        else:
            if result.get("OverallRecommendation"):
                st.markdown(
                    f"<div style='background-color:#4B0082; color:white; padding:10px; border-radius:5px; font-size:16px;'>"
                    f"💡 <b>Overall Recommendation:</b> {result['OverallRecommendation']}"
                    "</div>", unsafe_allow_html=True
                )

            severity_colors = {"Mild": "green", "Moderate": "orange", "Severe": "red"}

            st.markdown("## Individual Drug Interactions")
            for drug, info in result.get("Drugs", {}).items():
                st.markdown(f"### {drug}")

                interactions = info.get("Interactions", [])
                if interactions:
                    df_interactions = pd.DataFrame(interactions)
                    for idx, row in df_interactions.iterrows():
                        color = severity_colors.get(row.get('Severity', ''), 'black')
                        st.markdown(
                            f"- <b>{row.get('Drug', 'Unknown Drug')}</b> "
                            f"({row.get('Severity', 'Unknown')}): "
                            f"<span style='color:{color}'>{row.get('Advice', 'No advice available')}</span>",
                            unsafe_allow_html=True
                        )
                else:
                    st.markdown("No interactions reported.")

                side_effects = info.get("SideEffects", [])
                if side_effects:
                    st.markdown("**Side Effects:**")
                    st.write(side_effects)

                references = info.get("References", [])
                if references:
                    st.markdown("**References:**")
                    for ref in references:
                        st.markdown(f"- {ref}")

            st.download_button(
                label="📥 Download Results as JSON",
                data=json.dumps(result, indent=2),
                file_name="medicine_compatibility.json",
                mime="application/json"
            )
    else:
        st.error("Please enter at least one medication.")

