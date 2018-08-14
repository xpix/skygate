from lora import *
import time

def woo_got_a_packet(packet):
	print(packet)
	if not packet:
		print("Failed packet")
	elif (packet['packet'] and packet['packet'][0] & 0x80) == 0:
		# ASCII
		Sentence = ''.join(map(chr,bytes(packet['packet']).split(b'\x00')[0]))
		print("Sentence=" + Sentence, end='')
	else:
		print("Packet=", packet)
	
mylora = LoRa(0, 434.434, 1)

mylora.listen_for_packets(woo_got_a_packet)

print("listen for packets\n")


while 1:
	time.sleep(0.01)

