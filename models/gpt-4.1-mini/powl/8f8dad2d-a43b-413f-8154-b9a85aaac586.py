# Generated from: 8f8dad2d-a43b-413f-8154-b9a85aaac586.json
# Description: This process describes a complex urban farming system that integrates aquaponics, renewable energy, and real-time data analytics to optimize crop yield and resource efficiency. The cycle begins with environmental sensing and seed selection, followed by adaptive nutrient balancing and automated pest control. It incorporates waste recycling from local sources, energy management through solar and wind inputs, and dynamic scheduling based on weather predictions. Continuous monitoring ensures plant health, while machine learning algorithms adjust growth parameters. Harvesting is synchronized with market demand forecasts, and post-harvest processing includes packaging and distribution using sustainable logistics. The process closes with community feedback integration and system maintenance to enhance future cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Select = Transition(label='Seed Select')
Env_Sensing = Transition(label='Env Sensing')
Water_Filter = Transition(label='Water Filter')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Waste_Collect = Transition(label='Waste Collect')
Energy_Charge = Transition(label='Energy Charge')
Data_Monitor = Transition(label='Data Monitor')
Growth_Adjust = Transition(label='Growth Adjust')
Health_Check = Transition(label='Health Check')
Market_Sync = Transition(label='Market Sync')
Harvest_Crop = Transition(label='Harvest Crop')
Package_Goods = Transition(label='Package Goods')
Logistics_Plan = Transition(label='Logistics Plan')
Feedback_Loop = Transition(label='Feedback Loop')
System_Maintain = Transition(label='System Maintain')

# Initial phase: environmental sensing and seed selection can happen concurrently
init_phase = StrictPartialOrder(nodes=[Env_Sensing, Seed_Select])

# Followed by adaptive nutrient balancing and automated pest control:
nutrient_pest_PO = StrictPartialOrder(nodes=[Water_Filter, Nutrient_Mix, Pest_Control])
nutrient_pest_PO.order.add_edge(Water_Filter, Nutrient_Mix)
nutrient_pest_PO.order.add_edge(Nutrient_Mix, Pest_Control)

# Waste recycling and energy management also happen concurrently:
waste_energy_PO = StrictPartialOrder(nodes=[Waste_Collect, Energy_Charge])

# Dynamic scheduling based on weather predictions is tied with data monitoring and growth adjustment:
data_growth_PO = StrictPartialOrder(nodes=[Data_Monitor, Growth_Adjust])

data_growth_PO.order.add_edge(Data_Monitor, Growth_Adjust)

# Continuous monitoring ensures plant health:
health_PO = StrictPartialOrder(nodes=[Health_Check])

# Harvest synchronized with market demand forecasts:
harvest_PO = StrictPartialOrder(nodes=[Market_Sync, Harvest_Crop])
harvest_PO.order.add_edge(Market_Sync, Harvest_Crop)

# Post-harvest processing: packaging and distribution planning concurrently
post_harvest_PO = StrictPartialOrder(nodes=[Package_Goods, Logistics_Plan])

# Closing with community feedback and system maintenance sequentially:
closing_PO = StrictPartialOrder(nodes=[Feedback_Loop, System_Maintain])
closing_PO.order.add_edge(Feedback_Loop, System_Maintain)

# Compose main flow partial order:
# After init_phase, nutrient_pest_PO, then waste_energy_PO concurrent with data_growth_PO,
# then health_PO, then harvest_PO, then post_harvest_PO, then closing_PO

main_PO = StrictPartialOrder(nodes=[
    init_phase,
    nutrient_pest_PO,
    waste_energy_PO,
    data_growth_PO,
    health_PO,
    harvest_PO,
    post_harvest_PO,
    closing_PO,
])

# Define edges to order phases sequentially
main_PO.order.add_edge(init_phase, nutrient_pest_PO)
main_PO.order.add_edge(nutrient_pest_PO, waste_energy_PO)
main_PO.order.add_edge(nutrient_pest_PO, data_growth_PO)
# waste_energy_PO and data_growth_PO are concurrent, so no order between them

# Both waste_energy_PO and data_growth_PO must precede health_PO
main_PO.order.add_edge(waste_energy_PO, health_PO)
main_PO.order.add_edge(data_growth_PO, health_PO)

main_PO.order.add_edge(health_PO, harvest_PO)
main_PO.order.add_edge(harvest_PO, post_harvest_PO)
main_PO.order.add_edge(post_harvest_PO, closing_PO)

root = main_PO