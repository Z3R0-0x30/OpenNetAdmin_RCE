# OpenNetAdmin v18.1.1 - Remote Code Execution (RCE)

![Exploit Status](https://img.shields.io/badge/status-working-brightgreen)
![Language](https://img.shields.io/badge/python-3.x-blue)
![CVE](https://img.shields.io/badge/vulnerability-RCE-critical)

## 🚨 About the Exploit

This script exploits a Remote Code Execution (RCE) vulnerability in **OpenNetAdmin v18.1.1** via the `xajax` API endpoint.  
It allows authenticated or unauthenticated attackers (depending on the server config) to execute arbitrary OS commands on the server.

---

## 📌 Exploit Details

- **Exploit Title:** OpenNetAdmin v18.1.1 - Remote Code Execution (RCE)
- **Author:** `Z3R0 (0x30)`
- **Affected Version:** `v18.1.1`
- **Tested On:** Linux
- **Vendor:** [OpenNetAdmin](http://opennetadmin.com/)
- **Authentication Required:** ❌ Not required (by default)

---

## ⚙️ Usage

```bash
python3 exploit.py [check | exploit] <TARGET_URL>
