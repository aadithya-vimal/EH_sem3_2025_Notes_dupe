import os
from groq import Groq
client = Groq(api_key=os.environ.get("----THIS API KEY IS HIDDEN DELIBERATELY----"))
print("🐧 Linux AI Assistant (type 'exit' to quit)\n")
while True:
    user_input = input("Ask for a Linux command: ")
    if user_input.lower() == "exit":
        print("Goodbye! Stay safe.")
        break

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Suggest a Linux command to: {user_input}"}],
        model="llama3-8b-8192"
    )
    print("💡:", response.choices[0].message.content, "\n")
