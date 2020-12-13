import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def mean_gen_value(dataframe, col):
    grouped_gen_mean = dataframe.groupby("SOURCE_KEY").mean()
    grouped_gen_mean = grouped_gen_mean[col]
    mean_value = grouped_gen_mean.mean()

    return mean_value


def plot_week_power(dataframe, source_key, start_date):
    mean_col = mean_gen_value(dataframe, "AC_POWER")

    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date = start_date + timedelta(7)

    df_specified_gen = dataframe[dataframe["SOURCE_KEY"] == source_key]
    df_specified_date = df_specified_gen[(df_specified_gen["DATE_TIME"] > start_date) & (df_specified_gen["DATE_TIME"] < end_date)]
    df_specified_date.plot(y="AC_POWER", x="DATE_TIME")
    plt.axhline(mean_col, c="red")
    plt.show()


def gens_with_most_values_under_80percent(dataframe, how_many_gens):
    mean_col = mean_gen_value(dataframe, "AC_POWER")

    power_less = dataframe[["SOURCE_KEY", "AC_POWER"]]
    power_less = power_less[df["AC_POWER"] > mean_col * 0.8]
    power_less = power_less.groupby("SOURCE_KEY").count()
    power_less = power_less.sort_values(by="AC_POWER", ascending=False)

    return power_less.iloc[0:how_many_gens]


if __name__ == "__main__":
    df1 = pd.read_csv("Plant_1_Generation_Data.csv")
    df2 = pd.read_csv("Plant_2_Generation_Data.csv")
    df = pd.concat([df1, df2])
    df = df.dropna()
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])

    plot_week_power(df, "Et9kgGMDl729KT4", "2020-05-25 00:00:00")
    print(gens_with_most_values_under_80percent(df, 5))
