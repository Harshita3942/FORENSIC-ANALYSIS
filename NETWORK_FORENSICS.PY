from scapy.all import rdpcap
import argparse

def analyze_pcap(file_path):
    packets = rdpcap(file_path)
    print(f"Total packets: {len(packets)}")

    protocols = {}
    for packet in packets:
        protocol = packet.sprintf("%IP.proto%")
        if protocol:
            protocols[protocol] = protocols.get(protocol, 0) + 1

    print("Protocol Distribution:")
    for proto, count in protocols.items():
        print(f"  {proto}: {count} packets")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Forensics Tool")
    parser.add_argument("pcap", help="Path to the PCAP file for analysis")
    args = parser.parse_args()

    analyze_pcap(args.pcap)
