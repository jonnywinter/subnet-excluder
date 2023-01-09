#--- Documentation
#------ RFC Reserved ranges - https://www.rfc-editor.org/rfc/rfc6890

from ipaddress import ip_network, collapse_addresses

def findSubnets(largerSubnet, excludedSubnets):
    for excludedSubnet in excludedSubnets:
        excludedSubnet = ip_network(excludedSubnet)
        newSubnets = []
        for sub in largerSubnet:
            if excludedSubnet.subnet_of(sub):
                newSubnets.extend(list(sub.address_exclude(excludedSubnet)))
            else:
                newSubnets.append(sub)
        largerSubnet = newSubnets
    return list(collapse_addresses(newSubnets))

ipv4ReservedRanges = ['0.0.0.0/8','10.0.0.0/8','100.64.0.0/10','127.0.0.0/8','169.254.0.0/16','172.16.0.0/12','192.0.0.0/24','192.0.2.0/24','192.88.99.0/24','192.168.0.0/16','198.18.0.0/15','198.51.100.0/24','203.0.113.0/24','224.0.0.0/4','240.0.0.0/4']
exclusions = ['52.3.4.5/32']
result = findSubnets([ip_network('0.0.0.0/0')], ipv4ReservedRanges + exclusions)

for i in result:
  print(i)