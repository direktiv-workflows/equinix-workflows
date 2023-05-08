import packet
import os
import json
import pprint

# Initialise the packet client connection
manager = packet.Manager(auth_token=os.environ["EQUINIX_METAL_TOKEN"])
# pprint.pprint(vars(manager))

# Create the device, with the inputs as follow:
# env: PROJECT_ID = equinix metal project ID
# env: EQUINIX_PLAN = the size of the machine (default: c3.small.x86)
# env: EQUINIX_METRO = location of the machine (default: sv) 
# env: DEVICE_NAME_PREFIX = prefix to the machine name (default: direktiv) 
# env: DEVICE_COUNT = added to the machine name prfeix for hostname
# env: DEVICE_OS operating system for the machine (default: ubuntu_20_04)


# device = manager.create_device(project_id=os.environ["PROJECT_ID"],
#                                hostname=(os.environ["DEVICE_NAME_PREFIX"] + "-" + str(os.environ["DEVICE_COUNT"])),
#                                plan=os.environ["EQUINIX_PLAN"], metro=os.environ["EQUINIX_METRO"],
#                                operating_system=os.environ["DEVICE_OS"])

devices = manager.list_all_devices(project_id=os.environ["PROJECT_ID"])
for deviceId in devices:
    device = manager.get_device(deviceId.id)
    print(device.state)

#print(json.dumps({ "deviceid": device.id }))