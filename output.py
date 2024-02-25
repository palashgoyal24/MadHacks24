import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Read the CSV files
train_df = pd.read_csv('train_values.csv')
valid_df = pd.read_csv('valid_values.csv')
test_df = pd.read_csv('test_values.csv')

# Assume the structure of the CSV files aligns with the requirement (Defect type, MK, Expected Life)
# Preprocessing for categorical feature (Defect type)
categorical_features = ['Defect type']
one_hot_encoder = OneHotEncoder(handle_unknown='ignore')  # To handle any unknown categories in future data

preprocessor = ColumnTransformer(transformers=[
    ('cat', one_hot_encoder, categorical_features)
], remainder='passthrough')

# Pipeline with preprocessing and the regressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Prepare X and y for model training
X_train = train_df.drop(['Expected Life'], axis=1)
y_train = train_df['Expected Life']

# Fit the model
model.fit(X_train, y_train)


def returnoutput(input_list):
    defect_type = input_list[0]
    mk_values = sum(input_list[1:])  # Summing the MK values
    input_df = pd.DataFrame([{'Defect type': defect_type, 'MK': mk_values}])

    # Predict using the model
    predicted_life = model.predict(input_df)

    return predicted_life[0]  # Return the predicted value


