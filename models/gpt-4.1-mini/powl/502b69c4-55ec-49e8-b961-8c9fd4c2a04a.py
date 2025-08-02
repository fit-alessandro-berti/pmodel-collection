# Generated from: 502b69c4-55ec-49e8-b961-8c9fd4c2a04a.json
# Description: This process encompasses the end-to-end management of a vertical urban farm, integrating soil-less cultivation, energy optimization, and supply chain logistics within a dense city environment. It involves seed selection, nutrient balancing, climate control, pest monitoring, data analytics for growth optimization, harvest scheduling, packaging, and real-time delivery coordination. The process also includes waste recycling and energy reclaim strategies to maintain sustainability, alongside regulatory compliance checks and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Water_Calibration = Transition(label='Water Calibration')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Scan = Transition(label='Pest Scan')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Picking = Transition(label='Crop Picking')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Delivery_Sync = Transition(label='Delivery Sync')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Reclaim = Transition(label='Energy Reclaim')
Regulation_Audit = Transition(label='Regulation Audit')
Community_Outreach = Transition(label='Community Outreach')

# Construct subparts/concurrent sets and control-flow operators

# 1. Seed and nutrient setup (Seed Selection -> Nutrient Mix)
seed_and_nutrient = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix])
seed_and_nutrient.order.add_edge(Seed_Selection, Nutrient_Mix)

# 2. Climate & water calibration (Climate Setup -> Water Calibration)
climate_water = StrictPartialOrder(nodes=[Climate_Setup, Water_Calibration])
climate_water.order.add_edge(Climate_Setup, Water_Calibration)

# 3. Crop monitoring and data analytics
# Partial order: (Growth Monitor --> Pest Scan) and (Growth Monitor --> Data Analysis)
# Pest Scan and Data Analysis can run concurrently after Growth Monitor
monitoring = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Scan, Data_Analysis])
monitoring.order.add_edge(Growth_Monitor, Pest_Scan)
monitoring.order.add_edge(Growth_Monitor, Data_Analysis)
# Pest_Scan and Data_Analysis are concurrent (no edge)

# 4. Harvest planning and picking with quality check
harvest_sequence = StrictPartialOrder(nodes=[Harvest_Plan, Crop_Picking, Quality_Check])
harvest_sequence.order.add_edge(Harvest_Plan, Crop_Picking)
harvest_sequence.order.add_edge(Crop_Picking, Quality_Check)

# 5. Packaging and delivery sync (concurrent)
packaging_delivery = StrictPartialOrder(nodes=[Packaging_Prep, Delivery_Sync])

# 6. Sustainability loop: waste sorting and energy reclaim
# Loop: Execute Waste Sorting, then either exit or execute Energy Reclaim then back to Waste Sorting
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Sorting, Energy_Reclaim])

# 7. Regulatory audit and community outreach (can run concurrently)
reg_and_community = StrictPartialOrder(nodes=[Regulation_Audit, Community_Outreach])

# Now combine main phases in partial order:
# Seed & Nutrient ---> Climate & Water ---> Monitoring ---> Harvest ---> Packaging & Delivery
# Sustainability loop and regulatory/community can happen concurrently with harvesting and packaging

main_sequence = StrictPartialOrder(
    nodes=[
        seed_and_nutrient,
        climate_water,
        monitoring,
        harvest_sequence,
        packaging_delivery,
        sustainability_loop,
        reg_and_community
    ]
)

# Define order edges for main sequence
main_sequence.order.add_edge(seed_and_nutrient, climate_water)
main_sequence.order.add_edge(climate_water, monitoring)
main_sequence.order.add_edge(monitoring, harvest_sequence)
main_sequence.order.add_edge(harvest_sequence, packaging_delivery)
# sustainability_loop and reg_and_community are concurrent with harvesting and packaging (no edges, run in parallel)

# root model
root = main_sequence