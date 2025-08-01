# Generated from: 84d46e56-77fd-4064-b0eb-60335faa0c28.json
# Description: This process outlines the complex setup of an urban vertical farming system within a repurposed commercial building. It includes site analysis, structural reinforcement, environmental controls installation, automated irrigation programming, and crop selection optimization. Integration of renewable energy sources and real-time monitoring systems ensures sustainable, high-yield crop production. Post-installation training and community engagement complete the process, supporting urban agriculture innovation and local food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Permitting = Transition(label='Permitting')

Climate_Setup = Transition(label='Climate Setup')
Lighting_Install = Transition(label='Lighting Install')
Irrigation_Config = Transition(label='Irrigation Config')

Energy_Audit = Transition(label='Energy Audit')
Renewables_Setup = Transition(label='Renewables Setup')

Crop_Selection = Transition(label='Crop Selection')
Automation_Program = Transition(label='Automation Program')

Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Calibration = Transition(label='Data Calibration')

Staff_Training = Transition(label='Staff Training')
Trial_Growth = Transition(label='Trial Growth')

Community_Outreach = Transition(label='Community Outreach')

# Define a PO with initial site and structural steps in sequence
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Permitting])
initial_PO.order.add_edge(Site_Survey, Structural_Check)
initial_PO.order.add_edge(Structural_Check, Permitting)

# Environmental controls partial order (concurrent: climate, lighting, irrigation)
env_controls = StrictPartialOrder(
    nodes=[Climate_Setup, Lighting_Install, Irrigation_Config]
)
# No order edges here, all concurrent

# Energy section sequential
energy_PO = StrictPartialOrder(nodes=[Energy_Audit, Renewables_Setup])
energy_PO.order.add_edge(Energy_Audit, Renewables_Setup)

# Automation partial order (Crop Selection and Automation Program concurrent)
auto_PO = StrictPartialOrder(nodes=[Crop_Selection, Automation_Program])

# Sensor and data steps sequence
sensor_PO = StrictPartialOrder(nodes=[Sensor_Deploy, Data_Calibration])
sensor_PO.order.add_edge(Sensor_Deploy, Data_Calibration)

# Post-installation training and trial growth sequence
training_PO = StrictPartialOrder(nodes=[Staff_Training, Trial_Growth])
training_PO.order.add_edge(Staff_Training, Trial_Growth)

# Final community outreach (after training & trial)
final_PO = StrictPartialOrder(nodes=[Community_Outreach])

# Now organize the major blocks in partial order:
# initial_PO --> env_controls --> energy_PO --> auto_PO --> sensor_PO --> training_PO --> final_PO

nodes_all = [initial_PO, env_controls, energy_PO, auto_PO, sensor_PO, training_PO, final_PO]
root = StrictPartialOrder(nodes=nodes_all)
root.order.add_edge(initial_PO, env_controls)
root.order.add_edge(env_controls, energy_PO)
root.order.add_edge(energy_PO, auto_PO)
root.order.add_edge(auto_PO, sensor_PO)
root.order.add_edge(sensor_PO, training_PO)
root.order.add_edge(training_PO, final_PO)