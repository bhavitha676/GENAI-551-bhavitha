# **Multi-Provider LLM Integration Using Python**

## **1. Project Overview**

This project connects Python with two AI platforms: Google Gemini and Ollama. Users can choose either platform and ask questions. The selected AI model gives an answer and displays it on the screen.

If one Gemini model does not work, the program tries another model. Ollama runs AI models directly on the computer.

## **2. Objectives**

- To connect Python with AI models.
- To learn about Gemini and Ollama.
- To choose between two AI platforms.
- To ask questions and get answers.
- To handle errors when a model fails.
- To test the program.

## **3. Technologies Used**

- Python
- Google Gemini API
- Ollama
- Llama 3.2
- Google Gen AI SDK
- Requests
- python-dotenv
- Pytest
- Visual Studio Code

## **4. Project Structure**

```
week2/
│
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## **5. Features**

- Choose Gemini or Ollama.
- Enter your own questions.
- Get answers from Gemini AI.
- Get answers from Ollama.
- Try another Gemini model if one fails.
- Show error messages when something goes wrong.
- Check the program using tests.

## **6. Installation**

Install all required packages using:

```
pip install -r requirements.txt
```

## **7. Configuration**

For Gemini, create a `.env` file and add your API key.

```
GEMINI_API_KEY=your_api_key_here
```

For Ollama, install Ollama and download the Llama 3.2 model using:

```
ollama pull llama3.2
```

## **8. How to Run**

1. Open Visual Studio Code.
2. Open the project folder.
3. Open the terminal.
4. Install the required packages.
5. Run the program:

```
python main.py
```

The program asks you to choose an AI platform.

**Example:**

```
Choose provider (gemini/ollama):
```

Enter `gemini` or `ollama`.

Then enter your question:

```
Enter your question: Explain Artificial Intelligence in simple words.
```

The selected AI model gives an answer in the terminal.

## **9. Testing**

The project has a file called `test_client.py` to check whether the program is working correctly.

Run this command:

```
python -m pytest -v
```

**Test Result:** 1 test passed successfully.

## **10. Security**

- Keep the Gemini API key in the `.env` file.
- Do not share your API key.
- Add `.env` to `.gitignore`.
- Do not upload the API key to GitHub.

## **11. Future Improvements**

- Add more AI platforms.
- Create a simple website.
- Allow users to ask many questions.
- Improve error handling.
- Add more tests.

## **12. Conclusion**

This project helps us learn how to use Gemini and Ollama with Python. We can choose an AI platform, ask questions, and get answers. We also learn how to handle errors and test the program. In the future, more AI platforms and features can be added to this project.
