# import csv
import pandas


# 1. using import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)




# 2. using import pandas. This reads a TradeZero .csv file
# data = pandas.read_csv("trade_data.csv")
# net = round(data["Net Proceeds"].sum(),2)
# gross = round(data["Gross Proceeds"].sum(),2)
# commissions = round(data["Comm"].sum(),2)
# net_trading = round(net - gross, 2)
# sec = round(data["SEC"].sum(), 2)
# taf = round(data["TAF"].sum(),2)
# nscc = round(data["NSCC"].sum(),2)
# nasdaq = round(data["Nasdaq"].sum(),2)
# ecn_total = sec + taf + nscc + nasdaq
# qty = round(data["Qty"].sum())
# qty_average = round((data["Qty"].mean()))
# highest_price = round(data["Price"].max(), 2)
# currency_conversion = 0.82
#
# print(f"Total $ (Trading + Commissions): ${net}")
# print(f"Total (Trading): ${net_trading}")
# print(f"Total Platform Commissions: ${commissions}")
# print(f"Total ECN Commissions: ${ecn_total}")
# print(f"Total Shares Traded: {qty}")
# print(f"Average Shares Traded: {qty_average}")
# print(f"Highest Priced Share: ${highest_price}")
# print("*****************************************")
# print(f"Total € (Trading + Commissions): €{round(int(net) * currency_conversion, 2)}")

# more advanced queries. Getting rows.
# setting max_val to the row that has the highest gross proceeds. Then
# getting the symbol of that row
# max_val = data[data["Gross Proceeds"] == data["Gross Proceeds"].max()]
# print(max_val["Symbol"])

# date = data[data["T/D"] == "02/22/2019"]
# rows_date = date[date["Symbol"] == "HYRE"]
# print(rows_date)



# 3. using import pandas. Analysing squirrel data
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# all_primary = data["Primary Fur Color"]
# gray = 0
# cinnamon = 0
# black = 0
# for color in all_primary:
#     if color == "Gray":
#         gray += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#     elif color == "Black":
#         black += 1
# # print(all_primary)
# print(gray)
# print(cinnamon)
# print(black)
# new_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray, cinnamon, black]
# }
#
# data_for_csv = pandas.DataFrame(new_dict)
# data_for_csv.to_csv("squirrel_count.csv")

# alternate method for squirrel count
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
new_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}

data_for_csv = pandas.DataFrame(new_dict)
data_for_csv.to_csv("squirrel_count.csv")