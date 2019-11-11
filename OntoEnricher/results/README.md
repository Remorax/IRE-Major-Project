# README

## Project Structure

1. `results_regparser`: Consists of results from NE Regex Parser extraction followed by combinatorial matching. Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_regparser) 

2. `results_svo`: Consists of results from SVO triplet extraction followed by combinatorial matching. Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_svo) 

3. `results_pizza_dummy`: Consists of results from NE Regex Parser followed by combinatorial matching on pizza web corpus (https://www.webstaurantstore.com/article/101/types-of-pizza.html). Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_pizza_dummy) 

4. `results_multiclass`: Consists of results from NE Regex Parser followed by combinatorial matching on information security web corpus (https://tools.cisco.com/security/center/resources/virus_differences). Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_multiclass) 

## Conclusions

### Deliverable 2:

1. Regex parser gives the best results. We get 78.5% accuracy on a mere 2000 training examples, which is a toy dataset we created to test the code. We intend on creating a much larger dataset of around 40000-50000 training examples and expect even better results.

2. SVO was only able to extract 3 True relations, out of which only one was True Positive. Thus we get an accuracy of 33.33%

3. The dummy pizza dataset was created to check if the LSTM model is able to successfully negatively label all the relations since they are unrelated with security domain. And as expected, all relations were classified as False (False Negative).

### Deliverable 3:

1. Our model was able to perform significantly better than the state-of-the-art on ontology enrichment. It has higher accuracy (84%), great efficiency (running time: ~2-3 minutes) and requires minimal manual supervision once the trained model is obtained for a particular domain. 

2. We observed that concepts (or other concepts similar to them) which hadn’t been added in the training corpus (due to lack of validation due to time constraints) were misclassified. This sort of behavior is to be expected,  and can be fixed by improving the quality of our dataset.

3. As future work, we would like to experiment on a larger and more diverse training dataset, which we predict should give us better accuracies. 
