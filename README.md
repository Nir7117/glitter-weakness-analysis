# Glitter Weakness Analysis -- Final Project

This project was created as part of the **Magshimim Cyber Program**.\
The goal of the project was to **analyze a given social-media-style
application ("Glitter")**, identify weaknesses using tools such as
**Wireshark, BurpSuite, and manual protocol inspection**, and then
**implement proofs-of-concept exploits in Python**.

------------------------------------------------------------------------

## 🎯 Project Overview

The application provided simulated a real client-server system.\
My objective was to:

1.  **Capture and analyze network traffic** using Wireshark.
2.  **Reverse-engineer the communication protocol** used by the Glitter
    application.
3.  **Identify security vulnerabilities** in authentication, cookies,
    recovery mechanisms, and user actions.
4.  **Implement a Python script** demonstrating exploitation of these
    weaknesses safely and responsibly.

The Python code in this repository is a clean and organized collection
of all the weakness demonstrations.

------------------------------------------------------------------------

## 🔍 Identified Weaknesses & Implementations

### 1. Password Recovery Weakness

The password recovery system generated predictable recovery codes based
on: - Current date\
- User ID\
- Current time minus 6 minutes

I implemented a function that reconstructs this code and sends it to the
server for verification.

------------------------------------------------------------------------

### 2. Weak Login Mechanism

The login checksum was based on simple ASCII summation.\
By reversing the equation, I could compute a valid password or validate
inputs without knowing the real password.

------------------------------------------------------------------------

### 3. Weak Cookie Generation

The cookie is built from: - Current date\
- MD5(username)\
- Current time\
- Date again

Because everything is predictable and the hash is not salted, I was able
to reproduce valid cookies for arbitrary users.

------------------------------------------------------------------------

### 4. Publishing "Glits" (Posts)

By capturing the protocol in Wireshark and analyzing the TCP structure,
I learned the server accepts specific socket-based messages.\
I implemented full message crafting and server communication in Python.

------------------------------------------------------------------------

### 5. Weak Search Query

The search mechanism accepts unvalidated data and does not verify sender
identity, allowing searches with injected terms.

------------------------------------------------------------------------

### 6. Fake Comment Injection

I implemented a sequence of valid Glitter protocol requests to: - Fetch
user entity\
- Load feed\
- Inject comments\
- Spoof the `user_screen_name` field

------------------------------------------------------------------------

### 7. Fake Date Weakness

The server did not validate timestamps, allowing comments with arbitrary
or unrealistic dates.

------------------------------------------------------------------------

## 🛠️ Tools Used

-   **Python 3.10+**
-   **Wireshark** -- packet inspection & protocol discovery
-   **Requests Library** -- for HTTP weaknesses
-   **Raw Sockets** -- for Glitter protocol weaknesses
-   **Hashlib** -- MD5 reconstruction
-   **Datetime** -- for time-based calculations

------------------------------------------------------------------------

## 📁 Project Structure

    Final_glitter_project.py   # Main exploit demonstration script
    README.md                  # Documentation file

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project was developed **strictly for educational, academic, and
ethical purposes**.\
All testing was performed inside a **closed training environment**
provided by the Magshimim Cyber Program.\
No real-world systems were accessed, harmed, or interfered with.

------------------------------------------------------------------------

## 🚀 How to Run

1.  Install required Python modules:

        pip install requests

2.  Run the script:

        python Final_glitter_project.py

3.  Use the menu to select the weakness demonstration you want to run.

------------------------------------------------------------------------

## 👤 Author

**Nir Ben Saadon**\
Magshimim Cyber Program -- Class of 2025

