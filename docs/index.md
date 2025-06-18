# 🔐 Encryption Service

[![Build Status](https://github.com/PostgresCraft/encryption_service/actions/workflows/python-app.yml/badge.svg)](https://github.com/PostgresCraft/encryption_service/actions)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

> A lightweight Python-based encryption and decryption tool built with the [`cryptography`](https://cryptography.io/en/latest/) library.  
> Secure your sensitive data with ease through symmetric encryption, and manage your keys efficiently.

---

## ✨ Features

- 🔐 AES encryption and decryption (Fernet – symmetric key)
- 🔑 Key generation, saving, and loading
- 🧰 Easy CLI interface (coming soon)
- ⚙️ Ready for integration with PostgreSQL, APIs, or services
- 💻 Cross-platform (Windows, macOS, Linux)

---

## 📥 Clone the Repository

```bash
git clone https://github.com/PostgresCraft/encryption_service.git
cd encryption_service
```

![Clone Example](../screenshots/clone-the-repository.gif)

---

## 🚀 Quick Start

### Windows

```bash
py -3.12 -m venv venv
.\env\Scripts\Activate
```

![Windows Setup](../screenshots/Windows.gif)

---

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ⬆️ Optional: Upgrade pip

```bash
python -m pip install --upgrade pip
```

![Upgrade pip](../screenshots/Upgrade_pip.gif)

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

![Install Dependencies](../screenshots/install.gif)

---

## 🧱 Project Structure

![Project Tree](../screenshots/summary_tree.png)

<details>
<summary>📄 Click to view as text</summary>

```bash
encryption_service/
├── encryption.py           # Core encryption/decryption logic
├── keys_manager.py         # Key generation and key handling
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

</details>

---

## 🧪 Integration Guide

To use `encryption_service` in other projects:

1. Import `keys_manager` and `encryption`.
2. Load or generate your encryption key.
3. Use `encrypt()` and `decrypt()`.

✅ Perfect for PostgreSQL, APIs, Flask apps, and more.

---

## 💣 Brute-Force Simulation

Run the brute-force demo:

```bash
py tests\brute_force_simulation.py
```

![Brute Force GIF](../screenshots/brute_force_simulation.gif)

> Fernet uses 256-bit symmetric keys.  
> That's **2^256** combinations — brute-forcing is impractical.

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](../LICENSE) file for full terms.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)
