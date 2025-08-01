# Generated from: 3a071bf8-a0f0-42f8-b23f-827744b77f10.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a densely populated city environment. It begins with site analysis and regulatory assessment, followed by infrastructure design tailored to limited space. Procurement involves sourcing specialized hydroponic equipment and sustainable materials. Installation includes modular stacking, climate control systems, and automated irrigation setup. Subsequent stages cover crop selection based on urban climate data, nutrient solution formulation, and seeding protocols. Continuous monitoring is conducted through IoT sensors for growth optimization and pest detection. Finally, the process integrates urban community engagement for education and distribution logistics to local markets, ensuring sustainability and profitability within urban agriculture constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
regulatory_check = Transition(label='Regulatory Check')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
equipment_order = Transition(label='Equipment Order')
module_assembly = Transition(label='Module Assembly')
climate_setup = Transition(label='Climate Setup')
irrigation_install = Transition(label='Irrigation Install')
crop_selection = Transition(label='Crop Selection')
nutrient_mix = Transition(label='Nutrient Mix')
seeding_start = Transition(label='Seeding Start')
sensor_deploy = Transition(label='Sensor Deploy')
growth_monitor = Transition(label='Growth Monitor')
pest_detect = Transition(label='Pest Detect')
community_engage = Transition(label='Community Engage')
market_setup = Transition(label='Market Setup')

# Procurement: Material Sourcing and Equipment Order concurrently
procurement = StrictPartialOrder(nodes=[material_sourcing, equipment_order])  # concurrent, no order edges

# Installation with partial order:
# Module Assembly --> Climate Setup --> Irrigation Install
installation = StrictPartialOrder(nodes=[module_assembly, climate_setup, irrigation_install])
installation.order.add_edge(module_assembly, climate_setup)
installation.order.add_edge(climate_setup, irrigation_install)

# Crop preparation order:
# Crop Selection --> Nutrient Mix --> Seeding Start
crop_prep = StrictPartialOrder(nodes=[crop_selection, nutrient_mix, seeding_start])
crop_prep.order.add_edge(crop_selection, nutrient_mix)
crop_prep.order.add_edge(nutrient_mix, seeding_start)

# Monitoring partial order with concurrent growth_monitor and pest_detect after sensor_deploy:
monitoring = StrictPartialOrder(nodes=[sensor_deploy, growth_monitor, pest_detect])
monitoring.order.add_edge(sensor_deploy, growth_monitor)
monitoring.order.add_edge(sensor_deploy, pest_detect)
# growth_monitor and pest_detect concurrent

# Final community engagement followed by market setup
community_and_market = StrictPartialOrder(nodes=[community_engage, market_setup])
community_and_market.order.add_edge(community_engage, market_setup)

# Overall top-level partial order
nodes = [
    site_analysis,
    regulatory_check,
    design_layout,
    procurement,
    installation,
    crop_prep,
    monitoring,
    community_and_market
]

root = StrictPartialOrder(nodes=nodes)

# Site Analysis --> Regulatory Check --> Design Layout
root.order.add_edge(site_analysis, regulatory_check)
root.order.add_edge(regulatory_check, design_layout)

# Design Layout --> Procurement
root.order.add_edge(design_layout, procurement)

# Procurement --> Installation
root.order.add_edge(procurement, installation)

# Installation --> Crop Preparation
root.order.add_edge(installation, crop_prep)

# Crop Preparation --> Monitoring
root.order.add_edge(crop_prep, monitoring)

# Monitoring --> Community & Market
root.order.add_edge(monitoring, community_and_market)