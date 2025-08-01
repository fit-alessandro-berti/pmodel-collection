# Generated from: 51e8c314-9dca-4ca0-9cf1-0b7d316754e0.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to optimize space and resources in dense city environments. It begins with site analysis and zoning compliance checks, followed by infrastructure design tailored to vertical stacking of crops. The workflow includes environmental control calibration, hydroponic system installation, and seedling propagation. Advanced nutrient delivery and pest management protocols are integrated, along with real-time monitoring setup using IoT devices. Staff training on automated systems and continuous yield optimization strategies are conducted. Finally, the process culminates in a phased crop harvesting schedule and waste recycling plan to ensure sustainability and profitability within an atypical urban agricultural model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activity nodes
site_analysis     = Transition(label='Site Analysis')
zoning_review     = Transition(label='Zoning Review')
design_layout     = Transition(label='Design Layout')
stack_assembly    = Transition(label='Stack Assembly')
env_control       = Transition(label='Env Control')
hydro_install     = Transition(label='Hydro Install')
seed_propagation  = Transition(label='Seed Propagation')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_monitor      = Transition(label='Pest Monitor')
iot_setup         = Transition(label='IoT Setup')
staff_training    = Transition(label='Staff Training')
yield_audit       = Transition(label='Yield Audit')
harvest_plan      = Transition(label='Harvest Plan')
waste_manage      = Transition(label='Waste Manage')
market_prep       = Transition(label='Market Prep')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_review, design_layout, stack_assembly,
    env_control, hydro_install, seed_propagation,
    nutrient_mix, pest_monitor, iot_setup,
    staff_training, yield_audit,
    harvest_plan, waste_manage, market_prep
])

# Sequence edges
root.order.add_edge(site_analysis,    zoning_review)
root.order.add_edge(zoning_review,    design_layout)
root.order.add_edge(design_layout,    stack_assembly)
root.order.add_edge(stack_assembly,   env_control)
root.order.add_edge(env_control,      hydro_install)
root.order.add_edge(hydro_install,    seed_propagation)

# Parallel Nutrient Mix & Pest Monitor after seed propagation
root.order.add_edge(seed_propagation, nutrient_mix)
root.order.add_edge(seed_propagation, pest_monitor)

# Both join before IoT setup
root.order.add_edge(nutrient_mix,     iot_setup)
root.order.add_edge(pest_monitor,     iot_setup)

# Continue sequentially to the end
root.order.add_edge(iot_setup,        staff_training)
root.order.add_edge(staff_training,   yield_audit)
root.order.add_edge(yield_audit,      harvest_plan)
root.order.add_edge(harvest_plan,     waste_manage)
root.order.add_edge(waste_manage,     market_prep)