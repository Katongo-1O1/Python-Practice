from ipywidgets import FloatSlider, IntSlider, interact
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
import plotly.express as px


df = pd.read_csv("housing.csv")
df.drop(columns="ocean_proximity", inplace=True)
df.dropna(inplace=True)
sns.heatmap(df.corr())

fig = px.scatter_mapbox(df, df["latitude"], df["longitude"], mapbox_style="open-street-map", color = "median_house_value", width=300)


target = ["median_house_value"]
X = ["latitude", "longitude", "population"]

x_train_size = int(len(df[X]) * 0.8)


X_train = df[X][:x_train_size]
y_train = df[target][:x_train_size]

X_test = df[X][x_train_size:]

y_mean = y_train.mean()
y_baseline = [y_mean] * len(y_train)

mae = mean_absolute_error(y_train, y_baseline)


model = make_pipeline(SimpleImputer(), LinearRegression())
# model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_train)
mae1 = mean_absolute_error(y_train, y_pred)


def make_prediction(latitude, longitude, population):
    data = {"latitude":latitude, "longitude":longitude, "population": population}
    df_ = pd.DataFrame(data, index=[0])
    prediction = model.predict(df_).round(2)[0]
    return f"Predicted median_house_value: ${prediction}"

interact(
    make_prediction,

    latitude=FloatSlider(
        min=X_train["latitude"].min(),
        max=X_train["latitude"].max(),
        step=0.01,
        value=X_train["latitude"].mean(),
    ),
    longitude=FloatSlider(
        min=X_train["longitude"].min(),
        max=X_train["longitude"].max(),
        step=0.01,
        value=X_train["longitude"].mean(),
    ),
       population=IntSlider(
        min=X_train["population"].min(),
        max=X_train["population"].max(),
        value=X_train["population"].mean(),

))

