import nltk

class Analyzer():
    """Implements sentiment analysis."""
    def __init__(self, positives, negatives):
        self.positives=positives
        self.negatives=negatives

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        text.lower
        sp=0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            token.lower
            for str in self.positives:
                if str == token:
                 sp+=1

            for str1 in self.negatives:
                if str1== token:
                 sp-=1
        return sp
