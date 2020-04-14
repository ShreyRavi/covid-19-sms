# [COVID-19 SMS Update Service](https://covid-19-sms-update.herokuapp.com/)
A Twilio-powered SMS service that returns COVID-19 stats for zipcode, state, and city. Powered by Flask. Coded for the [Twilio Hackathon](https://dev.to/devteam/announcing-the-twilio-hackathon-on-dev-2lh8).

<img src="https://raw.githubusercontent.com/ShreyRavi/covid-19-sms/master/covid-19-sms-screenshot.PNG" height="30%" width="30%">

## Usage
The COVID-19 SMS Update Service can be used by texting [+1(231) 774-2545](sms://+12317742545) with a zipcode, a City, State Code (such as Chicago, IL), or a state (such as IL or Ohio) to get the latest COVID-19 updates for that area. One can call [+1(231) 774-2545](tel://+12317742545) to get these instructions read out loud.

### Examples
1. Text [+1(231) 774-2545](sms://+12317742545) a zipcode

Input:
```
77001
```
Output:
```
04/13 COVID-19 SMS Update:
Harris County, Texas:
Confirmed Cases: 3629
Deaths: 44
Source: New York Times. Thanks for using COVID-19 SMS Update!
```

2. Text [+1(231) 774-2545](sms://+12317742545) a city, state Code

Input:
```
Kansas City, MO
```
Output:
```
04/13 COVID-19 SMS Update for Kansas City, MO:

Platte County, Missouri:
Confirmed Cases: 25
Deaths: 0

Jackson County, Missouri:
Confirmed Cases: 213
Deaths: 7

Clay County, Missouri:
Confirmed Cases: 48
Deaths: 1

Source: New York Times. Thanks for using COVID-19 SMS Update!
```

3. Text [+1(231) 774-2545](sms://+12317742545) a state

Input:
```
WA
```
Output:
```
04/13 COVID-19 SMS Update for Washington:
Confirmed Cases: 10411
Deaths: 511
Source: New York Times. Thanks for using COVID-19 SMS Update!
```

4. Call [+1(231) 774-2545](tel://+12317742545)

See for yourself!

## [Live Homepage](https://covid-19-sms-update.herokuapp.com/)
The SMS and voice routes are hosted on the Heroku repo above.

## Local Setup
1. Clone Repository
```
git clone https://github.com/ShreyRavi/covid-19-sms.git
```
2. PIP install requirements
```
pip install -r requirements.txt
```
3. Run Flask app and open browser to `http://localhost:5000/`
```
python3 app.py
```
4. Use `ngrok` and Twilio to configure webhooks for your Twilio account.

## Built With
- [Flask](https://palletsprojects.com/p/flask/)
- [Twilio](https://www.twilio.com/)
- [ngrok](https://ngrok.com/)
- [zipcodes](https://pypi.org/project/zipcodes/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Heroku](http://heroku.com/)
- [Gunicorn](https://gunicorn.org/)

## Data Source/Attribution
The COVID-19 data is sourced from the New York Times's public GitHub repository CSV of COVID-19 data, from [here](https://github.com/nytimes/covid-19-data).

## Future Plans
- More intelligent request handling
- Efficiency improvements
- Multiple data sources
- More granular reports
- Regular subscription to reports
