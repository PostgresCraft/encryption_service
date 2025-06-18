
# Encryption Service

📘 [Live Documentation](https://postgrescraft.github.io/encryption_service/)

<p align="center">
  <img src="https://github.com/PostgresCraft/encryption_service/actions/workflows/python-app.yml/badge.svg" alt="Build Status"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"/>
</p>

A lightweight Python-based encryption and decryption tool built with the [`cryptography`](https://cryptography.io/en/latest/) library.  
Secure your sensitive data with ease through symmetric encryption, and manage your keys efficiently.

---


## Features

- 🔐 AES encryption and decryption (Fernet – symmetric key)
- 🔑 Key generation, saving, and loading
- 🧰 Easy CLI interface (coming soon)
- ⚙️ Ready for integration with PostgreSQL, APIs, or services
- 💻 Cross-platform (Windows, macOS, Linux)

[🔝 Back to Top](#table-of-contents)

---

## Clone the Repository

To get started, clone this repository to your local machine using Git:

```bash
git clone https://github.com/PostgresCraft/encryption_service.git
cd encryption_service
```

- Make sure you have Git installed: [https://git-scm.com](https://git-scm.com)

<p align="center">
  <a href="screenshots/clone-the-repository.gif">
    <img src="screenshots/clone-the-repository.gif" alt="Quick clone-the-repository" width="600"/>
  </a>
</p>

📽️ Quick Clone of the Encryption Service Tools in action  

[🔝 Back to Top](#table-of-contents)

---

## Quick Start

### 1. Create Virtual Environment

```bash
# Windows
py -3.12 -m venv venv
.\env\Scripts\Activate
```

<p align="center">
  <a href="screenshots/Windows.gif">
  <img src="screenshots/Windows.gif" alt="Encryption Service Tools Windows" width="600"/>
  </a>
</p>
📽️ Quick Windows of the Encryption Service Tools in action

[🔝 Back to Top](#table-of-contents)

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

<p align="center">
  <a href="screenshots/Upgrade_pip.gif">
  <img src="screenshots/Upgrade_pip.gif" alt="Upgrade pip Tools Windows" width="600"/>
  </a>
</p>
📽️ Upgrading pip on Windows (recommended)

[🔝 Back to Top](#table-of-contents)

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

<p align="center">
  <a href="screenshots/install.gif">
  <img src="screenshots/install.gif" alt="Encryption Service Tools install" width="600"/>
  </a>
</p>
📽️ Quick install of the Encryption Service Tools in action

[🔝 Back to Top](#table-of-contents)

---

## Project Structure

The following is the current structure of the project files:

<p align="center">
  <a href="screenshots/summary_tree.png">
  <img src="screenshots/summary_tree.png" alt="Project file structure" width="600"/>
  </a>
</p>
📸 Project file structure overview

<details>
<summary>📄 Click to view the text version</summary>

```bash
encryption_service/
├── encryption.py           # Core encryption/decryption logic
├── keys_manager.py         # Key generation and key handling
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

</details>

[🔝 Back to Top](#table-of-contents)

---

## 🧪 Integration Guide

Want to use `encryption_service` inside other projects?  
Here's how to integrate it in 3 simple steps...

1. Import `keys_manager` and `encryption` from the module.
2. Load or generate your encryption key.
3. Use `encrypt()` and `decrypt()` wherever needed in your project.

✅ Ready for PostgreSQL, APIs, Flask projects and more.

[🔝 Back to Top](#table-of-contents)

---

## Brute-Force Simulation — Why Fernet is Secure

The script [`brute_force_simulation.py`](tests/brute_force_simulation.py) demonstrates the strength of Fernet encryption by attempting to decrypt a message using 100,000+ random keys.

As expected, **none succeed** — showcasing the impracticality of brute-force attacks.

> Fernet uses 256-bit symmetric keys.
> That means **2^256 possible keys**, which is more than the number of atoms in the universe.  
> Brute-forcing such a key is computationally unfeasible.

### ▶️ Run the simulation:

```bash
py tests\brute_force_simulation.py
```

<p align="center">
  <a href="screenshots/brute_force_simulation.gif">
  <img src="screenshots/brute_force_simulation.gif" alt="Encryption Service Tools brute_force_simulation" width="600"/>
  </a>
</p>
📽️ It reinforces why using strong encryption like Fernet is essential.

[🔝 Back to Top](#table-of-contents)

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

[🔝 Back to Top](#table-of-contents)

---

## Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)

[🔝 Back to Top](#table-of-contents)

---