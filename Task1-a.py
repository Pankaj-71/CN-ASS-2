from mininet.net import Mininet

from mininet.node import Controller, OVSSwitch, Host

from mininet.link import TCLink

from mininet.cli import CLI



def create_topology():

    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)



    # Add Controller

    net.addController("c0")



    # Add Hosts

    h1 = net.addHost("h1")

    h2 = net.addHost("h2")

    h3 = net.addHost("h3")

    h4 = net.addHost("h4")

    h5 = net.addHost("h5")

    h6 = net.addHost("h6")

    h7 = net.addHost("h7")  # Server



    # Add Switches

    s1 = net.addSwitch("s1")

    s2 = net.addSwitch("s2")

    s3 = net.addSwitch("s3")

    s4 = net.addSwitch("s4")



    # Connect Hosts to Switches

    net.addLink(h1, s1)

    net.addLink(h2, s1)

    net.addLink(h3, s2)

    net.addLink(h4, s3)

    net.addLink(h5, s3)

    net.addLink(h6, s4)

    net.addLink(h7, s4)  # Server



    # Connect Switches

    net.addLink(s1, s2)  # S1-S2: 100Mbps

    net.addLink(s2, s3)   # S2-S3: 50Mbps

    net.addLink(s3, s4)  # S3-S4: 100Mbps



    # Start Network

    net.start()

    print("Mininet Topology Created!")

    CLI(net)

    net.stop()



if __name__ == "__main__":

    create_topology()