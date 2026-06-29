from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP, Raw
from scapy.layers.dns import DNS, DNSQR

def packet_callback(packet):

    print("\n" + "="*70)

    # Show complete packet details
    packet.show()

    print("\n---------------- Packet Summary ----------------")

    # Ethernet Information
    if packet.haslayer(Ether):
        print(f"Source MAC      : {packet[Ether].src}")
        print(f"Destination MAC : {packet[Ether].dst}")

    # IP Information
    if packet.haslayer(IP):
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")

    # TCP Information
    if packet.haslayer(TCP):
        print("Protocol        : TCP")
        print(f"Source Port     : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
        print(f"TCP Flags       : {packet[TCP].flags}")

    # UDP Information
    elif packet.haslayer(UDP):
        print("Protocol        : UDP")
        print(f"Source Port     : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    # ICMP Information
    elif packet.haslayer(ICMP):
        print("Protocol        : ICMP")
        print(f"Type            : {packet[ICMP].type}")
        print(f"Code            : {packet[ICMP].code}")

    # DNS Information
    if packet.haslayer(DNS):
        print("\n===== DNS Information =====")

        dns = packet[DNS]

        if dns.qd:
            try:
                print("Query Name      :", dns.qd.qname.decode())
            except:
                print("Query Name      :", dns.qd.qname)

        print("Transaction ID  :", dns.id)

        if dns.qr == 0:
            print("Message Type    : DNS Query")
        else:
            print("Message Type    : DNS Response")

    # Packet Size
    print(f"\nPacket Size     : {len(packet)} bytes")

    # Payload
    if packet.haslayer(Raw):
        print("\n===== Payload =====")
        try:
            print(packet[Raw].load.decode("utf-8", errors="ignore"))
        except:
            print(packet[Raw].load)

    print("="*70)


def main():
    print("="*55)
    print("         CodeAlpha Network Sniffer")
    print("="*55)
    print("Capturing packets...")
    print("Press Ctrl+C to stop.\n")

    sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
    main()