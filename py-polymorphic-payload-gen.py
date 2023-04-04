#!/usr/bin/env python3
# Dennis Chow April 02, 2023
# dchow[AT]xtecsystems.com
# No expressed or implied warranities. What you use this for is on you.
# Updates April 03, 2023 v1.1 - Added additional randomizers
import random, codecs, re

#define payload to be used for transforms
payload = 'subprocess.Popen("whoami", shell=True)'

#create random parameters for transform function output spec
random.seed(version=2)
random_key = random.randint(1, 25)
#extend with random encoding
repl_randchar = (random.choice(['###', 'zzz', 'abcd'])) * random_key


# separate functions for each transformer
def hextransform(payload):
  hex_payload = payload.encode().hex()
  print("Original payload: " + payload)
  print("Transformed payload: " + hex_payload)
  return hex_payload
  # reversal
  #original_payload = bytes.fromhex(hex_payload).decode()


def rot13transform(payload):
  # ensure  you have repl_randchar defined outside the func
  # using an second position argument will mess with the
  # random selector in main()
  rot13_payload = codecs.encode(payload, 'rot_13')
  # add a small mutated twist with spacing
  mutated_rot13_payload = re.sub(r"\s", repl_randchar, rot13_payload)
  print("Original payload: " + payload)
  print("Transformed payload: " + mutated_rot13_payload)
  return rot13_payload
  # reversal
  #derandchar_rot13_payload = re.sub(repl_randchar, " ",mutated_rot13_payload)
  #original_payload = codecs.decode(mutated_rot13_payload, 'rot_13')


# generators for dynamic payload
def genrot13wrap():
  yield '#!/usr/bin/env python3\n'
  yield 'import random, codecs, re, subprocess\n'
  yield f'random_key = {random_key}\n'
  yield f'repl_randchar = {repr(repl_randchar)}\n'
  yield '\n'
  yield 'def deobfuscate_payload():\n'
  yield '    transformed_payload = ' + repr(rot13transform(payload)) + '\n'
  yield '    s1_deobfuscated_payload = re.sub(repl_randchar, " ", transformed_payload)\n'
  yield '    s2_deobfuscated_payload = codecs.decode(s1_deobfuscated_payload, "rot_13")\n'
  yield '    return s2_deobfuscated_payload\n'
  yield '\n'
  yield 'executed_payload = eval(deobfuscate_payload())\n'


def genhexwrap():
  yield '#!/usr/bin/env python3\n'
  yield 'import codecs, subprocess\n'
  yield '\n'
  yield 'def deobfuscate_payload():\n'
  yield '    transformed_payload = ' + repr(hextransform(payload)) + '\n'
  yield '    deobfuscated_payload = bytes.fromhex(transformed_payload).decode()\n'
  yield '    return deobfuscated_payload\n'
  yield '\n'
  yield 'executed_payload = eval(deobfuscate_payload())\n'


# specify main driver
def main():

  # random transformation selector
  function_list = [hextransform, rot13transform]
  selectedfunction = random.choice(function_list)
  # ensure repl_randchar was defined earlier
  selectedfunction(payload)
  if "rot13transform" in str(selectedfunction):
    print('selected modified rot-13')
    rot13_wrapper = ''.join(genrot13wrap())
    print(rot13_wrapper)
  elif "hextransform" in str(selectedfunction):
    print('selected hex')
    hex_wrapper = ''.join(genhexwrap())
    print(hex_wrapper)


if __name__ == "__main__":
  main()
