# Abn_Albld_Masry-AI-Chatbot
# Abn_Albld_Masry-AI-Chatbot 🇪🇬🤖

**"Sahbi"** is an AI chatbot that talks like a true Egyptian! It's designed to be friendly, funny, and respectful, using the Egyptian slang dialect.

Built with 🦜 **LangChain** and powered by **Groq Cloud (Llama 3.3 70B)**.

---

## 🚀 Features
- **Authentic Egyptian Slang:** Responds naturally using local expressions.
- **Context Awareness:** Maintains conversation history using `RunnableWithMessageHistory`.
- **Blazing Fast:** Leveraging Groq's high-speed inference engine.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/sondosafify/Abn_Albld_Masry-AI-Chatbot.git](https://github.com/sondosafify/Abn_Albld_Masry-AI-Chatbot.git)
cd Abn_Albld_Masry-AI-Chatbot
2. Install requirements
Bash
pip install -r requirements.txt
3. API Key Configuration (IMPORTANT) 🔑
For security, the API key is hidden. You must use your own key to run the project:

Go to Groq Cloud Console and create an API Key.

Create a file named .env in the root directory of the project.

Add your key to the file exactly like this:

Code snippet
GROQ_API_KEY=your_actual_api_key_here
Note: The .env file is included in .gitignore to prevent your keys from being leaked.

🖥️ How to Run
Open the Chatbot.ipynb file in VS Code or Jupyter Notebook and run the cells. You can then chat with "Sahbi" directly in the terminal!

📦 Tech Stack
Language: Python

LLM: Llama-3.3-70b-versatile (via Groq)

Framework: LangChain

Environment Management: Python-dotenv
