# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

---- BEGIN ----
- Model Type: A hybrid system comparing a Rule-Based (Dictionary) classifier and a Machine Learning (Logistic Regression) classifier.

- Intended Purpose: To classify short social media-style posts into four moods: Positive, Negative, Neutral, or Mixed.
---- END ----
**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

## 2. Data

### --- BEGIN ---
- Dataset Description: Started with 6 base posts. Expanded to 11+ posts including slang (e.g., "absolute fire", "mid") and emojis (🔥, 💀).

- Labeling Process: Manually labeled by the developer.

- Key Characteristics: Contains examples of negation ("not happy") and mixed sentiment ("tired but hopeful") to test the limits of keyword-matching logic.
### --- END ----

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

## 3. How the Rule Based Model Works (if used)

### ----- BEGIN ----
- Rule-Based: Uses mood_analyzer.py. It counts keywords from a predefined list. I implemented Negation Handling, which looks for words like "not" or "never" before a keyword to flip the sentiment score (e.g., "not happy" = -1).

- Machine Learning: Uses ml_experiments.py. It uses a "Bag of Words" approach where the model learns which words correlate with which labels from the SAMPLE_POSTS.
### ---- END ----
**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

## 4. How the ML Model Works (if used)

### ---- BEGIN ----
- Rule-Based Accuracy: Moderate. It succeeds on simple sentences but is "blind" to any positive/negative words not explicitly in the dictionary (like "hopeful").

- ML Accuracy: High on training data, but sensitive to the size of the dataset.

- The "Fail" Case: The sentence "Feeling tired but kind of hopeful" originally failed in the Rule-Based model because "hopeful" was missing from the POSITIVE_WORDS list, resulting in a Negative score.
### ---- END ----

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

### ---- BEGIN ----
- Sarcasm: The model struggles with sarcasm (e.g., "I love getting flat tires").

- Bias: The dataset is currently optimized for English-speaking social media users. It may misinterpret dialects or cultural slang not included in the training set.

- Security: Input is sanitized of punctuation, but the model could still be "tricked" by creative spelling (e.g., "h4ppy").
### ---- END ----
**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
