# LLM Baseline Evaluation (v0.1)

A small, no-frills script that asks a local LLM 30 questions about how language models work, checks the answers for key terms, and saves everything to a CSV.

I built this to answer one simple question: *before I change anything about this model or its setup, how well does it do right now?* That's the baseline. Every future version gets compared against it.

## What it does

1. Loads 30 questions from `golden_set.json` (tokenization, decoding, embeddings, positional encoding, API costs and so on).
2. Sends each question to a local model through [Ollama](https://ollama.com), with `temperature` set to 0 so the answers are as repeatable as possible.
3. Scores each answer by checking how many of the expected keywords show up in it.
4. Writes every question, answer, score and status to `baseline_results.csv`.
5. Prints a summary at the end.

## Quick start

You'll need Python 3 and Ollama installed.

```bash
# 1. Install the one dependency
pip install -r requirements.txt

# 2. Pull the model and make sure Ollama is running
ollama pull llama3.2
ollama serve        # skip this if Ollama is already running in the background

# 3. Run the evaluation
python main.py
```

It takes a few minutes. Each request has a 120-second timeout, so a slow machine won't hang forever.

## What's in the folder

| File | What it's for |
|---|---|
| `main.py` | The whole evaluation, top to bottom |
| `golden_set.json` | The 30 questions, expected answers, keywords and sources |
| `baseline_results.csv` | Output from the latest run |
| `requirements.txt` | Just `requests` |

## The golden set

Each entry looks like this:

```json
{
  "id": "Q018",
  "question": "What is greedy decoding?",
  "expected_answer": "Greedy decoding selects the next token with the highest probability at each generation step.",
  "keywords": ["highest", "probability", "next token"],
  "source": "https://huggingface.co/docs/transformers/en/generation_strategies"
}
```

- `expected_answer` is the reference answer, there for a human to read when reviewing.
- `keywords` is what the script actually checks.
- `source` is where the answer comes from (Hugging Face docs, the Gemini API docs, the original Transformer and RoPE papers, SentencePiece).

Want to add a question? Add another entry to the JSON file with the same fields. No code changes needed.

## How scoring works

For each question, the script lowercases the answer and checks whether each keyword appears in it:

```
score = matched keywords / total keywords × 100
```

- **PASS**: score is 60 or above
- **REVIEW**: score is below 60, so a human should take a look
- **ERROR**: the request failed (Ollama not running, timeout, etc.)

I used "REVIEW" instead of "FAIL" on purpose. Keyword matching is a blunt tool, and a low score doesn't always mean a wrong answer (see limitations below).

## Baseline results (llama3.2, v0.1)

| | |
|---|---|
| Questions | 30 |
| Passed | 13 |
| Needs review | 17 |
| Errors | 0 |
| Average keyword coverage | 53.3% |

A few things stand out:

- **Strong on the basics.** Definitions like WordPiece, BPE vs WordPiece, embeddings and token ID vs embedding all scored 100%.
- **Weakest on specifics.** Q005 (SentencePiece), Q008 (token ratio), Q011 (API cost), Q016 (next-token prediction) and Q028 (sinusoidal encodings) all scored 0%.
- **Cost and API questions struggle.** The model tends to give general explanations instead of the exact framing the question was based on.

The full breakdown, including which keywords were missed for each question, is in `baseline_results.csv`.

## Limitations (worth knowing before you trust the numbers)

- **Keywords aren't meaning.** A correct answer worded differently, say "chops text into pieces" instead of "splitting", loses points. A wrong answer that happens to use the right words gains them. Some of the 0% scores may be fine answers phrased differently, so read the REVIEW rows before drawing conclusions.
- **Substring matching is loose.** `"one"` would match inside `"someone"`. For the current keyword list this rarely matters, but it's good to know.
- **The questions are sent bare.** There's no system prompt and no context, so the model answers from memory alone.
- **30 questions is a small sample.** Good for a baseline, not for firm claims.
- **Temperature 0 is repeatable, not guaranteed identical.** Small differences between runs can still happen across machines or Ollama versions.

## Ideas for what's next

- Score with an LLM judge or embedding similarity alongside keywords
- Add retrieval (RAG) using the `source` links and compare against this baseline
- Try other models by changing `MODEL_NAME` at the top of `main.py`
- Bump the release tag (`v0.2`, ...) so results from different runs stay easy to tell apart

## Configuration

Everything you'd want to tweak is at the top of `main.py`:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"
INPUT_FILE = "golden_set.json"
OUTPUT_FILE = "baseline_results.csv"
```

The CSV is saved with a UTF-8 BOM (`utf-8-sig`), so it opens cleanly in Excel.
