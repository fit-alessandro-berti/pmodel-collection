# Generated from: 210ac66b-05ac-4b2f-8db3-d14107bf9873.json
# Description: This process involves the planning, construction, and operational launch of an urban vertical farm within a repurposed industrial building. It includes assessing structural integrity, designing modular grow systems, selecting crop varieties suited for vertical cultivation, installing automated climate controls, integrating renewable energy sources, training staff on hydroponic techniques, establishing supply chain logistics for fresh produce distribution, and implementing sustainability metrics for continuous improvement. The process ensures efficient use of limited urban space while maximizing yield and minimizing environmental impact through innovative farming technologies and data-driven management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
System_Design = Transition(label='System Design')
Crop_Select = Transition(label='Crop Select')
Module_Build = Transition(label='Module Build')
Climate_Setup = Transition(label='Climate Setup')
Energy_Integrate = Transition(label='Energy Integrate')
Water_Install = Transition(label='Water Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Automation_Test = Transition(label='Automation Test')
Staff_Train = Transition(label='Staff Train')
Trial_Cultivate = Transition(label='Trial Cultivate')
Harvest_Plan = Transition(label='Harvest Plan')
Logistics_Setup = Transition(label='Logistics Setup')
Sustain_Monitor = Transition(label='Sustain Monitor')

# The process is roughly sequential with some concurrency possible in system setup

# Planning phase:
# Site Assess --> Structure Check
planning = StrictPartialOrder(nodes=[Site_Assess, Structure_Check])
planning.order.add_edge(Site_Assess, Structure_Check)

# System design and crop selection can be concurrent after structure check
design_crop = StrictPartialOrder(nodes=[System_Design, Crop_Select])
# no order edges -> concurrent

# Building modular grow system and installing components are concurrent:
# Module Build, Climate Setup, Energy Integrate, Water Install, Sensor Deploy
build_install_nodes = [Module_Build, Climate_Setup, Energy_Integrate, Water_Install, Sensor_Deploy]
build_install = StrictPartialOrder(nodes=build_install_nodes)
# no ordering between them => all concurrent

# Automation test follows component installs (all installs must be done)
automation_test = StrictPartialOrder(nodes=build_install_nodes + [Automation_Test])
for node in build_install_nodes:
    automation_test.order.add_edge(node, Automation_Test)

# Staff training and trial cultivation likely sequential but may be connected
training_trial = StrictPartialOrder(nodes=[Staff_Train, Trial_Cultivate])
training_trial.order.add_edge(Staff_Train, Trial_Cultivate)

# Harvest planning after trial cultivation
harvest = StrictPartialOrder(nodes=[Trial_Cultivate, Harvest_Plan])
harvest.order.add_edge(Trial_Cultivate, Harvest_Plan)

# Logistics setup after harvest plan
logistics = StrictPartialOrder(nodes=[Harvest_Plan, Logistics_Setup])
logistics.order.add_edge(Harvest_Plan, Logistics_Setup)

# Sustainability monitor runs after logistics setup (ongoing but place as final activity)
final_monitor = StrictPartialOrder(nodes=[Logistics_Setup, Sustain_Monitor])
final_monitor.order.add_edge(Logistics_Setup, Sustain_Monitor)

# Now connect all phases in order:
# planning --> design_crop --> automation_test --> training_trial --> harvest --> logistics --> sustain_monitor

root = StrictPartialOrder(
    nodes=[planning, design_crop, automation_test, training_trial, harvest, logistics, final_monitor]
)

root.order.add_edge(planning, design_crop)
root.order.add_edge(design_crop, automation_test)
root.order.add_edge(automation_test, training_trial)
root.order.add_edge(training_trial, harvest)
root.order.add_edge(harvest, logistics)
root.order.add_edge(logistics, final_monitor)