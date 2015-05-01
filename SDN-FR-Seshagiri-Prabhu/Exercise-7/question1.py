#! /usr/bin/env python2
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"

def runExp():
    """
    A function to run a mininet experiment
    """     
    """
    Creates an object of customTopo class with argument n=2, used to
    create link between switches and hosts
    """
    topo = customTopo( n=2 )
    """
    Creates a Mininet with with given custom topology. Network 
    emulation with hosts spawned in network namespaces. Mininet is 
    the main class to create and manage network
    """
    net = Mininet ( topo=topo )
    """
    Start controller, switches and network
    """
    net.start()
    """
    The mininet object is passed to simple command line interface 
    to talk to nodes
    """
    CLI( net )
    """
    Stops the mininet network
    """
    net.stop()


class customTopo( Topo ):
    """
    A class to create custom network topology
    """
    def __init__( self, n, **kwargs ):
        """
        Constructor of the class customTopo
        @args: self, n, kwargs
        """
        """
        Calling the base class for mininet topology
        """
        Topo.__init__( self, **kwargs )
        """
        Add two hosts to the topology and returns the host name to the respective objects
        """
        h1, h2 = self.addHost( 'h1' ), self.addHost( 'h2' )
        """
        Adds a switch to the topology and returns the switch name to the variable
        """
        s1 = self.addSwitch( 's1' )
        for _ in range( n ):
            """
            Adds bidirectional link between the elements in the network 
            """
            self.addLink( s1, h1 )
            self.addLink( s1, h2 )


if __name__ == '__main__':
    """
    Main function
    """ 
    """
    To set Mininet’s default output level. Informs mininet to print
    useful information
    """
    setLogLevel( 'info' )
    """
    Calls the function to run the experiment
    """
    runExp() 

