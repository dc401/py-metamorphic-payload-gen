#!/usr/bin/env python3
# Dennis Chow April 02, 2023
# dchow[AT]xtecsystems.com
# No expressed or implied warranities. What you use this for is on you.
import random, codecs, re
import subprocess

#define payload to be used for transforms
payload = 'subprocess.Popen("whoami", shell=True)'

#create random parameters for transform function output spec
random.seed(version=2)
random_key = random.randint(1, 25)
repl_hashes = '#' * random_key

def transformpayload(payload):
    # payload modification trials
    rot13_payload = codecs.encode(payload, 'rot_13')
    hashed_rot13_payload = re.sub(r"\s", repl_hashes, rot13_payload)
    print("Original payload: " + payload)
    print("Transformed payload: " + hashed_rot13_payload)
    return hashed_rot13_payload

def reversetransform(transformed_payload):
    dehashed_rot13_payload = re.sub(repl_hashes, " ", transformed_payload)
    original_payload = codecs.decode(dehashed_rot13_payload, 'rot_13')
    print("Transformed payload: " + transformed_payload)
    print("Original payload: " + original_payload)
    return original_payload

# generate wrapper for "refactored payload"
def genwrap():
    yield '#!/usr/bin/env python3\n'
    yield 'import random, codecs, re, subprocess\n'
    yield f'random_key = {random_key}\n'
    yield f'repl_hashes = "#" * random_key\n'
    yield '\n'
    yield 'def deobfuscate_payload():\n'
    yield '    transformed_payload = ' + repr(transformpayload(payload)) + '\n'
    yield '    deobfuscated_payload = codecs.decode(transformed_payload, "rot_13").replace(repl_hashes, " ")\n'
    yield '    return deobfuscated_payload\n'
    yield '\n'
    yield 'executed_payload = eval(deobfuscate_payload())\n'

# specify main driver
def main():
    # define our payload
    transformed_payload = transformpayload(payload)

    # generate wrapper code and print it out
    wrapper_code = ''.join(genwrap())
    print(wrapper_code)

if __name__ == "__main__":
    main()
