# OntoEnricher

An LSTM-based model to extract concepts and relationships from a text corpus to enrich a seed ontology.

## Methodology:

1.  We extracted the concepts from the seed (security) ontology and prepare a list of terms


2.  We extract the hypernyms and hyponyms of each of these concepts from online Wiki databases like DBPedia, Wikidata and Wordnet and build a dataset that consists of rows of (concept, hypernym) or (hyponym, concept) records.
    

  

3.  Each of these rows are validated by a domain expert and we mark the row as True  if and only if the relations belong to the same domain as the seed ontology and also share a subclass/hypernymy relationship. Otherwise they are marked as False.
    

  

4.  We also added false negatives to our dataset to negatively score our models. For this, we extracted other relations from DBPedia apart from hypernymy and autotagged them as False.
    

  

5.  The above dataset of (concept, hypernym, label) or (hyponym, concept, label) relationships becomes our training dataset. The small dataset we created this way has 2155 training examples.
    

  

6.  We then proceed to construct our training corpus as follows:
    

	a.  For the domain “information security”, we extract all the terms in the Information Security category in the category box on this [page](https://en.wikipedia.org/wiki/Information_security)
	b.  Next, extract articles from the Wikipedia dump that contain one of the words from the above extracted list of terms.
  c.  These articles together form the training corpus
    

  

7.  The LSTM model uses the tagged training dataset and the corpus to learn the edge weights between every pair of noun phrases in a sentence. Edges that contain a hypernymy relationship get higher weights using path-based methods. The concepts get higher weights if they are related to Information Security domain, using distributional (word-embedding) methods. Thus we build an integrated (path-based + distributional) model that gives higher weights only to those relations that contain a hypernymy relationship AND are related to the information security domain.
    

  

8.  The next step is to build our testing dataset from the text corpus. This is done as follows:
    

	a.  First we implement [coreference resolution](https://github.com/huggingface/neuralcoref) on the text corpus as pre-processing. This is done to ensure that the entities being referred to in each sentence are noun phrases, making it easier to extract them for the purpose of building the testing dataset.
	    
	b.  Next, for each paragraph in the text corpus, we extract all the noun phrases in that paragraph using the NLTK NE Grammar parser and perform a combinatorial pair-wise matching of each extracted entity.
	    
	c.  After doing this for each paragraph, we get a testing dataset
    
	d.  Optionally, depending on the size of the document (and consequently, the size of the testing dataset), we filter out a few relations based on their similarity (or dissimilarity) to “cybersecurity”
    

  

9.  We then use the trained LSTM model to predict the labels of the relations in the testing dataset. We filter relations the model identifies as True and pass it as input to the next stage of the pipeline, [OntoViewer](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoViewer).

## Project Structure

There are two folders in this project
- [src](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src): which contains the entire code-base 
- [results](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/results): which contains the results and the predictions of the test we performed

Check their READMEs for more info about how to setup and run this project 
