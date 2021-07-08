import json
import requests
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script need to be given the name of the json file")
    print("")
    print("python3 upload_racks.py input.json")
    print("")
    print("python3 upload_racks.py input.json")
    print("")
    exit()

headers = {"Content-Type": "application/json", "Accept": "application/json"}
try:
    with open("config.json", "r") as config:
        credentials = json.load(config)
        user = credentials['USERNAME']
        pwd = credentials['PASSWORD']
        url = credentials['URL']
except:
    print("unable to load config file")
    exit()
try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import json")
    exit()
print("<unload>")
for data in snow_data:
    print("<u_dcse_datacentervr_blocks action=\"INSERT_OR_UPDATE\">")
    print("<u_block_blue>" + str(data['u_block_blue']) + "</u_block_blue>")
    print("<u_block_green>" + str(data['u_block_green']) + "</u_block_green>")
    print("<u_block_name>" + data['u_block_name'] + "</u_block_name>")
    print("<u_block_red>" + str(data['u_block_red']) + "</u_block_red>")
    if (data['u_has_lines']):
        print("<u_has_lines>true</u_has_lines>")
    else:
        print("<u_has_lines>false</u_has_lines>")
    print("<u_line_blue>" + str(data['u_line_blue']) + "</u_line_blue>")
    print("<u_line_green>" + str(data['u_line_green']) + "</u_line_green>")
    print("<u_line_red>" + str(data['u_line_red']) + "</u_line_red>")
    print("<u_room_name>" + data['u_room_name'] + "</u_room_name>")
    print("<u_x_center>" + str(data['u_x_center']) + "</u_x_center>")
    print("<u_x_size>" + str(data['u_x_size']) + "</u_x_size>")
    print("<u_y_center>" + str(data['u_y_center']) + "</u_y_center>")
    print("<u_y_size>" + str(data['u_y_size']) + "</u_y_size>")
    print("<u_z_center>" + str(data['u_z_center']) + "</u_z_center>")
    print("<u_z_size>" + str(data['u_z_size']) + "</u_z_size>")
    print("</u_dcse_datacentervr_blocks>")
print("</unload>")
