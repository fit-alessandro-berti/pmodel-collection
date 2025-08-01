# Generated from: 83203132-fa5d-441d-8772-c50fb107f35b.json
# Description: This process outlines the end-to-end setup of an urban vertical farming facility designed to maximize crop yield in limited city spaces by integrating hydroponics, automated climate control, and renewable energy sources. It begins with site analysis and ends with real-time monitoring system deployment. The workflow includes critical steps such as equipment sourcing, nutrient solution formulation, and staff training for operational efficiency. Uniquely, it incorporates waste recycling loops from local restaurants as organic input and engages with city planners for regulatory compliance. This atypical business process blends agriculture, technology, and sustainability to meet growing urban food demands while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label="Site Survey")
design = Transition(label="Design Layout")

permit_obtain = Transition(label="Permit Obtain")
comp_check = Transition(label="Compliance Check")
# Loop: obtain permit, then check compliance; if not compliant, go back to obtain
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_obtain, comp_check])

supplier = Transition(label="Supplier Vetting")
equipment_order = Transition(label="Equipment Order")

install = Transition(label="Install Racks")
setup_light = Transition(label="Setup Lighting")
system_int = Transition(label="System Integration")

nutrient = Transition(label="Nutrient Mix")
waste = Transition(label="Waste Intake")
# Loop: mix nutrients, then optionally intake waste and mix again
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient, waste])

water = Transition(label="Water Testing")
climate = Transition(label="Climate Config")
# These three can proceed concurrently once the system is integrated
nutri_phase = StrictPartialOrder(nodes=[waste_loop, water, climate])
# No order edges => concurrent

staff = Transition(label="Staff Training")
trial = Transition(label="Trial Growth")

launch = Transition(label="Launch Monitor")
data = Transition(label="Data Logging")

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site, design, permit_loop,
        supplier, equipment_order,
        install, setup_light, system_int,
        nutri_phase,
        staff, trial,
        launch, data
    ]
)

# Define the sequential dependencies
root.order.add_edge(site, design)
root.order.add_edge(design, permit_loop)
root.order.add_edge(permit_loop, supplier)
root.order.add_edge(supplier, equipment_order)
root.order.add_edge(equipment_order, install)
root.order.add_edge(install, setup_light)
root.order.add_edge(setup_light, system_int)

root.order.add_edge(system_int, nutri_phase)
root.order.add_edge(nutri_phase, staff)
root.order.add_edge(staff, trial)

root.order.add_edge(trial, launch)
root.order.add_edge(launch, data)