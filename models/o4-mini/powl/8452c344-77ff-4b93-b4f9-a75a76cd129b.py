# Generated from: 8452c344-77ff-4b93-b4f9-a75a76cd129b.json
# Description: This process describes the complex operational cycle of an urban vertical farming facility that integrates automated hydroponics, AI-driven environmental control, and community engagement. It begins with nutrient formulation and seed selection, followed by automated planting and continuous environmental monitoring. The system adjusts lighting, humidity, and nutrient delivery dynamically, responding to real-time sensor data. Periodic pest detection and organic treatment application ensure crop health without chemicals. Harvesting is automated using robotic arms, then produce undergoes quality inspection and packaging. The process also includes data logging for yield optimization and community distribution planning. Finally, waste recycling and equipment maintenance close the loop, ensuring sustainability and operational efficiency in an atypical yet realistic urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
t_seed_selection = Transition(label='Seed Selection')
t_nutrient_mix    = Transition(label='Nutrient Mix')
t_automated_plant = Transition(label='Automated Plant')
t_enviro_monitor  = Transition(label='Enviro Monitor')
t_light_adjust    = Transition(label='Light Adjust')
t_humidity_ctrl   = Transition(label='Humidity Control')
t_nutrient_feed   = Transition(label='Nutrient Feed')
t_pest_detect     = Transition(label='Pest Detect')
t_organic_treat   = Transition(label='Organic Treat')
t_robotic_harvest = Transition(label='Robotic Harvest')
t_quality_check   = Transition(label='Quality Check')
t_produce_pack    = Transition(label='Produce Pack')
t_data_log        = Transition(label='Data Log')
t_yield_review    = Transition(label='Yield Review')
t_community_plan  = Transition(label='Community Plan')
t_waste_recycle   = Transition(label='Waste Recycle')
t_equip_maintain  = Transition(label='Equip Maintain')

# Build the environmental adjustment sub‐process (concurrent adjustments)
enviro_adjust = StrictPartialOrder(
    nodes=[t_light_adjust, t_humidity_ctrl, t_nutrient_feed]
)
# LOOP for continuous monitor → adjust repeated
enviro_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_enviro_monitor, enviro_adjust]
)

# LOOP for periodic pest detection → treatment
pest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_pest_detect, t_organic_treat]
)

# Build the overall POWL as a strict partial order
root = StrictPartialOrder(
    nodes=[
        # initial parallel seed & nutrient, then planting
        t_seed_selection, t_nutrient_mix, t_automated_plant,
        # the two loops
        enviro_loop, pest_loop,
        # harvesting and downstream
        t_robotic_harvest, t_quality_check, t_produce_pack,
        t_data_log, t_yield_review, t_community_plan,
        # closing activities
        t_waste_recycle, t_equip_maintain
    ]
)

# Define the control‐flow edges
# Seed & nutrient in parallel, both must complete before planting
root.order.add_edge(t_seed_selection, t_automated_plant)
root.order.add_edge(t_nutrient_mix,    t_automated_plant)
# Sequence: plant → enviro loop → pest loop → harvest …
root.order.add_edge(t_automated_plant, enviro_loop)
root.order.add_edge(enviro_loop,       pest_loop)
root.order.add_edge(pest_loop,         t_robotic_harvest)
root.order.add_edge(t_robotic_harvest, t_quality_check)
root.order.add_edge(t_quality_check,   t_produce_pack)
root.order.add_edge(t_produce_pack,    t_data_log)
root.order.add_edge(t_data_log,        t_yield_review)
root.order.add_edge(t_yield_review,    t_community_plan)
# Closing the loop
root.order.add_edge(t_community_plan,  t_waste_recycle)
root.order.add_edge(t_waste_recycle,   t_equip_maintain)