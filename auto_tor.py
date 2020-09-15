import time
import os
import subprocess

# checking pip installation status
try:
    check_pip = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip):
        pass

except subprocess.CalledProcessError:
    print('[!] Pip not installed in your system!')
    subprocess.check_output("sudo apt-get update", shell=True)
    subprocess.check_output("sudo apt-get install python3-pip -y", shell=True)
    print("[+] pip3 installed successfully!")

# Importiing requests
try:
    import requests

except Exception:
    print("[!] python3 requests is not installed!")
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[+] python3 requests installed successfully!')

# checking tor status
try:
    check_tor = subprocess.check_output("which tor", shell=True)
except subprocess.CalledProcessError:
    print("[!] Tor is not installed in your System")
    subprocess.check_output(
        "sudo apt-get install tor torbrowser-launcher -y", shell=True)
    print("[+] Tor is installed successfully!")

os.system("clear")


def my_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url, proxies=dict(
        http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text


def change_ip():
    os.system("sudo service tor reload")
    print("[+] your IP has been changed to: {}".format(str(my_ip())))


print("""\033[1;32;40m \n
  █████╗ ██╗   ██╗████████╗ ██████╗     ████████╗ ██████╗ ██████╗ 
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔══██╗
 ███████║██║   ██║   ██║   ██║   ██║       ██║   ██║   ██║██████╔╝
 ██╔══██║██║   ██║   ██║   ██║   ██║       ██║   ██║   ██║██╔══██╗
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝       ██║   ╚██████╔╝██║  ██║
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝""")
print("\033[1;40;31m made by http://github.com/sudipta9/\n")

os.system("sudo service tor start")

time.sleep(3)
print("\033[1;32;40m Change your SOCKES to 127.0.0.1:9050\n")
os.system("sudo service tor start")
x = int(input("[+] time to change IP in Second. >>"))
lin = int(
    input("[+] How many time you want to change your ip? (For infinite type 0)>>"))
if lin == 0:
    while True:
        try:
            time.sleep(x)
            change_ip()
        except KeyboardInterrupt:
            print("\n[!] auto tor is closing")
            os.system("sudo service tor stop")
            quit()

else:
    for i in range(lin):
        time.sleep(x)
        change_ip()
    os.system("sudo service tor stop")
