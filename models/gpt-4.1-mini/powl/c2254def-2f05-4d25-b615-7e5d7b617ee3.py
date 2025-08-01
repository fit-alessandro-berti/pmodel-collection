# Generated from: c2254def-2f05-4d25-b615-7e5d7b617ee3.json
# Description: This process involves the secure, legal, and environmentally controlled shipment of valuable and fragile artwork from multiple galleries across different continents to a central exhibition venue. It requires coordinating customs clearance, temperature and humidity monitoring, insurance validation, and specialized packing. Additionally, real-time tracking, provenance verification, and emergency contingency measures must be integrated to guarantee the artwork's integrity throughout transit. Communication between artists, insurers, handlers, and customs officials is continuous to resolve any unexpected delays or regulatory requirements. The process concludes with careful unpacking and condition verification at the destination, ensuring that each piece is exhibition-ready and documented for both provenance and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Artwork_Catalog = Transition(label='Artwork Catalog')
Pack_Securely = Transition(label='Pack Securely')
Insurance_Check = Transition(label='Insurance Check')
Customs_Submit = Transition(label='Customs Submit')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Log = Transition(label='Temperature Log')
Provenance_Verify = Transition(label='Provenance Verify')
Carrier_Assign = Transition(label='Carrier Assign')
Route_Optimize = Transition(label='Route Optimize')
Real_time_Track = Transition(label='Real-time Track')
Emergency_Plan = Transition(label='Emergency Plan')
Stakeholder_Update = Transition(label='Stakeholder Update')
Unload_Carefully = Transition(label='Unload Carefully')
Condition_Check = Transition(label='Condition Check')
Exhibit_Setup = Transition(label='Exhibit Setup')
Documentation_File = Transition(label='Documentation File')

# Model the shipping preparation phase: 
# Artwork Catalog -> (Pack Securely, Insurance Check, Customs Submit, Humidity Control, Temperature Log) in partial order
# These 5 activities happen after catalog and mostly in parallel except Customs Submit can depend on Insurance Check for regulatory check, let's model them concurrent except for Customs Submit that follows Insurance_Check

prep_PO = StrictPartialOrder(
    nodes=[Pack_Securely, Insurance_Check, Customs_Submit, Humidity_Control, Temperature_Log]
)
prep_PO.order.add_edge(Insurance_Check, Customs_Submit)

# The sequence: Artwork Catalog --> prep_PO
prep_full = StrictPartialOrder(
    nodes=[Artwork_Catalog, prep_PO]
)
prep_full.order.add_edge(Artwork_Catalog, prep_PO)

# Model the shipping logistics:
# Carrier Assign and Route Optimize are concurrent, both need to finish before Real-time Track can start
logistics_PO = StrictPartialOrder(
    nodes=[Carrier_Assign, Route_Optimize]
)

# After logistics is done, Real-time Track + Emergency Plan + Stakeholder Update run concurrently during transit, all in partial order
transit_PO = StrictPartialOrder(
    nodes=[Real_time_Track, Emergency_Plan, Stakeholder_Update]
)

# Link logistics to transit
logistics_full = StrictPartialOrder(
    nodes=[logistics_PO, transit_PO]
)
logistics_full.order.add_edge(logistics_PO, transit_PO)

# Model loop structure for Emergency contingencies:
# During transit, after Emergency Plan runs, either exit loop or Stakeholder Update then Emergency Plan again
# We approximate this with a LOOP operator on Emergency_Plan and Stakeholder_Update

emergency_loop = OperatorPOWL(operator=Operator.LOOP, children=[Emergency_Plan, Stakeholder_Update])

# Replace transit_PO's Emergency_Plan and Stakeholder_Update with emergency_loop and Real-time_Track remains parallel/concurrent

transit_mod_PO = StrictPartialOrder(
    nodes=[Real_time_Track, emergency_loop]
)

# logistics_full updated with modified transit
logistics_full = StrictPartialOrder(
    nodes=[logistics_PO, transit_mod_PO]
)
logistics_full.order.add_edge(logistics_PO, transit_mod_PO)

# All after prep_full (preparation) is logistics_full
mid_PO = StrictPartialOrder(
    nodes=[prep_full, logistics_full]
)
mid_PO.order.add_edge(prep_full, logistics_full)

# At destination: Unload Carefully --> Condition Check --> Exhibit Setup --> Documentation File
destination_PO = StrictPartialOrder(
    nodes=[Unload_Carefully, Condition_Check, Exhibit_Setup, Documentation_File]
)
destination_PO.order.add_edge(Unload_Carefully, Condition_Check)
destination_PO.order.add_edge(Condition_Check, Exhibit_Setup)
destination_PO.order.add_edge(Exhibit_Setup, Documentation_File)

# Provenance Verify can be done after Artwork Catalog and before unloading (i.e., after transit)
# Let's place Provenance_Verify concurrent with destination_PO but dependent on prep_full (catalog) and logistics_full (transit)

prov_PO = StrictPartialOrder(
    nodes=[Provenance_Verify]
)

prov_full = StrictPartialOrder(
    nodes=[mid_PO, prov_PO]
)
prov_full.order.add_edge(mid_PO, prov_PO)

# Final overall PO: after provenance verify is destination_PO
root = StrictPartialOrder(
    nodes=[prov_full, destination_PO]
)
root.order.add_edge(prov_full, destination_PO)