# Generated from: c01d5995-e4fd-496e-8b94-1fb581ffbfbf.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponics, renewable energy, and AI-driven climate control. It begins with site assessment and urban zoning compliance, followed by modular structure design and advanced nutrient system installation. After seed selection and germination, automated planting and growth monitoring commence. The process includes continuous environmental adjustments, pest anomaly detection, and adaptive resource allocation. Harvesting is synchronized with supply chain logistics to ensure freshness. Post-harvest, waste recycling and data analytics for yield optimization complete the cycle, emphasizing sustainability and urban food security within constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
site_assessment   = Transition(label='Site Assessment')
zoning_check      = Transition(label='Zoning Check')
structure_design  = Transition(label='Structure Design')
nutrient_setup    = Transition(label='Nutrient Setup')
seed_selection    = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
automated_planting= Transition(label='Automated Planting')
growth_monitor    = Transition(label='Growth Monitor')
climate_adjust    = Transition(label='Climate Adjust')
pest_detection    = Transition(label='Pest Detection')
resource_allocate = Transition(label='Resource Allocate')
harvest_sync      = Transition(label='Harvest Sync')
logistics_plan    = Transition(label='Logistics Plan')
waste_recycle     = Transition(label='Waste Recycle')
data_analytics    = Transition(label='Data Analytics')
yield_optimize    = Transition(label='Yield Optimize')

# Loop for continuous adjustments, pest detection, and resource allocation
body1 = StrictPartialOrder(nodes=[climate_adjust, pest_detection, resource_allocate])
body2 = StrictPartialOrder(nodes=[climate_adjust, pest_detection, resource_allocate])
loop_adjust = OperatorPOWL(operator=Operator.LOOP, children=[body1, body2])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_assessment,
    zoning_check,
    structure_design,
    nutrient_setup,
    seed_selection,
    germination_start,
    automated_planting,
    growth_monitor,
    loop_adjust,
    harvest_sync,
    logistics_plan,
    waste_recycle,
    data_analytics,
    yield_optimize
])

# Define the control-flow (strict ordering)
root.order.add_edge(site_assessment,   zoning_check)
root.order.add_edge(zoning_check,      structure_design)
root.order.add_edge(structure_design,  nutrient_setup)
root.order.add_edge(nutrient_setup,    seed_selection)
root.order.add_edge(seed_selection,    germination_start)
root.order.add_edge(germination_start, automated_planting)
root.order.add_edge(automated_planting, growth_monitor)
root.order.add_edge(growth_monitor,    loop_adjust)
root.order.add_edge(loop_adjust,       harvest_sync)
root.order.add_edge(harvest_sync,      logistics_plan)
root.order.add_edge(logistics_plan,    waste_recycle)
root.order.add_edge(waste_recycle,     data_analytics)
root.order.add_edge(data_analytics,    yield_optimize)