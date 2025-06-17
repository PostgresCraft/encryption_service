
---

# 🔐 Encryption Service

A lightweight Python-based encryption and decryption tool built with the [`cryptography`](https://cryptography.io/en/latest/) library.  
Secure your sensitive data with ease through symmetric encryption, and manage your keys efficiently.

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- 🔐 AES encryption and decryption (Fernet – symmetric key)
- 🔑 Key generation, saving, and loading
- 🧰 Easy CLI interface (coming soon)
- ⚙️ Ready for integration with PostgreSQL, APIs, or services
- 💻 Cross-platform (Windows, macOS, Linux)

---

## 📥 Clone the Repository

To get started, clone this repository to your local machine using Git:

```bash
git clone https://github.com/PostgresCraft/encryption_service.git
cd encryption_service
```

- Make sure you have Git installed: [https://git-scm.com](https://git-scm.com)

<div align="center">
  <img src="screenshots/Clone.gif" alt="Encryption Service Tools Clone" width="600"/>
</div>
<sub>📽️ Quick Clone of the Encryption Service Tools in action</sub>

---

## 🚀 Quick Start
### 1. Create Virtual Environment

```bash
# Windows
py -3.12 -m venv venv
.\venv\Scripts\Activate
```
<div align="center">
  <img src="screenshots/Windows.gif" alt="Encryption Service Tools Windows" width="600"/>
</div>
<sub>📽️ Quick Windows of the Encryption Service Tools in action</sub>

---

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### Optional: Upgrade pip (recommended)

Before installing dependencies, it's recommended to upgrade `pip` to the latest version to avoid compatibility issues.

```bash
python -m pip install --upgrade pip
```
<div align="center">
  <img src="screenshots/Upgradepip.gif" alt="Upgrade pip Tools Windows" width="600"/>
</div>
<sub>📽️ Upgrading pip on Windows (recommended)</sub>

---

### Install Dependencies

```bash
pip install -r requirements.txt
```
<div align="center">
  <img src="screenshots/install.gif" alt="Encryption Service Tools install" width="600"/>
</div>
<sub>📽️ Quick install of the Encryption Service Tools in action</sub>

---

## 🧱 Project Structure

The following is the current structure of the project files:

<div align="center">
  <img src="screenshots/summary_tree.txt.png" alt="Project file structure" width="600"/>
</div>
<sub>📸 Project file structure overview</sub>

<details>
<summary>📄 Click to view the text version</summary>

```bash
encryption_service/
├── encryption.py           # Core encryption/decryption logic
├── keys_manager.py         # Key generation and key handling
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)

---
