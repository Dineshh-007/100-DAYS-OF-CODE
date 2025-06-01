import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_count = len(data[data['Primary Fur Color']== "Gray"])
cinnamon_fur_count = len(data[data['Primary Fur Color']== "Cinnamon"])
white_fur_count = len(data[data['Primary Fur Color']== "Black"])

data_dict = {
    "fur color" : ["gray","cinnamon","black"] ,
    "total" : [gray_fur_count,cinnamon_fur_count,white_fur_count]
}

data_count = pandas.DataFrame(data_dict)
print(data_count)
data_count.to_csv("data_count.csv")