import requests
import pandas as pd
import json

host = "api-in21.leadsquared.com"

#Leads
url = f"https://api-in21.leadsquared.com/v2/LeadManagement.svc/Leads.RecentlyModified"

headers = {
    "x-LSQ-AccessKey": "u$rddebee3ce5d85685847e5149e5253be3",
    "x-LSQ-SecretKey": "26a5557bb1b6cf75134bb799a94fff922b986de3",
    "Content-Type": "application/json"
}

data = {
    "Parameter": {
        "FromDate": "2025-04-04 02:00:00",
        "ToDate": "2025-04-05 02:20:00"
    },
    "Paging": {
        "PageIndex": 1,
        "PageSize": 100
    },
    "Columns": {
        "Include_CSV": "ProspectID"
    },
    "Sorting": {
        "ColumnName": "ProspectAutoId",
        "Direction": "1"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

data = response.json()
leads_list = []

print(response.json().get("RecordCount"))

for lead in data["Leads"]:
    lead_df = pd.DataFrame(lead["LeadPropertyList"][:-5])
    lead_df.set_index("Attribute", inplace=True)
    leads_list.append(lead_df["Value"].to_frame().T)

all_leads_df = pd.concat(leads_list, ignore_index=True)
all_leads_df.to_csv('all_leads.csv', index=False)
