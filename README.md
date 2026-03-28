# Secure TLS CLI Chat (mTLS)

A minimal, production-style secure chat system using **TLS 1.3 with mutual authentication (mTLS)**.

---

# Overview

This system ensures:

* End-to-end encrypted communication
* Protection against MITM attacks
* Verified clients and server (mTLS)
* Strong identity using certificates

---

# IMPORTANT BEFORE YOU START

The `certs/` folder in this repo is intentionally empty.

You MUST generate your own certificates before running the app.

**Never upload private keys (`*.key`) to GitHub.**

---

# Project Structure

```
secure_chat_tls/
├── src/
│   ├── server.py
│   ├── client.py
│   ├── utils.py
├── certs/        ← You will generate files here
├── README.md
```

---

# SETUP GUIDE

## PART 1 — Server Setup

---

## Step 1: Install OpenSSL

### Linux:

```
sudo pacman -S openssl   # Arch
sudo apt install openssl # Ubuntu/Debian
```

### Windows:

Use Git Bash or install OpenSSL manually.

---

## Step 2: Generate Certificates

Run these commands inside your project folder:

---

### Create CA (Certificate Authority)

```
openssl genrsa -out certs/ca.key 4096
openssl req -x509 -new -nodes -key certs/ca.key -sha256 -days 3650 -out certs/ca.pem
```

This is your **root authority** — keep `ca.key` VERY safe.

---

### Create Server Certificate

```
openssl genrsa -out certs/server.key 2048
openssl req -new -key certs/server.key -out certs/server.csr
openssl x509 -req -in certs/server.csr -CA certs/ca.pem -CAkey certs/ca.key -CAcreateserial -out certs/server.pem -days 365 -sha256
```

---

### Create Client Certificate

```
openssl genrsa -out certs/client.key 2048
openssl req -new -key certs/client.key -out certs/client.csr
openssl x509 -req -in certs/client.csr -CA certs/ca.pem -CAkey certs/ca.key -CAcreateserial -out certs/client.pem -days 365 -sha256
```

---

## Step 3: Start Server

```
python src/server.py
```

---

# PART 2 — Client Setup

Each user (client) must receive **3 files from you**:

```
ca.pem
client.pem
client.key
```

---

## Step 1: Place files in `certs/`

```
certs/
├── ca.pem
├── client.pem
├── client.key
```

---

## Step 2: Run client

```
python src/client.py
```

---

# SECURITY RULES (VERY IMPORTANT)

## NEVER DO THIS

* Upload `.key` files to GitHub
* Share private keys publicly
* Commit secrets accidentally

---

## ALWAYS DO THIS

* Keep `.key` files private
* Use `.gitignore`:

```
certs/*.key
```

---

## If a key is leaked:

Delete all certs
Regenerate everything

---

# How it works (simple explanation)

* `ca.pem` → trusted authority
* `server.pem` → proves server identity
* `client.pem` → proves client identity
* TLS verifies everything automatically

Result: **secure, authenticated communication**

---

# Common Issues

## Connection fails

* Make sure cert files are in `certs/`
* Check filenames are correct

---

## TLS error

* Certificates may not be signed properly
* Regenerate them carefully

---

## Client not connecting

* Server must be running first
* Check IP address in client



