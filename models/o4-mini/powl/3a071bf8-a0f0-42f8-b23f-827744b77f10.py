# Generated from: 3a071bf8-a0f0-42f8-b23f-827744b77f10.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a densely populated city environment. It begins with site analysis and regulatory assessment, followed by infrastructure design tailored to limited space. Procurement involves sourcing specialized hydroponic equipment and sustainable materials. Installation includes modular stacking, climate control systems, and automated irrigation setup. Subsequent stages cover crop selection based on urban climate data, nutrient solution formulation, and seeding protocols. Continuous monitoring is conducted through IoT sensors for growth optimization and pest detection. Finally, the process integrates urban community engagement for education and distribution logistics to local markets, ensuring sustainability and profitability within urban agriculture constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis     = Transition(label='Site Analysis')
regulatory_check  = Transition(label='Regulatory Check')
design_layout     = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
equipment_order   = Transition(label='Equipment Order')
module_assembly   = Transition(label='Module Assembly')
climate_setup     = Transition(label='Climate Setup')
irrigation_install= Transition(label='Irrigation Install')
crop_selection    = Transition(label='Crop Selection')
nutrient_mix      = Transition(label='Nutrient Mix')
seeding_start     = Transition(label='Seeding Start')
sensor_deploy     = Transition(label='Sensor Deploy')
growth_monitor    = Transition(label='Growth Monitor')
pest_detect       = Transition(label='Pest Detect')
community_engage  = Transition(label='Community Engage')
market_setup      = Transition(label='Market Setup')

# Loop for continuous monitoring: Growth Monitor (A), then optionally Pest Detect (B) then back
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_detect]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, regulatory_check,
    design_layout,
    material_sourcing, equipment_order,
    module_assembly, climate_setup, irrigation_install,
    crop_selection, nutrient_mix, seeding_start,
    sensor_deploy, monitor_loop,
    community_engage, market_setup
])

# Add ordering constraints
root.order.add_edge(site_analysis,     design_layout)
root.order.add_edge(regulatory_check,  design_layout)

root.order.add_edge(design_layout,     material_sourcing)
root.order.add_edge(design_layout,     equipment_order)

root.order.add_edge(material_sourcing, module_assembly)
root.order.add_edge(equipment_order,   module_assembly)

root.order.add_edge(module_assembly,   climate_setup)
root.order.add_edge(module_assembly,   irrigation_install)

root.order.add_edge(climate_setup,     crop_selection)
root.order.add_edge(irrigation_install,crop_selection)

root.order.add_edge(crop_selection,    nutrient_mix)
root.order.add_edge(nutrient_mix,      seeding_start)

root.order.add_edge(seeding_start,     sensor_deploy)
root.order.add_edge(sensor_deploy,     monitor_loop)

root.order.add_edge(monitor_loop,      community_engage)
root.order.add_edge(community_engage,  market_setup)