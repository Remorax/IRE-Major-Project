# README

## Project Structure

1. `dataset-creation`: Consists of code to create training data from the seed ontology and online sources like DBpedia, Wikidata and Wordnet. It consists of the following subdirectories:
		a. `files`: Various files created from the extraction of hypernyms and hyponyms from the online sources mentioned above
		b. `ontologies`: Security seed ontologies used for enrichment
		c. `wikiextractor` : Extract (and filter based on domain) articles in plain text from a wikipedia dump
2. `LSTM-implementation`: Consists of an LSTM trained on a wiki-dump corpus using the datasets created from scripts in  `dataset-creation`

## How to Run

To create the dataset:

1. Go to `dataset-creation`. 
2. To create training dataset, run `python3 extract_training_dataset.py`  to extract the untagged training corpus from online sources using the concepts in the seed ontologies.
3. To create testing dataset, substitute the `url` variable in `extract_testing_dataset.py`with the url you want to extract concepts and relationships from. `thresholdWord`is an optional parameter that can be used to filter relevant terms if the size of the testing dataset is too large.
4. Then, run `python3 extract_testing_dataset.py`  to extract testing dataset from the URL given above.
