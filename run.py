import pandas as pd

from config import nas_key
import requests
import json
import pandas
#ensure api key is working print it out
print()
print(nas_key)

#can find the in usage tab of whatever data we are using in the quad.datanas website/ xom part is the exon mobile stock
#and can change depending on the info im looking for/at. Took the date out to get multi dates. Dont use their api key
# as we have our own
# ? is parameter saying this is the info that's being given
#everything is adaptable might be able to take out the ticker to get all stocks

url = "https://data.nasdaq.com/api/v3/datatables/QUOTEMEDIA/PRICES?&ticker=XOM&api_key=" + nas_key
print(url)

# retrieves the data from the url
response = requests.get(url)

if response.status_code != 200: #200 means gtg
    print(response.status_code)
    exit() #if not gtg it'll stop the code

#Alternative way to double check code
#if response.ok!= 200: #200 means gtg
    #print("GTG")



#prints as if a dictionary
print(response.json())

#Using 2 different programs buoth jsonn request and python dump
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)

print(response.text)




#making list of json function..... i think its a unfciton/module/statement possible
json_data_ex = [{
    "ticker": "XOM",
    "dividend": 35.28,
    "volume": 2500


}]
##ETL =  Extract .....

df = pd.DataFrame.from_dict(json_data_ex)
print(df)
#remember want to loop over the data
colum_data = response.json()["datatable"]["columns"]

new_colm = []
for data in colum_data:
    new_colm.append(data["name"])
print(new_colm)

main_data = response.json()["datatable"]["data"]
print(main_data)

df = pd.DataFrame(main_data, columns=new_colm)
print(df)

