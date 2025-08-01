# Generated from: 5bc20f9d-dbd3-4f3c-9d30-e1da52e781b5.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system in a densely populated city environment. It includes site analysis for optimal sunlight and space utilization, modular structure design to maximize crop yield vertically, integration of hydroponic and aeroponic systems for water and nutrient efficiency, automation setup for climate control and harvesting, and continuous monitoring through IoT sensors. The process also involves compliance checks with local regulations, community engagement for urban acceptance, pilot crop trials, and scaling strategies to expand production sustainably while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site         = Transition(label="Site Analysis")
light        = Transition(label="Light Mapping")
structure    = Transition(label="Structure Design")
system       = Transition(label="System Integration")
water        = Transition(label="Water Setup")
nutrient     = Transition(label="Nutrient Mix")
automation   = Transition(label="Automation Config")
sensor       = Transition(label="Sensor Install")
climate      = Transition(label="Climate Control")
compliance   = Transition(label="Compliance Review")
community    = Transition(label="Community Meet")
pilot        = Transition(label="Pilot Planting")
monitor      = Transition(label="Data Monitoring")
harvest      = Transition(label="Harvest Trial")
scale        = Transition(label="Scale Planning")
waste        = Transition(label="Waste Reuse")

# Sub‐process: concurrent water & nutrient setup
integration_po = StrictPartialOrder(nodes=[water, nutrient])
# (no edges => water and nutrient run in parallel)

# Loop for continuous monitoring and harvest trials
monitor_harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor, harvest]
)

# Root partial order
root = StrictPartialOrder(nodes=[
    site,
    light,
    structure,
    system,
    integration_po,
    automation,
    sensor,
    climate,
    compliance,
    community,
    pilot,
    monitor_harvest_loop,
    scale,
    waste
])

# Define the control‐flow dependencies
o = root.order
o.add_edge(site,         light)
o.add_edge(light,        structure)
o.add_edge(structure,    system)
o.add_edge(system,       integration_po)
o.add_edge(integration_po, automation)
o.add_edge(automation,   sensor)
o.add_edge(sensor,       climate)
o.add_edge(climate,      compliance)
o.add_edge(climate,      community)
o.add_edge(compliance,   pilot)
o.add_edge(community,    pilot)
o.add_edge(pilot,        monitor_harvest_loop)
o.add_edge(monitor_harvest_loop, scale)
o.add_edge(scale,        waste)