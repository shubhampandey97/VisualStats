# Statistics Explorer

An interactive Streamlit application for visualizing statistical concepts
such as mean, median, mode, and skewness.

---

## Features
- Interactive skewness control
- Dynamic histogram visualization
- Clear statistical markers
- Clear visual markers for mean, median, and mode
- Intuitive explanation of distribution behavior

---

## Run
```bash
pip install -r requirements.txt
streamlit run app.py


---

## 🧪 Engineering & Quality Practices

This project follows **real-world software engineering standards** to ensure reliability, maintainability, and scalability.

### 🔁 Branching Strategy
- `master` is a **protected branch**
- All development happens on **short-lived feature branches**
- Direct commits to `master` are **not allowed**

```text
master
  ↑
feature/* → Pull Request → CI → Review → Merge → Delete
