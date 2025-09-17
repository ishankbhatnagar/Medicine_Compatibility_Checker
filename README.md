# 💊 Medicine Compatibility Checker

A **web app** to check if multiple medications can be safely taken together using **AI-powered analysis**.

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

3. Set your **Google Gemini API key** in `app.py`:

   ```python
   API_KEY = "YOUR_API_KEY_HERE"
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## ⚡ Example

**Input:**  
`Dolo 650, Paracetamol`

**Output:**

- **Overall Recommendation:** Safe with mild monitoring.
- **Interactions:** Dolo 650 ↔ Paracetamol (Mild), advice: monitor liver.
- **Side Effects:** Nausea, Dizziness.

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

[Ishank](https://github.com/ishankbhatnagar)

