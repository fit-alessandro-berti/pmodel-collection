# Generated from: 37b42d35-6355-4f19-85d0-e951dd247895.json
# Description: This process outlines the intricate and multi-disciplinary steps required to establish an urban vertical farming operation within a repurposed industrial building. The workflow includes initial site analysis, environmental impact assessment, modular farm design, integration of IoT sensors, hydroponic system assembly, nutrient solution calibration, crop selection based on microclimate data, automated lighting configuration, workforce training on specialized equipment, real-time growth monitoring, pest management using biocontrol agents, yield forecasting with machine learning models, waste recycling protocols, energy consumption optimization, and final certification for organic produce standards. The process ensures sustainable urban agriculture by maximizing space efficiency and resource management while adhering to regulatory compliance and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey   = Transition(label='Site Survey')
impact_study  = Transition(label='Impact Study')
design_layout = Transition(label='Design Layout')
sensor_setup  = Transition(label='Sensor Setup')
hydro_build   = Transition(label='Hydroponics Build')
nutrient_mix  = Transition(label='Nutrient Mix')
crop_choice   = Transition(label='Crop Choice')
light_program = Transition(label='Light Program')
staff_train   = Transition(label='Staff Training')
growth_track  = Transition(label='Growth Track')
pest_control  = Transition(label='Pest Control')
yield_predict = Transition(label='Yield Predict')
waste_cycle   = Transition(label='Waste Cycle')
energy_audit  = Transition(label='Energy Audit')
certify_org   = Transition(label='Certify Organic')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, impact_study, design_layout,
    sensor_setup, hydro_build, nutrient_mix,
    crop_choice, light_program, staff_train,
    growth_track, pest_control, yield_predict,
    waste_cycle, energy_audit, certify_org
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,   impact_study)
root.order.add_edge(impact_study,  design_layout)
root.order.add_edge(design_layout, sensor_setup)
root.order.add_edge(design_layout, hydro_build)
root.order.add_edge(hydro_build,   nutrient_mix)
root.order.add_edge(sensor_setup,  crop_choice)
root.order.add_edge(sensor_setup,  light_program)
root.order.add_edge(nutrient_mix,  staff_train)
root.order.add_edge(light_program, staff_train)
root.order.add_edge(crop_choice,   staff_train)
root.order.add_edge(staff_train,   growth_track)
root.order.add_edge(staff_train,   pest_control)
root.order.add_edge(staff_train,   yield_predict)
root.order.add_edge(staff_train,   waste_cycle)
root.order.add_edge(staff_train,   energy_audit)
root.order.add_edge(growth_track,  certify_org)
root.order.add_edge(pest_control,  certify_org)
root.order.add_edge(yield_predict, certify_org)
root.order.add_edge(waste_cycle,   certify_org)
root.order.add_edge(energy_audit,  certify_org)