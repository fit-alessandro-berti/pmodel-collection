# Generated from: 502b69c4-55ec-49e8-b961-8c9fd4c2a04a.json
# Description: This process encompasses the end-to-end management of a vertical urban farm, integrating soil-less cultivation, energy optimization, and supply chain logistics within a dense city environment. It involves seed selection, nutrient balancing, climate control, pest monitoring, data analytics for growth optimization, harvest scheduling, packaging, and real-time delivery coordination. The process also includes waste recycling and energy reclaim strategies to maintain sustainability, alongside regulatory compliance checks and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
seed_selection     = Transition(label='Seed Selection')
nutrient_mix       = Transition(label='Nutrient Mix')
climate_setup      = Transition(label='Climate Setup')
water_calibration  = Transition(label='Water Calibration')
growth_monitor     = Transition(label='Growth Monitor')
pest_scan          = Transition(label='Pest Scan')
data_analysis      = Transition(label='Data Analysis')
harvest_plan       = Transition(label='Harvest Plan')
crop_picking       = Transition(label='Crop Picking')
quality_check      = Transition(label='Quality Check')
packaging_prep     = Transition(label='Packaging Prep')
delivery_sync      = Transition(label='Delivery Sync')
waste_sorting      = Transition(label='Waste Sorting')
energy_reclaim     = Transition(label='Energy Reclaim')
regulation_audit   = Transition(label='Regulation Audit')
community_outreach = Transition(label='Community Outreach')

# Model the repeated monitor-scan-analysis cycle as a loop
monitor_analysis = StrictPartialOrder(nodes=[growth_monitor, pest_scan, data_analysis])
monitor_analysis.order.add_edge(growth_monitor, data_analysis)
monitor_analysis.order.add_edge(pest_scan, data_analysis)

loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_analysis, monitor_analysis]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    climate_setup,
    water_calibration,
    loop_cycle,
    harvest_plan,
    crop_picking,
    quality_check,
    packaging_prep,
    delivery_sync,
    waste_sorting,
    energy_reclaim,
    regulation_audit,
    community_outreach
])

# Define the control‐flow edges
root.order.add_edge(seed_selection,    nutrient_mix)
root.order.add_edge(nutrient_mix,      climate_setup)
root.order.add_edge(climate_setup,     water_calibration)
root.order.add_edge(water_calibration, loop_cycle)

root.order.add_edge(loop_cycle,        harvest_plan)
root.order.add_edge(harvest_plan,      crop_picking)
root.order.add_edge(crop_picking,      quality_check)
root.order.add_edge(quality_check,     packaging_prep)
root.order.add_edge(packaging_prep,    delivery_sync)

# After delivery, sort waste and reclaim energy in parallel
root.order.add_edge(delivery_sync,     waste_sorting)
root.order.add_edge(delivery_sync,     energy_reclaim)

# Then do the regulation audit, followed by community outreach
root.order.add_edge(waste_sorting,     regulation_audit)
root.order.add_edge(energy_reclaim,    regulation_audit)
root.order.add_edge(regulation_audit,  community_outreach)