#get_data.py
#code to retrieve NYT Coronavirus data using Pandas

#imports
import zipcodes
import datetime
import numpy as np
import pandas as pd

#standard error message
ERROR_MSG = "CoronaUpdate ERROR: Your input was invalid! Please text +1(231)774-2545 with a zipcode (ex. 77001), City, State Code (ex. Chicago, IL), or a state (ex. IL or Ohio)."

#states dictionary
states_code_to_full = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

#get corona data from NYT 
URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
data = pd.read_csv(URL)
data = data[data.date == yesterday]

def get_data_from_state(state):
    """get data from NYT csv based on a state lookup"""
    if len(data[data.state == state][['cases']]) == 0:
        return ERROR_MSG
    try:
        return {
            'state': state,
            'confirmed': pd.to_numeric(data[data.state == state][['cases']].sum()).item(),
            'deaths': pd.to_numeric(data[data.state == state][['deaths']].sum()).item(),
        }
    except:
        return -1

def get_data_from_zipcode(zipcode):
    """get data from NYT csv based on a zip-code lookup"""
    #return -1 if zipcode doesn't exist
    if not zipcodes.is_real(zipcode):
        return -1
    try:
        zipcode_result = zipcodes.matching(zipcode)
        state = states_code_to_full[zipcode_result[0]['state']]
        county = zipcode_result[0]['county'].replace('County', '').strip()

        #special case for NYC for NYT data
        if "New York" in county:
            county = "New York City"
        return {
            'state': state,
            'county': county,
            'confirmed': data[data.county == county][data.state == state][['cases']].iat[0,0],
            'deaths': data[data.county == county][data.state == state][['deaths']].iat[0,0],
        }
    except:
        return -1
    
def reply(body):
    """main reply method which switches between types of requests"""
    #if City, State
    if ',' in body:
        return reply_citystate(body)
    #if zipcode
    elif body.isdecimal():
        return reply_zipcode(body)
    #else, try state?
    else:
        return reply_state(body)

def reply_state(state):
    """reply method by State or State Code request"""
    try:
        #if state request is a state code, convert to full state name
        if len(state) == 2:
            state = states_code_to_full[state.upper()]
        dat = get_data_from_state(state.capitalize())
        if dat == -1:
            return ERROR_MSG
        return str(datetime.date.today().strftime("%m/%d")) + " CoronaUpdate for " + dat['state'] + ": \nConfirmed Cases: " + str(dat["confirmed"]) + " \nDeaths: " + str(dat["deaths"]) + "\nSource: New York Times. Thanks for using CoronaUpdate!"
    except:
        return ERROR_MSG

def reply_citystate(body):
    """reply method by City, State Code request"""
    try:
        city = body.split(",")[0].strip().title()
        state = body.split(",")[1].strip().upper()
        if len(state) != 2 or state not in states_code_to_full.keys() or len(city) == 0:
            return ERROR_MSG
        body = city + ", " + state
        msg = str(datetime.date.today().strftime("%m/%d")) + " CoronaUpdate for "+ body +": \n"
        results = zipcodes.filter_by(city=city, state=state)
        temp_list = []
        for res in results:
            rep_zip = reply_zipcode(res['zip_code'], False)
            if rep_zip != ERROR_MSG:
                temp_list.append(rep_zip)
        msg += ''.join(list(set(temp_list))) + "\nSource: New York Times. Thanks for using CoronaUpdate!" if len(temp_list) > 0 else "City data not found. Thanks for using CoronaUpdate!"
        return msg
    except:
        return ERROR_MSG

def reply_zipcode(zipcode, intro=True):
    """reply method by zip-code request"""
    dat = get_data_from_zipcode(zipcode)
    if dat == -1:
        return ERROR_MSG
    try:
        return (str(datetime.date.today().strftime("%m/%d")) + " CoronaUpdate: \n" if intro else "\n") + dat['county'] + " County, " + dat['state'] + ": \nConfirmed Cases: " + str(dat["confirmed"]) + " \nDeaths: " + str(dat["deaths"]) + ("\nSource: New York Times. Thanks for using CoronaUpdate!" if intro else "\n")
    except:
        return ERROR_MSG