# Generated from: a48d8095-74ea-4c4c-abc5-1e1a0bede2e0.json
# Description: This process outlines the complex steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves site analysis, environmental impact assessment, modular system design, nutrient cycling integration, automation programming, stakeholder engagement, and regulatory compliance. The process demands coordination between agronomists, engineers, and city officials to ensure sustainable production of high-yield crops using limited space and resources, while maximizing energy efficiency and minimizing waste generation. Each phase requires iterative testing and optimization to adapt to local climatic conditions and market demands, ensuring profitability and ecological balance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
System_Design = Transition(label='System Design')

Module_Build = Transition(label='Module Build')
Water_Setup = Transition(label='Water Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')

Sensor_Install = Transition(label='Sensor Install')
Automation_Code = Transition(label='Automation Code')

Energy_Audit = Transition(label='Energy Audit')
Waste_Plan = Transition(label='Waste Plan')

Stakeholder_Meet = Transition(label='Stakeholder Meet')
Permit_Apply = Transition(label='Permit Apply')

Crop_Trial = Transition(label='Crop Trial')
Data_Review = Transition(label='Data Review')

Market_Launch = Transition(label='Market Launch')

# Loop for iterative testing and optimization: Crop_Trial and Data_Review
loop_testing_opt = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Trial, Data_Review])

# Partial order for modular system build: Module Build -> Water Setup & Nutrient Mix concurrent, all follow System Design
po_module_setup = StrictPartialOrder(nodes=[Module_Build, Water_Setup, Nutrient_Mix])
po_module_setup.order.add_edge(Module_Build, Water_Setup)
po_module_setup.order.add_edge(Module_Build, Nutrient_Mix)

# Partial order for sensor install and automation code - sequential
po_sensors_auto = StrictPartialOrder(nodes=[Sensor_Install, Automation_Code])
po_sensors_auto.order.add_edge(Sensor_Install, Automation_Code)

# Partial order for audits - concurrent
po_audits = StrictPartialOrder(nodes=[Energy_Audit, Waste_Plan])

# Partial order for stakeholder and permit - sequential
po_stakeholder_permit = StrictPartialOrder(nodes=[Stakeholder_Meet, Permit_Apply])
po_stakeholder_permit.order.add_edge(Stakeholder_Meet, Permit_Apply)

# Partial order after System Design:
# System Design -> po_module_setup -> po_sensors_auto -> po_audits & po_stakeholder_permit concurrent
# Then iterative testing loop, then Market Launch

# Combine audits and stakeholder/permit concurrent
po_audit_stakeholder = StrictPartialOrder(nodes=[po_audits, po_stakeholder_permit])
# No edges here as concurrent

# Combine all after System Design:
po_after_design = StrictPartialOrder(nodes=[po_module_setup, po_sensors_auto, po_audit_stakeholder])
# Define strict order chain between these:
po_after_design.order.add_edge(po_module_setup, po_sensors_auto)
po_after_design.order.add_edge(po_sensors_auto, po_audit_stakeholder)

# Finally, main process partial order:
nodes_main = [
    Site_Survey,
    Impact_Study,
    System_Design,
    po_after_design,
    loop_testing_opt,
    Market_Launch
]
root = StrictPartialOrder(nodes=nodes_main)

# Define top-level order:
# Site Survey and Impact Study concurrent, both precede System Design
root.order.add_edge(Site_Survey, System_Design)
root.order.add_edge(Impact_Study, System_Design)

# System design precedes po_after_design
root.order.add_edge(System_Design, po_after_design)

# po_after_design precedes iteration loop
root.order.add_edge(po_after_design, loop_testing_opt)

# loop_testing_opt precedes Market Launch
root.order.add_edge(loop_testing_opt, Market_Launch)