# Generated from: 2f643349-5e76-488c-9c65-e1e0946b7109.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating advanced hydroponic systems with AI-driven environmental controls. It begins with seed selection and germination, followed by nutrient solution preparation and automated planting. Continuous monitoring of microclimate variables such as temperature, humidity, and light intensity is performed to optimize growth. Periodic pest detection and organic treatment applications ensure plant health without chemical residues. Harvesting is synchronized with real-time demand forecasting to reduce waste, while post-harvest sorting and packaging employ robotic systems to maintain quality and freshness. Finally, logistics coordination manages last-mile delivery, integrating customer feedback loops to adapt production schedules dynamically, promoting sustainability and urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SeedSelect = Transition(label='Seed Select')
GerminateSeeds = Transition(label='Germinate Seeds')
PrepareNutrients = Transition(label='Prepare Nutrients')
AutomatedPlanting = Transition(label='Automated Planting')
MonitorClimate = Transition(label='Monitor Climate')
AdjustLighting = Transition(label='Adjust Lighting')
PestDetect = Transition(label='Pest Detect')
OrganicTreat = Transition(label='Organic Treat')
GrowthAnalysis = Transition(label='Growth Analysis')
HarvestCrops = Transition(label='Harvest Crops')
SortProduce = Transition(label='Sort Produce')
RoboticPackage = Transition(label='Robotic Package')
DemandForecast = Transition(label='Demand Forecast')
ScheduleDelivery = Transition(label='Schedule Delivery')
CollectFeedback = Transition(label='Collect Feedback')
UpdateProtocols = Transition(label='Update Protocols')

# Loop body for continuous monitoring and treatment:
# MonitorClimate, AdjustLighting, PestDetect, OrganicTreat, GrowthAnalysis in partial order:
# PestDetect --> OrganicTreat (must detect before treat)
# Others concurrent with appropriate order (MonitorClimate before AdjustLighting, GrowthAnalysis can be after some treatment)

# Define partial order for the monitoring-treatment-growth cycle
monitoring_treatment_growth = StrictPartialOrder(nodes=[
    MonitorClimate, AdjustLighting, PestDetect, OrganicTreat, GrowthAnalysis
])
monitoring_treatment_growth.order.add_edge(MonitorClimate, AdjustLighting)
monitoring_treatment_growth.order.add_edge(PestDetect, OrganicTreat)

# Create the loop:
# Loop structure: * (monitoring_treatment_growth, skip)
# Instead of skip, loop with exit or continue: in pm4py the loop is * (A, B)
# So B is the repeat part; here we want the loop as: execute A (monitoring treatment growth), then choose exit or repeat
# Using loop = OperatorPOWL(LOOP, [A, B])
# B is empty means exit or B is A again means repeat inner cycle
# But pm4py LOOP requires two children; so we can put a silent transition for exit
from pm4py.objects.powl.obj import SilentTransition

exit_silent = SilentTransition()
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_treatment_growth, exit_silent])

# Post-harvest processing: SortProduce, RoboticPackage in sequence
post_harvest = StrictPartialOrder(nodes=[SortProduce, RoboticPackage])
post_harvest.order.add_edge(SortProduce, RoboticPackage)

# Delivery and feedback cycle (loop):
# DemandForecast -> ScheduleDelivery -> CollectFeedback -> UpdateProtocols
# Then UpdateProtocols loops back to DemandForecast (to adapt production schedules dynamically)

delivery_feedback_nodes = [DemandForecast, ScheduleDelivery, CollectFeedback, UpdateProtocols]
delivery_feedback_po = StrictPartialOrder(nodes=delivery_feedback_nodes)
delivery_feedback_po.order.add_edge(DemandForecast, ScheduleDelivery)
delivery_feedback_po.order.add_edge(ScheduleDelivery, CollectFeedback)
delivery_feedback_po.order.add_edge(CollectFeedback, UpdateProtocols)

# Loop delivery feedback cycle around DemandForecast
loop_delivery_feedback = OperatorPOWL(operator=Operator.LOOP, children=[
    delivery_feedback_po,
    exit_silent  # exit option from feedback loop when needed
])

# Main initial sequence
initial_seq = StrictPartialOrder(nodes=[
    SeedSelect, GerminateSeeds, PrepareNutrients, AutomatedPlanting
])
initial_seq.order.add_edge(SeedSelect, GerminateSeeds)
initial_seq.order.add_edge(GerminateSeeds, PrepareNutrients)
initial_seq.order.add_edge(PrepareNutrients, AutomatedPlanting)

# Harvest crops after growth analysis and monitoring loop (the loop presumably ends before harvest)
# So HarvestCrops depends on loop_monitoring and initial processes complete
# We assume harvest after the monitoring loop (loop_monitoring)
# Then post_harvest, then delivery_feedback loop

# Define partial order with all main nodes in concurrency, adding edges to impose order:
# initial_seq --> loop_monitoring --> HarvestCrops --> post_harvest --> loop_delivery_feedback

main_po = StrictPartialOrder(nodes=[
    initial_seq, loop_monitoring, HarvestCrops, post_harvest, loop_delivery_feedback
])
main_po.order.add_edge(initial_seq, loop_monitoring)
main_po.order.add_edge(loop_monitoring, HarvestCrops)
main_po.order.add_edge(HarvestCrops, post_harvest)
main_po.order.add_edge(post_harvest, loop_delivery_feedback)

root = main_po