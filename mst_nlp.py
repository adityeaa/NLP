import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

story = """
Once upon a time in a quaint village nestled between lush green hills, there lived a young girl named Lily. She was known for her wild imagination and adventurous spirit. Every day after completing her chores, Lily would wander into the forest that bordered the village, eager to explore its mysteries.
One sunny afternoon, as Lily roamed deeper into the woods than usual, she stumbled upon a hidden glade blanketed with the most vibrant flowers she had ever seen. Mesmerized by their beauty, she started weaving a garland with them, humming a tune her grandmother had taught her. Lost in her reverie, Lily didn't notice the time slipping away until dusk began to cast long shadows across the glade.
Startled, Lily realized she was lost. Panic crept into her heart as darkness descended upon the forest. She called out for help, but only the echo of her voice answered her. With trembling hands, she tried to find her way back, but every path seemed unfamiliar in the dim light.
Just when despair threatened to consume her, Lily noticed a faint glow ahead. Heart pounding with hope, she followed the light until she reached a small clearing where an old, gnarled tree stood illuminated by a gentle, golden radiance. Beneath its branches sat a mysterious figure, hunched over a book.
Approaching cautiously, Lily called out, "Excuse me, sir. Can you help me find my way home?"
The figure looked up, revealing a kindly face framed by a long, silver beard. "Lost, are you, child?" he said with a gentle smile. "Fear not, for you have stumbled upon the home of the Forest Guardian. I am here to guide those who have lost their way."
Relief flooded Lily's heart as the Guardian offered her a seat beside him. With his guidance, she recounted her adventures in the forest, from the hidden glade to her desperate search for home. The Guardian listened intently, nodding in understanding.
"Ah, the forest is full of wonders and dangers alike," he mused. "But remember, every challenge is an opportunity for growth. Now, close your eyes and listen to the heartbeat of the forest."
Following his instructions, Lily focused on the sounds around her—the rustle of leaves, the chirping of crickets, the gentle breeze weaving through the trees. In that moment of stillness, she felt a deep connection with the woods, as if they were guiding her home.
When she opened her eyes, Lily found herself standing at the edge of the village, bathed in the warm light of dawn. Tears of gratitude welled in her eyes as she whispered a heartfelt thanks to the Forest Guardian.
From that day forward, Lily continued to explore the forest, but she did so with newfound respect and reverence for its mysteries. And though she never saw the Guardian again, she carried his wisdom in her heart, guiding her through every adventure life had in store.
"""

# Code for Tokenization
tokens = word_tokenize(story)
print("The tokens are as follows:\n")
print("\n")
print(tokens)

# Code for Stopwords removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

#  Code for Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("The lemmatized words are as follows:\n")
print("\n")
print(lemmatized_tokens)

# Code for segmentation
sentences = sent_tokenize(story)
print("The Segmentations are as follows:\n")
print("\n")
print(sentences)

# Code for frequency distribution
fdist = FreqDist(lemmatized_tokens)
print("Most common words and their frequencies:\n")
print("\n")
print(fdist.most_common(10))

# Removing all the punctuation marks present in the story
print("The story after the removal of all the punctuation marks is:\n")
story_cleaned = re.sub(r'[^\w\s]', '', story)

print(story_cleaned)

