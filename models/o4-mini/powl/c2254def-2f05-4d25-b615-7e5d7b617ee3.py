# Generated from: c2254def-2f05-4d25-b615-7e5d7b617ee3.json
# Description: This process involves the secure, legal, and environmentally controlled shipment of valuable and fragile artwork from multiple galleries across different continents to a central exhibition venue. It requires coordinating customs clearance, temperature and humidity monitoring, insurance validation, and specialized packing. Additionally, real-time tracking, provenance verification, and emergency contingency measures must be integrated to guarantee the artwork's integrity throughout transit. Communication between artists, insurers, handlers, and customs officials is continuous to resolve any unexpected delays or regulatory requirements. The process concludes with careful unpacking and condition verification at the destination, ensuring that each piece is exhibition-ready and documented for both provenance and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
art_catalog       = Transition(label='Artwork Catalog')
pack_securely     = Transition(label='Pack Securely')
insurance_check   = Transition(label='Insurance Check')
customs_submit    = Transition(label='Customs Submit')
humidity_control  = Transition(label='Humidity Control')
temperature_log   = Transition(label='Temperature Log')
provenance_verify = Transition(label='Provenance Verify')
carrier_assign    = Transition(label='Carrier Assign')
route_optimize    = Transition(label='Route Optimize')
real_time_track   = Transition(label='Real-time Track')
emergency_plan    = Transition(label='Emergency Plan')
stakeholder_update= Transition(label='Stakeholder Update')
unload_carefully  = Transition(label='Unload Carefully')
condition_check   = Transition(label='Condition Check')
exhibit_setup     = Transition(label='Exhibit Setup')
documentation_file= Transition(label='Documentation File')

# Define the main transport-and-monitoring body (concurrent)
main_transport = StrictPartialOrder(nodes=[
    temperature_log,
    humidity_control,
    real_time_track,
    stakeholder_update
])
# No edges → all four run in parallel

# Define the loop for transport with emergency contingency
# LOOP(children=[A, B]) means: do A, then either exit or do B then A again
transport_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_transport, emergency_plan]
)

# Define the overall partial order model
root = StrictPartialOrder(nodes=[
    art_catalog,
    pack_securely,
    carrier_assign,
    route_optimize,
    insurance_check,
    provenance_verify,
    customs_submit,
    transport_loop,
    unload_carefully,
    condition_check,
    exhibit_setup,
    documentation_file
])

# Add causal/order relations
root.order.add_edge(art_catalog,    pack_securely)
root.order.add_edge(pack_securely,  carrier_assign)
root.order.add_edge(carrier_assign, route_optimize)

# Insurance and provenance can be done in parallel after packing
root.order.add_edge(pack_securely,   insurance_check)
root.order.add_edge(pack_securely,   provenance_verify)

# Customs after carrier assignment or route optimization
root.order.add_edge(carrier_assign,  customs_submit)
root.order.add_edge(route_optimize,  customs_submit)

# After customs clearance, all monitoring & updates start (loop)
root.order.add_edge(customs_submit, transport_loop)
root.order.add_edge(insurance_check, transport_loop)
root.order.add_edge(provenance_verify, transport_loop)

# After transport loop ends, proceed to arrival steps
root.order.add_edge(transport_loop,     unload_carefully)
root.order.add_edge(unload_carefully,   condition_check)
root.order.add_edge(condition_check,    exhibit_setup)
root.order.add_edge(exhibit_setup,      documentation_file)