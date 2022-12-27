# SUBRENT
Subrental financial reports

## INSTALL
```
pip3 install -r requirements.txt

# Create/reset database
python3 subrent.py reset

# Import example data from json file
python3 subrent.py import examples/data.json
```

## USAGE
```
python3 subrent.py -h  # Get help
python3 subrent.py report  '2022-12-05'  # Get report for the day
```