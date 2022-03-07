import json
import pandas as pd
import os
import matplotlib.pyplot as plt

def progress_bar(current, total, bar_length = 20):
  percent = float(current) * 100 / total
  arrow   = '-' * int(percent/100 * bar_length - 1) + '>'
  spaces  = ' ' * (bar_length - len(arrow))

  print('\rProgress: [%s%s] %d %%' % (arrow, spaces, percent), end='')

path = '/smhi_weather_download/data/'

number_of_dirs = 0

for dir in os.listdir(path):
  path_dir = os.path.join(path, dir)
  if os.path.isdir(path_dir) and dir[:11] == 'smhi_wind_2' and dir[-6:] == '000000':
    number_of_dirs += 1
    print('\rNumber of dirs:', number_of_dirs, end='')

print('\nTotal number of dirs to import:', number_of_dirs)

df_days = pd.DataFrame()
#df_days.index.name = 'DateTime'
processed_number_of_dirs = 0

for dir in os.listdir(path):
  path_dir = os.path.join(path, dir)
  df_day = pd.DataFrame()

  if os.path.isdir(path_dir) and dir[:11] == 'smhi_wind_2' and dir[-6:] == '000000':
    progress_bar(processed_number_of_dirs, number_of_dirs)

    for filename in os.listdir(path_dir):
      f = os.path.join(path_dir, filename)
      if os.path.isfile(f) and filename[-5:] == '.json':
        
        with open(f) as data_file:    
          try: 
            data = json.load(data_file)
            data_file.close()
          except:
            print(f)
            continue

        df_hour = pd.DataFrame()
        df_hour = pd.json_normalize(data, record_path=['timeSeries', 'parameters', 'values'])

        try:
          df_day[data['timeSeries'][0]['validTime'][:-1]] = df_hour[df_hour.index % 10000 == 0]
        except:
          continue
    
    df_day.set_index(df_day.index.map(lambda x: dir + ' ' + str(x)), inplace=True)
    df_day = df_day.T
    df_day.set_index(df_day.index.map(lambda x: pd.to_datetime(x, errors='ignore')), inplace=True)
    df_day = df_day.resample('H').nearest()
    df_day.index.name = 'DateTime'

    processed_number_of_dirs += 1
  
  if not df_days.empty:
    if not df_day.empty:
      df_days = df_days.merge(df_day, on='DateTime', how='outer', sort=True)
    else:
      continue
  else:
    if not df_day.empty:
      df_days = df_day
    else:
      continue

progress_bar(processed_number_of_dirs, number_of_dirs)
print('\n')

df_days.to_pickle('/smhi_manipulated_data/df_days.pkl')

