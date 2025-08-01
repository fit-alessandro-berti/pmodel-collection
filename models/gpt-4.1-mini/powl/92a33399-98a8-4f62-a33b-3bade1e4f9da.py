# Generated from: 92a33399-98a8-4f62-a33b-3bade1e4f9da.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a dense metropolitan area. It includes initial site assessment, securing permits, soil testing, modular bed construction, irrigation system design, selecting climate-resilient crops, integrating renewable energy sources, pest management planning, community engagement, and ongoing yield optimization. The workflow balances environmental, regulatory, and social factors to promote urban agriculture as a viable food source while minimizing ecological footprint and maximizing space utilization on rooftops with structural and safety constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Soil_Testing = Transition(label='Soil Testing')
Bed_Assembly = Transition(label='Bed Assembly')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Selection = Transition(label='Crop Selection')
Energy_Integration = Transition(label='Energy Integration')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Nutrient_Planning = Transition(label='Nutrient Planning')
Water_Recycling = Transition(label='Water Recycling')
Growth_Monitoring = Transition(label='Growth Monitoring')
Yield_Analysis = Transition(label='Yield Analysis')
Safety_Inspection = Transition(label='Safety Inspection')
Waste_Composting = Transition(label='Waste Composting')

# Initial phase: Site Survey then Permit Filing and Soil Testing in parallel
initial_po = StrictPartialOrder(
    nodes=[Site_Survey, Permit_Filing, Soil_Testing]
)
initial_po.order.add_edge(Site_Survey, Permit_Filing)
initial_po.order.add_edge(Site_Survey, Soil_Testing)

# Construction and setup phase: Bed Assembly, Irrigation Setup, Energy Integration (concurrent)
construction_po = StrictPartialOrder(
    nodes=[Bed_Assembly, Irrigation_Setup, Energy_Integration]
)

# Crop and pest planning: Crop Selection then Pest Control and Nutrient Planning (both concurrent)
crop_plan_po = StrictPartialOrder(
    nodes=[Crop_Selection, Pest_Control, Nutrient_Planning]
)
crop_plan_po.order.add_edge(Crop_Selection, Pest_Control)
crop_plan_po.order.add_edge(Crop_Selection, Nutrient_Planning)

# Waste management and safety inspection run concurrently with community engagement
waste_safety_po = StrictPartialOrder(
    nodes=[Waste_Composting, Safety_Inspection, Community_Meet]
)

# Monitoring phase: Water Recycling, Growth Monitoring, Yield Analysis in order
monitoring_po = StrictPartialOrder(
    nodes=[Water_Recycling, Growth_Monitoring, Yield_Analysis]
)
monitoring_po.order.add_edge(Water_Recycling, Growth_Monitoring)
monitoring_po.order.add_edge(Growth_Monitoring, Yield_Analysis)

# Loop to represent ongoing yield optimization and monitoring:
# Loop body = monitoring_po
# Loop condition = Community_Meet (used as a silent transition here, to model periodic engagement)
# But Community_Meet is already used, so use silent transition for loop exit

skip = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_po, skip])

# Assemble the whole process partial order:

# Phase 1 (initial) --> Phase 2 (construction) --> Phase 3 (crop planning) --> Phase 4 (waste+safety+community) --> monitor_loop

root = StrictPartialOrder(
    nodes=[initial_po, construction_po, crop_plan_po, waste_safety_po, monitor_loop]
)
root.order.add_edge(initial_po, construction_po)
root.order.add_edge(construction_po, crop_plan_po)
root.order.add_edge(crop_plan_po, waste_safety_po)
root.order.add_edge(waste_safety_po, monitor_loop)