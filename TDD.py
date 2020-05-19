import unittest
import re

# This is a Test case class to test the customer names. Here we will compare the results after parsing the customer names and the expected customer names.
# Code has to be fixed until the parsed information is equal to the expected results.
class TestParse(unittest.TestCase):
	# This function compares the customer name returned from the parsing vs the expected names
	def test_parse_cust_name(self):
		cp = ConfParse()
		expected_name = ['CUSTOMER_A', 'CUSTOMER_B']
		parsed_names = cp.parse_cust_name()
		print("These are the customer names>>", parsed_names)
		self.assertEqual(list, type(parsed_names))
		self.assertEqual(expected_name, parsed_names)

	# This function compares the customer VLANs returned from the parsing vs the expected VLANs
	def test_parse_cust_vlan(self):
		cp = ConfParse()
		cust_name = ["CUSTOMER_A", "CUSTOMER_B"]
		cust_vlan = [100, 101]
		parsed_vlans = [cp.parse_cust_vlan(cust_name[0]), cp.parse_cust_vlan(cust_name[1])]
		print("These are the customer VLANs>>", parsed_vlans)
		self.assertEqual(cust_vlan, parsed_vlans)

	# This function will compare the IP Address assigned on those subinterfaces with the one which is expected.
	def test_parse_cust_IP(self):
		cp = ConfParse()
		cust_name = ["CUSTOMER_A", "CUSTOMER_B"]
		cust_IP = ['10.10.100.1', '10.10.101.1']
		parsed_IP = [cp.parse_cust_IP(cust_name[0]), cp.parse_cust_IP(cust_name[1])]
		print("These are the customer IP>>", parsed_IP)
		self.assertEqual(cust_IP, parsed_IP)

	# This Test will combine all the separated results and put the align the customer name with their specific data.
	def test_parse_cust_data(self):
		cp = ConfParse()
		expected_data = {"CUSTOMER_A": [100, "10.10.100.1"], "CUSTOMER_B": [101, "10.10.101.1"]}
		#parsed_data = cp.parse_cust_data()
		cust_name = cp.parse_cust_name()
		cust_data = {}
		for name in cust_name:
			cust_data[name] = [cp.parse_cust_vlan(name),cp.parse_cust_IP(name)]

		print("This is the parsed data for all the customer>>", cust_data)
		self.assertEqual(expected_data, cust_data)


# Now we will define a class which will have the function to parse the input and return the customer names, vlans and IP addresses.

class ConfParse():
	device_config = open("Config.txt", "r").read()

	# Parse the config and return the customer name.
	def parse_cust_name(self):
		cust_name_pattern = r'ip vrf ([a-zA-Z_]+)\n'
		cust_names = re.findall(cust_name_pattern, self.device_config)
		return cust_names

	# Parse the config and return the customer vlan.
	def parse_cust_vlan(self,cust):
		cust_vlan_pattern = (r"interface GigabitEthernet0/0.([0-9]+)\n  encapsulation dot1Q ([0-9]+)\n  ip vrf forwarding %s" %(cust))
		cust_vlan = re.search(cust_vlan_pattern, self.device_config)
		return int(cust_vlan.group(1))

	# Parse the config and return the customer vlan.
	def parse_cust_IP(self,cust):
		cust_IP_pattern = (r"ip vrf forwarding %s\n  ip address ([0-9.]+)" %(cust))
		cust_IP = re.search(cust_IP_pattern, self.device_config)
		return cust_IP.group(1)

	# Parse the  customer data and build a dictionary database in the same format as it is expected
	def parse_cust_data(self):
		cust_data = {}
		cust_name = parse_cust_name()
		for name in cust_name:
			cust_data[name] = [parse_cust_vlan(name),parse_cust_IP(name)]
		return cust_data




