
# py-obfuscation-payload-gen
A set of obfuscations generators for basic boiler plate demonstrations: 
- [py-polymorphic-payload-gen.py](https://github.com/dc401/py-obfuscation-payloadgen/blob/main/py-polymorphic-payload-gen.py "py-polymorphic-payload-gen.py") - simple polymorphic capabilities of obfuscating Python3 based payload using a simple integer as a random key, transposition with ROT-13, and substitution of whitespaces with random number of hashtags based on the count of the random key
- TBD: Planned metamorphic variant

### Walkthrough Article
- [Red Team Polymorphic Engine in Python](https://dwchow.medium.com/red-team-polymorphic-engine-in-python-167878a0f1cc)

## Usage

For: [py-polymorphic-payload-gen.py](https://github.com/dc401/py-obfuscation-payloadgen/blob/main/py-polymorphic-payload-gen.py "py-polymorphic-payload-gen.py")

 1. Modify your payload variable to utilize a suitable execution that the eval() or similar statement can use such as subprocess.Popen()
 2. Copy and paste the printed output into another python file and execute to test

![enter image description here](https://github.com/dc401/py-obfuscation-payloadgen/blob/main/py-polymorphic-payload-gen-runtime.gif?raw=true)

## Extending Functionality

It's a very primitive form of polymorphic mutation engine by definition. The dynamic changing of the key technically makes it a new decryption routine each time. However, a more "true" polymorphic example would also randomize a set of encryption and decryption routines. 

You could extend my example to randomly select from rot-13, rot-3, or some other encoding, save the select to a result in a separate variable and then have Python's [f-strings](https://realpython.com/python-f-strings/)  continue to substitute the layered strings needed for the generator.

![enter image description here](https://github.com/dc401/py-obfuscation-payloadgen/blob/main/polymorphic-diagram.png?raw=true)


## About

Dennis Chow dchow[AT]xtecsystems.com April 02, 2023
No expressed or implicit warranty or liability. What you use this script for is on you.
