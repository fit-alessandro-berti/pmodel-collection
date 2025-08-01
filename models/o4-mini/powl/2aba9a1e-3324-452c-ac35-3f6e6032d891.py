# Generated from: 2aba9a1e-3324-452c-ac35-3f6e6032d891.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a densely populated city environment. It includes site analysis, modular structure design, climate control integration, hydroponic system installation, nutrient solution calibration, automated monitoring setup, waste recycling strategy, and stakeholder coordination. The process also covers regulatory compliance checks, energy consumption optimization, pest control protocols, crop selection based on urban microclimates, data analytics for yield prediction, continuous maintenance scheduling, and market distribution planning. This atypical but realistic process ensures sustainable and efficient urban agriculture leveraging advanced technology and interdisciplinary collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the concrete activities
site_analysis      = Transition(label='Site Analysis')
structure_design   = Transition(label='Structure Design')
climate_setup      = Transition(label='Climate Setup')
hydroponic_install = Transition(label='Hydroponic Install')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
sensor_deploy      = Transition(label='Sensor Deploy')
waste_recycle      = Transition(label='Waste Recycle')
regulation_check   = Transition(label='Regulation Check')
energy_optimize    = Transition(label='Energy Optimize')
pest_control       = Transition(label='Pest Control')
crop_selection     = Transition(label='Crop Selection')
data_analytics     = Transition(label='Data Analytics')
maintenance_plan   = Transition(label='Maintenance Plan')
stakeholder_meet   = Transition(label='Stakeholder Meet')
market_planning    = Transition(label='Market Planning')

# A silent transition to serve as the loop “redo” marker
skip = SilentTransition()

# Build the maintenance loop: first do Data Analytics → Maintenance Plan,
# then either exit or take the silent skip and do it again.
maintenance_seq = StrictPartialOrder(nodes=[data_analytics, maintenance_plan])
maintenance_seq.order.add_edge(data_analytics, maintenance_plan)
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_seq, skip])

# Build the overall process as a partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structure_design, climate_setup,
    hydroponic_install, nutrient_calibrate, sensor_deploy,
    waste_recycle, regulation_check, energy_optimize,
    pest_control, crop_selection, stakeholder_meet,
    maintenance_loop, market_planning
])

# Main linear flow: Site Analysis → Structure Design → Climate Setup → ... → Sensor Deploy
root.order.add_edge(site_analysis,      structure_design)
root.order.add_edge(structure_design,   climate_setup)
root.order.add_edge(climate_setup,      hydroponic_install)
root.order.add_edge(hydroponic_install, nutrient_calibrate)
root.order.add_edge(nutrient_calibrate, sensor_deploy)

# After sensor deployment, six activities can proceed concurrently:
# Waste Recycle, Regulation Check, Energy Optimize, Pest Control, Crop Selection, Stakeholder Meet
concurrent_tasks = [
    waste_recycle, regulation_check,
    energy_optimize, pest_control,
    crop_selection, stakeholder_meet
]
for t in concurrent_tasks:
    # they all depend on sensor_deploy
    root.order.add_edge(sensor_deploy, t)
    # and all must finish before the maintenance loop
    root.order.add_edge(t, maintenance_loop)

# Finally, after maintenance (when the loop exits), do the Market Planning
root.order.add_edge(maintenance_loop, market_planning)