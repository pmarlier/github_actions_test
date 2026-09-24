import sys
import os

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(WORKING_DIR))

import pandas as pd
from src.main import load_data

def test_is_existing_data_file():
    assert os.path.isfile("data/regularite-mensuelle-tgv-aqst.csv")

def test_load_data():
    loaded_data = load_data()
    assert isinstance(loaded_data, pd.DataFrame)