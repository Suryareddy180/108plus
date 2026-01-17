# Emergency Response System - Firebase Deployment Guide

This document describes how to deploy the Emergency Response System to Firebase using Firebase Studio and the Firebase CLI.

## Prerequisites

1.  **Firebase CLI**: Install the Firebase CLI (`npm install -g firebase-tools`).
2.  **Firebase Project**: Create a new project in the [Firebase Console](https://console.firebase.google.com/).
3.  **Billing**: Enable billing for your Google Cloud project (required for Cloud Run).

## Local Preparation

The project already contains the necessary configuration files:
- `Dockerfile`: Containerizes the Flask application.
- `firebase.json`: Configures Firebase Hosting and rewrites.
- `apphosting.yaml`: Configures Firebase App Hosting settings.
- `.firebaserc`: Maps your local project to a Firebase project ID.

## Deployment Steps

### Option 1: Using Firebase Studio (Web-based)

1.  Connect your GitHub repository to [Firebase Studio](https://firebase.studio).
2.  Studio will detect the `Dockerfile` and `apphosting.yaml`.
3.  Click **Deploy** to initiate the build and rollout process.

### Option 2: Using Firebase CLI (Command Line)

1.  **Login**:
    ```bash
    firebase login
    ```
2.  **Initialize (if needed)**:
    ```bash
    firebase init hosting
    ```
    *Select "Cloud Run" when asked about the backend service.*
3.  **Deploy**:
    ```bash
    firebase deploy
    ```

## Important Considerations

- **Database**: This implementation uses SQLite (`emergency_response.db`). Note that files in Cloud Run are **ephemeral**. Any data stored in SQLite will be lost when the container restarts. For production, migrate to **Cloud Firestore** or **Cloud SQL**.
- **Socket.IO**: The `Dockerfile` uses the `eventlet` worker for Gunicorn to support real-time communication via WebSockets.
