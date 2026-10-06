# Smart Library Demand Forecasting & Resource Optimization System

## Overview

The **Smart Library Demand Forecasting & Resource Optimization System** is a data analytics and machine learning project designed to analyze historical library borrowing patterns and forecast future demand.

The system uses historical library loan data to identify high-demand libraries, resource types, monthly demand trends, and peak borrowing periods. A Linear Regression model is then used to forecast future library demand, classify demand levels, and generate resource optimization recommendations.

This project demonstrates how historical borrowing data can be transformed into practical insights for better library inventory, staffing, and resource planning.

## Problem Statement

Libraries handle large amounts of borrowing data, but manually analyzing this data can make it difficult to identify demand patterns and plan resources efficiently.

Without proper demand analysis, libraries may face:

- Excess stock of low-demand resources
- Insufficient availability of high-demand resources
- Inefficient staff allocation
- Difficulty identifying peak borrowing periods
- Poor planning for future resource requirements

The objective of this project is to analyze historical library loan data and develop a simple forecasting-based system that supports data-driven resource planning.

## Objectives

The main objectives of the project are:

- Analyze historical library borrowing data
- Identify libraries with the highest borrowing activity
- Analyze demand for different resource types
- Study monthly borrowing trends
- Identify peak-demand periods
- Forecast future library demand
- Classify future demand into Low, Medium, and High levels
- Generate practical resource optimization recommendations
- Present results using charts and CSV outputs

## Dataset

The project uses the **London Borough of Barnet Library Loans Dataset**.

The dataset contains aggregated monthly library loan information.

### Dataset Features

- `Local authority` – Name of the local authority
- `Library name` – Name of the library
- `Month` – Month of the recorded loans
- `Type` – Type of library resource
- `Loans` – Number of loans recorded

The dataset contains approximately **8,670 records** and covers historical monthly library borrowing activity.

## Data Source

The dataset was obtained from the official UK Government open data platform:

**London Borough of Barnet Library Loans**

Source:
https://www.data.gov.uk/dataset/106580f4-58dc-41f1-bc51-d496ca5d4bf9/library-loans

The dataset is used for academic data analysis and forecasting purposes.

## Technologies Used

- **Python**
- **Pandas** – Data cleaning and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Heatmap visualization
- **Scikit-learn** – Linear Regression forecasting
- **CSV** – Dataset and output storage
- **Git & GitHub** – Version control and project sharing

## Data Analytics Workflow

The project follows the following workflow:

**Library Loans Dataset**
↓
**Data Cleaning**
↓
**Library Demand Analysis**
↓
**Resource Type Analysis**
↓
**Monthly Demand Analysis**
↓
**Demand Visualization**
↓
**Demand Forecasting**
↓
**Demand Level Classification**
↓
**Resource Optimization Recommendations**

## Data Cleaning

The following preprocessing steps were performed:

- Loaded the library loan dataset using Pandas
- Converted the `Month` column into datetime format
- Converted the `Loans` column into numeric format
- Removed rows with missing library names
- Removed rows with missing months
- Removed rows with missing resource types
- Removed rows with missing loan values
- Removed duplicate records
- Removed invalid negative loan values

After preprocessing, the cleaned data was used for further analysis and forecasting.

## Analysis Performed

### 1. Library-wise Demand Analysis

The total number of loans was calculated for each library.

This analysis helps identify:

- Libraries with the highest borrowing activity
- Libraries with lower borrowing activity
- Overall demand distribution across libraries

The results are stored in:

`library_demand_ranking.csv`

### 2. Resource Type Demand Analysis

The total loans were grouped according to resource type.

This helps determine which categories of library resources are most frequently borrowed.

The results are stored in:

`resource_type_demand.csv`

### 3. Monthly Demand Analysis

Monthly borrowing activity was calculated by aggregating total loans for each month.

This analysis helps identify:

- Overall borrowing trends
- Increasing or decreasing demand
- Peak borrowing months
- Changes in library usage over time

The results are stored in:

`monthly_library_demand.csv`

### 4. Top Library Analysis

The top 10 libraries were identified based on total borrowing activity.

A bar chart was generated to make the comparison easier.

Output:

`top_10_libraries.png`

### 5. Resource Type Visualization

A visualization was created to compare borrowing demand across different resource types.

Output:

`resource_type_demand.png`

### 6. Monthly Demand Trend

A line chart was generated to visualize changes in total library demand over time.

Output:

`monthly_demand_trend.png`

### 7. Demand Heatmap

A heatmap was generated to provide a visual representation of demand patterns across libraries and months.

Output:

`demand_heatmap.png`

## Demand Forecasting

A **Linear Regression** model was used to forecast future library demand.

The monthly total loan count was used as the target variable.

A sequential time index was created to represent the progression of months.

The model learns the general historical trend and uses it to estimate demand for the next six months.

### Forecasting Process

1. Aggregate loan data by month
2. Create a numerical time index
3. Use the time index as the input feature
4. Use monthly loan count as the target
5. Train a Linear Regression model
6. Predict demand for the next six months
7. Store forecast results in a CSV file
8. Visualize historical and forecast demand

The forecasting output is stored in:

`library_demand_forecast.csv`

The forecast visualization is stored in:

`library_demand_forecast.png`

## Forecasting Model

### Linear Regression

Linear Regression was selected because it is:

- Simple to implement
- Easy to understand
- Suitable for demonstrating trend-based forecasting
- Computationally efficient
- Easy to explain during project presentation and viva

The model uses historical monthly demand to estimate the future trend.

This project focuses on a simple trend-based forecasting approach rather than advanced time-series models.

