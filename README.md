{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30\fsmilli15400 \cf2 Model Training
\f1\b0\fs26\fsmilli13090 \
\
The ANN model was trained using 
\f0\b Jupyter Notebook
\f1\b0 .\
\
Training process includes:\
\pard\tqr\tx100\tx260\li260\fi-260\sl250\slmult1\sb240\partightenfactor0
\cf2 	\'95	Data preprocessing\
	\'95	Feature selection\
	\'95	Model training\
	\'95	Prediction generation\
	\'95	Model evaluation\
\
Algorithm used:\
	\'95	
\f0\b Artificial Neural Network
\f1\b0  implemented using 
\f0\b Scikit-learn MLPRegressor
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\fs18\fsmilli9240 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\fs26\fsmilli13090 \cf2 \

\f0\b\fs30\fsmilli15400 Dashboard Development
\f1\b0\fs26\fsmilli13090 \
\
The trained model insights are visualized using an interactive dashboard built with:\
\pard\tqr\tx100\tx260\li260\fi-260\sl250\slmult1\sb240\partightenfactor0
\cf2 	\'95	
\f0\b Streamlit
\f1\b0 \
	\'95	
\f0\b Plotly
\f1\b0 \
\
The dashboard allows users to explore corruption trends dynamically.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\fs18\fsmilli9240 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\fs26\fsmilli13090 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs43\fsmilli21560 \cf2 Features
\f1\b0\fs26\fsmilli13090 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30\fsmilli15400 \cf2 Corruption Prediction
\f1\b0\fs26\fsmilli13090 \
\
Predict corruption amount using an ANN model.\
\

\f0\b\fs30\fsmilli15400 State-wise Analysis
\f1\b0\fs26\fsmilli13090 \
\
Compare corruption levels across states.\
\

\f0\b\fs30\fsmilli15400 City-wise Analysis
\f1\b0\fs26\fsmilli13090 \
\
Analyze corruption patterns across cities.\
\

\f0\b\fs30\fsmilli15400 Budget vs Actual Cost Analysis
\f1\b0\fs26\fsmilli13090 \
\
Identify differences between allocated budgets and actual spending.\
\

\f0\b\fs30\fsmilli15400 Project Category Analysis
\f1\b0\fs26\fsmilli13090 \
\
Analyze corruption across project types:\
\pard\tqr\tx100\tx260\li260\fi-260\sl250\slmult1\sb240\partightenfactor0
\cf2 	\'95	Roads\
	\'95	Bridges\
	\'95	Parks\
	\'95	Government Buildings\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30\fsmilli15400 \cf2 Population Corruption Impact
\f1\b0\fs26\fsmilli13090 \
\
Estimate how much money each citizen could receive if corruption did not occur.\
\

\f0\b\fs30\fsmilli15400 Citizen Wealth Loss Counter
\f1\b0\fs26\fsmilli13090 \
\
Shows total corruption loss and per-citizen wealth impact.\
\

\f0\b\fs30\fsmilli15400 AI Corruption Risk Analysis
\f1\b0\fs26\fsmilli13090 \
\
Identifies regions with higher corruption risk.\
\
corruption-ai-dashboard\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  app.py\
\uc0\u9500 \u9472 \u9472  corruption_model_training.ipynb\
\uc0\u9500 \u9472 \u9472  corruption_data.csv\
\uc0\u9500 \u9472 \u9472  requirements.txt\
\uc0\u9492 \u9472 \u9472  README.md\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs43\fsmilli21560 \cf2 Technologies Used
\f1\b0\fs26\fsmilli13090 \
\
Programming Language:\
\
Python\
\
Libraries:\
\pard\tqr\tx100\tx260\li260\fi-260\sl250\slmult1\sb240\partightenfactor0
\cf2 	\'95	
\f0\b Pandas
\f1\b0 \
	\'95	
\f0\b NumPy
\f1\b0 \
	\'95	
\f0\b Scikit-learn
\f1\b0 \
	\'95	
\f0\b Plotly
\f1\b0 \
	\'95	
\f0\b Matplotlib
\f1\b0 \
	\'95	
\f0\b Streamlit
\f1\b0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\fs18\fsmilli9240 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\fs26\fsmilli13090 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl250\slmult1\pardirnatural\partightenfactor0

\f0\b\fs43\fsmilli21560 \cf2 Python Version
\f1\b0\fs26\fsmilli13090 \
\
Python 3.10\
\
streamlit==1.30.0\
pandas==2.0.3\
numpy==1.24.3\
plotly==5.18.0\
scikit-learn==1.3.2\
matplotlib==3.7.2\
\
pip freeze > requirements.txt\
}