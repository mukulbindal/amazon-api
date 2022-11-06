import os 


properties = {}
properties_not_loaded = True
def set_properties(key, value):
    properties[key] = value 

def get_property(key):
    if key in properties:
        return properties[key]
    else:
        return None

if properties_not_loaded:
    file_path = "E:\\FastApiTutorial\\amazon-api\\resources\\DEV\\application.properties"
    with open(file_path, "r") as f:
        for line in f.readlines():
            key, value = line.split("=")
            set_properties(key, value)
    properties_not_loaded = False 
    print(properties)
            
   