# Generated from: 69989004-cfba-496b-aa7b-808747236ae8.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a densely populated city environment. It includes site assessment, modular infrastructure assembly, climate control calibration, nutrient delivery optimization, and automated harvesting integration. Special attention is given to sustainable energy use, waste recycling loops, pest management without chemicals, and real-time crop monitoring through IoT devices. Collaborative coordination with city planners, local suppliers, and technology vendors ensures compliance with urban regulations and maximizes resource efficiency. The process concludes with staff training and community engagement to promote urban agriculture awareness and long-term operational success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activity transitions
site_survey   = Transition(label="Site Survey")
design_layout = Transition(label="Design Layout")
permit_acquire = Transition(label="Permit Acquire")
modular_build = Transition(label="Modular Build")
climate_setup = Transition(label="Climate Setup")
water_install = Transition(label="Water Install")
nutrient_mix  = Transition(label="Nutrient Mix")
energy_sync   = Transition(label="Energy Sync")
sensor_deploy = Transition(label="Sensor Deploy")
lighting_adjust = Transition(label="Lighting Adjust")
pest_inspect  = Transition(label="Pest Inspect")
waste_cycle   = Transition(label="Waste Cycle")
harvest_plan  = Transition(label="Harvest Plan")
staff_train   = Transition(label="Staff Train")
community_meet = Transition(label="Community Meet")

# Build a loop for repeated pest inspection and waste cycling
# LOOP semantics: first execute pest_inspect, then choose to exit or do waste_cycle then pest_inspect again
pest_waste_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_inspect, waste_cycle]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_acquire,
    modular_build,
    climate_setup,
    water_install,
    nutrient_mix,
    energy_sync,
    sensor_deploy,
    lighting_adjust,
    pest_waste_loop,
    harvest_plan,
    staff_train,
    community_meet
])

# Sequential flow: Survey → Design → Permit → Build → Climate setup
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)
root.order.add_edge(permit_acquire, modular_build)
root.order.add_edge(modular_build, climate_setup)

# After climate setup, these steps can proceed concurrently
for nxt in [water_install, nutrient_mix, energy_sync, sensor_deploy, lighting_adjust]:
    root.order.add_edge(climate_setup, nxt)

# All five installations feed into the pest & waste loop
for prev in [water_install, nutrient_mix, energy_sync, sensor_deploy, lighting_adjust]:
    root.order.add_edge(prev, pest_waste_loop)

# After the pest/waste loop, plan harvesting, then train staff, then engage community
root.order.add_edge(pest_waste_loop, harvest_plan)
root.order.add_edge(harvest_plan, staff_train)
root.order.add_edge(staff_train, community_meet)