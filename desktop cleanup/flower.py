import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App
This app predicts the type of iris flower a flower is.\n
This uses the Iris Flower Dataset:\n
https://en.wikipedia.org/wiki/Iris_flower_data_set
""")

st.sidebar.header("User Input Parameters")


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)

    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_probability = clf.predict_proba(df)


probability = 1



prediction_string = f"The iris is a {iris.target_names[prediction][0]}, with a probability of {prediction_probability.flat[prediction][0]}"
st.write(prediction_string)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_probability)

st.subheader("Iris data set")
st.write(iris)
st.subheader("Data")
st.write(iris.data)
st.subheader("Targets")
st.write(iris.target)
