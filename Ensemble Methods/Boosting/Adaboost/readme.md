1. Ensemble techniques are machine learning methods that combine multiple models to obtain better predictive performance. There are several types of ensemble techniques commonly used:

1. **Bagging**: Bagging stands for Bootstrap Aggregating. It involves training multiple models independently 
on different subsets of the training data, and then aggregating their predictions to make the final prediction.
An example of a bagging ensemble technique is the Random Forest algorithm, which combines multiple decision trees.

2. **Boosting**: Boosting is an iterative ensemble technique where models are trained sequentially, with each subsequent model 
focusing more on the misclassified instances by the previous models.
Boosting aims to improve the overall performance by giving more weight to difficult instances.
Examples of boosting algorithms include AdaBoost (Adaptive Boosting) and Gradient Boosting.

3. **Stacking**: Stacking, or stacked generalization, combines multiple models by training a meta-model to 
make predictions based on the outputs of the base models. The base models' predictions serve as 
input features for the meta-model. Stacking aims to leverage the strengths of individual models. 
An example of stacking is combining different classifiers like Random Forest, K-Nearest Neighbors,
and Logistic Regression to make the final prediction.

4. **Voting**: Voting ensemble techniques combine the predictions of multiple models by
taking the majority vote (for classification tasks) or the average (for regression tasks) to make 
the final prediction. There are different types of voting techniques such as hard voting (simple majority)
and soft voting (weighted average based on confidence scores). An example is the VotingClassifier in scikit-learn.


-    These are some of the commonly used ensemble techniques in machine learning. 
    Each technique has its own advantages and is suitable for different scenarios.
    By combining multiple models, ensemble techniques can often achieve better predictive performance
    compared to individual models.
    
