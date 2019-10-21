# README

## Project Structure

1. `results_regparser`: Consists of results from NE Regex Parser extraction followed by combinatorial matching. Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_regparser) 

2. `results_svo`: Consists of results from SVO triplet extraction followed by combinatorial matching. Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_svo) 

3. `results_pizza_dummy`: Consists of results from NE Regex Parser followed by combinatorial matching on pizza web corpus (https://www.webstaurantstore.com/article/101/types-of-pizza.html). Corresponds to the dataset given [here](https://github.com/Remorax/IRE-Major-Project/tree/master/OntoEnricher/src/LSTM-implementation/dataset/dataset_pizza_dummy) 

## Conclusions

1. Regex parser gives the best results. We get 78.5% accuracy on a mere 2000 training examples, which is a toy dataset we created to test the code. We intend on creating a much larger dataset of around 40000-50000 training examples and expect even better results.

2. SVO was only able to extract 3 True relations, out of which only one was True Positive. Thus we get an accuracy of 33.33%

3. The dummy pizza dataset was created to check if the LSTM model is able to successfully negatively label all the relations since they are unrelated with security domain. And as expected, all relations were classified as False (False Negative).