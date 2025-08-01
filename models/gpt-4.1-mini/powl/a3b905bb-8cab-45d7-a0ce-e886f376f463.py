# Generated from: a3b905bb-8cab-45d7-a0ce-e886f376f463.json
# Description: This process outlines the complex and multidisciplinary steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental control system design, hydroponic and aeroponic installations, crop selection based on local demand, integration of AI monitoring for growth optimization, waste recycling mechanisms, and community engagement programs. The process ensures sustainable resource management, maximizes yield in limited space, and aligns with urban zoning regulations while fostering local food production and reducing supply chain emissions. Coordination between architects, agronomists, engineers, and city planners is critical throughout the implementation phases, from initial feasibility studies to full operational launch and continuous system upgrades.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Feasibility_Study = Transition(label='Feasibility Study')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Setup_Growbeds = Transition(label='Setup Growbeds')
Configure_Sensors = Transition(label='Configure Sensors')
Select_Crops = Transition(label='Select Crops')
Program_AI = Transition(label='Program AI')
Install_Lighting = Transition(label='Install Lighting')
Test_Irrigation = Transition(label='Test Irrigation')
Waste_Processing = Transition(label='Waste Processing')
Staff_Training = Transition(label='Staff Training')
Launch_Pilot = Transition(label='Launch Pilot')
Community_Meet = Transition(label='Community Meet')
Scale_Operations = Transition(label='Scale Operations')

# Phase 1: Initial studies and design
phase1 = StrictPartialOrder(nodes=[Site_Survey, Feasibility_Study, Design_Layout])
phase1.order.add_edge(Site_Survey, Feasibility_Study)
phase1.order.add_edge(Feasibility_Study, Design_Layout)

# Phase 2: Installation of systems (concurrent where possible)
install_hvac = Install_HVAC
setup_growbeds = Setup_Growbeds
configure_sensors = Configure_Sensors
install_lighting = Install_Lighting
test_irrigation = Test_Irrigation

phase2 = StrictPartialOrder(nodes=[install_hvac, setup_growbeds, configure_sensors, install_lighting, test_irrigation])
# Install HVAC before configuring sensors and irrigation testing (environmental setup first)
phase2.order.add_edge(install_hvac, configure_sensors)
phase2.order.add_edge(install_hvac, test_irrigation)
# Setup growbeds before irrigation test (since it's related)
phase2.order.add_edge(setup_growbeds, test_irrigation)

# Phase 3: Crop and AI configuration
phase3 = StrictPartialOrder(nodes=[Select_Crops, Program_AI])
phase3.order.add_edge(Select_Crops, Program_AI)

# Phase 4: Waste processing and staff training can be concurrent but after installation and configuration
phase4 = StrictPartialOrder(nodes=[Waste_Processing, Staff_Training])
# No precedence inside phase4

# Phase 5: Launch pilot and community engagement
phase5 = StrictPartialOrder(nodes=[Launch_Pilot, Community_Meet])
phase5.order.add_edge(Launch_Pilot, Community_Meet)

# Phase 6: Scale operations (final activity)
scale_operations = Scale_Operations

# Compose all phases in partial order with their dependencies:
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5, scale_operations]
)

# Define order edges between phases
root.order.add_edge(phase1, phase2)      # installation depends on initial design
root.order.add_edge(phase2, phase3)      # crop and AI after installation
root.order.add_edge(phase3, phase4)      # waste processing and training after crop & AI config
root.order.add_edge(phase4, phase5)      # pilot launch and community after waste/staff training
root.order.add_edge(phase5, scale_operations)  # scale operations after pilot & community
