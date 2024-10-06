# momentum
Setup
1. Create environment 
```
$ python3 -m venv vnev

# windows cmd 
$ venv\Scripts\activate

# mac terminal 
$ source venv/bin/activate
```
2. Install Requirements
```
$ pip install -r requirements.txt
```
3. Download *Security Daily* data (23.33 GiB) from *Wharton Research Data Services*
    1. CRSP > CRSP/Compustat Merged > Security Daily
    2. Select Start Date [2000-01-01]
    3. Select End Date [2024-10-04]
    4. Select [Search Entire Database]
    5. Select "All" for Query Variables 
    6. Download as .csv
    7. Place .csv in "data" folder 
4. Download *Fundamentals Quarterly* data (0.84 GiB) from *Wharton Research Data Services*
    1. CRSP > CRSP/Compustat Merged > Fundamentals Quarterly
    2. Select Start Date [2000-01-01]
    3. Select End Date [2024-10-04]
    4. Select [Search Entire Database]
    5. Select "All" for Query Variables
    6. Download as .csv
    7. Place .csv in "data" folder 
---

