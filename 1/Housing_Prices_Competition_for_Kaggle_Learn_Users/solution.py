import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Read the training file
file_path = 'C:/Users/tathen/PycharmProjects/ML/AI-ML/1/Housing_Prices_Competition_for_Kaggle_Learn_Users/home-data-for-ml-course/train.csv'
data = pd.read_csv(file_path)
data.dropna()
print(data.columns)
print(data.describe())


# Select features
features = [ 'LotFrontage',	'LotArea',	'OverallQual',
             'OverallCond',	'YearBuilt',	'YearRemodAdd',	'MasVnrArea',
             'BsmtFinSF1',	'BsmtFinSF2',	'BsmtUnfSF',
             'TotalBsmtSF',	'1stFlrSF',	'2ndFlrSF',
             'LowQualFinSF',	'GrLivArea',	'BsmtFullBath',	'BsmtHalfBath',	'FullBath',	'HalfBath',	'BedroomAbvGr',
             'KitchenAbvGr',		'TotRmsAbvGrd',		'Fireplaces',
             	'GarageYrBlt']
X = data[features]
X.describe()
y = data.SalePrice

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
# Define model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))
# print("Making predictions for house prices:")
# print(X.head())
# print("The predictions are")
# print(rf_model.predict(X.head()))
#
#
# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X,y)
rf_full_val_predictions = rf_model_on_full_data.predict(val_X)
rf_full_val_mae = mean_absolute_error(rf_full_val_predictions, val_y)
print("Validation MAE for full Random Forest Model: {:,.0f}".format(rf_full_val_mae))

# def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
#     model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
#     model.fit(train_X, train_y)
#     preds_val = model.predict(val_X)
#     mae = mean_absolute_error(val_y, preds_val)
#     return(mae)
#
# # compare MAE with differing values of max_leaf_nodes
# for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))


# Then in last code cell
test_data_path = 'C:/Users/tathen/PycharmProjects/ML/AI-ML/1/Housing_Prices_Competition_for_Kaggle_Learn_Users/home-data-for-ml-course/test.csv'
test_data = pd.read_csv(test_data_path)
test_X = test_data[features]
test_preds = rf_model_on_full_data.predict(test_X)


output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)