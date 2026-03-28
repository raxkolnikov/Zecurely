# Zecurely is a secure TLS CLI Chat

This project implements a secure CLI-based chat system using TLS 1.3 with mutual authentication.

## Features

- TLS 1.3 encryption (industry standard)
- Mutual TLS (client + server authentication)
- No custom cryptography
- Secure against MITM (with proper certificate handling)

## Setup

1. Generate certificates using OpenSSL (see instructions).
2. Place them inside the `certs/` directory.

## Run

### Start server
python src/server.py

### Start client
python src/client.py

## Security Notes

- Uses OS-trusted cryptographic primitives via Python `ssl`
- Forward secrecy handled by TLS
- Resistant to MITM if certificates are verified properly

## Warning

- Do NOT disable certificate verification in production
- Protect private keys at all costs
