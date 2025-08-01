# Generated from: 527fb39a-9849-4565-a440-c5ab2be20bef.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense city environment. It involves assessing structural integrity, securing permits, designing modular planting systems, selecting crop varieties suited for limited sunlight and space, integrating smart irrigation systems, recruiting local community volunteers, and setting up a supply chain for fresh produce distribution. The process also includes ongoing maintenance protocols, pest management strategies adapted to rooftop conditions, seasonal crop rotation planning, and data collection for yield optimization and environmental impact assessment. The goal is to create a self-sustaining, eco-friendly urban agricultural system that enhances city resilience and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_assess = Transition(label='Site Assess')
permit_secure = Transition(label='Permit Secure')
design_layout = Transition(label='Design Layout')
select_crops = Transition(label='Select Crops')
build_modules = Transition(label='Build Modules')
install_irrigation = Transition(label='Install Irrigation')
setup_sensors = Transition(label='Setup Sensors')
recruit_volunteers = Transition(label='Recruit Volunteers')

soil_prep = Transition(label='Soil Prep')
plant_seeds = Transition(label='Plant Seeds')

manage_pests = Transition(label='Manage Pests')
maintain_systems = Transition(label='Maintain Systems')
record_data = Transition(label='Record Data')
harvest_produce = Transition(label='Harvest Produce')
distribute_goods = Transition(label='Distribute Goods')
plan_rotation = Transition(label='Plan Rotation')

# Initial one-time setup sequence
initial_seq = StrictPartialOrder(nodes=[
    site_assess,
    permit_secure,
    design_layout,
    select_crops,
    build_modules,
    install_irrigation,
    setup_sensors,
    recruit_volunteers
])
initial_seq.order.add_edge(site_assess, permit_secure)
initial_seq.order.add_edge(permit_secure, design_layout)
initial_seq.order.add_edge(design_layout, select_crops)
initial_seq.order.add_edge(select_crops, build_modules)
initial_seq.order.add_edge(build_modules, install_irrigation)
initial_seq.order.add_edge(install_irrigation, setup_sensors)
initial_seq.order.add_edge(setup_sensors, recruit_volunteers)

# Loop: cycle start (soil prep & planting)
cycle_start = StrictPartialOrder(nodes=[soil_prep, plant_seeds])
cycle_start.order.add_edge(soil_prep, plant_seeds)

# Loop body: maintenance, data, harvest, distribution, planning
loop_body = StrictPartialOrder(nodes=[
    manage_pests,
    maintain_systems,
    record_data,
    harvest_produce,
    distribute_goods,
    plan_rotation
])
loop_body.order.add_edge(manage_pests, record_data)
loop_body.order.add_edge(maintain_systems, record_data)
loop_body.order.add_edge(record_data, harvest_produce)
loop_body.order.add_edge(harvest_produce, distribute_goods)
loop_body.order.add_edge(distribute_goods, plan_rotation)

# Define the loop structure
crop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle_start, loop_body]
)

# Root POWL: initial setup followed by repeated crop cycles
root = StrictPartialOrder(nodes=[initial_seq, crop_cycle])
root.order.add_edge(initial_seq, crop_cycle)