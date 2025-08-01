# Generated from: ccd402c4-7fb8-4427-94dc-6a71e35b8f01.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed high-rise building. It involves integrating IoT sensors for real-time monitoring of plant health, implementing hydroponic systems optimized for space and resource efficiency, and coordinating logistics for supply chain management of seeds, nutrients, and harvested crops. The process also includes securing permits, stakeholder engagement with local communities, and developing a renewable energy plan to ensure sustainability. Advanced data analytics are employed to predict yield and optimize growth cycles, while maintenance routines are scheduled to minimize downtime. Finally, marketing strategies are devised to position the farm as a local organic produce provider, emphasizing freshness and eco-friendliness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
permit_filing    = Transition(label='Permit Filing')
stakeholder_meet = Transition(label='Stakeholder Meet')
design_layout    = Transition(label='Design Layout')
iot_install      = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_sowing      = Transition(label='Seed Sowing')
climate_control  = Transition(label='Climate Control')
data_monitor     = Transition(label='Data Monitor')
yield_forecast   = Transition(label='Yield Forecast')
energy_plan      = Transition(label='Energy Plan')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_prep     = Transition(label='Harvest Prep')
supply_dispatch  = Transition(label='Supply Dispatch')
market_launch    = Transition(label='Market Launch')

# Loop: continuously monitor data and optionally forecast yield
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitor, yield_forecast]
)

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, permit_filing, stakeholder_meet, design_layout,
        iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix,
        seed_sowing, climate_control, energy_plan, maintenance_plan,
        harvest_prep, supply_dispatch, market_launch, loop_monitor
    ]
)

# Define the control-flow dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)

root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(stakeholder_meet, design_layout)

root.order.add_edge(design_layout, iot_install)
root.order.add_edge(design_layout, hydroponic_setup)
root.order.add_edge(design_layout, energy_plan)

root.order.add_edge(iot_install, sensor_calibrate)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_sowing)

root.order.add_edge(sensor_calibrate, climate_control)
root.order.add_edge(seed_sowing, climate_control)

# After systems are up, start monitoring loop and schedule maintenance
root.order.add_edge(climate_control, loop_monitor)
root.order.add_edge(energy_plan, loop_monitor)

root.order.add_edge(climate_control, maintenance_plan)
root.order.add_edge(energy_plan, maintenance_plan)

# Once monitoring/maintenance phases conclude, harvest and dispatch
root.order.add_edge(loop_monitor, harvest_prep)
root.order.add_edge(maintenance_plan, harvest_prep)

root.order.add_edge(harvest_prep, supply_dispatch)
root.order.add_edge(supply_dispatch, market_launch)