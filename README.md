# 🌍 Travel Recommendation System

An **AI-powered Travel Recommendation System** built using **FastAPI, Machine Learning, and Collaborative Filtering**.
This application provides **personalized travel destination suggestions** based on user preferences and historical data.

---

## 🚀 Features

* ✨ Personalized travel recommendations
* 🤖 Machine Learning-based popularity prediction
* 👥 Collaborative filtering using user similarity
* 🌐 Modern UI with Jinja2 templates
* ⚡ FastAPI backend (high-performance APIs)
* 🐳 Dockerized for easy deployment

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, Bootstrap (Jinja2 Templates)
* **ML Libraries:** Scikit-learn, Pandas, NumPy
* **Model Storage:** Pickle
* **Containerization:** Docker

---

## 📂 Project Structure

```
travel-recommendation-system/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── recommendation.py
│   ├── services/
│   │   └── recommender.py
│   ├── templates/
│   │   ├── index.html
│   │   └── recommendation.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── media/
│   └── utils/
│       └── encoders.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── model.pkl
│   └── label_encoders.pkl
│
├── notebooks/
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd travel-recommendation-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open in Browser

```
http://localhost:8000
```

---

## 🐳 Docker Setup

### 1️⃣ Build Docker Image

```bash
docker build -t travel-reco-app .
```

### 2️⃣ Run Container

```bash
docker run -p 8000:8000 travel-reco-app
```

### 3️⃣ Access Application

```
http://localhost:8000
```

---

## 🧠 How It Works

### 🔹 Collaborative Filtering

* Builds a **user-item matrix**
* Uses **cosine similarity**
* Recommends destinations liked by similar users

### 🔹 ML Prediction

* Encodes user input using label encoders
* Predicts **destination popularity score**

---

## 📊 Input Parameters

* User ID
* Destination Name
* Type (City, Beach, Adventure, etc.)
* State
* Best Time to Visit
* Preferences
* Gender
* Number of Adults & Children

---

## 📌 Output

* 🎯 Top recommended destinations
* 📈 Predicted popularity score

---

## ⚠️ Notes

* Ensure all datasets are placed in the correct `data/` directory
* Models (`.pkl`) must be present in `models/`
* `.venv` should NOT be included in Docker builds

---

## 🚀 Future Enhancements

* 🔐 User authentication (JWT)
* 📊 Dashboard with analytics
* ☁️ Cloud deployment (AWS / Azure)
* ⚡ Caching with Redis
* 📱 Mobile-friendly UI
* 🧠 Deep Learning-based recommendations

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Asit Kumar Sahoo**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it 🚀
