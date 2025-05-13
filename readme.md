# DwellWell AI : Real Estate Data Science Application (Live Link : https://dwellwell.streamlit.app)

In this comprehensive project, the primary focus was on leveraging data science techniques to provide insights, predictions, and recommendations in the real estate domain. The project unfolds through various stages, covering data gathering, cleaning, exploratory analysis, modeling, recommendation systems, and the deployment of a user-friendly application.

## Data Gathering:

The project commenced with the collection of real estate data, which was web scraped from the 99acres website. 
For scraping the data python libraries like **Selenium** and **BeautifulSoup** was used

## Data Cleaning and Merging:

To prepare the dataset for analysis, a meticulous data cleaning process was undertaken, handling missing values and ensuring consistency. 
This included steps like removing Nan values, Fixing data errors such as incorrect units for *built-up area* etc were performed in this step

## Feature Engineering:

The dataset underwent feature engineering to enhance its richness and informativeness. New features, such as additional room indicators, area with type specifications, age of possession, furnish details, and a luxury score, were introduced to provide a more detailed representation of the properties.

## Exploratory Data Analysis (EDA):

Univariate and multivariate analyses were conducted to uncover patterns and relationships within the data. The use of **univariate and multivariate analysis** techniques facilitated a deeper understanding of data distribution and structure.
To prepare a comprehensive report of the feature interations , **Sweetviz** library was used

## Outlier Detection, Missing Value Imputation:

Outliers were identified and removed to ensure the robustness of subsequent analyses. Missing values, particularly in critical columns like area and bedroom, were addressed using appropriate imputation techniques.

## Feature Selection:

Multiple feature selection techniques were employed to identify the most impactful variables for modeling. These included correlation analysis, random forest and gradient boosting feature importance, permutation importance, LASSO, recursive feature elimination, and SHAP (Explainable AI).

## Model Selection :

In the Model Selection  phase, an exhaustive comparison of various regression models was conducted to determine the most effective model for predicting property prices. The process involved implementing a detailed price prediction pipeline that incorporated encoding methods, ensuring the robustness and accuracy of the chosen model. The selected model was then deployed using Streamlit, creating an intuitive and user-friendly web interface for end-users.

**Model Comparison:**
We evaluated 11 regression models, including Linear Regression, SVR, tree-based methods (Random Forest, XGBoost), and neural networks (MLP). Performance was assessed using MAE on a held-out test set and using R2 score using KFold Cross Validation.

**Key Findings:**

It was noted that tree based models like DecisionTree,XGboost and Ensemble models like Gradient Boosting and ExtraTrees were performing the best likely due to their ability to handle non linear relationships
ExtraTrees Regressor achieved the best performance with **R2 score = 0.937** and **MAE= ₹0.30 Cr**.

**Final Pipeline:**
The chosen regression model was then integrated into a comprehensive price prediction pipeline, which included preprocessing steps, encoding methods, and handling of various features to ensure optimal performance. The final model was deployed using Streamlit, creating an interactive and user-friendly web interface for predicting property prices. This step made the model accessible to end-users, allowing them to make informed decisions in the real estate domain.

## Building the Analytics Module:

An analytics module was developed to visually represent key insights about the real estate data. Geographical maps, word clouds for amenities, scatter plots, pie charts, and box plots were employed to offer users a comprehensive understanding of the market.

## Building the Recommender System:

In the process of building the Recommender System, three distinct recommendation models were developed, each focusing on different aspects of the real estate dataset: top facilities, price details, and location advantages. The goal was to provide users with personalized recommendations tailored to their preferences and priorities. Additionally, a user-friendly recommendation interface was crafted using Streamlit, enhancing the accessibility of the recommendation systems.

## Deploying the Application on Streamlit:

The entire application, encompassing prediction, analytics, and recommendation functionalities, was deployed on **Streamlit Cloud**. 
Streamlit Cloud was chosen for its quick, hassle-free deployment and cost-effectiveness.
This step ensured the scalability and accessibility of the project.

This  project not only demonstrates proficiency in data science techniques such as feature engineering, exploratory analysis, and model building but also showcases the deployment of a real-world application, making valuable insights and recommendations accessible to end-users.


## Whats Next?
- Improve Hyper Parameter tuning for ML models to improve MAE in the Price Prediction module
- Incorporate different clusturing algorithms to improve the Recommender System.
- Gather data for other Indian cities to expand the functionality