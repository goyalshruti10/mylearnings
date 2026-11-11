##py -m pip install virtualenv

####py -m venv shrutienv

###import requests

import pandas as pd

url = "https://www.vic.gov.au/school-term-dates-and-holidays-victoria"

#response = requests.get(url)

df = pd.read_html(url)[0:4]

print(df)