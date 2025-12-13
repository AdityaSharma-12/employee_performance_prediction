import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
df = pd.read_csv(r"C:\Users\adity\Downloads\garments_worker_productivity.csv")
df.head()
X = df[['no_of_workers',
        'no_of_style_change',
        'targeted_productivity',
        'smv',
        'wip',
        'over_time',
        'incentive',
        'idle_time',
        'idle_men']]


y = df['actual_productivity']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))
pickle.dump(model, open('gwp.pkl', 'wb'))
