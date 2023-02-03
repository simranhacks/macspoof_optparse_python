import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option ("-i" , "--interface" , dest="interface" , help="interface to change mac address")
parser.add_option ("-m" , "--new_mac" , dest="new_mac" , help="new_mac")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["ifconfig", interface, "up"])
subprocess.run("ifconfig")

print("Your MAC is spoofed")
