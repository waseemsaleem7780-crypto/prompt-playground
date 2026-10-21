🧠 Prompt Engineering Playground

A simple Streamlit application that compares 4 different prompting techniques side-by-side on the same question.

🚀 What it does
The app takes a user question and processes it using:
1. **Zero-shot:** Direct question, no examples.
2. **Few-shot:** Provides examples to set the format and length.
3. **Chain-of-Thought (CoT):** Asks the model to think step-by-step.
4. **Role-based:** Assigns a persona (e.g., Senior Software Engineer) to change the depth and tone.

🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, OpenAI SDK
- **API:** Groq API (Llama 3 model)
- **Config:** python-dotenv

⚙️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/waseemsaleem7780-crypto/prompt-playground.git
