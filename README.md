# Crack the Black Box

A student-facing Streamlit classroom activity for teaching **black-box AI**, **pattern recognition**, **evidence-based testing**, and **explainability**.

Students test a mysterious AI system that only returns **YES** or **NO**. Their goal is to collect evidence and infer the hidden rule.

## Activity Concept

This activity is designed for an introductory AI class. It helps students understand that AI systems can learn or follow patterns that may not match what humans expect.

The hidden rule is implemented internally in the app:

> The black box says **YES** if the English word contains the letter **“a.”**

Do not reveal this rule until the end of the activity.

## Features

- Student-facing interface
- No teacher controls shown
- No API key required
- Clickable input cards
- Hidden YES/NO rule
- Evidence board showing tested inputs
- Reflection questions
- Clean modern UI
- Works locally or on Streamlit Community Cloud

## File Structure

```text
crack_the_black_box_project/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── config.toml
```

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal.

## Streamlit Cloud Deployment

1. Upload this project to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Create a new app.
4. Select your repository.
5. Set the main file path to:

```text
app.py
```

6. Deploy.

No secrets or API keys are needed.

## How to Run the Activity

Tell students:

> You are testing a mysterious AI system. It only answers YES or NO. Your mission is to collect evidence and figure out the hidden pattern.

Suggested flow:

1. Students choose input cards to test.
2. The class observes the YES/NO outputs.
3. Students propose possible rules verbally.
4. Keep testing until a proposed rule explains both YES and NO examples.
5. Reveal the hidden rule at the end.

## Suggested Debrief Questions

- Did the black box use the pattern you expected?
- How many tests were enough to feel confident?
- Why can hidden patterns be risky in real AI systems?
- What would make this system more explainable?

## Teaching Takeaway

AI can find patterns, but not always the pattern humans want. That is why we need evidence, testing, and explainability.

## Customizing the Activity

To change the input cards, edit the `INPUTS` list in `app.py`.

To change the hidden rule, edit this function in `app.py`:

```python
def black_box_rule(word: str) -> str:
    return "YES" if "a" in word.lower() else "NO"
```

Example alternative rules:

```python
# YES if the word has more than 5 letters
return "YES" if len(word) > 5 else "NO"

# YES if the word starts with a consonant
return "YES" if word[0].lower() not in "aeiou" else "NO"

# YES if the word contains the letter "o"
return "YES" if "o" in word.lower() else "NO"
```

## License

This classroom activity is free to use and modify for educational purposes.
