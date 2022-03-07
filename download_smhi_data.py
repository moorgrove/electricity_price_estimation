import requests
import os
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
hourNow = int(datetime.now().strftime("%H"))
time = datetime.now().strftime("%H0000")

print('Today:', today)
print('Hour Now:', hourNow)

root_path = '/mount/smhi_weather_download/data/'

# Wind
path_wind = root_path + 'smhi_wind_' + today + '_' + time

if os.path.exists(path_wind) == False:
    os.mkdir(path_wind)

print('Downloading wind')

for day in range(0,11):
    for hour in range(hourNow,24):
        if hour < 10:
            hour = '0' + str(hour) + '0000'
        else:
            hour = str(hour) + '0000'

        predict_date = datetime.fromtimestamp(datetime.now().timestamp() + 60*60*24*day).strftime("%Y%m%d") + 'T' + hour + 'Z'

        url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/multipoint/validtime/' + predict_date + '/parameter/ws/leveltype/hl/level/10/data.json?with-geo=false'
        r = requests.get(url, allow_redirects=True)

        open(path_wind + '/smhi_wind_' + predict_date + '.json', 'wb').write(r.content)
        #open(path_wind + '/smhi_wind_' + predict_date + '.json', 'wb').close()
        
# Wind direction
path_wind_dir = root_path + 'smhi_wind_dir_' + today + '_' + time

if os.path.exists(path_wind_dir) == False:
    os.mkdir(path_wind_dir)

print('Downloading wind direction')

for day in range(0,11):
    for hour in range(hourNow,24):
        if hour < 10:
            hour = '0' + str(hour) + '0000'
        else:
            hour = str(hour) + '0000'

        predict_date = datetime.fromtimestamp(datetime.now().timestamp() + 60*60*24*day).strftime("%Y%m%d") + 'T' + hour + 'Z'

        url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/multipoint/validtime/' + predict_date + '/parameter/wd/leveltype/hl/level/10/data.json?with-geo=false'
        r = requests.get(url, allow_redirects=True)

        open(path_wind_dir + '/smhi_wind_dir_' + predict_date + '.json', 'wb').write(r.content)
        #open(path_wind_dir + '/smhi_wind_dir_' + predict_date + '.json', 'wb').close()

# Temperature
path_temperature = root_path + 'smhi_temperature_' + today + '_' + time

if os.path.exists(path_temperature) == False:
    os.mkdir(path_temperature)

print('Downloading temperature')

for day in range(0,11):
    for hour in range(hourNow,24):
        if hour < 10:
            hour = '0' + str(hour) + '0000'
        else:
            hour = str(hour) + '0000'

        predict_date = datetime.fromtimestamp(datetime.now().timestamp() + 60*60*24*day).strftime("%Y%m%d") + 'T' + hour + 'Z'

        url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/multipoint/validtime/' + predict_date + '/parameter/t/leveltype/hl/level/2/data.json?with-geo=false'
        r = requests.get(url, allow_redirects=True)

        open(path_temperature + '/smhi_temperature_' + predict_date + '.json', 'wb').write(r.content)
        #open(path_temperature + '/smhi_temperature_' + predict_date + '.json', 'wb').close()

# Weather symbol
path_Wsymb2 = root_path + 'smhi_Wsymb2_' + today + '_' + time

if os.path.exists(path_Wsymb2) == False:
    os.mkdir(path_Wsymb2)

print('Downloading weather symbol')

for day in range(0,11):
    for hour in range(hourNow,24):
        if hour < 10:
            hour = '0' + str(hour) + '0000'
        else:
            hour = str(hour) + '0000'

        predict_date = datetime.fromtimestamp(datetime.now().timestamp() + 60*60*24*day).strftime("%Y%m%d") + 'T' + hour + 'Z'

        url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/multipoint/validtime/' + predict_date + '/parameter/t/leveltype/hl/level/2/data.json?with-geo=false'
        r = requests.get(url, allow_redirects=True)

        open(path_Wsymb2 + '/smhi_Wsymb2_' + predict_date + '.json', 'wb').write(r.content)
        #open(path_Wsymb2 + '/smhi_Wsymb2_' + predict_date + '.json', 'wb').close()


# Mean value of total cloud cover
path_tcc_mean = root_path + 'smhi_tcc_mean_' + today + '_' + time

if os.path.exists(path_tcc_mean) == False:
    os.mkdir(path_tcc_mean)

print('Downloading cloud cover')

for day in range(0,11):
    for hour in range(hourNow,24):
        if hour < 10:
            hour = '0' + str(hour) + '0000'
        else:
            hour = str(hour) + '0000'

        predict_date = datetime.fromtimestamp(datetime.now().timestamp() + 60*60*24*day).strftime("%Y%m%d") + 'T' + hour + 'Z'

        url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/multipoint/validtime/' + predict_date + '/parameter/tcc_mean/leveltype/hl/level/0/data.json?with-geo=false'
        r = requests.get(url, allow_redirects=True)

        open(path_tcc_mean + '/smhi_tcc_mean_' + predict_date + '.json', 'wb').write(r.content)
        #open(path_tcc_mean + '/smhi_tcc_mean_' + predict_date + '.json', 'wb').close()
        
print('Done')
