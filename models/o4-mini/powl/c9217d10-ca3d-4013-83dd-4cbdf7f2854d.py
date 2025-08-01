# Generated from: c9217d10-ca3d-4013-83dd-4cbdf7f2854d.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a repurposed industrial facility. It encompasses site analysis, environmental control system integration, crop selection based on microclimate data, automated nutrient delivery setup, and ongoing monitoring through IoT sensors. The process further includes workforce training for specialized hydroponic techniques, compliance with local agricultural regulations, marketing strategy alignment for direct-to-consumer sales, and continuous optimization of yield through data analytics. Each step demands coordination across engineering, agricultural science, logistics, and business development teams to ensure sustainable and profitable urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
climate_study   = Transition(label='Climate Study')
design_layout   = Transition(label='Design Layout')
system_install  = Transition(label='System Install')
crop_select     = Transition(label='Crop Select')
nutrient_plan   = Transition(label='Nutrient Plan')
sensor_setup    = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train     = Transition(label='Staff Train')
compliance_check= Transition(label='Compliance Check')
marketing_sync  = Transition(label='Marketing Sync')
data_monitor    = Transition(label='Data Monitor')
yield_analyze   = Transition(label='Yield Analyze')
supply_chain    = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Loop for continuous monitoring and yield analysis
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_analyze])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_study, design_layout, system_install,
    crop_select, nutrient_plan, sensor_setup, automation_test,
    staff_train, compliance_check, marketing_sync,
    data_monitor, yield_analyze,
    supply_chain, customer_engage,
    monitor_loop
])

# Define dependencies
root.order.add_edge(site_survey,   climate_study)
root.order.add_edge(climate_study, design_layout)
root.order.add_edge(climate_study, crop_select)
root.order.add_edge(design_layout, system_install)
root.order.add_edge(system_install, sensor_setup)
root.order.add_edge(sensor_setup,  automation_test)
root.order.add_edge(crop_select,   nutrient_plan)
root.order.add_edge(nutrient_plan, automation_test)

root.order.add_edge(automation_test, staff_train)
root.order.add_edge(automation_test, compliance_check)
root.order.add_edge(automation_test, marketing_sync)
root.order.add_edge(automation_test, monitor_loop)

root.order.add_edge(compliance_check, supply_chain)
root.order.add_edge(marketing_sync,   supply_chain)
root.order.add_edge(supply_chain,     customer_engage)