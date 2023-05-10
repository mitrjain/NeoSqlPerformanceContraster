#! /bin/bash

echo "*****Executing command: python createDB.py"
python sql-dbms/createDB.py

echo "*****Executing command python createTables.py"
python sql-dbms/createTables.py

echo "*****Executing command python loadData.py"
python sql-dbms/loadData.py