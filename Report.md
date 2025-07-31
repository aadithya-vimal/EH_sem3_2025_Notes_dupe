# Ethical Hacking Assignment #17
## Linux AI Help Chat using Groq API
**Student Roll No in Excel Sheet: 37**

**Student Name: Aadithya Vimal**

### Methodology
I developed a simple AI-powered chatbot using Python and the Groq API. The goal was to create a tool that helps users find Linux commands by asking questions in plain English. I installed the `groq` Python library using pip, set the Groq API key in the terminal, and wrote a 15-line script that interacts with the Llama3-8b AI model. The script runs in the command line and uses natural language processing to return relevant Linux commands.

### Screenshots
Below are two key screenshots showing the implementation:

#### 1.
<img width="959" height="539" alt="PythonScriptLINUXAIBOT" src="https://github.com/user-attachments/assets/5744c4c7-3699-4870-a89f-7dde85fae2fa" />
– Shows the Python script written in VS Code.

#### 2.
<img width="1919" height="1077" alt="image" src="https://github.com/user-attachments/assets/511ad1f3-13bd-410b-a033-3dbdfc93f72f" />
– Shows the chatbot responding to a query about checking if Apache is running.

These confirm that the system works as intended.

### Findings
The AI chatbot provides fast and accurate responses to common Linux command queries. For example:
- "How do I check if Apache is running?" → `systemctl status apache2`
- "How do I list all files?" → `ls -la`
- "How do I see open ports?" → `ss -tuln`

Responses appear in under 2 seconds. The Llama3 model is well-suited for technical queries and gives helpful context along with commands.

### Conclusions
This project demonstrates how AI can assist ethical hackers and system administrators by quickly retrieving Linux commands during real-world tasks. It also highlights the importance of secure API key handling and proper scripting practices. Using AI responsibly in cybersecurity can boost efficiency without compromising ethics.

### Code
The full source code is available in:
- `linux_ai_chat.py`

### NOTE: THE GROQ API KEY USED IS DELIBERATELY KEPT OUT OF THE PROGRAM, IT IS PRESENT ONLY IN HOST COMPUTER DUE TO PRIVACY COCERNS.
