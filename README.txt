Author: Jack Volonte
Date: 10/30/2022
Description: These files create histograms from images, perform a SVM model creation, and validation. A PCA of the model, and finds the accuracy of the resulting model's
using n # of components.

File Manifest:
	AurNonNormalizedSVMHistograms.txt
	AurSVMHistogramsNoFormat.dat
	AurSVMHistogramsNoFormat.txt
	hw4writeup_JackVolonte.pdf
	new_data_after_pca.txt
	PCAofHistogramData
	SVMWriteHistogramsToFile
	./svm_light:
		./svmModelThing:
			after_pca_n5
			after_pca_n10
			after_pca_n20
			after_pca_n50
			after_pca_n150
			after_pca_n200
			after_pca_n768
			histo_training
			histo_val
			model
			predictions
	README.txt


THESE FILE NAMES ARE NOT MEANT TO BE RUN - if run, this will ruin the histogram data converted before packaging this homework:
	PCAofHistogramData
	SVMWriteHistogramsToFile

These can be run, as all of the information contained for the SVM is found in the svm_light folder, but these will change the histogram containing files
within the main folder of the project. These two runnable files will not show anything useful, and are merely ways to format the data in a way the svm and pca can read.


USE OF FILES:
	Enter the terminal from the svm_light terminal, use the following commands to run the SVM learning and classification of the various 
testing data files:
	./svm_learn svmModelThing/histo_training.dat svmModelThing/model
	./svm_classify svmModelThing/histo_val.dat svmModelThing/model svmModelThing/predictions

	The histo_training.dat can be replaced with any of the 'after_pcan#' files containing the information from runnning a PCA on that n # of 
components, then using the same second command the accuracy will be produced and printed to terminal. 

	new_data_after_pca.txt - contains data from PCA after running PCAofHistogramData
	AurNonNormalizedSVMHistograms.txt - contains data manually moved after running SVMWriteHistogramsToFile
	AurSVMHistogramsNoFormat.dat - contains data manually moved after running SVMWriteHistogramsToFile
	AurSVMHistogramsNoFormat.txt -  contains data manually moved after running SVMWriteHistogramsToFile

	The after_pca_n5 & hist_training files are for use with the ./svm_learn command, the ./svm_classify command used the histo_val as validation data. 

	/svm_light:
		./svmModelThing:
			after_pca_n5
			after_pca_n10
			after_pca_n20
			after_pca_n50
			after_pca_n150
			after_pca_n200
			after_pca_n768
			histo_training
			histo_val
			model
			predictions

For any questions, please contact:
    volonte22@up.edu
    on Teams,
    volonte22@up.edu
    or by phone,
    503-980-8100

