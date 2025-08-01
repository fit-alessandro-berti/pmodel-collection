# Generated from: 74529cb4-cf29-475e-b715-9093bb213c91.json
# Description: This process governs the comprehensive management of urban beekeeping operations within city limits, balancing ecological sustainability, regulatory compliance, and community engagement. It includes site evaluation, hive installation, periodic health inspections, pest control, honey extraction, and data reporting. The process integrates stakeholder communication, emergency response for hive disturbances, and educational outreach programs to promote awareness and support for urban pollinators. Each step is designed to minimize environmental impact while maximizing hive productivity and public safety, adapting dynamically to seasonal changes and urban challenges such as pollution and limited green spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as Transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Hive_Setup = Transition(label='Hive Setup')
Colony_Transfer = Transition(label='Colony Transfer')
Health_Check = Transition(label='Health Check')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Wax_Processing = Transition(label='Wax Processing')
Data_Logging = Transition(label='Data Logging')
Community_Alert = Transition(label='Community Alert')
Education_Plan = Transition(label='Education Plan')
Emergency_Response = Transition(label='Emergency Response')
Seasonal_Audit = Transition(label='Seasonal Audit')
Equipment_Clean = Transition(label='Equipment Clean')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Waste_Disposal = Transition(label='Waste Disposal')

skip = SilentTransition()

# Defining segments reflecting the description:

# 1) Initial site and regulatory preparation: site survey and permit review in parallel
initial_po = StrictPartialOrder(nodes=[Site_Survey, Permit_Review])

# 2) Hive setup phase: Hive setup followed optionally by colony transfer (because it may be needed only sometimes)
colony_choice = OperatorPOWL(operator=Operator.XOR, children=[Colony_Transfer, skip])
hive_phase = StrictPartialOrder(nodes=[Hive_Setup, colony_choice])
hive_phase.order.add_edge(Hive_Setup, colony_choice)

# 3) Health and pest control loop:
# Loop: Health Check followed optionally by Pest Control, which leads back to Health Check, or loop exit (seasonal changes adapt here)
health_pest_loop = OperatorPOWL(operator=Operator.LOOP,
                               children=[Health_Check,
                                         OperatorPOWL(operator=Operator.XOR,
                                                      children=[Pest_Control, skip])
                                        ])

# 4) Honey processing sequence: Honey harvest then wax processing
honey_proc = StrictPartialOrder(nodes=[Honey_Harvest, Wax_Processing])
honey_proc.order.add_edge(Honey_Harvest, Wax_Processing)

# 5) Data Collection & Reporting: Data logging followed by community alert & education plan in parallel
com_alert_edu = StrictPartialOrder(nodes=[Community_Alert, Education_Plan])
data_reporting = StrictPartialOrder(nodes=[Data_Logging, com_alert_edu])
data_reporting.order.add_edge(Data_Logging, com_alert_edu)

# 6) Emergency branch (can happen any time after hive setup)
# Use XOR between emergency response or skip
emergency_xor = OperatorPOWL(operator=Operator.XOR, children=[Emergency_Response, skip])

# 7) Seasonal audit and maintenance loop: seasonal audit leads to equipment clean and waste disposal parallel, then stakeholder meet
# Stakeholder meet depends on equip clean and waste disposal finishing
maintenance_po = StrictPartialOrder(nodes=[Seasonal_Audit, Equipment_Clean, Waste_Disposal, Stakeholder_Meet])
maintenance_po.order.add_edge(Seasonal_Audit, Equipment_Clean)
maintenance_po.order.add_edge(Seasonal_Audit, Waste_Disposal)
maintenance_po.order.add_edge(Equipment_Clean, Stakeholder_Meet)
maintenance_po.order.add_edge(Waste_Disposal, Stakeholder_Meet)

# 8) Partial order connecting main phases:
root = StrictPartialOrder(nodes=[initial_po, hive_phase, health_pest_loop, honey_proc, data_reporting, emergency_xor, maintenance_po])

# Order dependencies to reflect logical partial order:
root.order.add_edge(initial_po, hive_phase)
root.order.add_edge(hive_phase, health_pest_loop)
root.order.add_edge(health_pest_loop, honey_proc)
root.order.add_edge(honey_proc, data_reporting)

# Emergency can trigger any time after hive setup, so concurrent but after hive_phase:
root.order.add_edge(hive_phase, emergency_xor)

# Maintenance happens after data reporting & emergency (stakeholder meet as final)
root.order.add_edge(data_reporting, maintenance_po)
root.order.add_edge(emergency_xor, maintenance_po)