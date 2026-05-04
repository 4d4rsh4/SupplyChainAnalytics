# Supply Chain Performance & Predictive Analytics


<img width="1001" height="763" alt="image" src="https://github.com/user-attachments/assets/6fc1cdf9-c2a1-4431-879b-bdfb51c5dca9" />
<img width="993" height="796" alt="image" src="https://github.com/user-attachments/assets/0a3c0d97-24eb-46b2-943c-992b758a56d9" />

# Project Overview
This project addresses the critical business challenge of logistics delays within a global supply chain. By analyzing 180,000+ transaction records from the DataCo dataset, I developed a comprehensive system that:
- Architected a relational database to ensure data integrity.
- Automated an ETL pipeline to clean and normalize raw data.
- Predicted late delivery risks using Machine Learning.
- Visualized strategic insights for executive decision-making.

# Technical Stack
- Database: SQL Server (Relational Schema, 3NF Normalization)
- Language: Python 3.10+
- Libraries: Pandas, Scikit-Learn, SQLAlchemy, Matplotlib
- Visualization: Tableau

# Data Architecture (SQL)
I transformed a flat, 52-column CSV into a 3rd Normal Form (3NF) relational database to optimize query performance and data consistency.
<img width="1233" height="808" alt="ERDiagram" src="https://github.com/user-attachments/assets/9fcd0083-ec4c-4c70-baaa-78f14c71cecc" />

- Normalization: Separated data into 6 logical entities: Customers, Categories, Items, Orders, Order_Items, and Delivery_Details.
- Referential Integrity: Implemented Primary and Foreign Key constraints.

# ETL & Data Pipeline (Python)
The raw data was 'dirty', containing legacy character encodings and duplicate transactions.
- Standardization: Converted source data from ISO-8859-1 to UTF-8 for cross-platform compatibility.
- Automated Migration: Developed a Python script using SQLAlchemy to programmatically de-duplicate and load 180,000+ rows into SQL Server.
  
# Machine Learning Model (Predictive Analytics)
The objective was to identify 'Late Delivery Risk' at the time of order entry.
- Model: Random Forest Classifier
- Feature Engineering: Managed categorical data via Label Encoding and scaled financial metrics.

- Precision: 0.69 (Class 1: Late Risk)
- Recall: 0.66
- Accuracy: 65% (Baseline)
 
# Business Intelligence (Tableau)
I developed a dual-layered dashboard suite to translate data into action:
- Executive Overview: Tracks $36M in revenue, profit margins (10.78%), and identifies a global 54% late delivery rate.
- AI Risk Analysis: Interactive heatmap allowing logistics managers to drill down into high-risk regions and shipping schedules.

# Key Business Insights
- Operational Bottleneck: The 4-day shipping schedule represents the highest volume of late-delivery risk, suggesting a need for logistics process re-engineering.
- Geographic Risk: Central America and Western Europe share similar sales volumes, but Central America exhibits a significantly higher predictive risk ratio.
  
# Installation & Usage
- Clone the Repo: git clone https://github.com/YourUsername/SupplyChainProject.git
- Install Dependencies: pip install -r requirements.txt
- Database Setup: Run schema/schema_setup.sql in SQL Server.
- Run Pipeline: Execute SupplyChainETL.py to populate the database.
- Run Model: Execute SupplyChainModel.py to view predictive results.
