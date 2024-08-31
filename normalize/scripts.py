import pandas as pd
import json
import os

from urllib import request


def normalizer(url):
    req = request.Request(url)
    with request.urlopen(req) as response:
        sheet = response.read()
        sheet = json.loads(sheet)
    # Saving sheet to local storage to allow read into dataframe
    with open('sheet.json', 'w') as f:
        json.dump(sheet, f)
    df = pd.read_json('sheet.json')
    # Delete the json file
    os.remove('sheet.json')

    # Set first row as column headers
    df.columns = df.iloc[0]
    # Delete that row
    df = df.drop([0], axis=0)
    # Set ID as index
    df = df.set_index('Id')

    # Convert to float if possible & then normalize
    def normalize(col):
        try:
            col = pd.to_numeric(col)
            maxi = col.max()
            mini = col.min()
            return (2 * ((col - mini) / (maxi - mini))) - 1
        except ValueError:
            return col

    df = df.apply(normalize, axis=0)


    # reset index
    df = df.reset_index()
    # reset column headers
    df = df.transpose().reset_index(allow_duplicates=True).transpose()

    # Convert to json string
    json_output = df.to_json(orient='values')
    return json_output