## Demand Level Classification

After forecasting future demand, each forecasted month is assigned a demand level.

The classification is based on the historical average demand.

### Classification Rules

- **High Demand** – Forecast is at least 20% above the historical average
- **Medium Demand** – Forecast is within the normal demand range
- **Low Demand** – Forecast is at least 20% below the historical average

The demand level classification is rule-based and is used to convert numerical forecasts into easier-to-understand planning categories.

## Resource Optimization

The forecasted demand levels are converted into practical resource planning recommendations.

### High Demand

Recommendation:

**Increase book availability, staff support, and borrowing capacity.**

### Medium Demand

Recommendation:

**Maintain normal inventory and staffing levels.**

### Low Demand

Recommendation:

**Reduce excess stock and promote underused resources.**

The final recommendations are stored in:

`library_resource_optimization.csv`

## Key Insights

The project provides the following types of insights:

- Identifies libraries with the highest borrowing activity
- Identifies the most frequently borrowed resource types
- Shows monthly library demand trends
- Identifies peak borrowing periods
- Provides future demand estimates
- Classifies future demand into Low, Medium, and High levels
- Converts demand forecasts into practical resource planning recommendations

These insights can help library management make more informed decisions about inventory and staffing.

## Recommendations

Based on the analysis and forecasting results, libraries can consider the following strategies:

### 1. High-Demand Resources

Increase the availability of frequently borrowed resources to reduce shortages.

### 2. Low-Demand Resources

Review low-demand resources and consider redistribution, promotion, or reduced purchasing.

### 3. Staff Allocation

Allocate additional staff support during periods of higher expected demand.

### 4. Inventory Planning

Use historical and forecast demand to support future inventory planning.

### 5. Demand Monitoring

Regularly update the forecasting model with new borrowing data to improve future planning.

## Project Outputs

The project generates both analytical datasets and visualizations.

### CSV Outputs

- `library_demand_ranking.csv`
- `resource_type_demand.csv`
- `monthly_library_demand.csv`
- `library_demand_forecast.csv`
- `library_resource_optimization.csv`

### Visualization Outputs

- `top_10_libraries.png`
- `resource_type_demand.png`
- `monthly_demand_trend.png`
- `demand_heatmap.png`
- `library_demand_forecast.png`

## Project Structure

    Smart_Library_Demand_Forecasting/
    │
    ├── loans.csv
    │
    ├── initial_analysis.py
    ├── library_demand_analysis.py
    ├── visualization.py
    ├── demand_forecasting.py
    ├── resource_optimization.py
    │
    ├── library_demand_ranking.csv
    ├── resource_type_demand.csv
    ├── monthly_library_demand.csv
    ├── library_demand_forecast.csv
    ├── library_resource_optimization.csv
    │
    ├── top_10_libraries.png
    ├── resource_type_demand.png
    ├── monthly_demand_trend.png
    ├── demand_heatmap.png
    ├── library_demand_forecast.png
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Installation Requirements

Make sure Python is installed on the system.

Install the required Python libraries using:

    pip install pandas numpy matplotlib seaborn scikit-learn

Alternatively, if a `requirements.txt` file is available:

    pip install -r requirements.txt

## How to Run the Project

Place the dataset file:

    loans.csv

inside the project folder.

Then run the scripts in the following order:

### Step 1 – Initial Dataset Analysis

    python initial_analysis.py

### Step 2 – Library Demand Analysis

    python library_demand_analysis.py

### Step 3 – Data Visualization

    python visualization.py

### Step 4 – Demand Forecasting

    python demand_forecasting.py

### Step 5 – Resource Optimization

    python resource_optimization.py

After running all scripts, the generated CSV files and visualizations will be available inside the project folder.

## Requirements

Python version:

    Python 3.x

Required libraries:

    pandas
    numpy
    matplotlib
    seaborn
    scikit-learn

## Limitations

The project has some limitations:

- The dataset contains aggregated library loan information rather than individual user-level data.
- The forecasting model uses a simple linear trend.
- Seasonality is not explicitly modeled.
- External factors such as holidays, weather, academic schedules, and special events are not included.
- Demand classification uses fixed rule-based thresholds.
- Forecast accuracy may change when new data becomes available.

## Future Scope

The project can be improved in the future by:

- Using advanced time-series forecasting models such as ARIMA, Prophet, or other suitable models
- Incorporating seasonal patterns
- Adding holiday and event information
- Including additional library characteristics
- Building an interactive dashboard
- Adding automated model retraining
- Comparing multiple forecasting algorithms
- Developing a web-based library resource planning system

## Academic Applications

This project demonstrates practical applications of:

- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Machine Learning
- Trend Forecasting
- Demand Classification
- Resource Optimization
- Decision Support Systems

It can be used as an academic project to demonstrate how data analytics and machine learning can support real-world library management.

## Conclusion

The **Smart Library Demand Forecasting & Resource Optimization System** demonstrates how historical library loan data can be analyzed to understand borrowing behavior and support future resource planning.

The project combines data preprocessing, exploratory analysis, visualization, Linear Regression forecasting, demand classification, and optimization recommendations into a single workflow.

By converting historical borrowing data into actionable insights, the system can help libraries improve inventory planning, staffing decisions, and overall resource utilization.

## Project Status

**Completed**

The project successfully performs:

- Data cleaning
- Library demand analysis
- Resource type analysis
- Monthly trend analysis
- Data visualization
- Demand forecasting
- Demand classification
- Resource optimization recommendations

## Author

**Konda Manvitha Yadav**

B.Tech – Computer Science and Engineering (Data Science)

## License

This project is developed for academic and educational purposes.