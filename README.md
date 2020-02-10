# Illumio Coding Challenge

### Problem Statement
Read a CSV file, given a set of firewall rules, a network packet will be accepted by the firewall if and only if the
direction, protocol, port, and IP address match at least one of the input rules. If a rule contains
a port range, it will match all packets whose port falls within the range. If a rule contains an IP
address range, it will match all packets whose IP address falls within the range.
Your job is to implement a Firewall class, whose interface contains two items:
1. A constructor, taking a single string argument, which is a file path to a CSV file whose contents are as described above,
Note that you do not need to define a static ‘new’ method – simply use the
constructor syntax in the language that you chose.
Remember that you may assume that all content in the input file is valid.
2. A function, accept_packet, that takes exactly four arguments and returns a boolean:
true, if there exists a rule in the file that this object was initialized with that allows traffic
with these particular properties, and false otherwise.


### Problem Solving and Designing a Solution

Dictionaries and tuples came to mind, when I was thinking of how to create a class with a constructor that could read and interpret a CSV file with 500k-1 million rules. 

When the CSVreader reads a CSV file, it reads each row as a list. By converting every rule into a tuple, I could then add each tuple to a dictionary. There are four components in each row or list of the CSV file; the four components of the list are as follows: 

>'Direction', 'protocol', 'port(s)','ip_address(es)'.

Because there could be ranges for the port component and for the IP-address component for each row of the CSV file, helper functions would be needed. The helper functions can read the 'port(s)' and 'ip_address(es)' components if there is a range in either component.

I wrote a helper function that could convert lists to tuples.
I also wrote a helper function to add all rules within a port range to a dictionary.
Lastly, I wrote a helper function to add all rules within an IP address range to a dictionary. 

Apparently, every single IP address from 0.0.0.0 to 255.255.255.255 is assigned to a corresponding integer. 0.0.0.0 is assigned to the integer 1, while 0.0.0.100 is assigned to the integer 101. 0.0.1.0 is assigned to the integer 256 and 255.255.255.255 is assigned to the integer 256^4. The ipaddress module is built-in to Python apparently, and you can convert IP addresses to integer with a simple command, and vice versa (converting integers to IP addresses).

Rather than trying to write an algorithm that could calculate a range of an octect for IP Addresses, I simply converted 
the two IP addresses (the range) to their corresponding integers. Once I knew the range between the two IP addresses, I could determine how many tuples were needed to be added. You can see the source code to see more clearly how I converted IP Address ranges, as well as the port ranges.

All rules were converted into tuples, and then added to a dictionary class Firewall. 
The constructor function of class Firewall would start up the CSVreader. 

### Running the Code

From the terminal, you can execute the code by inputting the following command:

> python3 main.py

And you will get output with boolean values (Either true or false). See the source code to see which rules are being queried.

### Testing the Code

The end-user can alter the CSV file however she desires. If the end-user is running the code in a Python IDE or interpreter
the accept_packet function works. 

Example:

> fw.accept_packet ("inbound","tcp",80,"192.168.2.3")            
> True

#would return a boolean value True or False, it depends on what is listed in the CSV file. End-user can alter it 
however she wants to test the code but it should work as long as the values in the CSV file are formatted properly
(no spaces, no empty rows).

Two methods I wrote associated with the 'Firewall' class are 

>fw.print_packet()
    and
>fw.return_length()

The print_packet method will allow you to view the contents of the Firewall dictionary class. The return_length() method 
allows you to see how many unique entries or rules are in the Firewall class.


### Refinements

If I had more time, I would run unit tests and timer tests to determine the speed with which my constructor can 
construct the dictionary, with all the rules. I think that the code performs well but it could be slightly faster.
PyCharm crashed when I tried to include the IP address range from 0.0.0.0 - 255.255.255.255 (that's over 4 billion IP addresses) but the code can handle 65,000 ports easily. The code can handle 500k-1million entries as well; you can test for 
1 million entries by adjusting the IP address ranges in the CSV file. It took under 1 second for me to crunch 450k rules with the code. Not sure why the program crashes the maximum IP range (0.0.0.0 - 255.255.255.255); maybe because of the limitations of the Python interpreter, the dictionary data structure itself, and/or limited memory. 

### Team Preference

My top preference is the Data Team. My second preference is the Platform team.

### Closing

This project was developed on Linux Ubuntu OS 16GB RAM and PyCharm. Linux is the best operating system. Cheers!

