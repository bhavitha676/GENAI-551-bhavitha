Google Gemini AI Integration Using Python
1. Project Overview
This project connects Python with Google Gemini AI. It allows users to ask questions and get answers from Gemini AI. The answers are displayed in the Python terminal.

If one Gemini model does not work, the program tries another model.
2. Objectives
- To connect Python with Gemini AI.
- To learn about Generative AI.
- To ask questions using Python.
- To get answers from Gemini AI.
- To learn how to handle errors.
3. Technologies Used
- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- Visual Studio Code
4. Project Structure
Gemini-AI-Project/
│
├── main.py
├── .env
├── .gitignore
└── README.md


5. Features
- Connects Python to Gemini AI.
- Uses an API key to access Gemini.
- Saves the API key in the .env file.
- Tries another model if one fails.
- Answers user questions.
- Shows answers in the terminal.
6. Installation
Install the required packages using this command:
pip install google-genai python-dotenv


7. API Key Setup
Create a .env file in the project folder and add your API key.
GEMINI_API_KEY=your_api_key_here


This key helps Python connect to Gemini AI.
8. How to Run the Project
1. Open Visual Studio Code.
2. Open the project folder.
3. Open the terminal.
4. Install the required packages.
5. Add the API key to the .env file.
6. Run the program using:
python main.py


9. Expected Output
When we run the program, it connects to Gemini AI and sends the question. Gemini generates an answer and displays it in the terminal.

Example Question:

"What is Artificial Intelligence?"

Output: Gemini AI gives an answer explaining Artificial Intelligence.
10. Security
- Keep the API key in the .env file.
- Do not share the API key.
- Add .env to .gitignore.
- Do not upload the API key to GitHub.
11. Future Improvements
- Allow users to ask different questions.
- Create a simple website.
- Add more AI features.
- Improve error handling.
- Make a simple chatbot.
12. Conclusion
This project helps us learn how to use Gemini AI with Python. We can ask questions and get answers using the Gemini API. We also learn how to use API keys and handle errors.































