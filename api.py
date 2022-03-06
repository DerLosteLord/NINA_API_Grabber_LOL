import requests
import json
import time
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



# Gebietscode von https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json
# ab Stelle 6 nur Nullen verwenden!
ninaBaseUrl = "https://warnung.bund.de/api31"
gebietscodeAugsburg="130750000000"
 

response = requests.get(ninaBaseUrl+"/dashboard/"+gebietscodeAugsburg+".json") # TODO:


warnungen = response.json()
baum = 1

while baum == 1: 
    for warnung in warnungen:
        
        clearConsole()
        id = warnung["payload"]["id"]
        warningDetails = requests.get(ninaBaseUrl+"/warnings/"+id+".json").json() # TODO:
        
        textp = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["description"]
        severitya = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["severity"]
        urgencya = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["urgency"]
        certaintya = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["certainty"]
        eventa = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["event"]
        texta = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["description"]

        severityb = severitya.split(": ", 1)
        urgencyb = urgencya.split(": ", 1)
        certaintyb = certaintya.split(": ", 1)
        eventb = eventa.split(": ", 1)
        textb = texta.split(": ", 1)

        severityc = severityb[1]
        urgencyc = urgencyb[1]
        certaintyc = certaintyb[1]
        eventc = eventb[1]
        #textc = textb[1]
        textc = ""


        if (textp.startswith("Coronavirus") != True):
            print(f'{urgencyc},{severityc},{certaintyc},{eventc},{textc}')
            
        time.sleep(5)