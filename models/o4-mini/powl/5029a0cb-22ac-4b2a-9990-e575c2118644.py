# Generated from: 5029a0cb-22ac-4b2a-9990-e575c2118644.json
# Description: This process governs the comprehensive cycle of urban vertical farming operations, integrating advanced hydroponics, AI-driven climate control, and waste recycling to optimize crop yield in limited spaces. It begins with site assessment and modular setup, followed by nutrient solution preparation and seed germination under automated lighting. Continuous monitoring adjusts environmental factors to maintain ideal growth conditions. Pollination is handled mechanically or via introduced insects. Harvesting is robotic, with quality sorting and packaging tailored for urban distribution channels. Waste biomass is processed into compost or bioenergy, closing the sustainability loop. Data analytics feed into predictive maintenance and crop planning, ensuring maximum efficiency and minimal resource consumption throughout the cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site        = Transition(label='Site Assess')
module      = Transition(label='Module Setup')
nutrient    = Transition(label='Nutrient Mix')
seed        = Transition(label='Seed Germinate')
climate     = Transition(label='Climate Control')
monitor     = Transition(label='Growth Monitor')
pest        = Transition(label='Pest Detect')
pollination = Transition(label='Pollination Aid')
harvest     = Transition(label='Harvest Crop')
quality     = Transition(label='Quality Check')
package     = Transition(label='Package Goods')
waste       = Transition(label='Waste Process')
compost     = Transition(label='Compost Create')
energy      = Transition(label='Energy Generate')
data        = Transition(label='Data Analyze')
maintenance = Transition(label='Maintenance Plan')

# Model the exclusive choice between composting and energy generation
waste_choice = OperatorPOWL(operator=Operator.XOR, children=[compost, energy])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, module, nutrient, seed,
    climate, monitor, pest,
    pollination, harvest, quality, package,
    waste, waste_choice,
    data, maintenance
])

# Define the control‐flow dependencies
root.order.add_edge(site, module)
root.order.add_edge(module, nutrient)
root.order.add_edge(nutrient, seed)

# After germination, environmental processes run in parallel
root.order.add_edge(seed, climate)
root.order.add_edge(seed, monitor)
root.order.add_edge(seed, pest)

# All three environment tasks must complete before pollination
root.order.add_edge(climate, pollination)
root.order.add_edge(monitor, pollination)
root.order.add_edge(pest, pollination)

# Harvesting sequence
root.order.add_edge(pollination, harvest)
root.order.add_edge(harvest, quality)
root.order.add_edge(quality, package)

# Waste processing and choice
root.order.add_edge(package, waste)
root.order.add_edge(waste, waste_choice)

# After waste outcome, do data analytics and maintenance planning
root.order.add_edge(waste_choice, data)
root.order.add_edge(data, maintenance)