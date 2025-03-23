import requests
import json
import xml.dom.minidom
import xmltodict
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://10.10.20.1/cucm-uds'
endpoint = 'servers'

users_url = f'{url}/{endpoint}'

username = 'administrator'
pw = 'ciscopsdt'

headers = {
    'Accept': 'application/xml',
    'Content-type': 'application/xml'
}

response = requests.get(
    users_url,
    headers=headers,
    auth=(username, pw),
    verify=False
)

tree = xml.dom.minidom.parseString(response.text)
pretty = tree.toprettyxml()
xmldata = xmltodict.parse(pretty)

print(json.dumps(xmldata, indent=2, sort_keys=True))
