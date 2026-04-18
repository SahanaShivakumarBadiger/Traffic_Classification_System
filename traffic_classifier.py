from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ipv4, tcp, udp, icmp

log = core.getLogger()

tcp_count = 0
udp_count = 0
icmp_count = 0

def _handle_PacketIn(event):
    global tcp_count, udp_count, icmp_count

    try:
        packet = event.parsed

        if not packet or not packet.parsed:
            return

        ip = packet.find('ipv4')

        if ip:
            if ip.find('tcp'):
                tcp_count += 1
                log.info("TCP Packet")
            elif ip.find('udp'):
                udp_count += 1
                log.info("UDP Packet")
            elif ip.find('icmp'):
                icmp_count += 1
                log.info("ICMP Packet")

        log.info(f"Stats → TCP:{tcp_count}, UDP:{udp_count}, ICMP:{icmp_count}")

        # Forward packet
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

    except Exception as e:
        # Ignore parsing errors (Python 3.12 issue)
        log.debug("Packet parsing error ignored")

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Traffic Classifier Started")
