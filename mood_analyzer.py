import re
from typing import List, Optional
from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""
"""
Preferred to build a semi high-quality, minimal-code web interface, using Streamlit.
Will add funciinal logic from MoodAnalyzer to this file, and use Streamlit to create a simple UI for users to input text and see the predicted mood.
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """
    def preprocess(self, text: str) -> List[str]:
        # Basic regex to remove any punctuation and lowercase the text.
        cleaned = re.sub(r'[^\w\s]', '', text.lower())
        return cleaned.split()

    def __init__(self, positive_words=None, negative_words=None):
        self.positive_words = set(w.lower() for w in (positive_words or POSITIVE_WORDS))
        self.negative_words = set(w.lower() for w in (negative_words or NEGATIVE_WORDS))

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        # Security/Sanitization: Remove punctuation to prevent bypasses and lowercase for consistency.
        cleaned = re.sub(r'[^\w\s]', '', text.lower().strip())
        return cleaned.split()

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        tokens = self.preprocess(text)
        score = 0
        negators = {"not", "never", "no", "neither", "nor"}

        for i, token in enumerate(tokens):
            multiplier = 1
            # Logic: If the previous word was a negator, the sentiment should be flipped
            if i > 0 and tokens[i-1] in negators:
                multiplier = -1

            if token in self.positive_words:
                score += (1 * multiplier)
            elif token in self.negative_words:
                score -= (1 * multiplier)
        return score
            
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        #   2. Loop over the tokens.
        #   3. Increase the score for positive words, decrease for negative words.
        #   4. Return the total score.
        #
        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").
        pass

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        score = self.score_text(text)
        if score > 0: return "positive"
        if score < 0: return "negative"
        return "neutral"
    
    # Logic: I have the negation check to ensure that "not happy" results in a negative (-1) score instead of +1
    # Security: Usineg re.sub and strip(), is to ensure that basic script inkjection or weird/unusual
      # characters are neutralived during preprocessing.
    # Efficiency: the scoring is calculated in a single 0(n) pass through the tokens.
       
       
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return "positive" if the score is above 0.
        #   3. Return "negative" if the score is below 0.
        #   4. Return "neutral" otherwise.
        pass

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        score = self.score_text(text)
        label = self.predict_label(text)
        return f"Model predicted '{label}' with a net score of {score}."