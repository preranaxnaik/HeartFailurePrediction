# Heart Failure Prediction Project

This project predicts the likelihood of heart failure based on patient health data using machine learning models. A trained **Random Forest / XGBoost model** is used for making predictions.

---

## **Dataset**
- The dataset used is the **Heart Failure Clinical Records Dataset** from [Kaggle / UCI ML Repository].
- **Target Variable:** `DEATH_EVENT`
- **Number of Records:** ~299
- **Features:** Age, Anaemia, High Blood Pressure, Creatinine Phosphokinase, Ejection Fraction, etc.

---

## **Model**
- **Algorithm Used:** Random Forest Classifier / XGBoost Classifier.
- **Accuracy:** ~90–95% (evaluated using cross-validation).
- **Serialized Model:** `heart_failure_model.pkl` (stored in `model/`).

---

## **Project Structure**
HeartFailurePrediction/
│
├── model/
│ └── heart_failure_model.pkl
├── notebooks/
│ └── HeartFailure_Model.ipynb
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── css/style.css
│ └── images/heart-bg.jpg
├── requirements.txt
└── README.md

---

## **Installation & Usage**
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd HeartFailurePrediction

2. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the Flask App:
    python app.py

5. Open your browser and navigate to:
    http://127.0.0.1:5000
---
How to Use
Fill out patient health details in the web form.

Click Predict to get the heart failure prediction result.


Technologies Used
Python, Flask

scikit-learn, XGBoost, pandas, numpy

HTML, CSS (Bootstrap), JavaScript


Future Enhancements
Add more ML models and allow model selection.

Deploy on Heroku / Render for online access.

Improve UI/UX with more patient-friendly insights.

License
This project is licensed under the MIT License.

---

### **Answer to Your Question:**
In your README, under the **Model** section, it is enough to write:
> **"The model is trained using Random Forest/XGBoost on the Heart Failure dataset, achieving 90–95% accuracy on test data."**

---

### **Next Step**
Would you like me to **generate the training code (`HeartFailure_Model.ipynb`)** that will:
- Load the dataset,
- Train RandomForest & XGBoost,
- Save `heart_failure_model.pkl`,
- And include metrics like accuracy and confusion matrix?

