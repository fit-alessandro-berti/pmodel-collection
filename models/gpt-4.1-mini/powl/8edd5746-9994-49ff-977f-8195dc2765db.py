# Generated from: 8edd5746-9994-49ff-977f-8195dc2765db.json
# Description: This process involves establishing a multi-layered urban vertical farm within a constrained city environment. It begins with site analysis and zoning approval, followed by modular infrastructure design tailored to limited space. The process includes hydroponic system installation, nutrient solution calibration, and automated climate control integration. Subsequent activities address seed selection, germination scheduling, and pest management using bio-controls. Continuous monitoring via IoT sensors ensures optimal growth conditions, while data analytics optimize yield cycles. The process concludes with harvest planning, packaging automation, and distribution logistics adapted to urban markets, focusing on sustainability and minimal carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Zoning_Approval = Transition(label='Zoning Approval')
Modular_Design = Transition(label='Modular Design')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Control = Transition(label='Climate Control')
Seed_Selection = Transition(label='Seed Selection')
Germination_Plan = Transition(label='Germination Plan')
Pest_Control = Transition(label='Pest Control')
Sensor_Installation = Transition(label='Sensor Installation')
Data_Monitoring = Transition(label='Data Monitoring')
Yield_Analysis = Transition(label='Yield Analysis')
Harvest_Planning = Transition(label='Harvest Planning')
Packaging_Setup = Transition(label='Packaging Setup')
Urban_Shipping = Transition(label='Urban Shipping')

# Site Analysis and Zoning Approval in sequence (site analysis then zoning approval)
site_phase = StrictPartialOrder(nodes=[Site_Analysis, Zoning_Approval])
site_phase.order.add_edge(Site_Analysis, Zoning_Approval)

# Modular Design follows site_phase
infra_phase = StrictPartialOrder(nodes=[Modular_Design, Hydroponic_Setup, Nutrient_Mix, Climate_Control])
# Modular Design before hydroponic setup, nutrient mix, climate control (which are concurrent among themselves)
infra_phase.order.add_edge(Modular_Design, Hydroponic_Setup)
infra_phase.order.add_edge(Modular_Design, Nutrient_Mix)
infra_phase.order.add_edge(Modular_Design, Climate_Control)

# Seed Selection, Germination Plan, Pest Control can start after infra_phase
seed_phase = StrictPartialOrder(nodes=[Seed_Selection, Germination_Plan, Pest_Control])
# They can be concurrent, no internal order needed

# Sensor Installation, Data Monitoring, Yield Analysis come after seed_phase concurrently
monitor_phase = StrictPartialOrder(nodes=[Sensor_Installation, Data_Monitoring, Yield_Analysis])
# All three concurrent, no order

# Harvest Planning, Packaging Setup, Urban Shipping in sequence
final_phase = StrictPartialOrder(nodes=[Harvest_Planning, Packaging_Setup, Urban_Shipping])
final_phase.order.add_edge(Harvest_Planning, Packaging_Setup)
final_phase.order.add_edge(Packaging_Setup, Urban_Shipping)

# Combine phases with order edges reflecting the overall flow

# Combine all partial orders nodes
all_nodes = [site_phase, infra_phase, seed_phase, monitor_phase, final_phase]

root = StrictPartialOrder(nodes=all_nodes)

# Add order between phase nodes to represent process flow
root.order.add_edge(site_phase, infra_phase)
root.order.add_edge(infra_phase, seed_phase)
root.order.add_edge(seed_phase, monitor_phase)
root.order.add_edge(monitor_phase, final_phase)