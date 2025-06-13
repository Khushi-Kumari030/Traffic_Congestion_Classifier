# 🚦 Traffic Congestion Classifier

This project predicts traffic congestion levels (`Low`, `Medium`, `High`) based on input parameters like area name, average speed, traffic volume, environmental impact, and more. The model is built using **Random Forest** .
---


## 🧠 Model

The backend model is a **Random Forest Classifier** trained with:
- One-hot encoding for categorical features (`Area Name`)
- Missing value imputation:
  - Mean for numeric
  - Mode for categorical
- Min-Max normalization for numeric features
- Label encoding for congestion level (`0 = Low`, `1 = Medium`, `2 = High`)

Saved as a pipeline using `pickle`.

---

