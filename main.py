import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.metrics import classification_report


# DATASET:

# upload the excel file in a Dataframe
df = pd.read_excel("Data_FIA.xlsx")

# drop the first column
df = df.drop('ID', axis=1)

# features tables (all the columns except the last one)
F = df.iloc[:, :-1]

# label tables (only the last columns)
L = df.iloc[:, -1]

# classes values
C = np.unique(L)

# PRE-PROCESSING:

# ANALYZING THE NaN VALUES
# select of columns with at least one NaN value
F_nan = np.where(np.any(np.isnan(F), axis=0))[0]
for Fn_i in F_nan:
    for j in range(len(C)):
        C_j_map = L == C[j]
        nan_map = np.isnan(F.iloc[:, Fn_i])
        C_j_nan_map = nan_map & C_j_map
        C_j_not_nan_map = ~nan_map & C_j_map
        mean_ij = np.mean(F.iloc[:, Fn_i][C_j_not_nan_map])
        F.iloc[:, Fn_i][C_j_nan_map] = mean_ij


# SPLIT the DATA into TRAINING and TESTING SETS
X_train, X_test, y_train, y_test = train_test_split(F, L, test_size=0.2, random_state=17)


# STANDARDIZATION of features
scaler = StandardScaler()
scaler.fit(X_train)
X_train = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)


# PCA
pca = PCA(n_components=min(63, 249))  # if test_size=0.3 -> min(55,249) / test_size=0.2 -> min(63,249)
pca.fit(X_train)

# evaluating the variance
exp_var = pca.explained_variance_
print(pca.explained_variance_)
exp_var_perc = [np.sum(exp_var[:i]) for i in range(len(exp_var))]/np.sum(exp_var)
plt.figure(figsize=[10, 6])
plt.plot(exp_var_perc, 'o-')
loads = pca.components_.T * np.sqrt(pca.explained_variance_)
# find the best number of parameters (15)

# PCA on 15 components
pca = PCA(n_components=15)
pca.fit(X_train)
X_train_elab = pca.transform(X_train)
X_test_elab = pca.transform(X_test)
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

# MODEL:

# Support Vectors Machine
classifier = svm.SVC(kernel='linear', gamma='auto', C=2)
classifier.fit(X_train_elab, y_train)

# PERFORMANCE:

# Analysis of perfomance
y_predict = classifier.predict(X_test_elab)
print(classification_report(y_test, y_predict))
