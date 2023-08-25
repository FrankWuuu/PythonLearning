import json

path = "demo.json"

with open(path,"r") as f:
  data_json = json.load(f)

with open("demo_out.json","w") as f:
  json.dump(data_json,f,indent=4) # indent=4 the indent distance
