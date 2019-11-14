# Ontology Determiner

# Requirements:
- python3 and pip are prerequisites

#SetUp:
- go to src folder and run `pip install -r requirements.txt`, incase of any missing modules , please report

#Data Requirements:
Place your seed file in src/onto_app/data/input as .owl file
Place your new relations and concepts file in src/onto_app/data/input as .txt file
The name of both .owl file and .txt file should be the same 


#Ontology Viewer
- go to 'onto_app' directory and set `FLASK_APP=routes.py` and `FLASK_ENV=development`
- start the server by flask run
- accept or reject relationships by loggin in with twitter account

#Final Ontology file
-remove the files in /src/data/final
- run python3 get_verified_ontology.py <file_name>
- final ontology is stored in 

#Changing the Source code of WEBVOWL
To see how to change the source code of WEBVOWL go to src/WEBVOWL and read the readme and follow the instructions.


