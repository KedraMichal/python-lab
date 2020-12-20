import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


def ratio_chosen_gen_to_mean_daily_yield(dataframe, source_key):
    mean_by_day = dataframe.groupby(dataframe["DATE_TIME"].dt.date).mean()

    chosen_gen_daily_yield = dataframe.groupby(["SOURCE_KEY", dataframe["DATE_TIME"].dt.date]).mean()
    chosen_gen_daily_yield = chosen_gen_daily_yield.loc[source_key]
    chosen_gen_daily_yield = chosen_gen_daily_yield.rename(columns={"DAILY_YIELD": "CHOSEN_GEN_DAILY_YIELD"})

    df3 = pd.concat([chosen_gen_daily_yield["CHOSEN_GEN_DAILY_YIELD"], mean_by_day["DAILY_YIELD"]], axis=1)
    df3["Ratio"] = df3["CHOSEN_GEN_DAILY_YIELD"] / df3["DAILY_YIELD"]

    return df3


def get_one_week_data(dataframe, source_key, start_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date = start_date + timedelta(7)
    df_specified_gen = dataframe[dataframe["SOURCE_KEY"] == source_key]
    one_week_df = df_specified_gen[(df_specified_gen["DATE_TIME"] > start_date) & (df_specified_gen["DATE_TIME"] <= end_date)]

    return one_week_df


def line_style1(dataframe, source_key, start_date, which_col, color):
    df = get_one_week_data(dataframe, source_key, start_date)
    plt.plot(df["DATE_TIME"], df[which_col], linewidth=2, color=color)


def line_style2(dataframe, source_key, start_date, which_col, color):
    df = get_one_week_data(dataframe, source_key, start_date)
    plt.plot(df["DATE_TIME"], df[which_col], "--", linewidth=1, color=color)


def plot1(power_column, start_date):
    line_style1(df, "bvBOhCH3iADSZry", start_date, power_column, "red")
    line_style1(df, "3PZuoBAID5Wc2HD", start_date, power_column, "black")
    line_style2(df, "7JYdWkrLSPkdwr4", start_date, power_column, "blue")
    line_style2(df, "VHMLBKoKgIrUVDU", start_date, power_column, "green")
    line_style2(df, "ZnxXDlPa8U1GXgE", start_date, power_column, "purple")
    line_style2(df, "ZoEaEvLYb1n2sOq", start_date, power_column, "orange")


def bar_plot_ratio(dataframe):
    p = dataframe[dataframe["Ratio"] > 1.25].shape[0]
    p1 = dataframe[(dataframe["Ratio"] > 1.15) & (dataframe["Ratio"] < 1.25)].shape[0]
    p2 = dataframe[(dataframe["Ratio"] > 1.05) & (dataframe["Ratio"] < 1.15)].shape[0]
    p3 = dataframe[(dataframe["Ratio"] > 0.95) & (dataframe["Ratio"] < 1.05)].shape[0]
    p4 = dataframe[(dataframe["Ratio"] > 0.85) & (dataframe["Ratio"] < 0.95)].shape[0]
    p5 = dataframe[(dataframe["Ratio"] > 0.75) & (dataframe["Ratio"] < 0.85)].shape[0]
    p6 = dataframe[dataframe["Ratio"] < 0.75].shape[0]
    y_values = [p6, p5, p4, p3, p2, p1, p]
    how_many_col = np.arange(len(y_values))
    plt.bar(how_many_col, y_values)
    plt.xticks(ticks=how_many_col, labels=["<75", "75-85", "85-95", "95-105", "105-115", "115-125", ">125"])
    plt.xlabel("Stosunek DAILY_YIELD generatora do średniej w %")


def main_plot(start_date):
    plt.figure()
    plt.subplot(2, 2, 1)
    plot1("AC_POWER", start_date)
    plt.subplot(2, 2, 2)
    plot1("DC_POWER", start_date)
    plt.subplot(2, 2, 3)
    gen_ratio_df = ratio_chosen_gen_to_mean_daily_yield(df, "1BY6WEcLGh8j5v7")
    bar_plot_ratio(gen_ratio_df)
    plt.subplot(2, 2, 4)
    gen_ratio_df = ratio_chosen_gen_to_mean_daily_yield(df, "3PZuoBAID5Wc2HD")
    bar_plot_ratio(gen_ratio_df)
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("Plant_1_Generation_Data.csv")
    df = df.dropna()
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
    gen1_ratio_df = ratio_chosen_gen_to_mean_daily_yield(df, "1BY6WEcLGh8j5v7")
    gen2_ratio_df = ratio_chosen_gen_to_mean_daily_yield(df, "3PZuoBAID5Wc2HD")
    print(gen1_ratio_df, "\n", gen2_ratio_df)

    main_plot("2020-05-25 00:00:00")



