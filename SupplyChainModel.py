import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

df = pd.read_csv('data/SupplyChainETL.csv')

df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])
df['order month'] = df['order date (DateOrders)'].dt.month
df['order day'] = df['order date (DateOrders)'].dt.day_of_week
df['order hour'] = df['order date (DateOrders)'].dt.hour

city_risk = df.groupby('Order City')['Late_delivery_risk'].mean()
category_risk = df.groupby('Category Name')['Late_delivery_risk'].mean()
df['city risk score'] = df['Order City'].map(city_risk)
df['category risk score'] = df['Category Name'].map(category_risk)

le = LabelEncoder()
sc = StandardScaler()

df['Order Item Total'] = sc.fit_transform(df[['Order Item Total']])
df['Order Region'] = le.fit_transform(df[['Order Region']])
df['Order Status'] = le.fit_transform(df[['Order Status']])
df['Shipping Mode'] = le.fit_transform(df[['Shipping Mode']])
df['Market'] = le.fit_transform(df[['Market']])
df['Category Name'] = le.fit_transform(df[['Category Name']])

X = df[['Days for shipment (scheduled)',
        'Order Region',
        'order month',
        'Order Status',
        'order hour',
        'order day',
        'city risk score',
        'category risk score',
        'Shipping Mode',
        'Market',
        'Order Item Total']]

y = df['Late_delivery_risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state = 42)

model = XGBClassifier( n_estimators=5000, learning_rate=0.01, max_depth=10, subsample=0.8, random_state=42 )
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Accuracy Score')
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

result = X_test.copy()
result['actual_late_risk'] = y_test
result['predicted_late_risk'] = y_pred

result.to_csv('data/ModelResultsTableau.csv', index = False)

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})
importance_df.to_csv('data/FeatureImportance.csv', index = False)