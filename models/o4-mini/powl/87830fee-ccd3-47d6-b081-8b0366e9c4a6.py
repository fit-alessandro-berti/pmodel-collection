# Generated from: 87830fee-ccd3-47d6-b081-8b0366e9c4a6.json
# Description: This process outlines the intricate steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site analysis, structural modifications, environmental controls, hydroponic system installation, nutrient management, automated monitoring integration, crop selection and rotation planning, pest management without chemicals, energy optimization, waste recycling, and community engagement to ensure sustainable urban agriculture that maximizes yield in limited city spaces while minimizing ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
struct_check = Transition(label='Structural Check')
layout_design = Transition(label='Layout Design')
lighting_setup = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')
hydro_install = Transition(label='Hydroponic Install')
nutrient_mix = Transition(label='Nutrient Mix')
crop_planning = Transition(label='Crop Planning')
pest_monitoring = Transition(label='Pest Monitoring')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
automation_setup = Transition(label='Automation Setup')
waste_sorting = Transition(label='Waste Sorting')
harvest_schedule = Transition(label='Harvest Schedule')
community_outreach = Transition(label='Community Outreach')
market_analysis = Transition(label='Market Analysis')

# Initial site analysis and design
init = StrictPartialOrder(nodes=[site_survey, struct_check, layout_design])
init.order.add_edge(site_survey, struct_check)
init.order.add_edge(struct_check, layout_design)

# Environmental controls and installation
env_inst = StrictPartialOrder(nodes=[layout_design, lighting_setup, climate_control, hydro_install])
env_inst.order.add_edge(layout_design, lighting_setup)
env_inst.order.add_edge(layout_design, climate_control)
env_inst.order.add_edge(lighting_setup, hydro_install)
env_inst.order.add_edge(climate_control, hydro_install)

# Inner operational cycle
inner_ops = StrictPartialOrder(nodes=[pest_monitoring, water_recycling, waste_sorting, harvest_schedule])
inner_ops.order.add_edge(pest_monitoring, water_recycling)
inner_ops.order.add_edge(water_recycling, waste_sorting)
inner_ops.order.add_edge(waste_sorting, harvest_schedule)

# Loop: crop planning then inner operations repeatedly
loop_ops = OperatorPOWL(operator=Operator.LOOP, children=[crop_planning, inner_ops])

# Build the root POWL model
root = StrictPartialOrder(nodes=[
    init,
    env_inst,
    nutrient_mix,
    automation_setup,
    energy_audit,
    loop_ops,
    community_outreach,
    market_analysis
])
root.order.add_edge(init, env_inst)
root.order.add_edge(env_inst, nutrient_mix)
root.order.add_edge(nutrient_mix, automation_setup)
root.order.add_edge(nutrient_mix, energy_audit)
root.order.add_edge(nutrient_mix, loop_ops)
root.order.add_edge(loop_ops, community_outreach)
root.order.add_edge(loop_ops, market_analysis)