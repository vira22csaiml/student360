import requests

host = "api-in21.leadsquared.com"
#Users
url = f"https://marvin-api-in21.leadsquared.com/api/cache/r21/v1/63281/User/Key?key=MANAGE_LEADS&accessKey=u$rddebee3ce5d85685847e5149e5253be3&secretKey=26a5557bb1b6cf75134bb799a94fff922b986de3"

#Leads
#url = f"https://{host}/v2/LeadManagement.svc/LeadsMetaData.Get?schemaName=ProspectID"

#List
#url = f"https://{host}/v2/LeadSegmentation.svc/Lists.GetByLeadId?leadId=LeadId"

accessKey = "u$rddebee3ce5d85685847e5149e5253be3"
secretKey = "26a5557bb1b6cf75134bb799a94fff922b986de3"

headers = {
    "x-LSQ-AccessKey": accessKey,
    "x-LSQ-SecretKey": secretKey
}

response = requests.get(url, headers=headers)
import pandas as pd
import json

data = response.json()

df = pd.DataFrame(data)
df.to_csv('leadsquared_true.csv', index=False)

