# Generated from: e01de5dc-964d-49a5-8d9b-25e36abc0945.json
# Description: This process outlines the end-to-end management of an urban vertical farming system that integrates automated nutrient delivery, climate control, pest management, and crop harvesting within a multi-level indoor environment. The cycle begins with seed selection and germination under controlled light spectrums, followed by transplanting seedlings into hydroponic towers. Nutrient mixing and precise pH balancing ensure optimal growth conditions, while AI-powered sensors continuously monitor humidity, temperature, and CO2 levels. Pest detection triggers environmentally friendly interventions, avoiding chemical use. Harvesting is scheduled by maturity models and robots collect produce for packaging. Waste is composted on-site and water is recycled to minimize resource use, closing the loop for sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
t_select       = Transition(label='Seed Select')
t_germinate    = Transition(label='Germinate Seeds')
t_transplant   = Transition(label='Transplant Seedlings')
t_mix          = Transition(label='Mix Nutrients')
t_ph           = Transition(label='Adjust pH')
t_monitor      = Transition(label='Monitor Climate')
t_humidity     = Transition(label='Control Humidity')
t_co2          = Transition(label='CO2 Regulation')
t_detect       = Transition(label='Detect Pests')
t_deploy       = Transition(label='Deploy Biocontrols')
t_schedule     = Transition(label='Schedule Harvest')
t_picking      = Transition(label='Automate Picking')
t_package      = Transition(label='Package Produce')
t_compost      = Transition(label='Compost Waste')
t_recycle      = Transition(label='Recycle Water')
t_logging      = Transition(label='Data Logging')
t_maint        = Transition(label='System Maintenance')

# Silent skip for optional biocontrol deployment
skip = SilentTransition()

# XOR for optional deployment of biocontrols after pest detection
xor_deploy = OperatorPOWL(operator=Operator.XOR, children=[t_deploy, skip])

# Initial seed-to-transplant sequence
preproc = StrictPartialOrder(nodes=[t_select, t_germinate, t_transplant])
preproc.order.add_edge(t_select, t_germinate)
preproc.order.add_edge(t_germinate, t_transplant)

# Body A: nutrient mixing and pH adjustment
body_a = StrictPartialOrder(nodes=[t_mix, t_ph])
body_a.order.add_edge(t_mix, t_ph)

# Body B: monitoring, controls, detection, optional deployment, logging
body_b = StrictPartialOrder(
    nodes=[t_monitor, t_humidity, t_co2, t_detect, xor_deploy, t_logging]
)
# monitor precedes the controls, detection, and logging
body_b.order.add_edge(t_monitor, t_humidity)
body_b.order.add_edge(t_monitor, t_co2)
body_b.order.add_edge(t_monitor, t_logging)
# after humidity/co2/logging, detect pests
body_b.order.add_edge(t_humidity, t_detect)
body_b.order.add_edge(t_co2, t_detect)
body_b.order.add_edge(t_logging, t_detect)
# detection leads to XOR choice
body_b.order.add_edge(t_detect, xor_deploy)

# Loop: repeat nutrient/mix cycle until exit (harvest)
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_a, body_b])

# After finishing loop, schedule harvest and downstream steps
root = StrictPartialOrder(
    nodes=[
        preproc, loop,
        t_schedule, t_picking, t_package,
        t_compost, t_recycle,
        t_maint
    ]
)
# Connect the main flow
root.order.add_edge(preproc, loop)
root.order.add_edge(loop, t_schedule)
root.order.add_edge(t_schedule, t_picking)
root.order.add_edge(t_picking, t_package)
# parallel composting and recycling after packaging
root.order.add_edge(t_package, t_compost)
root.order.add_edge(t_package, t_recycle)
# both waste flows lead to final maintenance
root.order.add_edge(t_compost, t_maint)
root.order.add_edge(t_recycle, t_maint)