#Homework 1 - Yüsra DAĞILMA

#1) How would you define Machine Learning?

	# It is a sub-branch of artificial intelligence.Machine learning is gaining skills equivalent to human intelligence without programming computers.

#2) What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.

	# Supervised learning --> Your class number is certain, you have trained data.It tries to make a new estimate by giving input and output values.
		# Breast cancer research, benign or malignant tumors
		# Real estate company research, finding the relationship between house size and house prices and determining the price for a new house to be sold
		# Estimating the age of a person when given a picture
	# Unsupervised learning --> Creating certain groups with the Clustering method according to the characteristics of the data you have.
		# It is tried to discover whether people who buy product X tend to buy Y product as well.
		# Marketers discover groups of customers based on interests to develop different marketing programs
		#People can analyze large volumes of emails that they cannot analyze and reveal features and patterns that indicate spam and improve this feature over time.

#3) What are the test and validation set, and why would you want to use them?
	# Validation dataset is a sub-dataset used to evaluate the performance of the model obtained during the training phase.
	# In addition, this dataset provides a test platform to determine which model is good and to adjust the optimal parameters for the models.Not all models require a validation data set.
	
	# The Testing Dataset (which has never been seen in subsets of the data set) is used to evaluate the future performance of the model.
	# If the results in the test data are worse than the training stage, it is the case that we are faced with overfitting.

#4) What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?
	# Duplicate Values : In most cases, the duplicates are removed so as to not give that particular data object an advantage or bias, when running machine learning algorithms.
	# Imbalanced Data : An Imbalanced dataset is one where the number of instances of a class(es) are significantly higher than another class(es), thus leading to an imbalance and creating rarer class(es).
	# Missing Values : Eleminate missing values / Filling with mean or median
	# 
	#
	
#5) How you can explore countionus and discrete variables?

#6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)
