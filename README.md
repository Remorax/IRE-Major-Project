# README

The purpose of this project is to propose and implement a framework for ontology enrichment, visualization and validation. As part of this pipeline, the first stage involves the creation of ***OntoEnricher***, an LSTM model to extract concepts and relationships from a text corpus. The extracted concepts and relationships, along with the seed ontology, are fed to ***OntoViewer***, a WebVOWL-based ontology visualization and validation tool. This tool allows the ontology validator to accept/reject the newly extracted concepts and relationships, incorporates crowdsourcing quality control mechanisms and uses them to make the final decisions about accepting/rejecting these relations. These decisions are then written to the ontology and saved as a final owl file. We do a short survey of the literature on crowdsourcing and quality control mechanisms and post that, incorporate quality control mechanisms by assessing the credibility of the ontologist based on their social media (particularly Twitter) content. In line with this, we propose ***TweetCredibility***, a model that uses ML to predict a credibility score for an account based on their tweets and followers. As the first step towards implementing this, we implement a model to predict the domain of tweets given a twitter handle.

  

We thus divided our work into the following subprojects as follows:

1.  OntoEnricher, the LSTM-based model to extract concepts and relationships (done by Vivek)
    
2.  OntoViewer, a WebVOWL based tool to visualize and validate ontologies (done by Harish)

3. TweetCredibility,  to predict the credibility of a twitter account based on posts and followers (done by Apoorav)