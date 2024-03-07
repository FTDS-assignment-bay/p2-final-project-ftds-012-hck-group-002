[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/x2EymKzp)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14110511&assignment_repo_type=AssignmentRepo)  

---  

# 🏁 Final Project Group 2 HCK-012 🏁  

**Group Member**  
🔴 Nicku Rendy Perdana, enrolled as Data Analyst (🖥️[Github](https://github.com/nickuperdana), 👤[LinkedIn](https://www.linkedin.com/in/nickurendyperdana/))  
🟠 Ogi Hadicahyo, enrolled as Data Scientist (🖥️[Github](https://github.com/ogi092), 👤[LinkedIn](https://www.linkedin.com/in/ogi-hadicahyo/))  
🟡 Panji Putra Rianto, enrolled as Data Engineer (🖥️[Github](https://github.com/panjiputra-r), 👤[LinkedIn](https://www.linkedin.com/in/panji-putra-rianto-207789213/))  
🟢 Samuel Tatang Surja, enrolled as Data Scientist (🖥️[Github](https://github.com/samueltatsu), 👤[LinkedIn](https://www.linkedin.com/in/samuel-tatang-surja-000529294/))  

---

## Getting Started  
### Situation  
- Our client, a European-based bank, requires assistance from our Business Intelligence division to classify customers when contacted by the bank's telemarketing team, determining whether they subscribe to the bank's term deposit service or not.

### Task  
- Our team, consisting of Nicku R. Perdana (Data Analyst), Ogi Hadicahyo (Data Scientist), Panji P. Rianto (Data Engineer), and Samuel T. Surja (Data Scientist), is tasked with designing a model capable of predicting customers' final decisions regarding subscription to the bank's term deposit service, based on contacts made by our client's telemarketing team.
- The bank aims for this model to accurately predict customer classifications and optimize campaign resources to target customers who are more likely to be interested and continue subscribing to the bank's term deposit service.
- The Data Engineer will focus on acquiring and processing data until it is ready for analysis and modeling, including preparing a system to manage data automatically.
- The Data Analyst will seek business insights from the final dataset provided.
- The Data Scientist will develop prediction models using the most optimal algorithms for the given case.

### Action  
- Data Engineering by Data Engineer:
  - In the data preparation process, it was found that the data provided by the bank was still in a raw format, such as lowercase category values, missing values imputed as 'unknown', and column names not yet representative of the essence of each column's information. The data engineer is tasked with preparing a data processing and preparation workflow automatically by setting up an Airflow framework using Docker connected to a local RDBMS to fetch and store data.
- Data Analysis by Data Analyst:
  - The cleaned data revealed imbalanced customer classifications, which can be addressed by focusing on data trends based on each variable/column. Visualization outputs are presented using the Tableau platform, and observation and data analysis reports are documented in a notebook file.
  - Analyzing specific data to depict the characteristics of customers who responded to telemarketing.
  - Conducting statistical tests to explore the relationships between variables in the dataset and the target variable (the final subscription status of respondents after being contacted by the bank's telemarketing team).
  - Formulating strategic conclusions to guide modeling considerations and recommending further business findings for the implementation of modeling results and predictions.
- Data Modeling by Data Scientists:
  - Given the unbalanced composition of the modeling data, data balancing needs to be performed using methods that do not significantly affect evaluation scores. To test data performance, modeling is conducted using two learning techniques: machine learning classification and deep learning. This is done to determine the appropriate algorithm capable of predicting customer subscription interest using a case study of the provided data. The model will utilize accuracy and recall metrics to accommodate modeling requiring high prediction accuracy and minimizing the probability of false negatives in each predictive action.

### Result  
- Data Analysis by Data Analyst:
  - The modeling process ultimately utilizes logistic regression, considering the accuracy and recall values of this algorithm.
  - The model is deployed and made available online using Streamlit running on a local server.
  - Tableau visualization results and analysis can be accessed through the following [link](https://public.tableau.com/app/profile/nicku.rendy.perdana2598/viz/BankMarketingAnalysis_17096191008530/Main_Dashboard?publish=yes).

---

## Tools
- Docker
- ElasticSearch
- Kibana
- PostgreSQL
- Tableau ([link](https://public.tableau.com/app/profile/nicku.rendy.perdana2598/viz/BankMarketingAnalysis_17096191008530/Main_Dashboard?publish=yes))
- Streamlit
- HuggingFace ([link](https://huggingface.co/spaces/panjiputra-r/ProspectPredictor))
- Python
- Scikit-learn
- Tensorflow
- imblearn
- Pandas
- Scipy
- Pickleshare
- Numpy
