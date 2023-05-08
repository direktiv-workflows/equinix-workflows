import packet
import os
import json
import pprint

manager = packet.Manager(auth_token=os.environ["EQUINIX_METAL_TOKEN"])
pprint.pprint(vars(manager))

projects_dict = dict()
devices_dict = dict()

projects = manager.list_projects()
for project in projects:
    pprint.pprint(project)
#jsonProjects['projects]'] = json.dumps(projects)
#print(projects)
#print(type(projects[0]))
#my_dict['projects'] = projects

devices = manager.list_devices(project_id=os.environ["PROJECT_ID"])
for device in devices:
    pprint.pprint(vars(manager.get_device(device.id)))
    #print(manager.get_device(device))
#print(devices[0])
#print(type(devices[0]))
#my_dict['devices'] = devices
#print(type(my_dict))
#json_object = json.dumps(my_dict, indent = 4) 
#print(my_dict)

jsonStr = json.dumps(laptop1.__dict__)