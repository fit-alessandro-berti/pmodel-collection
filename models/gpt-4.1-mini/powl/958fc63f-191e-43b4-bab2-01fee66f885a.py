# Generated from: 958fc63f-191e-43b4-bab2-01fee66f885a.json
# Description: This process involves the design, development, and assembly of custom drones tailored for specialized applications such as environmental monitoring, precision agriculture, and industrial inspection. Starting from client consultation to understand unique requirements, it proceeds through iterative prototype design, component sourcing from niche suppliers, and integration of advanced sensors. Quality assurance includes rigorous flight testing under varied conditions and software calibration for autonomous navigation. The process concludes with client training and after-sales support including firmware updates and maintenance scheduling to ensure optimal drone performance over its operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Client_Consult = Transition(label='Client Consult')
Requirement_Gather = Transition(label='Requirement Gather')
Concept_Sketch = Transition(label='Concept Sketch')
Prototype_Build = Transition(label='Prototype Build')
Sensor_Select = Transition(label='Sensor Select')
Component_Source = Transition(label='Component Source')
Flight_Testing = Transition(label='Flight Testing')
Software_Upload = Transition(label='Software Upload')
Autonomy_Setup = Transition(label='Autonomy Setup')
Calibration_Run = Transition(label='Calibration Run')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Warranty_Setup = Transition(label='Warranty Setup')
Maintenance_Plan = Transition(label='Maintenance Plan')
Firmware_Update = Transition(label='Firmware Update')

# Define iterative prototype design loop = (* (Concept Sketch, Prototype Build))
# After Concept Sketch, either exit loop or do Prototype Build then Concept Sketch again
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[Concept_Sketch, Prototype_Build])

# After Client Consult we gather requirements
# Then iterative prototype design loop
# Then source components and sensors in partial order (concurrent)
component_sensor_PO = StrictPartialOrder(nodes=[Component_Source, Sensor_Select])

# Hardware and sensor integration leads to Flight Testing (part of Quality Assurance)
# Software Upload, Autonomy Setup, Calibration Run for software calibration
software_PO = StrictPartialOrder(nodes=[Software_Upload, Autonomy_Setup, Calibration_Run])
software_PO.order.add_edge(Software_Upload, Autonomy_Setup)
software_PO.order.add_edge(Autonomy_Setup, Calibration_Run)

# Quality Check comes after Flight Testing and software calibration (which is in software_PO)
quality_PO = StrictPartialOrder(nodes=[Flight_Testing, software_PO, Quality_Check])
quality_PO.order.add_edge(Flight_Testing, Quality_Check)
quality_PO.order.add_edge(software_PO, Quality_Check)

# Packaging and then Client Training
packaging_training_PO = StrictPartialOrder(nodes=[Packaging_Prep, Client_Training])
packaging_training_PO.order.add_edge(Packaging_Prep, Client_Training)

# After-sales support in partial order: Warranty Setup, Maintenance Plan, Firmware Update (concurrent)
after_sales_support = StrictPartialOrder(nodes=[Warranty_Setup, Maintenance_Plan, Firmware_Update])

# Root partial order with dependencies:
# Client Consult -> Requirement Gather -> prototype_loop -> component_sensor_PO
# component_sensor_PO -> quality_PO -> packaging_training_PO -> after_sales_support

root = StrictPartialOrder(nodes=[
    Client_Consult,
    Requirement_Gather,
    prototype_loop,
    component_sensor_PO,
    quality_PO,
    packaging_training_PO,
    after_sales_support
])

# Set ordering edges according to the process flow
root.order.add_edge(Client_Consult, Requirement_Gather)
root.order.add_edge(Requirement_Gather, prototype_loop)
root.order.add_edge(prototype_loop, component_sensor_PO)
root.order.add_edge(component_sensor_PO, quality_PO)
root.order.add_edge(quality_PO, packaging_training_PO)
root.order.add_edge(packaging_training_PO, after_sales_support)