# Imports ---------------------------------------------------------------------
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# Imports ---------------------------------------------------------------------

#M49 Country codes ------------------------------------------------------------
keys = [4,8,10,12,16,20,24,28,31,32,36,40,44,48,50,51,52,56,58,60,64,68,70,72,
        74,76,80,84,86,90,92,96,97,100,104,108,112,116,120,124,129,132,136,140,
        144,148,152,156,162,166,170,174,175,178,180,184,188,191,192,196,200,
        203,204,208,212,214,218,221,222,226,230,231,232,233,234,238,239,242,
        246,248,250,251,254,258,260,262,266,268,270,275,276,278,280,283,288,
        290,292,296,300,304,308,312,316,320,324,328,332,334,336,340,344,348,
        352,356,360,364,368,372,376,380,384,388,392,398,400,404,408,410,412,
        414,417,418,422,426,428,430,434,438,440,442,446,450,454,457,458,459,
        461,462,466,470,471,472,474,478,480,484,488,490,492,496,498,499,500,
        504,508,512,516,520,524,527,528,530,531,532,533,534,535,536,540,548,
        554,558,562,566,568,570,574,577,578,579,580,581,582,583,584,585,586,
        588,590,591,592,598,600,604,608,612,616,620,624,626,630,634,636,637,
        638,642,643,646,647,652,654,658,659,660,662,663,666,670,674,678,680,
        682,686,688,690,694,697,698,699,702,703,704,705,706,710,711,716,717,
        720,724,728,729,732,736,740,744,748,752,756,757,760,762,764,768,772,
        776,780,784,788,792,795,796,798,800,804,807,810,818,826,831,832,833,
        834,835,836,837,838,839,840,841,842,849,850,854,858,860,862,866,868,
        872,876,879,882,886,887,890,891,894]
#M49 Country codes ------------------------------------------------------------

