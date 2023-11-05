# finalYearProject - Liver Disease Detection

<h3> TLDR <br>
•	Designed & Programmed a Full Stack web application using Flask with 6 web pages, integrating it with 13 machine learning & deep learning models trained on UCI ILPD dataset to accurately detect liver disease. <br>
•	Leveraged Drop-Off & Genetic Algorithm techniques identify optimal features & fine-tune model performance.<br>
•	Published research findings (<a href="https://www.annalsofrscb.ro/index.php/journal/article/view/2768/2300"> Reasearch Paper Link</a>) derived from comparative analysis, contributing to the medical data analysis field.
</h1>
<h1> What Inspired this?</h1>

<div>
<p>
Liver diseases are one of the major causes of death in the world. We, humans, have come a long way in the medical field and scientific advancements to treat diseases and it's evident that when these liver diseases are detected early, they can be treated easily. In order to be able to accurately predict if there’s a chance of the liver disease it is imperative to identify the features/symptoms which play a significant role in causing the LD. It is crucial to select the correct combination of significant features as it will improve the performance of the prediction models.
We are proposing a system which will first identify the significant features and then use them to predict whether or not a person may suffer or is suffering from LD. Our system ought to be used as a supplementary tool in diagnosis. Data is essential and We will be using the dataset available on the UIC repository. We will be using genetic algorithms to identify the significant features and then use those features to train different classification models like k-Nearest Neighbors, k-means, Random Forest, Support Vector Machines, Naïve Bayes, Logistic Regression, etcetera which will predict if there’s a chance of LD for a person’s data. We will also be using neural networks with backpropagation to  perform binary classification.
Ideally our proposed solution should be able to identify the significant features and find the best model which will be able to predict with more accuracy or another statistical measure

  
</p>
</div>



<h1> This is how the Application looks like ! </h1>
<h2>
1. Sign Up Screen <br><hr><img width="1195" alt="Screenshot 2023-08-22 at 4 34 00 PM" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/fc577eda-b225-4c34-b86f-0beaf1213867">
2. Login Screen<br><hr> <img width="1195" alt="login" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/eb883fa2-78b6-4257-b32d-c8e0685598b3">
3. Profile Page<br><hr> <img width="1195" alt="profile" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/7d691ef2-6031-44d3-b2a9-6786cea2aad9">
4. Predict Form<br><hr>
<img width="1195" alt="Screenshot 2023-08-22 at 4 34 09 PM" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/ee871b8c-6b26-44fb-a65f-d03dfbaa53e5">
5. Landing Page<<img width="1195" alt="landing" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/938a3767-abf8-4e05-b39b-05f772d0d630">
</h2>


<br><hr>


<h1> Flow between Pages </h1><img width="1195" alt="flow" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/fe5f3fb0-d658-4411-b4a2-4629f4a1030c">
<br><hr>
<h1> Architecture of Proposed System</h1>
<img width="1195" alt="architecture" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/6729f2ce-b6f2-4ead-a4af-e31277656682">

<br><hr>

<h1> State Diagram</h1>
State diagrams require that the system described is composed of a finite number of states sometimes, this is indeed the case, while at other times this is a reasonable abstraction. 
It’s a behavioral diagram and it represents the behavior using finite state transitions.
<img width="1195" alt="state" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/c96045ce-0b07-437a-9e32-781c351c0c64">

<br><hr>

<h1> Results </h1>
<img width="800" alt="Results" src="https://github.com/mmaashraf/finalYearProject/assets/37049007/d5384b8b-1c2d-4b0f-82b9-11c959d9bb7a">
<br><hr>

<h3> The findings were published as a Reasearch Paper at 'Annals of the Romanian Society for Cell Biology' - https://www.annalsofrscb.ro/index.php/journal/article/view/2768/2300.
</h3>
Note: I haven't tested the below steps in a while, so please take it with a grain of salt.

<h2>How to Install?</h2>
use this to install all the dependencies 
$ cd final_project
$ pip install -r requirements.txt

for venv
$ source final_project/final/bin/activate

create branches for use
$ git branch <<branch_name>>

after u after installed the dependencies and activated the virtual environment, run the below cmds to run the web app
$ export FLASK_APP=final_project
$ export FLASK_DEBUG=0
$ flask run
<br><hr>
