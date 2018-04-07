
# Fishing Fisher's Flower Figures - An exploration of the Iris Dataset - update

## Helen O’Shea
## Galway Mayo Institute of Technology - Data Analytics - Programming and Scripting
## Date: April 2018
## The Iris Data and Data Analytics
### Background
The Iris data set, also known as Fisher or Anderson’s Iris flower data set, was popularised by the statistician Ronald Fisher in his 1936 paper [“The use of multiple measurements in taxonomic problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x). It was collected by the American botanist, Edgar Anderson in 1935 yet remained unpublished till Fisher published his paper which used this data set. Anderson’s data consists of fifty samples each, from the three species of Iris, Iris setosa, Iris virginica and Iris versicolor. Two of the species, Iris virginica and Iris setosa, were sampled from the same region and used by Fisher to illustrate discriminant functions. In addition Fisher extended this method to investigate Randolph’s hypothesis that the third species, Iris versicolor, was a hybrid of the Iris virginica and setosa species (ibid). Anderson recorded species type and measured the length and width of their petals and sepals in centimetres. The petals are the inner flower while the sepals are the outer structures as seen here 

![Sepal/petal differences in Iris](/img/icon_iris.png)
Identifying sepal from petals in Iris versicolor

 
You can see images of the various Iris species used in Fisher's Data Set below.

![Iris Setosa](/img/setosa[220].jpg) 
Iris Setosa


![Iris Versicolor](/img/versicolor.jpg) 
Iris Versicolor


![Iris Virginica](/img/virginica.jpg) 
Iris Virginica

This gives the data set five dimensions,  namely 4 one dimensional measures in centimetres, sepal length (sepalL), sepal width (sepalW), petal length (petalL),  petal width (petalW); And one categorical dimension of Iris species (name). This project used the version of the Iris data hosted at [UCI machine learning repository](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)This version contains [two errors](https://www.researchgate.net/profile/Ludmila_Kuncheva/publication/3335819_Will_the_real_Iris_data_please_stand_up/links/55d66ff908ae9d65948bdb42/Will-the-real-Iris-data-please-stand-up.pdf) from Anderson’s original data which were not amended in the analysis.

Fisher’s analysis investigated if petal/sepal measurements alone could predict which species of Iris the sample came from. This makes the data useful in exploring machine learning methods, statistical techniques and data visualisation. The Iris data set is well known, and often cited. Iris Data Set hosted at [UCI notes](https://archive.ics.uci.edu/ml/datasets/iris) 99 citations with citations from as recently as 2005. The set has historical significance, as does Fisher, and is widely recognised in computer science. Fisher’s Iris data set is often used as a learning tool in data analytics. The data is small enough to be manageable for beginners yet sufficiently challenging in what it can reveal. Its historical use means that there is a body of work and continuity based on it, which can be used as a benchmark to test program results and explore data analytic methods. 
## Project Layout
## Folders

This project consists of subfolders containing 
1. images [/img/](/img/)
2. data [/data/](/data/)
3. python scripts [/pyscripts/](/pyscripts/)
4. graphics [/graphs/](/graphs/)
5. research [/research/](/research/)
6. and the project write up project report.docx or project report.pdf

### Images
Images of the flowers can be found in the folder named [img](/img/) 

### CSV files

A csv file of the Iris Data Set can be found in the folder here, (/data/iris.csv) named data. Also present in this folder are descriptive results from the analysis (python script - desc.py) found [here](/pyscripts/desc.py) in /pyscripts/desc.py
* desc_se.csv contains the descriptive results from the Iris Setosa
* desc_ve.csv contains the descriptive results from the Iris Versicolor
* desc_vi.csv contains the descriptive results from the Iris Virginica
* description.csv contains the descriptive results from all 3 Iris species


### Python Scripts
The python scripts are found [here](/pyscripts/) in the folder pyscripts
* desc.py contains the code to calculate descriptive statistics for the 3 Iris species
* infer.py contains the code to calculate inferential statistics (t-tests or Welch's t-test depending on the indpendence of the variances under investigation)
* visu.py contains the code to visualise the data, results of which are saved in the [folder graphs](/graphs/)
* test.py contains code extracts for testing purposes
* nn.py was to contain some code on machine learning - but not really relevent for data analysis so maybe drop it. 

### Visualisations
The visualisations produced from [visu.py](/pyscripts/visu.py) are listed below.
* Andrews Curves
	* andrewscs.jpg
* Box Plots 
	* bp2petalL.jpg
	* bp2petalW.jpg
	* bp2sepalL.jpg
	* bp2sepalW.jpg
	* bppetalL.jpg
	* bppetalW.jpg
	* bpsepalL.jpg
	* bpsepalW.jpg
* KDE Kernel Desnity Estimation graphs
  * kdepetalL.jpg
  * kdepetalW.jpg
  * kdesepalL.jpg
  * kdesepalW.jpg
* Pair Plots
  * histogram along diagonal
   * pairploth.jpg
  * kde curve along diagonal
   * pairplotk.jpg  
* Parallel Coordiante Curve
 * parac.jpg
* Rad
  * rad.jpg - add desc in later
* QQ Plots - add desc in later
 * setosa_qqplot.jpg  - delete this one
 * setosaL_qqplot.jpg - and this
 * setosaW_qqplot.jpg - add this
 * setosaPL_qqplot.jpg
 * setosaPW_qqplot.jpg
 * setosaSL_qqplot.jpg
 * setosaSW_qqplot.jpg
 * versicolor_qqplot.jpg
 * versicolorL_qqplot.jpg
 * versicolorPL_qqplot.jpg
 * versicolorPW_qqplot.jpg
 * versicolorSL_qqplot.jpg
 * versicolorSW_qqplot.jpg
 * virginica_qqplot.jpg
 * virginicaL_qqplot.jpg
 * virginiaPL_qqplot.jpg
 * virginicaPW_qqplot.jpg
 * virginicaSL_qqplot.jpg
 * virginicaSW_qqplot.jpg
* Red line thingy test for normality
 * setosapetalL.jpg
 * setosapetalW.jpg
 * setosasepalL.jpg
 * setosasepalW.jpg
 * versicolorpetalL.jpg
 * versicolorpetalW.jpg
 * versicolorsepalL.jpg
 * versicolorsepalW.jpg
 * virginicapetalL.jpg
 * virginicapetalW.jpg
 * virginicasepalL.jpg
 * virginicasepalW.jpg
* Scatter plots
 * Labelled
  * snpetal2.jpg
  * snsepal2.jpg
 * Unlabelled
  * snpetal.jpg - seaborn
  * snsepal.jpg
  * spsepal.jpg - pandas
* Violin Plots
 * vppetalL.jpg
 * vppetalW.jpg
 * vpsepalL.jpg
 * vpsepalW.jpg	

### Research 
This [folder](/research/) contains some papers used to research the project. 

### Project Report
The full write up of the project can be found [in word format here](project%20report.docx) and [in pdf format here] (project%20report.pdf). 