#Conutry names ----------------------------------------------------------------
values = ["Afghanistan","Albania","Antarctica","Algeria","American Samoa",
          "Andorra","Angola","Antigua and Barbuda","Azerbaijan","Argentina",
          "Australia","Austria","Bahamas","Bahrain","Bangladesh","Armenia",
          "Barbados","Belgium","Belgium-Luxembourg","Bermuda","Bhutan",
          "Bolivia","Bosnia and Herzegovina","Botswana","Bouvet Island",
          "Brazil","British Antarctic Territories","Belize",
          "British Indian Ocean Territories","Solomon Islands",
          "British Virgin Islands","Brunei Darussalam","European Union (28)",
          "Bulgaria","Myanmar","Burundi","Belarus","Cambodia","Cameroon",
          "Canada","Caribbean, not elsewhere specified","Cape Verde",
          "Cayman Islands","Central African Republic","Sri Lanka","Chad",
          "Chile","China","Christmas Island","Cocos (Keeling) Islands",
          "Colombia","Comoros","Mayotte","Congo",
          "Democratic Republic of the Congo","Cook Islands","Costa Rica",
          "Croatia","Cuba","Cyprus","Former Czechoslovakia","Czechia","Benin",
          "Denmark","Dominica","Dominican Republic","Ecuador",
          "Eastern Europe, not elsewhere specified","El Salvador",
          "Equatorial Guinea","Former Ethiopia","Ethiopia","Eritrea","Estonia",
          "Faeroe Islands","Falkland Islands (Malvinas)",
          "South Georgia and the South Sandwich Islands","Fiji","Finland",
          "Åland Islands","France","France and Monaco",
          "French Guiana","French Polynesia","French Southern Territories",
          "Djibouti","Gabon","Georgia","Gambia","State of Palestine","Germany",
          "Former Democratic Republic of Germany",
          "Former Federal Republic of Germany",
          "South America not elsewhere specified","Ghana",
          "Northern Africa, not elsewhere specified","Gibraltar","Kiribati",
          "Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala",
          "Guinea","Guyana","Haiti","Heard Island and McDonald Islands",
          "Holy See","Honduras","China Hong Kong","Hungary","Iceland",
          "India, excluding Sikkim","Indonesia","Iran","Iraq","Ireland",
          "Israel","Italy","Côte d'Ivoire","Jamaica","Japan","Kazakhstan",
          "Jordan","Kenya","Democratic People's Republic of Korea",
          "Republic of Korea","Kosovo","Kuwait","Kyrgyzstan",
          "Lao People's Democratic Republic","Lebanon","Lesotho","Latvia",
          "Liberia","Libya","Liechtenstein","Lithuania","Luxembourg",
          "China Macau","Madagascar","Malawi","Sarawak","Malaysia",
          "Peninsula Malaysia","Sabah","Maldives","Mali","Malta",
          "Central American Common Market, not elsewhere specified",
          "Africa CAMEU region, not elsewhere specified","Martinique",
          "Mauritania","Mauritius","Mexico","Midway Islands",
          "Asia, not elsewhere specified","Monaco","Mongolia",
          "Republic of Moldova","Montenegro","Montserrat","Morocco",
          "Mozambique","Oman","Namibia","Nauru","Nepal",
          "Oceania, not elsewhere specified","Netherlands",
          "Former Netherlands Antilles, excluding Aruba","Curaçao",
          "Former Netherlands Antilles, including Aruba","Aruba",
          "Sint Maarten (Dutch part)","Bonaire, Saint Eustatius and Saba",
          "Neutral zone","New Caledonia","Vanuatu","New Zealand","Nicaragua",
          "Niger","Nigeria","Europe, not elsewhere specified","Niue",
          "Norfolk Island","Africa, not elsewhere specified",
          "Norway, excluding Svalbard and Jan Mayen","Norway",
          "Northern Mariana Islands","United States Minor Outlying Islands",
          "Former Pacific Islands (Trust Territory)",
          "Micronesia(Federated States of)","Marshall Islands","Palau",
          "Pakistan","East and West Pakistan",
          "Former Panama, excluding Canal Zone","Panama",
          "Former Panama-Canal-Zone","Papua New Guinea","Paraguay","Peru",
          "Philippines","Pitcairn","Poland","Portugal","Guinea-Bissau",
          "Timor-Leste","Puerto Rico","Qatar",
          "Rest of America, not elsewhere specified",
          "Northern and Central America nes","Réunion","Romania",
          "Russian Federation","Rwanda","Ryukyu Island","Saint-Barthélemy",
          "Saint Helena","Saint Kitts, Nevis and Anguilla",
          "Saint Kitts and Nevis","Anguilla","Saint Lucia",
          "Saint Martin (French part)","Saint Pierre and Miquelon",
          "Saint Vincent and the Grenadines","San Marino",
          "Sao Tome and Principe","Sark","Saudi Arabia","Senegal","Serbia",
          "Seychelles","Sierra Leone","Europe EFTA, not elsewhere specified",
          "Sikkim","India","Singapore","Slovakia","Vietnam","Slovenia",
          "Somalia","South Africa","Southern African Customs Union","Zimbabwe",
          "Former Rhodesia Nyas","Former Democratic Yemen","Spain",
          "South Sudan","Sudan","Western Sahara","Former Sudan","Suriname",
          "Svalbard and Jan Mayen Islands","Eswatini","Sweden","Switzerland",
          "Switzerland","Syrian Arab Republic","Tajikistan","Thailand","Togo",
          "Tokelau","Tonga","Trinidad and Tobago","United Arab Emirates",
          "Tunisia","Turkey","Turkmenistan","Turks and Caicos Islands",
          "Tuvalu","Uganda","Ukraine","North Macedonia",
          "Former Union of Soviet Socialist Republics","Egypt",
          "United Kingdom","Guernsey","Jersey","Isle of Man","Tanzania",
          "Former Tanganyika","Former Zanzibar and Pemba Island","Bunkers",
          "Free Zones","Special Categories","United States of America",
          "United States of America, including Puerto Rico",
          "United States of America",
          "United States Miscellaneous Pacific Islands",
          "United States Virgin Islands","Burkina Faso","Uruguay","Uzbekistan",
          "Venezuela","Former Democratic Republic of Vietnam",
          "Former Republic of Vietnam","Wake Island",
          "Wallis and Futuna Islands","Western Asia, not elsewhere specified",
          "Samoa","Former Arab Republic of Yemen","Yemen","Former Yugoslavia",
          "Former Serbia and Montenegro","Zambia"]
