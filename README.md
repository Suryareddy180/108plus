# techmedics-108+ (ATLAS Hackathon Edition)

![Project Banner](about.jpeg)

## 🏆 Hackathon Context: ATLAS
Welcome to **ATLAS – GDG on Campus Hackathon**, hosted by **GDG on Campus - NIST** and powered by **Hack2skill**.

ATLAS is an open innovation hackathon where student developers identify real challenges in their campuses or local communities and build practical solutions using Google technologies. 

### 👥 Team: DOONDILEONS
We are proud to present **techmedics-108+**, a solution built for impact.
1. **Nallimilli Surya Prakash Reddy**
2. **Mandela Doondi Usha Sri**
3. **Vinayaka Gowdra chandrashekarappa**
4. **Anya Sree Kadali**

---

## 👨‍⚖️ For the Jury (Verification Guide)

**Dear Dr. Sushanta Kumar, Mr. Prabhas Raj, and Dr. Sandipan Mallik,**

Thank you for reviewing our project. **techmedics-108+** is a high-performance Emergency Response System (ERS) designed to streamline communication between callers, dispatchers, and ambulance drivers.

### How to Verify the Project:
1. **Dispatcher Dashboard**: Access at `http://localhost:8080/`. You can see active calls and ambulance locations.
2. **Driver Portal**: Click the **"Driver Portal"** button on the dashboard or go to `http://localhost:8080/api/ambulance/app`.
3. **Location Tracking**: Use the **"Initiate Emergency Response"** form to simulate a call. You will receive a location sharing link (simulated for the demo).
4. **Real-time Sync**: Notice how maps update instantly across the Dashboard and Driver Portal when an ambulance is assigned or a location is shared.

---

---

## 📺 Project Demonstration
Watch our detailed project explanation and demo here:
[![Project Demo](https://img.shields.io/badge/YouTube-Watch%20Demo-red?style=for-the-badge&logo=youtube)](https://youtu.be/v0NK8BFeIeQ?si=Sx3pkmjgE1nXoYSD)

---

## 🚀 Key Features

- **Dispatcher Dashboard**: Real-time view of all active emergency calls and ambulance locations.
- **Smart Dispatching**: Automatically identifies the nearest available ambulance for rapid response.
- **Ambulance Driver Portal**: Dedicated interface for drivers to receive assignments, navigate to victims, and update status.
- **Victim Location Sharing**: Secure, link-based location sharing that works even in low-bandwidth environments.
- **SMS Protocol Fallback**: Integrated SMS-based location sharing for offline or zero-data scenarios.
- **Production-Ready**: Fully containerized with Docker and optimized for Firebase Studio/Cloud Run deployment.

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Real-time**: Socket.IO (WebSockets)
- **Database**: SQLite (SQLAlchemy)
- **Map Engine**: Leaflet.js & OpenStreetMap
- **Deployment**: Firebase Hosting & Google Cloud Run

## 💻 Local Setup

1. **Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run Application**:
   ```bash
   python start_app.py
   ```

## 🐳 Docker Preview

To test the production environment locally:

```bash
docker build -t ers-preview .
docker run -p 8080:8080 ers-preview
```

## ☁️ Firebase Deployment

This project is configured for **Firebase Studio**.
1. Connect this repository to [Firebase Studio](https://firebase.studio).
2. Deploy to **Cloud Run** (Backend) and **Firebase Hosting** (Frontend).

For detailed deployment steps, see [README_FIREBASE.md](README_FIREBASE.md).
For preview instructions, see [PREVIEW_GUIDE.md](PREVIEW_GUIDE.md).

---

© 2026 TechMedics Team | 108+ Emergency Response System
