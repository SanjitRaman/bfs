import csv
from pathlib import Path


def read_my_csv(file_path: Path):
    if(not file_path.exists()):
        raise FileNotFoundError
    with open(file_path) as f:
        
