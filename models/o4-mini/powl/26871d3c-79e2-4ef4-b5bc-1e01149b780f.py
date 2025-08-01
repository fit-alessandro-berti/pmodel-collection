# Generated from: 26871d3c-79e2-4ef4-b5bc-1e01149b780f.json
# Description: This process outlines the complex sequence of activities required to establish a fully operational urban vertical farm within a constrained city environment. It involves site assessment, modular structure design, climate control calibration, nutrient cycling optimization, automation integration, and compliance with local agricultural and environmental regulations. The process also includes workforce training, system testing, crop scheduling, pest monitoring, and community engagement to ensure sustainability and productivity in a high-density urban setting, reflecting a cutting-edge approach to food production and resource management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
struct_build     = Transition(label='Structural Build')
install_panels   = Transition(label='Install Panels')
climate_setup    = Transition(label='Climate Setup')
water_system     = Transition(label='Water System')
nutrient_mix     = Transition(label='Nutrient Mix')
automation_config= Transition(label='Automation Config')
staff_training   = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
seed_selection   = Transition(label='Seed Selection')
planting_cycle   = Transition(label='Planting Cycle')
pest_monitor     = Transition(label='Pest Monitor')
data_collection  = Transition(label='Data Collection')
harvest_plan     = Transition(label='Harvest Plan')
waste_manage     = Transition(label='Waste Manage')
community_outreach = Transition(label='Community Outreach')

# Loop for ongoing monitoring and data collection after planting
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, data_collection])

# Build the partial order model
nodes = [
    site_survey, design_layout, struct_build, install_panels,
    climate_setup, water_system, nutrient_mix, automation_config,
    staff_training, compliance_check, seed_selection, planting_cycle,
    pest_loop, harvest_plan, waste_manage, community_outreach
]
root = StrictPartialOrder(nodes=nodes)

# Define the control-flow dependencies
root.order.add_edge(site_survey,     design_layout)
root.order.add_edge(design_layout,   struct_build)
root.order.add_edge(struct_build,    install_panels)
# Parallel setup of climate and water system
root.order.add_edge(install_panels,  climate_setup)
root.order.add_edge(install_panels,  water_system)
root.order.add_edge(water_system,    nutrient_mix)
# Automation depends on climate and nutrient readiness
root.order.add_edge(climate_setup,   automation_config)
root.order.add_edge(nutrient_mix,    automation_config)
# Training and compliance in parallel after automation configured
root.order.add_edge(automation_config, staff_training)
root.order.add_edge(automation_config, compliance_check)
# Both must finish before selecting seeds and planting
root.order.add_edge(staff_training,  seed_selection)
root.order.add_edge(compliance_check, seed_selection)
root.order.add_edge(seed_selection,  planting_cycle)
# After planting, enter monitoring & data-collection loop
root.order.add_edge(planting_cycle,  pest_loop)
# Exit loop to harvesting plan
root.order.add_edge(pest_loop,       harvest_plan)
# Final parallel activities
root.order.add_edge(harvest_plan,    waste_manage)
root.order.add_edge(harvest_plan,    community_outreach)