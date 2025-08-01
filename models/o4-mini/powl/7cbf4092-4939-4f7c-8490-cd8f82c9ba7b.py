# Generated from: 7cbf4092-4939-4f7c-8490-cd8f82c9ba7b.json
# Description: This process details the establishment of a vertical farming operation within an urban environment, integrating sustainable agricultural practices with advanced technology. It involves site analysis, modular construction, environmental controls calibration, nutrient solution management, and crop cycle optimization. The procedure also includes stakeholder coordination, regulatory compliance checks, energy use monitoring, and waste recycling strategies to maximize yield and minimize footprint in a confined city space. Continuous data collection and adaptive growth algorithms ensure efficient resource use and crop quality throughout multiple harvest cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
stakeholder_meet = Transition(label='Stakeholder Meet')
regulation_check = Transition(label='Regulation Check')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
module_assembly  = Transition(label='Module Assembly')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
climate_control  = Transition(label='Climate Control')
nutrient_mix     = Transition(label='Nutrient Mix')

seed_planting    = Transition(label='Seed Planting')
growth_monitoring= Transition(label='Growth Monitoring')
pest_screening   = Transition(label='Pest Screening')
harvest_planning = Transition(label='Harvest Planning')
yield_analysis   = Transition(label='Yield Analysis')
waste_handling   = Transition(label='Waste Handling')
energy_tracking  = Transition(label='Energy Tracking')

# Build the cycle body (B)
cycle_body = StrictPartialOrder(nodes=[
    growth_monitoring,
    pest_screening,
    harvest_planning,
    yield_analysis,
    waste_handling,
    energy_tracking
])
cycle_body.order.add_edge(growth_monitoring, pest_screening)
cycle_body.order.add_edge(pest_screening, harvest_planning)
cycle_body.order.add_edge(harvest_planning, yield_analysis)
cycle_body.order.add_edge(yield_analysis, waste_handling)
cycle_body.order.add_edge(waste_handling, energy_tracking)

# Build the loop: do Seed Planting then repeat the rest until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, cycle_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    stakeholder_meet,
    regulation_check,
    design_layout,
    material_sourcing,
    module_assembly,
    irrigation_setup,
    lighting_install,
    climate_control,
    nutrient_mix,
    loop
])

# Sequencing edges
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(stakeholder_meet, regulation_check)
root.order.add_edge(regulation_check, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, module_assembly)

# Module setup can proceed in parallel
root.order.add_edge(module_assembly, irrigation_setup)
root.order.add_edge(module_assembly, lighting_install)
root.order.add_edge(module_assembly, climate_control)

# After all setups, mix nutrients then start the harvest loop
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(lighting_install, nutrient_mix)
root.order.add_edge(climate_control, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)