# Generated from: b0c5e5a6-ecb6-4c96-ae43-b8b33bd457ec.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site analysis, modular system design, integration of hydroponic and aeroponic technologies, environmental control calibration, nutrient solution preparation, automated seeding, growth monitoring through IoT sensors, pest management using biological agents, data-driven yield optimization, energy consumption balancing with renewable sources, and final product packaging for local distribution. The process demands multidisciplinary coordination between architects, agronomists, engineers, and supply chain managers to ensure sustainability, efficiency, and scalability within a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Tech_Integration = Transition(label='Tech Integration')
Env_Control = Transition(label='Env Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Data_Analysis = Transition(label='Data Analysis')
Energy_Balance = Transition(label='Energy Balance')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Supply_Chain = Transition(label='Supply Chain')
Quality_Audit = Transition(label='Quality Audit')
Market_Launch = Transition(label='Market Launch')

# Partial order for initial site and design activities
init_PO = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
init_PO.order.add_edge(Site_Survey, Design_Layout)

# Partial order for tech integration and environmental control
tech_PO = StrictPartialOrder(nodes=[Tech_Integration, Env_Control])
tech_PO.order.add_edge(Tech_Integration, Env_Control)

# Partial order for nutrient mix and seed automation
nut_seed_PO = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Automation])
nut_seed_PO.order.add_edge(Nutrient_Mix, Seed_Automation)

# Partial order for growth monitoring, pest control, and data analysis
growth_pest_data_PO = StrictPartialOrder(
    nodes=[Growth_Monitor, Pest_Control, Data_Analysis]
)
growth_pest_data_PO.order.add_edge(Growth_Monitor, Pest_Control)
growth_pest_data_PO.order.add_edge(Pest_Control, Data_Analysis)

# Partial order for energy balance and harvest planning
energy_harvest_PO = StrictPartialOrder(nodes=[Energy_Balance, Harvest_Plan])
energy_harvest_PO.order.add_edge(Energy_Balance, Harvest_Plan)

# Partial order for packaging prep, supply chain, quality audit, market launch
pack_supply_quality_market_PO = StrictPartialOrder(
    nodes=[Packaging_Prep, Supply_Chain, Quality_Audit, Market_Launch]
)
pack_supply_quality_market_PO.order.add_edge(Packaging_Prep, Supply_Chain)
pack_supply_quality_market_PO.order.add_edge(Supply_Chain, Quality_Audit)
pack_supply_quality_market_PO.order.add_edge(Quality_Audit, Market_Launch)

# Combine initial phases partial orders: init_PO --> tech_PO --> nut_seed_PO
phase1_PO = StrictPartialOrder(
    nodes=[init_PO, tech_PO, nut_seed_PO]
)
phase1_PO.order.add_edge(init_PO, tech_PO)
phase1_PO.order.add_edge(tech_PO, nut_seed_PO)

# Combine monitoring and control phase with energy_harvest_PO, after nutrient and seed
phase2_PO = StrictPartialOrder(
    nodes=[growth_pest_data_PO, energy_harvest_PO]
)
phase2_PO.order.add_edge(growth_pest_data_PO, energy_harvest_PO)

# Overall order:
# phase1_PO --> phase2_PO --> packaging to market PO
root = StrictPartialOrder(
    nodes=[phase1_PO, phase2_PO, pack_supply_quality_market_PO]
)
root.order.add_edge(phase1_PO, phase2_PO)
root.order.add_edge(phase2_PO, pack_supply_quality_market_PO)