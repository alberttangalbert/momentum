# momentum
---
Setup
1) Create environment 
```
$ python3 -m venv vnev

# windows cmd 
$ venv\Scripts\activate

# mac terminal 
$ source venv/bin/activate
```
2) Install Requirements
```
$ pip install -r requirements.txt
```
3) Download *Security Daily* data (23.33 GiB) from *Wharton Research Data Services*
    a. CRSP > CRSP/Compustat Merged > Security Daily
    b. Select Start Date [2000-01-01]
    b. Select End Date [2024-10-04]
    c. Select [Search Entire Database]
    d. Select "All" for Query Variables 
    e. Download as .csv
    f. place in "data" folder 
4) Download *Fundamentals Quarterly* data (0.84 GiB) from *Wharton Research Data Services*
    a. CRSP > CRSP/Compustat Merged > Fundamentals Quarterly
    b. Select Start Date [2000-01-01]
    b. Select End Date [2024-10-04]
    c. Select [Search Entire Database]
    d. Select "All" for Query Variables 
    e. Download as .csv
    f. place in "data" folder 
---

