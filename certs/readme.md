# 📁 certs/

This folder is used to store TLS certificates required for secure communication.

## ⚠️ Important

* This directory is intentionally empty in the repository.
* You must generate your own certificates before running the application.
* **Do NOT upload private keys (`*.key`) to GitHub.**

## 📌 Required Files (locally)

After setup, this folder should contain:

### For Server:

* `ca.pem`
* `server.pem`
* `server.key`

### For Client:

* `ca.pem`
* `client.pem`
* `client.key`

## 🔐 Security Note

Private keys (`*.key`) must always remain confidential.
If any key is exposed, regenerate all certificates immediately.
