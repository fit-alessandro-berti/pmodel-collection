# Generated from: 442aa379-9694-48f2-b2a0-b8a82f52ba02.json
# Description: This process outlines the complex orchestration required to establish a bespoke urban farming system tailored to specific environmental constraints and client preferences. It begins with site analysis and soil testing, followed by modular design iterations and resource allocation. The process integrates IoT sensor calibration, automated irrigation programming, and nutrient cycle optimization. Throughout, regulatory compliance and sustainability assessments are conducted to ensure ecological impact is minimized. Finally, staff training and digital monitoring setup finalize the system, enabling scalable urban agriculture with precise environmental controls and remote management capabilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Soil_Testing = Transition(label='Soil Testing')
Design_Draft = Transition(label='Design Draft')
Resource_Plan = Transition(label='Resource Plan')
Permits_Check = Transition(label='Permits Check')
Module_Build = Transition(label='Module Build')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Config = Transition(label='Irrigation Config')
Nutrient_Mix = Transition(label='Nutrient Mix')
Compliance_Audit = Transition(label='Compliance Audit')
Sustainability_Eval = Transition(label='Sustainability Eval')
Staff_Training = Transition(label='Staff Training')
System_Install = Transition(label='System Install')
Data_Sync = Transition(label='Data Sync')
Remote_Enable = Transition(label='Remote Enable')
Performance_Review = Transition(label='Performance Review')

# Loop for modular design iterations: run Design Draft then Resource Plan repeatedly
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Draft, Resource_Plan])

# Parallel after Site Survey and Soil Testing (both must be done before design_loop)
# So Site Survey --> Soil Testing --> design_loop
# but Site Survey and Soil Testing are sequential in description ("begins with site analysis and soil testing")
po1 = StrictPartialOrder(nodes=[Site_Survey, Soil_Testing, design_loop])
po1.order.add_edge(Site_Survey, Soil_Testing)
po1.order.add_edge(Soil_Testing, design_loop)

# IoT sensor calibration (Sensor Setup), automated irrigation programming (Irrigation Config), nutrient cycle optimization (Nutrient Mix)
# These three are integrated, so concurrent (no order between them)
iot_subprocess = StrictPartialOrder(nodes=[Sensor_Setup, Irrigation_Config, Nutrient_Mix])

# Compliance related: Permits Check, Compliance Audit, Sustainability Eval
# "Throughout, regulatory compliance and sustainability assessments are conducted"
# Model as Permits Check --> Compliance Audit --> Sustainability Eval
compliance_po = StrictPartialOrder(nodes=[Permits_Check, Compliance_Audit, Sustainability_Eval])
compliance_po.order.add_edge(Permits_Check, Compliance_Audit)
compliance_po.order.add_edge(Compliance_Audit, Sustainability_Eval)

# Staff Training and Digital Monitoring Setup ("staff training and digital monitoring setup finalize the system")
# Model Staff Training, then System Install, then Data Sync, Remote Enable (monitoring)
# These four are sequential in finalization
finalize_po = StrictPartialOrder(nodes=[Staff_Training, System_Install, Data_Sync, Remote_Enable])
finalize_po.order.add_edge(Staff_Training, System_Install)
finalize_po.order.add_edge(System_Install, Data_Sync)
finalize_po.order.add_edge(Data_Sync, Remote_Enable)

# Performance Review likely last
# So Remote Enable --> Performance Review
finalization_with_review = StrictPartialOrder(nodes=[finalize_po, Performance_Review])
finalization_with_review.order.add_edge(finalize_po, Performance_Review)

# The Resource Plan is part of the design_loop, 
# so build module after design loop ends:
# design_loop --> Module Build
mono1 = StrictPartialOrder(nodes=[design_loop, Module_Build])
mono1.order.add_edge(design_loop, Module_Build)

# Module Build --> IoT sub-process and Compliance assessments can start after module build (integrating hardware and meeting regulations)
post_module = StrictPartialOrder(nodes=[Module_Build, iot_subprocess, compliance_po])
post_module.order.add_edge(Module_Build, iot_subprocess)
post_module.order.add_edge(Module_Build, compliance_po)

# After these integrations and compliance checks complete, finalize setup
final_full = StrictPartialOrder(nodes=[post_module, finalization_with_review])
final_full.order.add_edge(post_module, finalization_with_review)

# Starting from initial site analysis + soil testing + design loop, then module build etc.
root = StrictPartialOrder(nodes=[po1, mono1, post_module, finalization_with_review])
root.order.add_edge(po1, mono1)
root.order.add_edge(mono1, post_module)
root.order.add_edge(post_module, finalization_with_review)