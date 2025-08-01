# Generated from: f16c6a99-d440-49c1-ad75-d36c578e95fa.json
# Description: This process outlines the complex and multifaceted steps required to establish an urban vertical farming system within a constrained metropolitan environment. It involves site analysis, modular design adaptation, integrating IoT sensors for environmental control, selecting optimal crop varieties, installing hydroponic and aeroponic systems, setting up renewable energy sources, managing water recycling, implementing pest management protocols, establishing supply chain logistics for fresh produce delivery, securing regulatory approvals, conducting staff training on advanced agricultural technologies, and creating data analytics dashboards for ongoing yield optimization. This atypical business process combines elements of agriculture, technology, sustainability, and urban planning to create a scalable and efficient food production model tailored for city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
sensor_deploy    = Transition(label='Sensor Deploy')
crop_select      = Transition(label='Crop Select')
system_install   = Transition(label='System Install')
energy_setup     = Transition(label='Energy Setup')
water_cycle      = Transition(label='Water Cycle')
pest_control     = Transition(label='Pest Control')
regulatory_check = Transition(label='Regulatory Check')
staff_training   = Transition(label='Staff Training')
data_configure   = Transition(label='Data Configure')
supply_plan      = Transition(label='Supply Plan')
market_launch    = Transition(label='Market Launch')

# Build the loop body: Harvest Schedule -> Quality Audit
harvest_schedule = Transition(label='Harvest Schedule')
quality_audit    = Transition(label='Quality Audit')
a = StrictPartialOrder(nodes=[harvest_schedule, quality_audit])
a.order.add_edge(harvest_schedule, quality_audit)

# Feedback transition
feedback_loop = Transition(label='Feedback Loop')

# Loop operator: execute (Harvest Schedule -> Quality Audit), then loop on Feedback and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[a, feedback_loop])

# Root partial order with all nodes
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, sensor_deploy, crop_select, system_install,
    energy_setup, water_cycle, pest_control, regulatory_check, staff_training,
    data_configure, supply_plan, loop, market_launch
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,    design_layout)
root.order.add_edge(design_layout,  sensor_deploy)
root.order.add_edge(sensor_deploy,  crop_select)
root.order.add_edge(crop_select,    system_install)
root.order.add_edge(system_install, energy_setup)
root.order.add_edge(energy_setup,   water_cycle)
root.order.add_edge(water_cycle,    pest_control)
root.order.add_edge(pest_control,   regulatory_check)
root.order.add_edge(regulatory_check, staff_training)
root.order.add_edge(staff_training,   data_configure)
root.order.add_edge(data_configure,   supply_plan)
root.order.add_edge(supply_plan,      loop)
root.order.add_edge(loop,             market_launch)