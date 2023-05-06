
# Your original data
data = [
  {
    "targets": [ "myslave1:9104", "myslave2:9104" ],
    "labels": {
      "env": "prod",
      "job": "mysql_slave"
    }
  },
  {
    "targets": [ "mymaster:9104" ],
    "labels": {
      "env": "prod",
      "job": "mysql_master"
    }
  },
  {
    "targets": [ "mymaster:9100", "myslave1:9100", "myslave2:9100" ],
    "labels": {
      "env": "prod",
      "job": "node"
    }
  }
]
# The item to add to the "targets" list
new_target = "myslave3:9104"
# Loop through each dictionary in the list
for d in data:
    # Add the new target to the "targets" list
    if d["labels"]["job"] == "mysql_master":
       d["targets"].append(new_target)

# The updated data now contains the new item in the "targets" list of each dictionary
print(data)
