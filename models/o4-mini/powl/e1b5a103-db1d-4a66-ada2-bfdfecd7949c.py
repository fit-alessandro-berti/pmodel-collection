# Generated from: e1b5a103-db1d-4a66-ada2-bfdfecd7949c.json
# Description: This process involves establishing an urban vertical farming system within a repurposed building. It begins with site analysis and structural assessment to ensure suitability, followed by climate control calibration and hydroponic system installation. Nutrient mixing and seed selection are carefully managed to optimize crop yield. Automated lighting and irrigation scheduling are configured to simulate ideal growth conditions. Continuous monitoring of plant health and pest control methods are integrated to maintain quality. Harvesting is done using robotics to minimize labor, and post-harvest processing includes cleaning, packaging, and distribution planning. Finally, data collection and system feedback loops help refine future crop cycles, ensuring sustainability and profitability within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis      = Transition(label="Site Analysis")
structure_check    = Transition(label="Structure Check")
climate_setup      = Transition(label="Climate Setup")
hydroponics_install= Transition(label="Hydroponics Install")
nutrient_mix       = Transition(label="Nutrient Mix")
seed_select        = Transition(label="Seed Select")
light_schedule     = Transition(label="Light Schedule")
irrigation_plan    = Transition(label="Irrigation Plan")
health_monitor     = Transition(label="Health Monitor")
pest_control       = Transition(label="Pest Control")
robotic_harvest    = Transition(label="Robotic Harvest")
clean_packaging    = Transition(label="Clean Packaging")
distribution_plan  = Transition(label="Distribution Plan")
data_collection    = Transition(label="Data Collection")
cycle_feedback     = Transition(label="Cycle Feedback")

# Group the naturally concurrent steps into partial‐order fragments
phase2 = StrictPartialOrder(nodes=[climate_setup, hydroponics_install])
phase3 = StrictPartialOrder(nodes=[nutrient_mix, seed_select])
phase4 = StrictPartialOrder(nodes=[light_schedule, irrigation_plan])
phase5 = StrictPartialOrder(nodes=[health_monitor, pest_control])

# Define the feedback loop: Data Collection (A) then optionally Cycle Feedback (B) then back to A
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_collection, cycle_feedback]
)

# Assemble the root partial order
root = StrictPartialOrder(
    nodes=[
        site_analysis,
        structure_check,
        phase2,
        phase3,
        phase4,
        phase5,
        robotic_harvest,
        clean_packaging,
        distribution_plan,
        feedback_loop
    ]
)

# Specify the control‐flow edges
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, robotic_harvest)
root.order.add_edge(robotic_harvest, clean_packaging)
root.order.add_edge(clean_packaging, distribution_plan)
root.order.add_edge(distribution_plan, feedback_loop)