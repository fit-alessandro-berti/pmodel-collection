# Generated from: c01d5995-e4fd-496e-8b94-1fb581ffbfbf.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponics, renewable energy, and AI-driven climate control. It begins with site assessment and urban zoning compliance, followed by modular structure design and advanced nutrient system installation. After seed selection and germination, automated planting and growth monitoring commence. The process includes continuous environmental adjustments, pest anomaly detection, and adaptive resource allocation. Harvesting is synchronized with supply chain logistics to ensure freshness. Post-harvest, waste recycling and data analytics for yield optimization complete the cycle, emphasizing sustainability and urban food security within constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Assessment = Transition(label='Site Assessment')
Zoning_Check = Transition(label='Zoning Check')
Structure_Design = Transition(label='Structure Design')
Nutrient_Setup = Transition(label='Nutrient Setup')
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Automated_Planting = Transition(label='Automated Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Climate_Adjust = Transition(label='Climate Adjust')
Pest_Detection = Transition(label='Pest Detection')
Resource_Allocate = Transition(label='Resource Allocate')
Harvest_Sync = Transition(label='Harvest Sync')
Logistics_Plan = Transition(label='Logistics Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analytics = Transition(label='Data Analytics')
Yield_Optimize = Transition(label='Yield Optimize')

# Continuous environmental adjustments, pest anomaly detection and adaptive resource allocation 
# happen "continuously" - modeled as concurrent with growth monitoring
env_adjust = Climate_Adjust
pest_det = Pest_Detection
resource_alloc = Resource_Allocate

# Harvesting synchronized with supply chain logistics: model as partial order with dependency
harvest_sync = Harvest_Sync
logistics_plan = Logistics_Plan

# Post-harvest waste recycling and data analytics for yield optimization close the cycle
waste_recycle = Waste_Recycle
data_analytics = Data_Analytics
yield_optimize = Yield_Optimize

# Model phases:
# 1) Initial assessment and compliance: Site Assessment --> Zoning Check
initial_assess = StrictPartialOrder(nodes=[Site_Assessment, Zoning_Check])
initial_assess.order.add_edge(Site_Assessment, Zoning_Check)

# 2) Modular structure and nutrient setup: Structure Design --> Nutrient Setup
structure_nutrient = StrictPartialOrder(nodes=[Structure_Design, Nutrient_Setup])
structure_nutrient.order.add_edge(Structure_Design, Nutrient_Setup)

# 3) Seed and germination: Seed Selection --> Germination Start
seed_germination = StrictPartialOrder(nodes=[Seed_Selection, Germination_Start])
seed_germination.order.add_edge(Seed_Selection, Germination_Start)

# 4) Planting and growth monitoring start concurrently with environmental adjustments and pest/resource management
# Growth monitor runs concurrently with env_adjust, pest_det, resource_alloc
planting_growth = StrictPartialOrder(nodes=[Automated_Planting, Growth_Monitor, env_adjust, pest_det, resource_alloc])
planting_growth.order.add_edge(Automated_Planting, Growth_Monitor)
# other three concurrent with Growth_Monitor - no edges needed

# 5) Harvest and logistics synchronization: Harvest Sync --> Logistics Plan
harvest_logistics = StrictPartialOrder(nodes=[harvest_sync, logistics_plan])
harvest_logistics.order.add_edge(harvest_sync, logistics_plan)

# 6) Closure cycle: Waste Recycle --> Data Analytics --> Yield Optimize
closing_cycle = StrictPartialOrder(nodes=[waste_recycle, data_analytics, yield_optimize])
closing_cycle.order.add_edge(waste_recycle, data_analytics)
closing_cycle.order.add_edge(data_analytics, yield_optimize)

# Compose the full process in a partial order as follows:
# Phase 1 complete before Phase 2
# Phase 2 complete before Phase 3
# Phase 3 complete before Phase 4
# Phase 4 complete before Phase 5
# Phase 5 complete before Phase 6

root = StrictPartialOrder(nodes=[
    initial_assess, 
    structure_nutrient, 
    seed_germination,
    planting_growth,
    harvest_logistics,
    closing_cycle
])

root.order.add_edge(initial_assess, structure_nutrient)
root.order.add_edge(structure_nutrient, seed_germination)
root.order.add_edge(seed_germination, planting_growth)
root.order.add_edge(planting_growth, harvest_logistics)
root.order.add_edge(harvest_logistics, closing_cycle)