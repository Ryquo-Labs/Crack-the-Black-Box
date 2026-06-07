# Crack the Black Box

A Streamlit classroom activity for teaching **black-box AI**, **pattern recognition**, **evidence-based testing**, and **explainability**.

Students test a mysterious AI system that only returns **YES** or **NO**. Their goal is to collect evidence and infer the hidden rule.

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
