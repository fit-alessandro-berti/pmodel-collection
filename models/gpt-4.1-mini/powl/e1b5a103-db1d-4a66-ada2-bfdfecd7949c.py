# Generated from: e1b5a103-db1d-4a66-ada2-bfdfecd7949c.json
# Description: This process involves establishing an urban vertical farming system within a repurposed building. It begins with site analysis and structural assessment to ensure suitability, followed by climate control calibration and hydroponic system installation. Nutrient mixing and seed selection are carefully managed to optimize crop yield. Automated lighting and irrigation scheduling are configured to simulate ideal growth conditions. Continuous monitoring of plant health and pest control methods are integrated to maintain quality. Harvesting is done using robotics to minimize labor, and post-harvest processing includes cleaning, packaging, and distribution planning. Finally, data collection and system feedback loops help refine future crop cycles, ensuring sustainability and profitability within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
climate_setup = Transition(label='Climate Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_mix = Transition(label='Nutrient Mix')
seed_select = Transition(label='Seed Select')
light_schedule = Transition(label='Light Schedule')
irrigation_plan = Transition(label='Irrigation Plan')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
robotic_harvest = Transition(label='Robotic Harvest')
clean_packaging = Transition(label='Clean Packaging')
distribution_plan = Transition(label='Distribution Plan')
data_collection = Transition(label='Data Collection')
cycle_feedback = Transition(label='Cycle Feedback')

# Initial partial order: Site Analysis -> Structure Check
po1 = StrictPartialOrder(nodes=[site_analysis, structure_check])
po1.order.add_edge(site_analysis, structure_check)

# Next partial order: Climate Setup -> Hydroponics Install
po2 = StrictPartialOrder(nodes=[climate_setup, hydroponics_install])
po2.order.add_edge(climate_setup, hydroponics_install)

# Nutrient Mix and Seed Select happen sequentially
po3 = StrictPartialOrder(nodes=[nutrient_mix, seed_select])
po3.order.add_edge(nutrient_mix, seed_select)

# Light Schedule and Irrigation Plan happen concurrently (no order needed)
po4 = StrictPartialOrder(nodes=[light_schedule, irrigation_plan])

# Health Monitor and Pest Control happen concurrently
po5 = StrictPartialOrder(nodes=[health_monitor, pest_control])

# Clean Packaging and Distribution Plan happen sequentially
po6 = StrictPartialOrder(nodes=[clean_packaging, distribution_plan])
po6.order.add_edge(clean_packaging, distribution_plan)

# Data Collection followed by Cycle Feedback in a loop: (Data Collection, then loop of Cycle Feedback feeding back to Data Collection)
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, cycle_feedback])

# Assemble the workflow connections:

# Build initial sequential parts combined into partial orders with edges:
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5, robotic_harvest, po6, loop_cycle]
)

# Add dependencies between these parts that reflect the described sequence:

# po1(order: Site Analysis->Structure Check) -> po2(Climate Setup -> Hydroponics Install)
root.order.add_edge(po1, po2)

# po2 -> po3 (Nutrient Mix -> Seed Select)
root.order.add_edge(po2, po3)

# po3 -> po4 (Light Schedule, Irrigation Plan)
root.order.add_edge(po3, po4)

# po4 -> po5 (Health Monitor, Pest Control)
root.order.add_edge(po4, po5)

# po5 -> robotic_harvest
root.order.add_edge(po5, robotic_harvest)

# robotic_harvest -> po6 (Clean Packaging -> Distribution Plan)
root.order.add_edge(robotic_harvest, po6)

# po6 -> loop_cycle (Data Collection and feedback loop)
root.order.add_edge(po6, loop_cycle)