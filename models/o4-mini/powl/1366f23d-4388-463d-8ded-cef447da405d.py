# Generated from: 1366f23d-4388-463d-8ded-cef447da405d.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a city environment. It involves site evaluation, modular system design, nutrient solution formulation, and integration of IoT sensors for real-time monitoring. The process further includes seed selection optimized for vertical growth, automated planting, climate control calibration, and pest management using bio-controls. Post-harvest handling features automated sorting and quality inspection, coupled with data analytics to improve yield cycles. Finally, the system incorporates waste recycling and energy optimization to ensure sustainability and scalability within limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey    = Transition(label="Site Survey")
system_design  = Transition(label="System Design")
seed_selection = Transition(label="Seed Selection")
nutrient_mix   = Transition(label="Nutrient Mix")
iot_setup      = Transition(label="IoT Setup")
planting_auto  = Transition(label="Planting Automation")
climate_adj    = Transition(label="Climate Adjust")
pest_control   = Transition(label="Pest Control")
water_recycle  = Transition(label="Water Recycling")
harvest_sort   = Transition(label="Harvest Sort")
quality_insp   = Transition(label="Quality Inspect")
data_analysis  = Transition(label="Data Analysis")
yield_report   = Transition(label="Yield Report")
waste_manage   = Transition(label="Waste Manage")
energy_mon     = Transition(label="Energy Monitor")

# A silent transition for optional paths
skip = SilentTransition()

# Build a loop for ongoing climate adjustment and pest control:
#   execute climate_adj, then either exit or do pest_control then repeat climate_adj
pest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[climate_adj, pest_control]
)

# After planting we optionally enter the climate/pest loop or skip it
planting_after = OperatorPOWL(
    operator=Operator.XOR,
    children=[pest_loop, skip]
)

# Build the main partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        system_design,
        seed_selection,
        nutrient_mix,
        iot_setup,
        planting_auto,
        planting_after,
        water_recycle,
        harvest_sort,
        quality_insp,
        data_analysis,
        yield_report,
        waste_manage,
        energy_mon
    ]
)

# Define control-flow relations
# 1. Site survey precedes design and seed selection
root.order.add_edge(site_survey, system_design)
root.order.add_edge(site_survey, seed_selection)

# 2. System design precedes nutrient mix and IoT setup
root.order.add_edge(system_design, nutrient_mix)
root.order.add_edge(system_design, iot_setup)

# 3. Nutrient mix, IoT setup, and seed selection all precede automated planting
root.order.add_edge(nutrient_mix, planting_auto)
root.order.add_edge(iot_setup, planting_auto)
root.order.add_edge(seed_selection, planting_auto)

# 4. After planting, go into the optional loop / skip
root.order.add_edge(planting_auto, planting_after)

# 5. After climate/pest loop (or skip), proceed to water recycling
root.order.add_edge(planting_after, water_recycle)

# 6. Water recycling precedes harvest sorting
root.order.add_edge(water_recycle, harvest_sort)

# 7. Harvest sorting precedes quality inspection
root.order.add_edge(harvest_sort, quality_insp)

# 8. Quality inspection precedes data analysis
root.order.add_edge(quality_insp, data_analysis)

# 9. Data analysis leads to yield report, waste management, and energy monitoring (these can be concurrent)
root.order.add_edge(data_analysis, yield_report)
root.order.add_edge(data_analysis, waste_manage)
root.order.add_edge(data_analysis, energy_mon)