#! /bin/bash

echo "*****Executing command: python createDB.py"
python createDB.py

echo "*****Executing command python createTables.py"
python createTables.py

echo "*****Executing command python loadData.py"
python loadData.py