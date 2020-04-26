# Native imports
import json
import ipaddress
# Import local file -- (moved JSON data to its own file)
from device_data import deviceJSON


#print(f'The Python data format for the "deviceJSON" variable is {type(deviceJSON)}')
#print()
#print(deviceJSON)

def is_private_address(address: str) -> bool:
    return ipaddress.IPv4Address(address).is_private


if __name__ == '__main__':
    # DeviceJSON is a 'str' so json.loads() is used to handle str input.
    # json.load() takes a file object or a, "'.read()'--supporting file-like object containing a JSON document."
    device_data = json.loads(deviceJSON)

    for interfaces in device_data['interfaces']['interface']:

        for interface, address in interfaces.items():

            if is_private_address(address['ipv4']):
                print(f'{interface} has an IP address of {address["ipv4"]} and is a Private Address')
            else:
                print(f'{interface} has an IP address of {address["ipv4"]} and is not a Private Address')
