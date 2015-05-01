#! /usr/bin/env python2
"""
sdn_simulator.py: A mock implementation of sdn simulator in python
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"

switch_objects = []

help = """
Welcome to SDN Simulator
NAME
\t SDN SIMULATOR - an interpreter, interactive SDN simulator

OPTIONS
\t <SWITCH-A> ping <SWITCH-B>
\t  -- Send an ICMP like request between two switches

\t dump
\t  -- Dump all the flow tables of the switches

\t exit
\t  -- Exit the simulator 

\t help
\t  -- Display the help text
"""

class Switch:
    """
    A switch will process a packet according to its flow table
    """
    flow_table = {}

    def __init__(self, id, left=None, right=None):
        self.id, self.flow_table['left'], self.flow_table['right'] = id, left, right


class Controller:
    """
    Controller will setup switches' flow tables upon a switch request
    for an unknown flow_table
    """
    def __init__(self, number_of_switches):
        self.number_of_switches = number_of_switches

    def update_flow_table(self, packet):
        """
        Updates the flow table of the switch
        """
        current_switch = packet.source
        packet_src_index = get_switch_object_index(packet.source.id)
        packet_dst_index = get_switch_object_index(packet.destination.id)

        while current_switch != packet.destination:
            current_switch_index = get_switch_object_index(current_switch.id)
            # First switch
            if current_switch_index == 0:
                current_switch.flow_table['left'] = None
                current_switch.flow_table['right'] = switch_objects[current_switch_index + 1]
            
            # Last switch
            elif current_switch_index == self.number_of_switches - 1:
                current_switch.flow_table['left'] = switch_objects[current_switch_index - 1]
                current_switch.flow_table['right'] = None
            
            # Any other switches
            else:
                current_switch.flow_table['left'] = switch_objects[current_switch_index - 1]
                current_switch.flow_table['right'] = switch_objects[current_switch_index + 1]
            
            # Packet flow is from left to right
            if packet_dst_index > packet_src_index:
                current_switch = switch_objects[current_switch_index + 1]
            
            # Packet flow is from right to left
            else: current_switch = switch_objects[current_switch_index - 1]


class Packet:
    """
    The object that is passed between switches and the Controller
    """
    def __init__(self, source, destination):
        self.source, self.destination = source, destination


def get_switch_object_index(id):
    """
    Returns the index of the object from the switch object list 
    """
    for x in range(len(switch_objects)): 
        if switch_objects[x].id == id: return x
    return None


def ping_switch(packet, controller):
    """
    Checks the flow table of switches if not found contacts the 
    controller to update the flow table of the respective switch
    """
    print "Packet Source: ", packet.source.id,
    print "Packet Desination: ", packet.destination.id

    current_switch = packet.source
    packet_src_index = get_switch_object_index(packet.source.id)
    packet_dst_index = get_switch_object_index(packet.destination.id)

    while True:
        print current_switch.id,
        current_switch_index = get_switch_object_index(current_switch.id)
        
        # Packet reached destination switch
        if packet.destination.id == current_switch.id: print "(Packet delivered)"; break
        
        # When Switch doesn't have any flow table entries
        if current_switch.flow_table['left'] == None or \
            current_switch.flow_table['right'] == None: controller.update_flow_table(packet)

        # When there's flow table entries in the switch
        if packet_dst_index > packet_src_index:
            current_switch = switch_objects[current_switch_index + 1]
        else: current_switch = switch_objects[current_switch_index - 1]
        print " -> ",


def dump_switch_flow_table():
    """
    Prints the flow table of all switches
    """
    for x in xrange(len(switch_objects)):
        print "+++++++++++++++++++"
        print "+Switch   +     %s+" % (switch_objects[x].id)
        if x == 0: print "+Left     +    NIL+"
        elif switch_objects[x].flow_table['left'] == None: print "+Left     +    NIL+"
        else: print "+Left     +     %s+" % (switch_objects[x-1].id)
        if x == len(switch_objects) - 1: print "+Right    +    NIL+"
        elif switch_objects[x].flow_table['right'] == None: print "+Right    +    NIL+"
        else: print "+Right    +     %s+" % (switch_objects[x+1].id)
        print "+++++++++++++++++++"


if __name__=="__main__":
    """
    Main function
    """
    print help 
    number_of_switches = int(raw_input("SDN Simulator > Enter the number of switches: "))
    print "Creating Switches ",
    for x in xrange(number_of_switches):
        obj = Switch('s' + str(x))
        switch_objects.append(obj)
        print 's' + str(x) + "... ",
    controller = Controller(number_of_switches)

    while True:
        user_input = raw_input("\nSDN Simulator > ")

        if  user_input == "exit": break

        # If the user is trying to ping between switches
        if "ping" in user_input:
            split_list = user_input.split(' ')
            host1 = host2 = False

            # Get the object of the packet source 
            x = get_switch_object_index(split_list[0])
            if x != None: host1 = True; host1_obj = switch_objects[x]

            # Get the object of the destination switch
            y = get_switch_object_index(split_list[2])
            if y != None: host2 = True; host2_obj = switch_objects[y]

            # If the objects are valid
            if host1 and host2: 
                packet = Packet(host1_obj, host2_obj);
                ping_switch(packet, controller)
            
            # If switches cannot be found
            else: print "Switch not found"

        # If the user is trying to dump the flow table rules in all switches
        if "dump" in user_input: dump_switch_flow_table()
        
        # If the user is tring to print the help instructions
        if "help" in user_input: print help
