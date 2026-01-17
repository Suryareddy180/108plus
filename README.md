# techmedics-108+ (ATLAS Hackathon Edition)

[![Deployed on Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://techmedics-108.onrender.com/)
[![Demo Video](https://img.shields.io/badge/Watch-Demo_Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/file/d/1XYbmHxfMWaXSHama5ysZLa_DLIiKNXnn/view?usp=sharing)

## 🏆 Hackathon Context: ATLAS
Welcome to **ATLAS – GDG on Campus Hackathon**, hosted by **GDG on Campus - NIST** and powered by **Hack2skill**.

**Project**: techmedics-108+
**Theme**: Emergency Response & Healthcare
**Team**: DOONDILEONS

### 👥 The Team
1. **Nallimilli Surya Prakash Reddy**
2. **Mandela Doondi Usha Sri**
3. **Vinayaka Gowdra chandrashekarappa**
4. **Anya Sree Kadali**

---

## 🚀 LIVE DEMO
**Experience the App Live**: [https://techmedics-108.onrender.com/](https://techmedics-108.onrender.com/)

---

## 👨‍⚖️ For the Jury: Verification Guide
**Distinguished Jury Members:**
*   **Dr. Sushanta Kumar** (Associate Professor, ME, NIST University)
*   **Mr. Prabhas Raj** (Founder and CEO, Protionix Group)
*   **Dr. Sandipan Mallik** (Professor, ECE, NIST University)

**Dear Jury Members,**

Thank you for reviewing **techmedics-108+**. We have built a robust, real-time Emergency Response System that works even in low-bandwidth scenarios.

### Step-by-Test Instructions:

#### 1. The "Wow" Factor (Real-time Sync)
*   **Step 1**: Open the [Call Center Dashboard](https://techmedics-108.onrender.com/callcenter) in one tab.
*   **Step 2**: Open the [Ambulance App](https://techmedics-108.onrender.com/api/ambulance/app) in a second tab (or Incognito window).
    *   **Login**: Use ID `DVG-AMB-001` (Pre-loaded test account).
*   **Step 3**: On the Call Center, initiate a call with any number (e.g., `9876543210`).
*   **Step 4**: Click "Assign Nearest Ambulance".
*   **Result**: Watch the Ambulance App instantly receive an **"EMERGENCY ALERT"** popup without refreshing the page!

#### 2. Advanced Location Sharing (Glassmorphism UI)
*   **Step 1**: After initiating a call, click **"Share Location"**.
*   **Step 2**: Open the generated link on your phone.
*   **Step 3**: Click **"Share My Exact Location"**.
*   **Result**: The dispatcher map updates *instantly* with the victim's precise GPS coordinates.

#### 3. Why This Wins?
*   ✅ **Zero-Setup Login**: Test drivers (`DVG-AMB-001`) are auto-created on every deploy.
*   ✅ **Resilient**: Works on minimal internet using optimized sockets.
*   ✅ **User-Centric Design**: Modern "Glassmorphism" UI for high-stress usability.

---

## 📺 Project Walkthrough
If you cannot test it live, watch our full demonstration video here:
[**WATCH DEMO VIDEO**](https://drive.google.com/file/d/1XYbmHxfMWaXSHama5ysZLa_DLIiKNXnn/view?usp=sharing)

---

## 🛠️ Key Features
- **Real-time Dispatch**: Socket.IO powered instant communication.
- **Smart Assignment**: Algorithms to find the nearest available ambulance.
- **Offline-First SMS**: Fallback SMS protocol for areas with no data.
- **Responsive Design**: Mobile-first interface for drivers and victims.
- **Live Tracking**: Leaflet.js maps for real-time visualization.

## 💻 Tech Stack
- **Backend**: Python (Flask)
- **Real-time**: Socket.IO
- **Database**: SQLite (SQLAlchemy)
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript
- **Deployment**: Render (Cloud)

---

© 2026 TechMedics Team | Built for ATLAS Hackathon
