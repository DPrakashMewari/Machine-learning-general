## Decision Tree Classification Algorithm 

Decision Tree is supervised learning that can be used for both classification and regression

# Why we use Decison trees?
Decision Tree Usually Mimic thinking ability while making a decison so it is easy to understand.

# Decision tree Contains :
<li> Root Node : Root node is from where the decison tree starts.</li>
<li> Leaf Node : Leaf Node are the final output node</li>
<li> Splitting : Splitting is the process of dividing the decision node/root into subnode based on some condition </li>
<li> Pruning : It is the process of removing unwanted branches from the tree </li>
<li> Parent/Child Node : The root Node is Parent and other are child nodes. </li>

# How Decision Tree Algorithm Work ?

<li> Step 1. Begin from root node ,say d which has full data </li>
<li> Step 2. Find the best attribute selection measure </li>
<li> Step 3 . Divide the d into subsets that contain possible values for the best attributes </li>
<li> Step 4 . Generate a Decison tree which contain the best attribute </li>
<li> Step 5 . Recursively make a new decison tree using the subsets of the dataset created - Step 3 Continue the process until a stage is reached where you cannot further classify the node and called the final node or leaf node.</li>

# Attribute selection Measures :
Information Gain: It calculates How much information provides about the class

Entropy : Entropy is Metric to measure the impurity in given attribute.

Gini Index : It is also a measure of impurity or purity while creating a decison tree.It create binary splits.


