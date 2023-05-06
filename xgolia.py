# By dsweb19778

import requests
import json
import colorama

# Set some colors
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE

# Logo & headers
print(red, """
  ┏━┓┏━┳━━━┓╋╋┏┓
  ┗┓┗┛┏┫┏━┓┃╋╋┃┃
  ╋┗┓┏┛┃┃╋┗╋━━┫┃┏┳━━┓
  ╋┏┛┗┓┃┃┏━┫┏┓┃┃┣┫┏┓┃
  ┏┛┏┓┗┫┗┻━┃┗┛┃┗┫┃┏┓┃
  ┗━┛┗━┻━━━┻━━┻━┻┻┛┗┛
""")
print(green, " # by [DSWEB19778]")

# take info from user
appid = input(blue+"  # APPID : ")
key = input(blue+"  # KEY : ")

# trying to get info
try:

    baseurl = "https://{}-1.algolia.net/1/keys/{}?x-algolia-application-id={}&x-algolia-api-key={}".format(appid, key, appid.upper(), key)
    getdata = requests.get(url=baseurl).text
    tojson = json.loads(getdata)
    if "Invalid Application-ID or API key" in tojson:

        print(red, " [-] Invalid Keys")
        print(red, " [-] Message : ", tojson)

    elif key in tojson['value']:

        print(green, " [+] Valid Keys")
        print(green, " [+] Trying to get info...")

        # check if the keys misconfigured or not
        acls = tojson['acl']
        aclscount = len(acls)
        is_vuln = 0
        if aclscount == 1:
            for aclsc in acls:
                if "search" in aclsc:
                    break;
        else:
            is_vuln = is_vuln + 1

        if is_vuln == 1:
            print(red, " [-] This keys is misconfigured")
        else:
            print(red, " [-] This keys is not misconfigured")

        # Get Permissions
        print(green, " [+] Permissions : ")
        for acls in tojson['acl']:
            print(blue, " [+] ", acls)

        # get Indexes
        print(green, " [+] Indexes : ", )
        for indexex in tojson['indexes']:
            print(blue, " [+] ", indexex)

    else:

        print(red, " [-] Error")

except Exception as er:
    print(red, " [-] Error : ", er)
