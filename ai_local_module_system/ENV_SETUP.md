# ENVIRONMENT SETUP (CRITICAL)

## OBJECTIVE
Create a stable LOCAL environment that never breaks across projects.

---

## 1. BASE STORAGE LOCATION

Use ONE global path only:

Linux/Mac:
~/ai_storage

Windows:
C:\ai_storage

---

## 2. STRUCTURE (DO NOT CHANGE)

ai_storage/
├── data/
├── models/
├── modules/
├── experience/
├── logs/

---

## 3. PYTHON ENVIRONMENT

Create isolated env:

python -m venv venv

Activate:
Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

Install:
pip install -r requirements.txt

---

## 4. SYSTEM RULES

- NEVER change base storage path
- NEVER mix project storage
- ALWAYS use StorageManager
- ALWAYS run via start_training.py first

---

## 5. MULTI-PROJECT DESIGN

All projects MUST:
- read/write same storage
- reuse models
- reuse experience

---

## 6. BACKUP STRATEGY

Backup weekly:

zip ai_storage/

---

## FINAL NOTE

This environment is your AI brain.
If broken → all learning is lost.
Protect it.
