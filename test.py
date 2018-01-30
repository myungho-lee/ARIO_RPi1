import pifacedigitalio
import RPIO


def socket_callback(socket, val):
    print("socket %s: '%s'" % (socket.fileno(), val))
    #socket.send("echo: %s\n" % val)
    #RPIO.close_tcp_client(socket.fileno())
    if val == "TurnOn":
    	pfd.relays[1].value = 1
    elif val == "TurnOff":
    	pfd.relays[1].value = 0
    elif val == "Disconnect":
    	RPIO.close_tcp_client(socket.fileno())
        sys.exit(1)
    else:
    	val = val + " not supported"
    socket.send("echo: %s\n" % val)



# creates a PiFace Digtal object
pfd = pifacedigitalio.PiFaceDigital()

# One TCP interrupt callback (opens socket server at port 8080)
RPIO.add_tcp_callback(8080, socket_callback)

# Starts waiting for interrupts (exit with Ctrl+C)
RPIO.wait_for_interrupts()
