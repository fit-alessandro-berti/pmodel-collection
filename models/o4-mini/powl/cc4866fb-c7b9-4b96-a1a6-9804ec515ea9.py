# Generated from: cc4866fb-c7b9-4b96-a1a6-9804ec515ea9.json
# Description: This process outlines the complex and multi-disciplinary approach to establishing a sustainable urban vertical farm within a repurposed industrial building. It involves coordinating architectural redesign, hydroponic system installation, energy optimization, crop selection, and regulatory compliance. The process integrates smart sensor deployment for environmental control, waste recycling systems for nutrient management, and market analysis for crop profitability. It also includes staff training in urban agriculture techniques and community engagement to promote local food initiatives. Each step requires detailed project management to ensure that the facility operates efficiently, sustainably, and profitably in an urban context with limited space and resources.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_planning = Transition(label='Design Planning')
permit_filing = Transition(label='Permit Filing')
structural_reinforce = Transition(label='Structural Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
sensor_install = Transition(label='Sensor Install')
energy_audit = Transition(label='Energy Audit')
crop_selection = Transition(label='Crop Selection')
nutrient_mix = Transition(label='Nutrient Mix')
waste_process = Transition(label='Waste Process')
staff_training = Transition(label='Staff Training')
market_study = Transition(label='Market Study')
community_meet = Transition(label='Community Meet')
launch_trial = Transition(label='Launch Trial')
data_monitor = Transition(label='Data Monitor')
climate_control = Transition(label='Climate Control')

# Loop for ongoing monitoring and environmental control adjustments
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitor, climate_control]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_planning,
    permit_filing,
    structural_reinforce,
    hydroponic_setup,
    sensor_install,
    energy_audit,
    crop_selection,
    nutrient_mix,
    waste_process,
    staff_training,
    market_study,
    community_meet,
    launch_trial,
    monitor_loop
])

# Define the control-flow dependencies
o = root.order
o.add_edge(site_survey, design_planning)
o.add_edge(design_planning, permit_filing)
o.add_edge(permit_filing, structural_reinforce)
o.add_edge(structural_reinforce, hydroponic_setup)

o.add_edge(hydroponic_setup, sensor_install)
o.add_edge(hydroponic_setup, energy_audit)
o.add_edge(sensor_install, crop_selection)
o.add_edge(energy_audit, crop_selection)

o.add_edge(crop_selection, nutrient_mix)
o.add_edge(nutrient_mix, waste_process)

o.add_edge(waste_process, staff_training)
o.add_edge(waste_process, market_study)
o.add_edge(waste_process, community_meet)

o.add_edge(staff_training, launch_trial)
o.add_edge(market_study, launch_trial)
o.add_edge(community_meet, launch_trial)

o.add_edge(launch_trial, monitor_loop)