# We Know Boosting is Ensemble technique that attempts to create  strong classifier from a number of weak classifier.

# So Here is our First Boosting Technique : 

- AdaBoost ::

<p>
Adaboost is Nothing but N number of Forest {Group of Trees}
called Strumps. Adaboost will put more weight to Difficult classifier rather then those were already handled well.
 Adaboost is used in both regression and classification.
</p>

<p> Adaboost Algorithm from Scratch : </p>

- 1. Assign Equal Weights to all observations :Intially assign same weights to each records in the dataset
            <center>Same Weight = 1/N</center>
 
- 2. Classify Random Sample Using Strumps :
it Fit the Model to Random Samples and predict classes for the orignal data


- 3. Calculate Total Error : 
Total Error is Nothing But the sum of weight of Misclassified Records 
Total error = Weights of Misclassfied records
{Total error : Will be Always Between 0 [Represents Perfect or correct] and 1[ Weak Misclassification ]}

- 4. Calculate Performance of the Stump : 
  Performace of the strump(alpha) = 1/2 ln(1- Total error/Total Error)

- 5. Update Weights : Based on the Performance of Strump (alpha) update the weights

- 6. Update Weights in Iteration : Used the Normalised weight and make the second strump in the forest.Create a new dataset of same size of orignal dataset .Repeat 2 to 5 steps again by updating the weights of particular number of iteration.


- 7. Final Prediction : Final Prediction is Done By obtaining the sign of weighted sum of final predicted value .


<span> Pros : </span>
<li> It is Fast simple and easy to program </li>
<li> Boosting shown it is robust with overfitting </li>


