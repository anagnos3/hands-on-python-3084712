import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

print(response.json()[2])

#for year in last_twenty_years:
#  bar_count = year["value"] // 10_000_000
#  print(year["date"], "=" * bar_count)