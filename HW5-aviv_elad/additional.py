import pandas as pd
import joblib

DESIGN_CLASS = "bg-opacity-10 p-2 m-1 bg-primary text-dark fw-bold rounded"

df = pd.read_csv('data/fixed_names_df.csv')
gb = joblib.load('GradientBoostingClassifier')

options_job = [{'label': i, 'value': i} for i in list(df['job'].unique())]
mode_job = df['job'].mode()[0]

options_marital = [{'label': i, 'value': i} for i in list(df['marital'].unique())]
mode_marital = df['marital'].mode()[0]

options_education = [{'label': i, 'value': i} for i in list(df['education'].unique())]
mode_education = df['education'].mode()[0]

options_default = [{'label': i, 'value': i} for i in list(df['default'].unique())]
mode_default = df['default'].mode()[0]

options_housing = [{'label': i, 'value': i} for i in list(df['housing'].unique())]
mode_housing = df['housing'].mode()[0]

options_loan = [{'label': i, 'value': i} for i in list(df['loan'].unique())]
mode_loan = df['loan'].mode()[0]

options_contact = [{'label': i, 'value': i} for i in list(df['contact'].unique())]
mode_contact = df['contact'].mode()[0]

options_month = [{'label': i, 'value': i} for i in list(df['month'].unique())]
mode_month = df['month'].mode()[0]

options_day_of_week = [{'label': i, 'value': i} for i in list(df['day_of_week'].unique())]
mode_day_of_week = df['day_of_week'].mode()[0]

options_poutcome = [{'label': i, 'value': i} for i in list(df['poutcome'].unique())]
mode_poutcome = df['poutcome'].mode()[0]


median_age = int(df['age'].median())
min_age = int(df['age'].min())
max_age = int(df['age'].max())

median_campaign = float(df['campaign'].median())
min_campaign = float(df['campaign'].min())
max_campaign = float(df['campaign'].max())

median_previous = float(df['previous'].median())
min_previous = float(df['previous'].min())
max_previous = float(df['previous'].max())

median_cons_price_idx = float(df['cons_price_idx'].median())
min_cons_price_idx = float(df['cons_price_idx'].min())
max_cons_price_idx = float(df['cons_price_idx'].max())

median_cons_conf_idx = float(df['cons_conf_idx'].median())
min_cons_conf_idx = float(df['cons_conf_idx'].min())
max_cons_conf_idx = float(df['cons_conf_idx'].max())

median_euribor3m = float(df['euribor3m'].median())
min_euribor3m = float(df['euribor3m'].min())
max_euribor3m = float(df['euribor3m'].max())


x0 = {'age': 0.0,
 'campaign': 0.0,
 'previous': 0.0,
 'cons_price_idx': 0.0,
 'cons_conf_idx': 0.0,
 'euribor3m': 0.0,
 'job_admin': 0.0,
 'job_blue-collar': 0.0,
 'job_entrepreneur': 0.0,
 'job_housemaid': 0.0,
 'job_management': 0.0,
 'job_retired': 0.0,
 'job_self-employed': 0.0,
 'job_services': 0.0,
 'job_student': 0.0,
 'job_technician': 0.0,
 'job_unemployed': 0.0,
 'job_unknown': 0.0,
 'marital_divorced': 0.0,
 'marital_married': 0.0,
 'marital_single': 0.0,
 'marital_unknown': 0.0,
 'education_basic_4y': 0.0,
 'education_basic_6y': 0.0,
 'education_basic_9y': 0.0,
 'education_high_school': 0.0,
 'education_illiterate': 0.0,
 'education_professional_course': 0.0,
 'education_university_degree': 0.0,
 'education_unknown': 0.0,
 'default_no': 0.0,
 'default_unknown': 0.0,
 'default_yes': 0.0,
 'housing_no': 0.0,
 'housing_unknown': 0.0,
 'housing_yes': 0.0,
 'loan_no': 0.0,
 'loan_unknown': 0.0,
 'loan_yes': 0.0,
 'contact_cellular': 0.0,
 'contact_telephone': 0.0,
 'month_apr': 0.0,
 'month_aug': 0.0,
 'month_dec': 0.0,
 'month_jul': 0.0,
 'month_jun': 0.0,
 'month_mar': 0.0,
 'month_may': 0.0,
 'month_nov': 0.0,
 'month_oct': 0.0,
 'month_sep': 0.0,
 'day_of_week_fri': 0.0,
 'day_of_week_mon': 0.0,
 'day_of_week_thu': 0.0,
 'day_of_week_tue': 0.0,
 'day_of_week_wed': 0.0,
 'poutcome_failure': 0.0,
 'poutcome_nonexistent': 0.0,
 'poutcome_success': 0.0}

p = pd.DataFrame(x0, index=[0])

