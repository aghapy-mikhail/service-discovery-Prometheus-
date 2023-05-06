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
new_target_name = "myslave3:9104"
label="mysql_master"
# Loop through each dictionary in the list


def add_new_target(data,new_target_name,label):
    for d in data:
        # Add the new target to the "targets" list
        if d["labels"]["job"] == label :           
           d["targets"].append(new_target_name)
    print(data)           
    # The updated data now contains the new item in the "targets" list of each dictionary


add_new_target(data,new_target_name,label)
