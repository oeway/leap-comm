from __future__ import print_function
import Pyro4

uri = input("Enter the uri of the warehouse: ").strip()
leap_win_server = Pyro4.Proxy(uri)

def test_server():
    data = leap_win_server.read_spectrometer()
    assert len(data) == 2 and len(data[0]) == 1024 and len(data[1]) == 1024
    
    ret = leap_win_server.set_gating_parameters(10, 100)
    assert ret == True
    
    
    print("tests passed")
    
if __name__=="__main__":
    test_server()