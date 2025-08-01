# Generated from: 2f643349-5e76-488c-9c65-e1e0946b7109.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating advanced hydroponic systems with AI-driven environmental controls. It begins with seed selection and germination, followed by nutrient solution preparation and automated planting. Continuous monitoring of microclimate variables such as temperature, humidity, and light intensity is performed to optimize growth. Periodic pest detection and organic treatment applications ensure plant health without chemical residues. Harvesting is synchronized with real-time demand forecasting to reduce waste, while post-harvest sorting and packaging employ robotic systems to maintain quality and freshness. Finally, logistics coordination manages last-mile delivery, integrating customer feedback loops to adapt production schedules dynamically, promoting sustainability and urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_select      = Transition(label='Seed Select')
germinate_seeds  = Transition(label='Germinate Seeds')
prepare_nutrients = Transition(label='Prepare Nutrients')
automated_planting = Transition(label='Automated Planting')
monitor_climate  = Transition(label='Monitor Climate')
adjust_lighting  = Transition(label='Adjust Lighting')
growth_analysis  = Transition(label='Growth Analysis')
pest_detect      = Transition(label='Pest Detect')
organic_treat    = Transition(label='Organic Treat')
demand_forecast  = Transition(label='Demand Forecast')
harvest_crops    = Transition(label='Harvest Crops')
sort_produce     = Transition(label='Sort Produce')
robotic_package  = Transition(label='Robotic Package')
schedule_delivery = Transition(label='Schedule Delivery')
collect_feedback = Transition(label='Collect Feedback')
update_protocols = Transition(label='Update Protocols')

# A silent transition for loop exits
skip = SilentTransition()

# Environment control loop: Monitor -> Adjust -> Analyze, repeated until exit
env_ctrl = StrictPartialOrder(
    nodes=[monitor_climate, adjust_lighting, growth_analysis]
)
env_ctrl.order.add_edge(monitor_climate, adjust_lighting)
env_ctrl.order.add_edge(adjust_lighting, growth_analysis)
env_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_ctrl, skip])

# Pest control loop: Detect -> Treat, repeated until exit
pest_ctrl = StrictPartialOrder(
    nodes=[pest_detect, organic_treat]
)
pest_ctrl.order.add_edge(pest_detect, organic_treat)
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_ctrl, skip])

# Assemble the full process
root = StrictPartialOrder(
    nodes=[
        seed_select,
        germinate_seeds,
        prepare_nutrients,
        automated_planting,
        env_loop,
        pest_loop,
        demand_forecast,
        harvest_crops,
        sort_produce,
        robotic_package,
        schedule_delivery,
        collect_feedback,
        update_protocols
    ]
)

# Define the partial order
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, prepare_nutrients)
root.order.add_edge(prepare_nutrients, automated_planting)

# After planting, both control loops run (concurrently) until ready to forecast demand
root.order.add_edge(automated_planting, env_loop)
root.order.add_edge(automated_planting, pest_loop)

# Once loops complete, move to harvesting synchronized with demand forecasting
root.order.add_edge(env_loop, demand_forecast)
root.order.add_edge(pest_loop, demand_forecast)
root.order.add_edge(demand_forecast, harvest_crops)

# Post-harvest sorting and packaging
root.order.add_edge(harvest_crops, sort_produce)
root.order.add_edge(sort_produce, robotic_package)

# Logistics and feedback loop to update protocols
root.order.add_edge(robotic_package, schedule_delivery)
root.order.add_edge(schedule_delivery, collect_feedback)
root.order.add_edge(collect_feedback, update_protocols)