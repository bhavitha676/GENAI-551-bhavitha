# Autoregressive Text Generator

A small Python script that generates text one word at a time. I built it to understand the basic idea behind how language models like ChatGPT work, without needing any heavy libraries or math.

It's tiny (about 50 lines) and uses only Python's built-in `random` module.

## What it does

You give it a start word, like `the`, and it keeps predicting the next word until it hits a limit. Each word it picks becomes the input for the next pick. That feedback loop is what "autoregressive" means.

Example output:

```
Generated Text:
the student studied hard and passed examination the student studied well
```

Your output will be different every time, because the next word is chosen randomly.

## How to run it

You need Python 3 installed. No other setup.

1. Save the code as `autoregression.py`
2. Open a terminal in that folder
3. Run:

```bash
python autoregression.py
```

On Windows you can also use `py autoregression.py`, and on Mac/Linux `python3 autoregression.py`.

## How it works

**1. Build the "model."**
The training text is split into words. For every word, the script records which words came right after it. For example, in this text "the" is followed by "student" four times and "teacher" twice, so the model stores:

```
"the" -> [student, student, student, student, teacher, teacher]
```

There's no real training here, it's just counting.

**2. Generate text.**
Starting from your word, the script looks up its list of followers and picks one at random. Since common followers appear more often in the list, they get picked more often. Then it repeats with the new word.

```
the -> student -> studied -> hard -> and -> passed -> ...
```

It stops when it reaches the word limit, or if the current word has no known follower.

## Try it yourself

Near the bottom of the file, change this line:

```python
result = generate_text("the", 10)
```

- Change `"the"` to another word from the training text, like `"students"` or `"teacher"`
- Change `10` to make the output longer or shorter
- Edit the `text` variable to train it on your own sentences

The start word has to appear in the training text. If it doesn't, you'll just get that one word back.

## Known limitations

- **It only remembers one word.** This is called a bigram model, and it's why sentences wander off and mix together.
- **Line breaks are ignored.** The text is split into one flat list of words, so a word at the end of one line can be followed by the first word of the next. That's why you'll see things like `passed examination the student...`
- **It can only repeat what it has seen.** It can't come up with word pairs that aren't in the training text.

## How this compares to real language models

The loop is the same: predict the next word, add it, repeat. What's different is how the prediction is made.

| This script | Real language models |
|---|---|
| Looks at the last 1 word | Looks at thousands of previous words |
| Uses counted examples | Uses a neural network with billions of parameters |
| Only repeats seen pairs | Can handle sentences it has never seen |

## Ideas for next steps

- Treat each line as its own sentence so generation can stop naturally
- Look at the last two words instead of one (a trigram model)
- Train it on a longer text, like a book chapter
- Show the actual probabilities instead of using `random.choice`
