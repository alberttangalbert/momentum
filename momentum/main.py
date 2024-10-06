import pandas as pd 
import os 
from decouple import config 

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    fundementals_quarterly_file_path = os.path.join(BASE_DIR, config('FUNDAMENTALS_PATH'))
    fundementals_quarterly_raw = pd.read_csv(fundementals_quarterly_file_path)
    print(fundementals_quarterly_raw.head(10))

if __name__ == "__main__":
    main()