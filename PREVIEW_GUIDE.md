# Local Preview Guide

Before deploying to Firebase, you can preview the Emergency Response System locally using these three methods.

## 1. Fast Preview (Standard Python)
This is the quickest way to test the application logic and UI.

1.  **Activate Environment**:
    ```bash
    .\venv\Scripts\activate
    ```
2.  **Start Application**:
    ```bash
    python start_app.py
    ```
3.  **Access**: 
    - Dashboard: `http://localhost:5000/` (Now includes a **Driver Portal** button)
    - Driver App: `http://localhost:5000/api/ambulance/app`

---

## 2. Production Preview (Docker)
This mirrors the Firebase Cloud Run environment exactly. Use this to ensure your container configuration is correct.

1.  **Build Image**:
    ```bash
    docker build -t ers-preview .
    ```
2.  **Run Container**:
    ```bash
    docker run -p 8080:8080 ers-preview
    ```
3.  **Access**: `http://localhost:8080/`

---

## 3. Firebase Preview (Hosting Emulators)
This tests the `firebase.json` rewrites and how Hosting interacts with your backend.

1.  **Install Emulator**:
    ```bash
    firebase setup:emulators:hosting
    ```
2.  **Start Emulator**:
    ```bash
    firebase emulators:start --only hosting
    ```
    *Note: This usually requires your backend to be reachable or mocked if you're testing full integration.*

---

## Verification Checklist
- [ ] **Real-time updates**: Open the dashboard and driver app in two windows. Try assigning an ambulance.
- [ ] **Static Assets**: Ensure all CSS/JS files load without 404s (check browser console).
- [ ] **Route Rewrites**: Ensure `http://localhost:5000/callcenter` loads the same as `index.html`.
