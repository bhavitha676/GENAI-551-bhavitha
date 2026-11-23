# **LLM Client with Usage Tracking**

## **1. Project Overview**

This project uses Python to connect with AI models and get answers to user questions. It supports Gemini and Ollama. It also saves details like token usage, time taken, and cost in MongoDB.

## **2. Providers**

- **Gemini:** An online AI model from Google.
- **Ollama:** An AI model that runs on our computer.

## **3. Project Files**

- `main.py` – Runs the program.
- `llm_client.py` – Connects to Gemini and Ollama.
- `usage_logger.py` – Saves usage details in MongoDB.
- `test_client.py` – Checks whether the program works.
- `requirements.txt` – Contains the required packages.

## **4. Installation**

Install the required packages using:

```
pip install -r requirements.txt
```

## **5. Configuration**

Create a `.env` file and add the following details:

```
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=your_mongodb_connection_string
GEMINI_INPUT_PRICE_PER_MILLION=0
GEMINI_OUTPUT_PRICE_PER_MILLION=0
```

These details help the program connect to Gemini and MongoDB and calculate the estimated cost.

## **6. Ollama Setup**

If you want to use Ollama, run these commands:

```
ollama pull llama3.2
ollama serve
```

## **7. How to Run**

Run the following command:

```
python main.py
```

Choose `gemini` or `ollama` and enter your question. The AI will give an answer on the screen.

## **8. MongoDB Data**

The program saves the following details in MongoDB:

- AI provider name.
- Model name.
- Input and output tokens.
- Total tokens used.
- Time taken to answer.
- Estimated cost.
- Success or failure status.
- Date and time.

The database name is `llm_monitoring` and the collection name is `api_usage`.

## **9. Testing**

Run this command to check the program:

```
python -m unittest test_client.py
```

It checks whether the program is working correctly.

## **10. Error Handling**

- If a request fails, the program tries again up to 3 times.
- If a model is not working, it can try another Gemini model.
- The program saves whether the request was successful or failed.

## **11. Security**

- Keep API keys in the `.env` file.
- Do not share the `.env` file.
- Do not upload private keys to GitHub.

## **12. Conclusion**

This project helps us connect Python with Gemini and Ollama. It gives answers to user questions and saves usage details in MongoDB. We can also check token usage, time, and estimated cost. It helps us understand how AI models work and how to track their usage.
