import requests
import datetime as dt
from tabulate import tabulate
import sys




# print(f"Legal Name: {jsonify['result']['source_output']['legal_name']}")
def date(received):
    if "-" in received:
        
        d_o_r = received.split("-")

        year = int(d_o_r[0])
        month = int(d_o_r[1])
        day = int(d_o_r[2])
        d_o_r_new = dt.datetime(year, month, day)
        return d_o_r_new.strftime('%b %d, %Y')
    else:
        return 'NA'
    # print(d_o_r_new.strftime("%b %d %Y"))
    # Sep 15 2022 00:00:00
    # print(f"Date of registration: {d_o_r_new.strftime('%b %d, %Y')}")

# print(f"GSTIN Status: {jsonify['result']['source_output']['gstin_status']}")

def trd_name(jsonify_trd):
    lsss = ["1","2","3","4","5","6","7","8","9","0"]
    count = 0
    for i in range(len(jsonify_trd)):
        if jsonify_trd[i] in lsss:
          count = count + 1


    if count == 0:
        trade_nam = jsonify_trd
        return trade_nam
    else:
        return "NA"
    # print(f"Trade name: {tradeName}")

def addres():
    base_addr = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['door_number']


    dist = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['dst']

    location = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['location']
    #taluka

    pincode = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['pincode']

    state = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['state_name']

    return f"{base_addr}, {location}, {dist}, {state}, {pincode}"

# print(f"Address: {base_addr}, {location}, {dist}, {state}, {pincode}")
def tx_p_type(rcv_type):
    return rcv_type

# print(f"Taxpayer type: {tp_type}")



'''
print(f"Nature of business activity:")
for i in range(len(jsonify['result']['source_output']['nature_of_business_activity'])):
    print(b_a[i])
'''

def nat_of_wok(nooow):
    lsss = ["1","2","3","4","5","6","7","8","9","0"]
    count = 0
    for i in range(len(nooow)):
        if nooow[i] in lsss:
          count = count + 1


    if count == 0:
        return nooow
    else:
        return "NA"
    # print(f"Nature of principal place of business: {n_o_w}")

def main():
    url = "https://gst-verification.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_gst_certificate"

    gstin = input("Enter the GSTIN : ")


    if len(gstin) != 15:
      sys.exit("GSTIN is either too short or too long!")

    print("")

    payload = {
        "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
	    "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
        "data": {"gstin": gstin}
    }
    headers = {
        "content-type": "application/json",
	    "X-RapidAPI-Key": "73adfb854emshbf64d78a4d8f881p18823cjsnad21eccdd68b",
	    "X-RapidAPI-Host": "gst-verification.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    global jsonify
    jsonify = response.json()
    # print(jsonify)



    b_a = []
    for i in jsonify['result']['source_output']['nature_of_business_activity']:
        b_a.append(i)

    mylist = [
        ['Legal Name:',jsonify['result']['source_output']['legal_name']],
        ['Date of registration:',date(jsonify['result']['source_output']['date_of_registration'])],
        ['GSTIN Status:',jsonify['result']['source_output']['gstin_status']],
        ['Trade name:',trd_name(jsonify['result']['source_output']['trade_name'])],
        ['Address:',addres()],
        ['Taxpayer type:',tx_p_type(jsonify['result']['source_output']['taxpayer_type'])],
        ['Nature of business activity:',b_a],
        ['Nature of place of business:',nat_of_wok(jsonify['result']['source_output']['principal_place_of_business_fields']['nature_of_principal_place_of_business'])]
    ]

    print(tabulate(mylist, tablefmt="outline"))



if __name__ == "__main__":
    main()