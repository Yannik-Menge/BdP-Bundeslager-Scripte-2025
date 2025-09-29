
import pathlib

import pandas as pd

from Tools.Pretix_API import Pretix_API

user = Pretix_API()
path = str(pathlib.Path(__file__).parent.resolve())


staemme = pd.read_csv(path+"\\data\\"+"",delimiter=";").to_dict(orient="records")


for stamm in staemme:
    
    update_dict = {
        "name" : f'LaPfiLa Anmeldung - {stamm["name"]} ',
        "slug" : f'{stamm["alias"]} ',
        "date_from": "2026-07-30T00:00:00+02:00",
        "date_to": "2024-08-09T00:00:00+02:00"
        
    }
    
    r = user.clone_event("lapfila", update_dict)
    
# stamm.update(
#        {
#           "public_url" : r["public_url"],
#           "backend_url" : f'https://ticket.pfadfinderei.de/api/v1/organizers/lapfila/{stamm["alias"]}'
#       }          
#    )
    print(stamm["alias"])
    
    

df = pd.DataFrame(staemme)
df.to_csv('output.csv', index=False, header=True)