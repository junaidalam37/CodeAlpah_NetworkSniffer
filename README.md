# CodeAlpah_NetworkSniffer
bult a python program to capture network traffic packets and alalyze the packets find out the useful information like src ips dst ips prptocols and payload 
i)	Built a python program to capture network traffic packets.

Open cmd and make a directory with the name of CodeAlpah_NetworkSniffer
mkdir CodeAlpha_NetworkSniffer
And save the python file in my C drive inside the above directory with the name of sniffer.py  py means the extension of python 
This is the right path of the sniffer.py file:
 C:\Users\Ayub Khan\CodeAlpha_NetworkSniffer
This is the python program for the network traffic packets capturing : 
Here the simple explaination of the python code :
This program is a network packet sniffer that captures data packets traveling through the network. 
It uses the Scapy library to monitor and inspect network traffic in real time. 
The packet_callback() function runs every time a new packet is captured. 
It displays the complete details of the packet using packet.show(). 
The program extracts and prints the source and destination MAC addresses. 
It also shows the source and destination IP addresses if the packet contains IP information. 
If the packet uses TCP, UDP, or ICMP, it prints the protocol type and related information like ports or flags. 
For DNS packets, it displays the domain name being requested and whether it is a query or a response. 
If the packet contains data (payload), it tries to display the readable text inside it. 
The main() function starts the packet capture and continues sniffing until the user presses Ctrl + C to stop the program.
ii)	Use libraries like (scapy) or (socket) for packet capturing.

Installation of scapy library for packet capturing :
Open the cmd commond prompt and enter
pip install scapy 
then test it for installation to complete 
here another tool which is the specialized driver interface for the scapy is called Npcap
open commond terminal and type and enter:
curl -L -o npcap-installer.exe https://npcap.com/dist/npcap-1.80.exe
and then type and enter for installation lounching:
npcap-installer.exe .
iii)	Analyze network captured packets to understand their structure and content.
Here it is required to run the cmd terminal as an administrator and run the python file here in administrator terminal type cd and copy the actual path of the python file and paste here and enter :
cd C:\Users\Ayub Khan\CodeAlpha_NetworkSniffer
and then run sniffer.py file :
python sniffer.py
now open another terminal of cmd and ping google ip 
then see here in administrator terminal here starting the capturing of the traffic packets which is going out from the pc to the google and other and go back into the pc from outside like google.
Source ips: is my pc ip 172.20.10.4
Destination ips: is the google ip 8.8.8.8
Protocols: ICMP. 
Packet size : 74 bytes 
Payload : here payload is the actual data.

Useful information :

Source ips: is the google ip 8.8.8.8
Destination ips: is my pc ip 172.20.10.4
Protocols: ICMP. 
Packet size : 74 bytes 
Payload : here payload is the actual data.

