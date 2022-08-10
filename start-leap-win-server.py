from __future__ import print_function
import Pyro4
import numpy as np
import socket


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class LeapWinServer(object):
    def __init__(self):
        self.contents = ["chair", "bike", "flashlight", "laptop", "couch"]

    def set_spectrometer_parameters(self, config):
        print("set_spectrometer_parameters")
        return True

    def read_spectrometer(self):
        # generate a random array with 2x 1024 elements in float between 0 and 65535.0
        data = np.random.randint(0, 65535, size=(2, 1024))
        print("read_spectrometer")
        return data.tolist()

    def turn_on_laser(self):
        print("Laser turned on.")
        return True

    def set_laser_wavelength(self, wavelength):
        print("Laser wavelength set to {0}.".format(wavelength))
        return True

    def turn_off_laser(self):
        print("Laser turned off.")
        return True

    def start_gating(self):
        print("gating started.")
        return True

    def set_gating_parameters(self, gate_width, gate_delay):
        print("gating parameters set to {0} and {1}.".format(
            gate_width, gate_delay))
        return True

    def read_iv_curve_live(self, size=1024):
        print("iv curve read.")
        return np.random.randint(0, 65535, size=(2, size))


def main():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print("Your Computer Name is: " + hostname)
    print("Your Computer IP Address is: "+ip_addr)
    Pyro4.Daemon.serveSimple(
        {
            LeapWinServer: "leap_win_server"
        },
        host=ip_addr,
        port=9090,
        ns=False
    )


if __name__ == "__main__":
    main()
