# Generated from: c1e58648-3d17-4dc8-a2c4-a1c7f8604899.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a metropolitan environment. It covers site selection in dense urban areas, integration of advanced hydroponic systems, environmental control calibration, and multi-level crop scheduling. The process also includes securing permits, implementing renewable energy sources, establishing supply chain logistics for fresh produce, and coordinating with local community stakeholders to ensure sustainability and compliance with urban regulations. Each activity is designed to optimize yield while minimizing ecological footprint, ensuring year-round production with minimal human intervention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label="Site Survey")
permit_filing  = Transition(label="Permit Filing")
design_layout  = Transition(label="Design Layout")
community_meet = Transition(label="Community Meet")
hydro_setup    = Transition(label="Hydro Setup")
lighting_install = Transition(label="Lighting Install")
climate_tune   = Transition(label="Climate Tune")
energy_setup   = Transition(label="Energy Setup")
seed_sourcing  = Transition(label="Seed Sourcing")
water_testing  = Transition(label="Water Testing")
nutrient_mix   = Transition(label="Nutrient Mix")
planting_cycle = Transition(label="Planting Cycle")
pest_control   = Transition(label="Pest Control")
harvest_plan   = Transition(label="Harvest Plan")
logistics_map  = Transition(label="Logistics Map")
waste_manage   = Transition(label="Waste Manage")
data_monitor   = Transition(label="Data Monitor")

# 1) Initial site selection, permitting, and design
init = StrictPartialOrder(nodes=[site_survey, permit_filing, design_layout])
init.order.add_edge(site_survey, permit_filing)
init.order.add_edge(permit_filing, design_layout)

# 2) Community engagement after design
#    (must follow design, so we treat it in the main PO)
# 3) System setup: hydroponics, lighting, climate, energy
setup = StrictPartialOrder(nodes=[hydro_setup, lighting_install, climate_tune, energy_setup])
setup.order.add_edge(hydro_setup, lighting_install)
setup.order.add_edge(lighting_install, climate_tune)
setup.order.add_edge(climate_tune, energy_setup)

# 4) Pre-cultivation: sourcing seeds then water & nutrient prep (parallel)
pre_cult = StrictPartialOrder(nodes=[seed_sourcing, water_testing, nutrient_mix])
pre_cult.order.add_edge(seed_sourcing, water_testing)
pre_cult.order.add_edge(seed_sourcing, nutrient_mix)

# 5) Growing cycle loop: Plant & protect, then harvest & downstream tasks
growA = StrictPartialOrder(nodes=[planting_cycle, pest_control])
growA.order.add_edge(planting_cycle, pest_control)

growB = StrictPartialOrder(nodes=[harvest_plan, logistics_map, waste_manage, data_monitor])
growB.order.add_edge(harvest_plan, logistics_map)
growB.order.add_edge(logistics_map, waste_manage)
growB.order.add_edge(waste_manage, data_monitor)

cycle = OperatorPOWL(operator=Operator.LOOP, children=[growA, growB])

# 6) Assemble the full process
root = StrictPartialOrder(
    nodes=[init, community_meet, setup, pre_cult, cycle]
)
# order everything in sequence
root.order.add_edge(init, community_meet)
root.order.add_edge(community_meet, setup)
root.order.add_edge(setup, pre_cult)
root.order.add_edge(pre_cult, cycle)