from __future__ import print_function
import Pyro4

uri = input("Enter the uri of the warehouse: ").strip()
warehouse = Pyro4.Proxy(uri)

print(warehouse.list_contents())