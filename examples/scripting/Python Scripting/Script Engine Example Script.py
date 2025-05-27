# encoding:utf-8
from __future__ import print_function
from scriptengine import *
import sys
import os

# Environment setup
script_path = os.getcwd()
sys.path.append(script_path)

# Configuration
PROJECT_NAME = 'Script Engine Example.project'
DEVICE_NAME = 'Your Device Name'
GATEWAY_NAME = 'Gateway-1'
BOILERPLATE_CODE = '// Some boiler plate code'
TARGET_TREE_OBJECT = 'PLC_PRG'
FIND_TYPE = 'Device'


def scan_for_devices():
    found_devices = projects.primary.find(FIND_TYPE, False)
    assert(found_devices and len(found_devices) == 1, 'No or more than one device found')
    selected_device = found_devices[0]
    gateway = online.gateways[GATEWAY_NAME]
    targets = gateway.perform_network_scan()
    matching_target = None

    for target in targets:
        print("Name: {} Addr: {}".format(target.device_name, target.address))
        if DEVICE_NAME in target.device_name:
            matching_target = target
            break
    if matching_target:
        print("Applying gateway settings...")
        selected_device.set_gateway_and_device_name(gateway, target.device_name)
    return found_devices

def main():
    if projects.primary:
        projects.primary.close()

    project_path = script_path + "\\"+ PROJECT_NAME
    project = projects.open(project_path)
    app = project.active_application

    # Inset boilerplate code
    tree_object = app.find(TARGET_TREE_OBJECT, recursive = True)[0]
    line_number = 0
    line_offset = 0
    tree_object.textual_implementation.insert(line_number, line_offset, BOILERPLATE_CODE)

    # Download to device
    device_found = scan_for_devices()

    if device_found:
        print("Downloading to device, do not close this window...")
        online_app = online.create_online_application(app)
        online_app.login(OnlineChangeOption.Never, True)
    else:
        print("Device not found!")

    # Checks and cleanup
    if online_app.application_state != ApplicationState.run:
        online_app.start()
        print("Download Successful")
    else:
        print("Download failed!")

    # Optional logout, save and close
    #online_app.logout()
    #project.save()
    #project.close()

if __name__ == "__main__":
    main()