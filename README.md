# Devnet_Programs
It contains the practice programs under Devnet Cert.

"TDD.py"
This program is about "Test Driven Development" concept. Under this, we first write the test code and then start with the main code.
We keep writing the code until all the tests are passed. Once the tests are passed, then we relook into the code and try to refactor
(Making it more efficient) it.

To run this program, download TDD.py and Config.txt file into your machine and put them inside a folder. Open a terminal and navigate 
to that folder and execute the command:
python –m unittest TDD.py

Expected output of the code runs succesfully:
########
These are the customer IP>> ['10.10.100.1', '10.10.101.1']
.This is the parsed data for all the customer>> {'CUSTOMER_A': [100, '10.10.100.1'], 'CUSTOMER_B': [101, '10.10.101.1']}
.These are the customer names>> ['CUSTOMER_A', 'CUSTOMER_B']
.These are the customer VLANs>> [100, 101]
.
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

########
