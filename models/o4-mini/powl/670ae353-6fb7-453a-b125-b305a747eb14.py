# Generated from: 670ae353-6fb7-453a-b125-b305a747eb14.json
# Description: This process outlines the establishment of a vertical urban farm within a repurposed industrial building, integrating advanced hydroponics, IoT monitoring, and renewable energy systems. It begins with site evaluation and structural assessment, followed by modular rack installation and environment calibration. Subsequent steps include nutrient solution formulation, seed selection, and automated planting. Continuous monitoring leverages sensor data for climate adjustments and pest detection, while energy management optimizes solar and battery usage. Harvest scheduling coordinates with local distribution logistics. The process concludes with waste recycling and system maintenance planning, ensuring sustainability and scalability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
structure_check= Transition(label='Structure Check')
rack_install   = Transition(label='Rack Install')
climate_setup  = Transition(label='Climate Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
automated_plant= Transition(label='Automated Plant')
sensor_deploy  = Transition(label='Sensor Deploy')
data_monitor   = Transition(label='Data Monitor')
pest_detect    = Transition(label='Pest Detect')
energy_balance = Transition(label='Energy Balance')
harvest_plan   = Transition(label='Harvest Plan')
logistics_sync = Transition(label='Logistics Sync')
waste_process  = Transition(label='Waste Process')
system_review  = Transition(label='System Review')

# Define the repeating monitoring sub‐process:
# After 'Data Monitor' we either exit or do concurrent 'Pest Detect' & 'Energy Balance' then loop again
rep_subprocess = StrictPartialOrder(nodes=[pest_detect, energy_balance])
loop_monitor   = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, rep_subprocess])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_check,
    rack_install,
    climate_setup,
    nutrient_mix,
    seed_selection,
    automated_plant,
    sensor_deploy,
    loop_monitor,
    harvest_plan,
    logistics_sync,
    waste_process,
    system_review
])

# Add the control‐flow edges
root.order.add_edge(site_survey,    structure_check)
root.order.add_edge(structure_check, rack_install)
root.order.add_edge(rack_install,    climate_setup)
root.order.add_edge(climate_setup,   nutrient_mix)
root.order.add_edge(nutrient_mix,    seed_selection)
root.order.add_edge(seed_selection,  automated_plant)
root.order.add_edge(automated_plant, sensor_deploy)
root.order.add_edge(sensor_deploy,   loop_monitor)
root.order.add_edge(loop_monitor,    harvest_plan)
root.order.add_edge(harvest_plan,    logistics_sync)
root.order.add_edge(logistics_sync,  waste_process)
root.order.add_edge(waste_process,   system_review)