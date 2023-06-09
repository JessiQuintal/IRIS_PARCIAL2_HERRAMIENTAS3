import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

def show():
    URL= 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dfIris= pd.read_csv(URL, names=names)
    dfIris = dfIris[dfIris["sepal-length"] != "sepal.length"]

    x_train, x_test, y_train, y_test = train_test_split(dfIris[dfIris.columns[0:4]], dfIris[dfIris.columns[-1]], test_size=0.2)


    modelos = []
    #print(x_train, x_test)
    modelo = LogisticRegression(random_state=0).fit(x_train, y_train)
    modelo.score(x_test, y_test)
    modelo.predict(x_test)
    modelos.append(("LR", LogisticRegression()))

    st.header('Modelo Score de Precisión:')
    st.write(modelo.score(x_test, y_test))
    st.header('Modelo Predicción:')
    st.write(modelo.predict(x_test))

    #kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True )
    #resultados = cross_val_score(modelo, xtrain, y_train, cv=kflod, scoring="accuracy")
    #resultados

    #modeloKN= KNeighborsClassifier(n_neighbors=3)
    #modeloKN.fit(x_train, y_train)
    #modeloKN.score(x_test)
show()