#Conutry names ----------------------------------------------------------------


Countries_dict = dict(zip(keys, values))
TrTy_dict = {"M": 'Import', "X": "Export"}
years_list = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,
              2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,
              2016,2017,2018,2019,2020]
dataset = []
base_url = 'https://comtradeapi.un.org/public/V1/preview/'
#varaibles --------------------------------------------------------------------

#Function to fetch and clean Data ---------------------------------------------
def fetch_trade_data(country_code, year):
    url = f'{base_url}S/A/EB?reporterCode={country_code}&period={year}&partnerCode=0&motCode=0&cmdCode=200&flowCode=M,X'
    response = requests.get(url)
    data = response.json()
    if data['count'] == 0:
        return

    for dato in data ['data']:
        Trade_Table = {
        "Country": Countries_dict[(dato['reporterCode'])],
        "Year": dato['period'],
        "Trade Type": TrTy_dict[dato['flowCode']],
        "Trade Value": dato['primaryValue']
        }
        dataset.append(Trade_Table)

    return dataset
#End of function to fetch and clean Data --------------------------------------

#Format the country codes to use them as string parameter on the API ----------
country_code = ','.join(str(val) for val in keys)

#Fetching each year Data ------------------------------------------------------
for year in years_list:
    trade_data = fetch_trade_data(country_code, year)
    time.sleep(5) #the server needs a delay, otherways response not OK
#Fetching each year Data ------------------------------------------------------

#Grouping Data ----------------------------------------------------------------
data_frame = pd.DataFrame(trade_data)
grouped_df = data_frame.groupby('Country').sum()
grouped_df['Total Trade'] = grouped_df['Trade Value']
grouped_df = grouped_df[['Total Trade']]
grouped_df = grouped_df.sort_values('Total Trade', ascending=False)
#Grouping Data ----------------------------------------------------------------

# Get the top 10 and bottom 10 countries --------------------------------------
top_10_countries = grouped_df.head(10)
bottom_10_countries = grouped_df.tail(10)
# Get the top 10 and bottom 10 countries --------------------------------------

print(top_10_countries)
print(bottom_10_countries)

# Plotting the top 10 countries -----------------------------------------------
plt.figure(figsize=(10, 6))
bar_width = 0.8
x_offset = bar_width / 2
plt.bar(
    top_10_countries.index, top_10_countries['Total Trade'],
    width=bar_width, align='center'
)
plt.xlabel('Country')
plt.ylabel('Trade Volume\n(US$ Millions of Millions)')
plt.title('Top 10 Countries in International Trade in Services (EBOPS)\n(1990-2020)')
# Set an offset to the right for the x-axis labels
plt.gca().set_xticklabels(
    top_10_countries.index,
    rotation=45,
    fontsize=8,
    ha='right',
    va='top',
    rotation_mode='anchor',
    x=-0.5,
)
def millions_millions_formatter(x, pos):
    return f'{x/1e12:.2f}'

formatter = ticker.FuncFormatter(millions_millions_formatter)
plt.gca().yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.show()
# End of Plotting the top 10 countries ----------------------------------------

# Plotting the bottom 10 countries --------------------------------------------
plt.figure(figsize=(10, 6))
bar_width = 0.8
x_offset = bar_width / 2
plt.bar(
    bottom_10_countries.index, bottom_10_countries['Total Trade'],
    width=bar_width, align='center'
)
plt.xlabel('Country')
plt.ylabel('Trade Volume\n(US$ Thusands of Millions)')
plt.title('Bottom 10 Countries in International Trade in Services (EBOPS)\n(1990-2020)')
# Set an offset to the right for the x-axis labels
plt.gca().set_xticklabels(
    bottom_10_countries.index,
    rotation=45,
    fontsize=8,
    ha='right',
    va='top',
    rotation_mode='anchor',
    x=-0.5,
)
def millions_millions_formatter(x, pos):
    return f'{x/1e9:.4f}'

formatter = ticker.FuncFormatter(millions_millions_formatter)
plt.gca().yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.show()
# End of Plotting the bottom 10 countries -------------------------------------
