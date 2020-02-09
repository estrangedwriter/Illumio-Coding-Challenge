#### Illumio Coding Challenge
### Read a CSV file, given a set of firewall rules, a network packet will be accepted by the firewall if and only if the
### direction, protocol, port, and IP address match at least one of the input rules. If a rule contains
### a port range, it will match all packets whose port falls within the range. If a rule contains an IP
### address range, it will match all packets whose IP address falls within the range.
### Your job is to implement a Firewall class, whose interface contains two items:
### 1. A constructor, taking a single string argument, which is a file path to a CSV file whose contents are as described above,
### Note that you do not need to define a static ‘new’ method – simply use the
### constructor syntax in the language that you chose.
### Remember that you may assume that all content in the input file is valid.
### 2. A function, accept_packet, that takes exactly four arguments and returns a boolean:
### true, if there exists a rule in the file that this object was initialized with that allows traffic
### with these particular properties, and false otherwise.

import csv
import re
import ipaddress
import timeit

filename = "list-of-rules.csv"
ports = {}

### helper function to convert list into tuple
def convert(list):
    return tuple(list)

### helper function to convert tuples with a port range, to individual tuples with port integer(s)
def parseports(list):

    if re.search('-', list[2]):                                ### If there is a dash in the ports column...
        ranges = re.findall('([0-9.]+)', list[2])              ### determine the range between the dashes
        low = int(ranges[0])
        high = int(ranges[1])
        for i in range(low,high+1):                           ###create individual rules for all port ranges listed
            individuallist = (list[0],list[1],i,list[3])
            individualrule = convert(individuallist)          ### ensures that the rules are converted into tuples
            ports[individualrule] = ports.get(individualrule,0) + 1      ##inputs into dictionary
    else:
        list[2] = int(list[2])
        tup = convert(list)
        ports[tup] = ports.get(tup,0)+1

### helper function to convert tuples with an IP Address range, to individual tuple(s) with individual IP Address(es)
def parseip_address(list):

    if re.search('-', list[3]):
        ranges = re.findall('([0-9.]+)', list[3])
        low = int(ipaddress.IPv4Address(ranges[0]))
        high = int(ipaddress.IPv4Address(ranges[1]))
        for x in range (low, high+1):
            ip_address = str(ipaddress.IPv4Address(x))
            individuallist = (list[0],list[1],int(list[2]),ip_address)
            individualrule = convert(individuallist)
            ports[individualrule] = ports.get(individualrule,0) + 1
    else:
        tup = convert(list)
        ports[tup] = ports.get(tup,0)+1

###Dictionary class to map all of the Rules
class Firewall(dict):

    def __init__(self):                                    ### Constructor to read the CSV file with the inputs
        self.items = {}                                    ###Stores all of the rules from the CSV file into the dictionary
        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                parseports(row)
                parseip_address(row)

            for rules in ports:
                if rules not in self.items:
                    self.items[rules] = self.items.get(rules,0) + 1

    def print_packet(self):
        return (self.items)

    def accept_packet(self, direction, protocol, port, ip_address):
        rule = (direction, protocol, port, ip_address)

        if rule not in self.items:
            return False
        else:
            return True

### main executable function
if __name__ == '__main__':
    fw = Firewall()               ### The main executable function will initialize 'Packets' into a Firewall class which stores all of the rules in a dictionary.
    print(fw.accept_packet("inbound","tcp",80,"192.168.1.2"))
    print(fw.accept_packet("inbound","udp",53,"192.168.2.1"))
    print(fw.accept_packet("outbound","tcp",10234,"192.168.10.11"))
    print(fw.accept_packet("inbound","tcp",81,"192.168.1.2"))
    print(fw.accept_packet("inbound","udp",24,"52.12.48.92"))