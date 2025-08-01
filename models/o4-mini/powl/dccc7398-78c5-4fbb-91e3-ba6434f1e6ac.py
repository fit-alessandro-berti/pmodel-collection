# Generated from: dccc7398-78c5-4fbb-91e3-ba6434f1e6ac.json
# Description: This process outlines the complex steps involved in establishing a fully automated urban vertical farm within a metropolitan area. It begins with site evaluation and ends with ongoing crop optimization. The workflow integrates architectural design, environmental control installation, nutrient cycling, robotic planting, AI-based growth monitoring, pest management using bio-controls, and energy-efficient harvesting. Stakeholders coordinate across disciplines including agronomy, engineering, logistics, and IT to ensure sustainable production in limited urban spaces while minimizing water and energy usage. The process also involves regulatory compliance checks, community engagement, and market integration for fresh produce distribution, making it a multifaceted endeavor requiring precise orchestration of technology and human expertise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
survey = Transition(label='Site Survey')
design = Transition(label='Design Draft')
permit = Transition(label='Permit Review')
build = Transition(label='Structure Build')
enviro = Transition(label='Enviro Setup')
nutrient = Transition(label='Nutrient Mix')
seed = Transition(label='Seed Selection')
robots = Transition(label='Plant Robots')
sensors = Transition(label='Sensor Install')
sync = Transition(label='Data Sync')
growth = Transition(label='Growth Monitor')
pest = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
quality = Transition(label='Quality Check')
market = Transition(label='Market Launch')
feedback = Transition(label='Feedback Loop')

# Loop body: Pest Control -> Feedback Loop
b_loop = StrictPartialOrder(nodes=[pest, feedback])
b_loop.order.add_edge(pest, feedback)

# Loop operator: repeat Growth Monitor and then optionally the body
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[growth, b_loop])

# Root partial order with concurrency after structure build
root = StrictPartialOrder(nodes=[
    survey, design, permit, build,
    enviro, nutrient, seed, robots, sensors,
    sync, loop_node, harvest_plan, quality, market
])

# Sequencing edges
root.order.add_edge(survey, design)
root.order.add_edge(design, permit)
root.order.add_edge(permit, build)

# After build, these run in parallel
root.order.add_edge(build, enviro)
root.order.add_edge(build, nutrient)
root.order.add_edge(build, seed)
root.order.add_edge(build, robots)
root.order.add_edge(build, sensors)

# Synchronize to data sync
root.order.add_edge(enviro, sync)
root.order.add_edge(nutrient, sync)
root.order.add_edge(seed, sync)
root.order.add_edge(robots, sync)
root.order.add_edge(sensors, sync)

# Continue with loop and final stages
root.order.add_edge(sync, loop_node)
root.order.add_edge(loop_node, harvest_plan)
root.order.add_edge(harvest_plan, quality)
root.order.add_edge(quality, market)