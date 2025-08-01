# Generated from: 4c46611c-da16-40c4-bbfe-b8153ea3468c.json
# Description: This process manages the end-to-end supply chain of an urban vertical farming operation, integrating automated planting, environmental monitoring, nutrient delivery, and harvest scheduling with downstream distribution logistics. It involves coordination between IoT sensors, AI-driven growth optimization, quality inspections, packaging automation, and last-mile delivery to retailers and consumers within a metropolitan area. The process ensures minimal waste, energy efficiency, and freshness, while adapting dynamically to demand fluctuations and seasonal variations, requiring continuous data analysis and prompt decision-making across multiple departments and external partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
tray_preparation = Transition(label='Tray Preparation')
automated_planting = Transition(label='Automated Planting')

env_monitoring = Transition(label='Env Monitoring')
nutrient_delivery = Transition(label='Nutrient Delivery')

growth_analysis = Transition(label='Growth Analysis')
pest_detection = Transition(label='Pest Detection')

harvest_scheduling = Transition(label='Harvest Scheduling')
quality_inspection = Transition(label='Quality Inspection')
automated_packaging = Transition(label='Automated Packaging')

inventory_tracking = Transition(label='Inventory Tracking')
demand_forecast = Transition(label='Demand Forecast')

order_processing = Transition(label='Order Processing')
last_mile_dispatch = Transition(label='Last-Mile Dispatch')

customer_feedback = Transition(label='Customer Feedback')

waste_management = Transition(label='Waste Management')
energy_optimization = Transition(label='Energy Optimization')

# Partial order for the initial preparation phase
prep_phase = StrictPartialOrder(
    nodes=[seed_selection, tray_preparation, automated_planting]
)
prep_phase.order.add_edge(seed_selection, tray_preparation)
prep_phase.order.add_edge(tray_preparation, automated_planting)

# Partial order for monitoring and delivery, can be concurrent
monitoring_phase = StrictPartialOrder(
    nodes=[env_monitoring, nutrient_delivery]
)

# Growth analysis and pest detection run in parallel (concurrent)
analysis_phase = StrictPartialOrder(
    nodes=[growth_analysis, pest_detection]
)

# Harvest and quality related workflow: harvest -> quality -> packaging
harvest_phase = StrictPartialOrder(
    nodes=[harvest_scheduling, quality_inspection, automated_packaging]
)
harvest_phase.order.add_edge(harvest_scheduling, quality_inspection)
harvest_phase.order.add_edge(quality_inspection, automated_packaging)

# Inventory and demand forecast in parallel
inventory_demand = StrictPartialOrder(
    nodes=[inventory_tracking, demand_forecast]
)

# Order processing and last mile delivery sequentially
order_delivery = StrictPartialOrder(
    nodes=[order_processing, last_mile_dispatch]
)
order_delivery.order.add_edge(order_processing, last_mile_dispatch)

# Waste management and energy optimization can run concurrently anytime after harvest phases
sustainability = StrictPartialOrder(
    nodes=[waste_management, energy_optimization]
)

# Customer feedback is after last-mile delivery
customer_feedback_phase = StrictPartialOrder(
    nodes=[customer_feedback]
)

# Compose the higher-level partial order

# Root nodes of the big PO:
# 1) prep_phase
# 2) monitoring_phase and nutrient_delivery run concurrent after planting
# 3) analysis_phase after monitoring and nutrient delivery (for growth and pest)
# 4) harvest_phase after analysis_phase
# 5) inventory_demand concurrent after harvest_phase
# 6) order_delivery after inventory_demand
# 7) sustainability concurrent with or after harvest_phase (we put after harvest)
# 8) customer_feedback after order_delivery

root = StrictPartialOrder(
    nodes=[
        prep_phase,
        monitoring_phase,
        analysis_phase,
        harvest_phase,
        inventory_demand,
        order_delivery,
        sustainability,
        customer_feedback_phase
    ]
)

# Define edges between phases

# prep -> monitoring
root.order.add_edge(prep_phase, monitoring_phase)

# monitoring -> analysis
root.order.add_edge(monitoring_phase, analysis_phase)

# analysis -> harvest
root.order.add_edge(analysis_phase, harvest_phase)

# harvest -> inventory_demand
root.order.add_edge(harvest_phase, inventory_demand)

# inventory_demand -> order_delivery
root.order.add_edge(inventory_demand, order_delivery)

# harvest -> sustainability (concurrent but after harvest)
root.order.add_edge(harvest_phase, sustainability)

# order_delivery -> customer_feedback
root.order.add_edge(order_delivery, customer_feedback_phase)