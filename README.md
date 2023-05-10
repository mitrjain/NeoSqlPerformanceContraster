# Python client to intialise the SQL & Neo4j DBMS

The code implemented in this repository is a direct implementation of the research paper: https://dl.acm.org/doi/abs/10.1145/3568562.3568648

## Overall prerequisites
Extract the dataset in the ./dataset directory by executing the following command in the root directory:

`unzip data-science-for-good-careervillage.zip -d dataset`

OR 

manually unzip in a folder called dataset in the root directory

## Overall code organization/ directory structure
- `neo4j-dbms` : contains python scripts to load data into Neo4j database
- `sql-dbms` : contains python scripts to load data into sql database
- `initialise_neo4j.sh` : shell script to automate data loading process for Neo4j
- `initialise_sql.sh` : shell script to automate data loading process for MySQL
- `data-science-for-good-careervillage.zip` : compressed version of dataset

## Steps for Neo4j


Make sure you update the paths of the csv in the `neo4j/load_nodes.py` & `neo4j/create_relationships.py` in the bottom. I have use absolute paths as relative paths don't work in the cypher queries. 


1. Install [Neo4j Desktop](https://neo4j.com/download/)
2. Click on the 3 dots besides the big blue button, and then Settings. Paste the contents of `neo4j.conf` file.
3. Edit the username and password in the .env file
4. Create a database named `sample2`
5. Click the big blue button `Open` which will route you to Neo4j Desktop Client
6. Run the following command in the prompt `:server user add`. Set your Username & Password=and assign the role 'Admin'.
7. Install the dependencies using `pip3 install neo4j/requirements.txt`
8. Just run the initialise_neo4j.sh bash script which will will run the below 2 .py files. 
    a. Runs the `neo4j/load_nodes.py` which will create a node corresponding to each record in the CSV file.
    b. Runs the `neo4j/create_relationships.py` which will create relationships between nodes.

9. Run the following set of queries specified in the queries file and visualise the results visually on Neo4j Desktop Client. 
A fancier way to do it would be drag and drop the cypher query in the `neo4j/cypher_queries` folder one by one onto the Neo4j Desktop Client.

Post completion, a beautiful graph will emerge like the one below...

![image](./neo4j-dbms/images/schema.png)

## Steps for MySQL

### Pre-requisities to run this mysql-python-client
- Installed and running instance of MySQL server (tested on version 8.0.32)
- Python (tested on version 3.9.13)
- Python packages:
    - mysql-connector-python
    - python-dotenv
- all csv files of the dataset present in ./dataset directory

### Code organization/ Directory structure
- `sql-dbms/createDB.py` : python script to create the required datbase
- `sql-dbms/createTables.py` : python script to create the required tables
- `sql-dbms/createDB.py` : python script to load csv file data into tables

### Running the mysql-python-client
Steps to run this application
- Set up envornment varaibles file `.env` in the ./sql-dbms directory
```
DB_USER=""
DB_PWD=""
```
- Execute the following command

`./initialise_sql.sh`

The complete process of loading the data has been automated and progress updates are displayed on terminal

### Result
After successfully loading the daatset into MySQL the following databse will be created

![ER Diagram](https://user-images.githubusercontent.com/26086412/237060808-940d1ae2-9532-49a2-9b0b-73f8fc7d3a9e.png)

Workload Dsitribution: 


### Project Contributions :

- Project Selection Search and Discovery : Cajetan, Mit and Ashish shortlisted 3 papers and voted 
- BrainStorm and come up with Milestones :  Cajetan, Mit and Ashish 
- MySQL and Neo4j Installation and setup :  Cajetan, Mit and Ashish 
- Related Work / Literature Review : Ashish 
- Script to load data into MySQL : Mit 
- Script to load data into Neo4j : Cajetan
- Analysis of MySQL queries : Mit
- Analysis of Neo4j Cyphers : Ashish 
- Comparative analysis and inferencing conclusions : Ashish

- Demo : Cajetan, Mit and Ashish have presented
- IEEE Report :  Cajetan, Mit and Ashish / Responsible to write sections the same way as presented above

All members are working on having both configurations that are described  so that at the end we can see
3 different systems and tally if the benchmarks vary significantly. We have worked on asynchronous format
and any progress made was shared in a shared doc to avoid solving the same problems. Overall, in this
moment we were able to build and contribute significantly to the development progress and helping each other out in every step whenever required.

### Environment specifications
Following are the specifications of the environment on which this mysql-pyhton-client  was last executed/tested: 
- MacBook Air M1
- OS: Montery
- Memory: 16 GB
- MySQL version: Community Edition - 8.0.32
- Python version: 3.9.13


