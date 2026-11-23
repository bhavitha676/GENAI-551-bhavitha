# **Tokenizer Comparison Using Python**

## **1. Project Overview**

This project compares three different tokenizers using Python. It checks how they split sentences into small parts called tokens.

The project uses three languages: English, Telugu, and Hindi. It helps us understand how different tokenizers work with different languages.

## **2. Tokenizers Used**

- **BPE (GPT-2):** Splits text into small parts.
- **WordPiece (BERT):** Breaks words into smaller pieces.
- **SentencePiece (XLM-R):** Splits text into tokens.

## **3. Languages Used**

**English:**

```
Artificial intelligence is changing the world.
```

**Telugu:**

```
కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.
```

**Hindi:**

```
कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।
```

## **4. Project Files**

- `tokenizer_comparison.py` – Main Python program.
- `requirements_1.txt` – Contains the required packages.

## **5. Installation**

Install the required packages using:

```
pip install -r requirements_1.txt
```

Make sure you have an internet connection the first time you run the program. It downloads the tokenizers from Hugging Face.

## **6. How to Run**

Open the terminal and run:

```
python tokenizer_comparison.py
```

The program compares all three tokenizers and displays the results.

## **7. Expected Output**

The program displays three things for each language:

- **Tokens:** Shows how the sentence is divided into small parts.
- **Token IDs:** Gives a number to each token.
- **Token Count:** Shows the total number of tokens.

## **8. Why This Project Is Useful**

- Helps us understand how tokenizers work.
- Shows the difference between three tokenizers.
- Helps compare English, Telugu, and Hindi.
- Shows which tokenizer uses fewer tokens for each sentence.
- Helps understand token usage in AI models.

## **9. Conclusion**

This project helps us understand how different tokenizers divide sentences into small parts. We compare three tokenizers using English, Telugu, and Hindi. By checking the token count, we can understand how each tokenizer works with different languages.
