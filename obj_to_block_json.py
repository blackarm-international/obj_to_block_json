import json
import requests
import sys

if (len(sys.argv) != 3):
    print("")
    print("this script to be given the name of the obj file and the room name")
    print("python3 obj_to_block_json.py input.obj roomName")
    print("")
    exit()

file_name_obj = sys.argv[1]
file_name_mtl = file_name_obj.replace("obj","mtl")
# process materials
materials = {}
with open(file_name_mtl) as fp:
    line = fp.readline()
    while line:
        if (line.startswith('newmtl ')):
            material_name = line.split(" ")[1].replace("\n","")
            fp.readline()
            fp.readline()
            material_data = fp.readline().split(" ")
            red = float(material_data[1])
            green = float(material_data[2])
            blue = float(material_data[3])
            materials[material_name] = {
                "red": red,
                "green": green,
                "blue": blue
            }
        line = fp.readline()
# process meshes
blocklist = []
with open(file_name_obj) as fp:
    line = fp.readline()
    while line:
        if (line.startswith('o ')):
            name = line.rstrip("\n").split(' ')[1]
            red = 0.0
            green = 0.0
            blue = 0.0
            xmin = None
            xmax = None
            ymin = None
            ymax = None
            zmin = None
            zmax = None
            reading = True
            while reading:
                if (line.startswith('v ')):
                    xyz = line.rstrip("\n").split(' ')
                    #x = float(xyz[3]) * -1
                    #y = float(xyz[2])
                    #z = float(xyz[1])
                    x = float(xyz[1])
                    y = float(xyz[3]) * -1
                    z = float(xyz[2])
                    if (xmin == None):
                        xmin = x
                    if (xmax == None):
                        xmax = x
                    if (ymin == None):
                        ymin = y
                    if (ymax == None):
                        ymax = y
                    if (zmin == None):
                        zmin = z
                    if (zmax == None):
                        zmax = z
                    if (x < xmin):
                        xmin = x
                    if (x  > xmax):
                        xmax = x
                    if (y < ymin):
                        ymin = y
                    if (y > ymax):
                        ymax = y
                    if (z < zmin):
                        zmin = z
                    if (z > zmax):
                        zmax = z
                if (line.startswith('usemtl')):
                    reading = False
                    material_name = line.split(" ")[1].replace("\n","")
                    if (material_name in materials):
                        red = materials[material_name]['red']
                        green = materials[material_name]['green']
                        blue = materials[material_name]['blue']
                    blocklist.append({
                        "u_block_blue": blue,
                        "u_block_green": green,
                        "u_block_name": name,
                        "u_block_red": red,
                        "u_has_lines": False,
                        "u_line_blue": 0.0,
                        "u_line_green": 0.0,
                        "u_line_red": 0.0,
                        "u_room_name": sys.argv[2],
                        "u_x_center": round((xmin + xmax) * 0.5, 4),
                        "u_x_size": round(xmax - xmin, 4),
                        "u_y_center": round((ymin + ymax) * 0.5, 4),
                        "u_y_size": round(ymax - ymin, 4),
                        "u_z_center": round((zmin + zmax) * 0.5, 4),
                        "u_z_size": round(zmax - zmin, 4)
                    })
                line = fp.readline()
        line = fp.readline()
print(json.dumps(blocklist, indent=4, sort_keys=True))
