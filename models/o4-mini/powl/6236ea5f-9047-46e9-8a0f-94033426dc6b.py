# Generated from: 6236ea5f-9047-46e9-8a0f-94033426dc6b.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a dense metropolitan area. It includes site assessment, infrastructure customization to maximize limited space, integration of IoT sensors for environmental control, selection of crop varieties suited for vertical growth, installation of automated hydroponic systems, and the deployment of a renewable energy solution. The process further encompasses regulatory compliance with urban agriculture policies, staff training on advanced farming technologies, implementation of a logistics framework for fresh produce distribution, and continuous monitoring for yield optimization and sustainability metrics. This atypical yet realistic process addresses the complexities of modern urban farming to achieve efficient, scalable, and eco-friendly food production within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess = Transition(label='Site Assess')
space_design = Transition(label='Space Design')
iot_setup = Transition(label='IoT Setup')
crop_select = Transition(label='Crop Select')
hydroponic_install = Transition(label='Hydroponic Install')
energy_install = Transition(label='Energy Install')
policy_review = Transition(label='Policy Review')
permit_obtain = Transition(label='Permit Obtain')
staff_train = Transition(label='Staff Train')
system_test = Transition(label='System Test')
logistics_plan = Transition(label='Logistics Plan')
market_launch = Transition(label='Market Launch')
growth_monitor = Transition(label='Growth Monitor')
yield_analyze = Transition(label='Yield Analyze')
sustainability_audit = Transition(label='Sustainability Audit')

# Silent transition for loop entry/exit
tau = SilentTransition()

# Define loop body: Growth Monitor -> Yield Analyze -> Sustainability Audit
loop_body = StrictPartialOrder(nodes=[growth_monitor, yield_analyze, sustainability_audit])
loop_body.order.add_edge(growth_monitor, yield_analyze)
loop_body.order.add_edge(yield_analyze, sustainability_audit)

# Define the LOOP operator for continuous monitoring/yield/sustainability cycle
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[tau, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_assess, space_design, iot_setup, crop_select,
    hydroponic_install, energy_install, policy_review,
    permit_obtain, system_test, staff_train,
    logistics_plan, market_launch, loop_monitor
])

# Define the control‐flow dependencies
root.order.add_edge(site_assess, space_design)
root.order.add_edge(site_assess, policy_review)

root.order.add_edge(space_design, iot_setup)
root.order.add_edge(space_design, crop_select)

root.order.add_edge(policy_review, permit_obtain)

root.order.add_edge(space_design, hydroponic_install)
root.order.add_edge(iot_setup, hydroponic_install)
root.order.add_edge(crop_select, hydroponic_install)

root.order.add_edge(space_design, energy_install)
root.order.add_edge(permit_obtain, energy_install)

root.order.add_edge(hydroponic_install, system_test)
root.order.add_edge(energy_install, system_test)

root.order.add_edge(system_test, staff_train)
root.order.add_edge(staff_train, logistics_plan)
root.order.add_edge(logistics_plan, market_launch)

root.order.add_edge(market_launch, loop_monitor)