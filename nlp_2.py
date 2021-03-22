from textblob import TextBlob
import nltk

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())