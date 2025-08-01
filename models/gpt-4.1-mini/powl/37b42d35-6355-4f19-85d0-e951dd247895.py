# Generated from: 37b42d35-6355-4f19-85d0-e951dd247895.json
# Description: This process outlines the intricate and multi-disciplinary steps required to establish an urban vertical farming operation within a repurposed industrial building. The workflow includes initial site analysis, environmental impact assessment, modular farm design, integration of IoT sensors, hydroponic system assembly, nutrient solution calibration, crop selection based on microclimate data, automated lighting configuration, workforce training on specialized equipment, real-time growth monitoring, pest management using biocontrol agents, yield forecasting with machine learning models, waste recycling protocols, energy consumption optimization, and final certification for organic produce standards. The process ensures sustainable urban agriculture by maximizing space efficiency and resource management while adhering to regulatory compliance and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
design_layout = Transition(label='Design Layout')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_build = Transition(label='Hydroponics Build')
nutrient_mix = Transition(label='Nutrient Mix')
crop_choice = Transition(label='Crop Choice')
light_program = Transition(label='Light Program')
staff_training = Transition(label='Staff Training')
growth_track = Transition(label='Growth Track')
pest_control = Transition(label='Pest Control')
yield_predict = Transition(label='Yield Predict')
waste_cycle = Transition(label='Waste Cycle')
energy_audit = Transition(label='Energy Audit')
certify_organic = Transition(label='Certify Organic')

# Create the StrictPartialOrder with nodes
root = StrictPartialOrder(
    nodes=[
        site_survey,
        impact_study,
        design_layout,
        sensor_setup,
        hydroponics_build,
        nutrient_mix,
        crop_choice,
        light_program,
        staff_training,
        growth_track,
        pest_control,
        yield_predict,
        waste_cycle,
        energy_audit,
        certify_organic
    ]
)

# Add edges defining the partial order based on the described workflow:
# Site Survey --> Impact Study --> Design Layout
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, design_layout)

# Design Layout --> Sensor Setup and Hydroponics Build (concurrent)
root.order.add_edge(design_layout, sensor_setup)
root.order.add_edge(design_layout, hydroponics_build)

# Hydroponics Build --> Nutrient Mix
root.order.add_edge(hydroponics_build, nutrient_mix)

# Sensor Setup --> Crop Choice and Light Program (concurrent)
root.order.add_edge(sensor_setup, crop_choice)
root.order.add_edge(sensor_setup, light_program)

# Nutrient Mix --> Crop Choice
root.order.add_edge(nutrient_mix, crop_choice)

# Crop Choice --> Staff Training
root.order.add_edge(crop_choice, staff_training)

# Light Program --> Staff Training
root.order.add_edge(light_program, staff_training)

# Staff Training --> Growth Track --> Pest Control
root.order.add_edge(staff_training, growth_track)
root.order.add_edge(growth_track, pest_control)

# Pest Control --> Yield Predict
root.order.add_edge(pest_control, yield_predict)

# Yield Predict --> Waste Cycle and Energy Audit (concurrent)
root.order.add_edge(yield_predict, waste_cycle)
root.order.add_edge(yield_predict, energy_audit)

# Waste Cycle and Energy Audit --> Certify Organic
root.order.add_edge(waste_cycle, certify_organic)
root.order.add_edge(energy_audit, certify_organic)