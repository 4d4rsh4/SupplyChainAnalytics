import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('data/SupplyChainETL.csv')

le = LabelEncoder()
sc = StandardScaler()

df['Order Item Total'] = sc.fit_transform(df[['Order Item Total']])
df['Order Status'] = le.fit_transform(df[['Order Status']])
df['Order Region'] = le.fit_transform(df[['Order Region']])

X = df[['Days for shipment (scheduled)',
        'Order Status',
        'Order Region',
        'Order Item Total']]

y = df['Late_delivery_risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state = 42)

model = RandomForestClassifier(random_state = 42 )
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Accuracy Score')
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

result = X_test.copy()
result['actual_late_risk'] = y_test
result['predicted_late_risk'] = y_pred

result.to_csv('ModelResultsTableau.csv', index = False)