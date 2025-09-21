# 💊 Medicine Compatibility Checker

A **web app** to check if multiple medications can be safely taken together using **AI-powered analysis**.  
You can try it live at: [https://medicinecompatibilitychecker.streamlit.app/](https://medicinecompatibilitychecker.streamlit.app/)

---

## 📝 About

Enter multiple medications to get:

- Potential **drug interactions** with severity (Mild/Moderate/Severe).  
- **Side effects** for each drug.  
- **Overall recommendation** on safety.  
- **References** if available.  
- Downloadable results in **JSON format**.

Built with **Streamlit** and **Google Gemini API**.

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/Medicine_Compatibility_Checker.git
   cd Medicine_Compatibility_Checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## ⚡ Example

**Input:**  
`Paracetamol, Montair LC`

**Output:**

- **Overall Recommendation:** Generally safe, but mild monitoring is advised.  
- **Individual Interactions:**  
  - Paracetamol ↔ Montair LC: Mild, advice: monitor for potential minor side effects.  
- **Side Effects:** Nausea, Dizziness (if any).  
- **References:** Available links or sources provided by the AI output.  

> If the AI output is malformed, the app will show the **raw output** for review instead of crashing.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend / AI:** Google Gemini API  
- **Data Handling:** Python, Pandas

---

## ⚠️ Disclaimer

For **educational purposes only**. Always consult a healthcare professional before taking medications.

---

## 👨‍💻 Author

[Ishank Bhatnagar](https://github.com/ishankbhatnagar)
