
# Fishing Fisher's Flower Figures - An exploration of the Iris Dataset - update

## Helen O’Shea
## Galway Mayo Institute of Technology - Data Analytics - Programming and Scripting
## Date: April 2018
## Project Report
The full write up of the project can be found [in word format here](project%20report.docx) and [in pdf format here] (project%20report.pdf)
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
* icon_iris.png picture illustrating sepal and petals in Iris Versicolor
* setosa.jpg - picture of iris setosa 
* setosa[220].jpg picture of resized iris setosa
* versicolor.jpg picture of iris versicolor
* virginica.jpg picture of iris virginica

### CSV files

A csv file of the Iris Data Set can be found in the folder here, (/data/iris.csv) named data. Also present in this folder are descriptive results from the analysis (python script - desc.py) found [here](/pyscripts/desc.py) in /pyscripts/desc.py
* desc_se.csv contains the descriptive results from the Iris Setosa
* desc_ve.csv contains the descriptive results from the Iris Versicolor
* desc_vi.csv contains the descriptive results from the Iris Virginica
* description.csv contains the descriptive results from all 3 Iris species
* s_p_desc.csv contains the descriptive results of the length to width ratio of the setosa petals
* s_s_desc.csv contains the descriptive results of the length to width ratio of the setosa sepals
* ve_p_desc.csv contains the descriptive results of the length to width ratio of the versicolor petals
* ve_s_desc.csv contains the descriptive results of the length to width ratio of the versicolor sepals
* vi_p_desc.csv contains the descriptive results of the length to width ratio of the virginica petals
* vi_p_desc.csv contains the descriptive results of the length to width ratio of the virginica sepals
* iris.csv contains the iris data downloaded from [uci](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)

### Python Scripts
The python scripts are found [here](/pyscripts/) in the folder pyscripts
* desc.py contains the code to calculate descriptive statistics for the 3 Iris species
* infer.py contains the code to calculate inferential statistics (t-tests or Welch's t-test depending on the indpendence of the variances under investigation)
* visu.py contains the code to visualise the data, results of which are saved in the [folder graphs](/graphs/)
* test.py contains code extracts for rough work and testing purposes and is not relevent to the final project.


### Visualisations
The visualisations produced from [visu.py](/pyscripts/visu.py) are listed below and availabe in folder [graphs](/graphs/).
* Andrews Curves
	* andrewscs.jpg
* Box Plots 
	* bp2petalL.jpg box plot of petal lengths with sample overlay
	* bp2petalW.jpg box plot of petal widths with sample overlay
	* bp2sepalL.jpg box plot of sepal lengths with sample overlay
	* bp2sepalW.jpg box plot of sepal widths with sample overlay
	* bppetalL.jpg box plot of petal lengths
	* bppetalW.jpg box plot of petal widths
	* bpsepalL.jpg box plot of sepal lengths
	* bpsepalW.jpg box plot of sepal widths
* Histograms of Iris data broken down by category 
  * hSPL.jpg Histogram of setosa petal lengths
  * hSPW.jpg Histogram of setosa petal widths
  * hSSL.jpg Histogram of setosa sepal lengths
  * hSSW.jpg Histogram of setosa sepal widths
  * hVePL.jpg Histogram of versicolor petal lengths
  * hVePW.jpg Histogram of versicolor petal widths
  * hVeSL.jpg Histogram of versicolor sepal lengths
  * hVeSW.jpg Histogram of versicolor sepal widths
  * hViPL.jpg Histogram of virginica petal lengths
  * hViPW.jpg Histogram of virginica petal widths
  * hViSL.jpg Histogram of virginica sepal lengths
  * hViSW.jpg Histogram of virginica sepal widthss
* Histogram of Full Iris   
 * iPL.jpg Histogram of Iris data petal lengths
 * iPW.jpg Histogram of Iris data petal widths
 * iSL.jpg Histogram of Iris data sepal lengths
 * iSW.jpg Histogram of Iris data sepal widths
* KDE Kernel Desnity Estimation graphs
  * kdepetalL.jpg kde plot of petal lengths
  * kdepetalW.jpg kde plot of petal widths
  * kdesepalL.jpg kde plot of sepal lengths
  * kdesepalW.jpg kde plot of sepal widths
* Pair Plots
  * histogram along diagonal 
   * pairploth.jpg pair plot with histogram along the diagonals
  * kde curve along diagonal
   * pairplotk.jpg  pair plot with kde plot along the diagonals
* Parallel Coordiante Curve
  * parac.jpg parallel coordiantes plot of iris data
* Radvis plot
  * rad.jpg - Radviz plot of iris data
* QQ Plots - add desc in later
  * setosaPL_qqplot.jpg qq plot of setosa petal lengths
  * setosaPW_qqplot.jpg qq plot of setosa petal widths
  * setosaSL_qqplot.jpg qq plot of setosa sepal lengths
  * setosaSW_qqplot.jpg qq plot of setosa sepal widths
  * versicolorPL_qqplot.jpg qq plot of versicolor petal lengths
  * versicolorPW_qqplot.jpg qq plot of versicolor petal widths
  * versicolorSL_qqplot.jpg qq plot of versicolor sepal lengths
  * versicolorSW_qqplot.jpg qq plot of versicolor sepal widths
  * virginiaPL_qqplot.jpg qq plot of virginica petal lengths
  * virginicaPW_qqplot.jpg qq plot of virginica petal widths
  * virginicaSL_qqplot.jpg qq plot of virginica sepal lengths
  * virginicaSW_qqplot.jpg qq plot of virginica sepal widths
* Histograms with axis labels
  * setosapetalL.jpg histogram of setosa petal length 
  * setosapetalW.jpg histogram of setosa petal width
  * setosasepalL.jpg histogram of setosa sepal length 
  * setosasepalW.jpg histogram of setosa sepal width
  * versicolorpetalL.jpg histogram of versicolor petal length
  * versicolorpetalW.jpg histogram of versicolor petal length
  * versicolorsepalL.jpg histogram of versicolor sepal length
  * versicolorsepalW.jpg histogram of versicolor sepal width
  * virginicapetalL.jpg histogram of virginica petal length
  * virginicapetalW.jpg histogram of virginica petal width
  * virginicasepalL.jpg histogram of virginica sepal length
  * virginicasepalW.jpg histogram of virginica petal width
* Scatter plots
  * Labelled
    * snpetal2.jpg catogory labeled scatter plot of iris petal data
    * snsepal2.jpg catogory labled scatter plot of iris data sepal data
  * Unlabelled
    * snpetal.jpg - seaborn scattor plot of unlabelled iris petal data with pearsons r. 
    * snsepal.jpg - seaborn scatter plot of unlabelled iris sepal data with persons r. 
    * sppetal.jpg - pandas scatter plot of unlabelled iris petal data
    * spsepal.jpg - pandas scatter plot of unlabeled sepal data
* Violin Plots
  * vppetalL.jpg violin plot of petal lengths
  * vppetalW.jpg violin plot of petal widths
  * vpsepalL.jpg violin plot of sepal lengths
  * vpsepalW.jpg violin plot of sepal widths

### Research 
This [folder](/research/) contains some papers used to research the project. 

### Project Report
The full write up of the project can be found [in word format here](project%20report.docx) and [in pdf format here] (project%20report.pdf). 


