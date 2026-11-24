# Next-Token Probabilities with GPT-2

This script loads GPT-2, a small open-source language model, and shows what it thinks the next word should be for a few short prompts. For each prompt it prints the five most likely next tokens along with their probabilities, and saves everything to a CSV file.

I made it to see what actually happens inside a language model when it "predicts the next word." Instead of just getting generated text, you get to look at the raw probabilities behind each choice.

## What it does

For each prompt (like `"The cat is"`), the script:

1. Converts the text into token IDs using GPT-2's tokenizer
2. Runs the tokens through the model to get **logits**, one raw score for every token in the vocabulary
3. Applies **softmax** to turn those scores into probabilities that add up to 1
4. Picks the **top 5** most likely tokens and prints them
5. Saves the results to `week7_probability_results.csv`

The prompts used are:

- `The cat is`
- `Artificial intelligence is`
- `India is a`
- `Machine learning helps`

You can change them in the `prompts` list at the top of `main.py`.

## Requirements

- Python 3.9 to 3.12 works best (very new versions sometimes don't have a matching `torch` build)
- An internet connection the first time you run it, because GPT-2 (about 500 MB) is downloaded from Hugging Face
- The libraries listed in `requirements.txt`:

```
torch
transformers
```

## Setup and running

Open the project folder in VS Code, open a terminal, and run these one at a time.

**1. Create and activate a virtual environment (optional but recommended)**

```powershell
py -m venv venv
venv\Scripts\activate
```

If PowerShell says running scripts is disabled, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**2. Install the libraries**

```powershell
pip install -r requirements.txt
```

(or `pip install torch transformers`). This takes a few minutes because `torch` is large.

**3. Run the script**

```powershell
py main.py
```

The first run is slow since it downloads the model. After that it starts much faster.

## What you'll see

For every prompt, the terminal shows the token IDs of the input, then a ranked list like this:

```
Rank: 1 | Token: ' ...' | Probability: 0.xxxxxx
Rank: 2 | Token: ' ...' | Probability: 0.xxxxxx
...
```

The exact words and numbers depend on the prompt. Unlike the text generators that pick randomly, this output is the same every time, because the model's probabilities are fixed.

Token strings are printed with `repr()`, so you'll often see a space inside the quotes, like `' a'`. That's real: GPT-2 tokens usually include the space before the word.

## Output file

`week7_probability_results.csv` is created in the same folder, with these columns:

| Column | Meaning |
|---|---|
| Prompt | The input text |
| Rank | Position in the top 5 (1 = most likely) |
| Candidate Token | The predicted next token |
| Token ID | The token's number in GPT-2's vocabulary |
| Probability | The model's probability for that token |

You can open it in Excel or any spreadsheet app.

## Try it yourself

- Add your own prompts to the `prompts` list
- Change `TOP_K = 5` to see more or fewer candidates
- Compare how confident the model is across prompts. Some have one clear favorite, others spread the probability over many tokens

## Troubleshooting

- **`No module named 'torch'`**: the install didn't finish, or you're not in the virtual environment. Activate it and run the install again.
- **`requirements.txt` not found**: make sure you're in the same folder as the file, or just run `pip install torch transformers`.
- **`torch` won't install**: check your Python version. If it's 3.13 or newer, install Python 3.12 and recreate the virtual environment.
- **Slow or laggy installs inside OneDrive**: the `venv` folder has thousands of files that OneDrive tries to sync. Pause syncing while installing, or keep the project outside OneDrive.

## How this connects to text generation

When a language model writes a sentence, it does this exact step over and over: get probabilities for the next token, choose one, add it to the text, and repeat. This script stops after the first step so you can see the probabilities themselves.