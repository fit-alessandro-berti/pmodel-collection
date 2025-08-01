# Generated from: a3b905bb-8cab-45d7-a0ce-e886f376f463.json
# Description: This process outlines the complex and multidisciplinary steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental control system design, hydroponic and aeroponic installations, crop selection based on local demand, integration of AI monitoring for growth optimization, waste recycling mechanisms, and community engagement programs. The process ensures sustainable resource management, maximizes yield in limited space, and aligns with urban zoning regulations while fostering local food production and reducing supply chain emissions. Coordination between architects, agronomists, engineers, and city planners is critical throughout the implementation phases, from initial feasibility studies to full operational launch and continuous system upgrades.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
feas_study       = Transition(label='Feasibility Study')
design_layout    = Transition(label='Design Layout')
install_hvac     = Transition(label='Install HVAC')
setup_growbeds   = Transition(label='Setup Growbeds')
install_lighting = Transition(label='Install Lighting')
configure_sensors= Transition(label='Configure Sensors')
test_irrigation  = Transition(label='Test Irrigation')
select_crops     = Transition(label='Select Crops')
waste_processing = Transition(label='Waste Processing')
staff_training   = Transition(label='Staff Training')
community_meet   = Transition(label='Community Meet')
launch_pilot     = Transition(label='Launch Pilot')
program_ai       = Transition(label='Program AI')
scale_operations = Transition(label='Scale Operations')

# Phase 1: Implementation up to pilot launch
phase1 = StrictPartialOrder(nodes=[
    site_survey, feas_study, design_layout,
    install_hvac, setup_growbeds, install_lighting,
    configure_sensors, test_irrigation, select_crops,
    waste_processing, staff_training, community_meet,
    launch_pilot
])
# Sequential edges
phase1.order.add_edge(site_survey,      feas_study)
phase1.order.add_edge(feas_study,       design_layout)
# After design, installations run in parallel
phase1.order.add_edge(design_layout,    install_hvac)
phase1.order.add_edge(design_layout,    setup_growbeds)
phase1.order.add_edge(design_layout,    install_lighting)
# Configuration after all installs
phase1.order.add_edge(install_hvac,     configure_sensors)
phase1.order.add_edge(setup_growbeds,   configure_sensors)
phase1.order.add_edge(install_lighting, configure_sensors)
# Continue sequence
phase1.order.add_edge(configure_sensors, test_irrigation)
phase1.order.add_edge(test_irrigation,   select_crops)
phase1.order.add_edge(select_crops,      waste_processing)
# Waste processing then staff training and community engagement in parallel
phase1.order.add_edge(waste_processing,  staff_training)
phase1.order.add_edge(waste_processing,  community_meet)
# Both training and meet must complete before pilot
phase1.order.add_edge(staff_training,    launch_pilot)
phase1.order.add_edge(community_meet,    launch_pilot)

# Phase 2: Continuous improvement loop (AI programming & scaling)
cont_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[program_ai, scale_operations]
)

# Root POWL: phase1 followed by the improvement loop
root = StrictPartialOrder(nodes=[phase1, cont_loop])
root.order.add_edge(phase1, cont_loop)