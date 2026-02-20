import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
