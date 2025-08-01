# Generated from: 274e086b-4f15-4b6a-bb74-293da2b52fd4.json
# Description: This process involves the planning, installation, and operationalization of a vertical farming system within an urban environment. It includes site analysis, modular structure assembly, automated irrigation configuration, crop selection tailored for vertical growth, integration of IoT sensors for monitoring microclimate conditions, nutrient solution preparation, and the deployment of AI-driven growth optimization software. The process also covers staff training on maintenance protocols, pest management using biocontrol agents, and establishing distribution channels for fresh produce. Continuous data collection and system calibration ensure sustainable yield and energy efficiency, adapting to urban constraints and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
AI_Deploy = Transition(label='AI Deploy')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Energy_Audit = Transition(label='Energy Audit')
Compliance_Check = Transition(label='Compliance Check')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

# Planning phase partial order: Site Survey --> Design Layout
planning = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
planning.order.add_edge(Site_Survey, Design_Layout)

# Installation phase partial order:
# Structure Build, Irrigation Setup, Crop Select, Sensor Install, Nutrient Mix, AI Deploy
# Structure Build must precede Irrigation Setup, Crop Select, and Sensor Install
# Nutrient Mix and AI Deploy come after those three, order: Nutrient Mix --> AI Deploy
installation = StrictPartialOrder(
    nodes=[Structure_Build, Irrigation_Setup, Crop_Select, Sensor_Install, Nutrient_Mix, AI_Deploy]
)
installation.order.add_edge(Structure_Build, Irrigation_Setup)
installation.order.add_edge(Structure_Build, Crop_Select)
installation.order.add_edge(Structure_Build, Sensor_Install)
# Nutrient Mix after Irrigation Setup, Crop Select, Sensor Install (all must finish first)
installation.order.add_edge(Irrigation_Setup, Nutrient_Mix)
installation.order.add_edge(Crop_Select, Nutrient_Mix)
installation.order.add_edge(Sensor_Install, Nutrient_Mix)
installation.order.add_edge(Nutrient_Mix, AI_Deploy)

# Operational phase partial order:
# Staff Train --> Pest Control
staff_pest = StrictPartialOrder(nodes=[Staff_Train, Pest_Control])
staff_pest.order.add_edge(Staff_Train, Pest_Control)

# Monitoring and analysis flow:
# Data Monitor --> Yield Analyze --> Energy Audit --> Compliance Check
monitoring = StrictPartialOrder(
    nodes=[Data_Monitor, Yield_Analyze, Energy_Audit, Compliance_Check]
)
monitoring.order.add_edge(Data_Monitor, Yield_Analyze)
monitoring.order.add_edge(Yield_Analyze, Energy_Audit)
monitoring.order.add_edge(Energy_Audit, Compliance_Check)

# Market launch is last after compliance check
# Feedback Loop is a loop after Market Launch feeding back to Data Monitor for continuous improvement

# Create a loop: execute Feedback_Loop then Data Monitor repeatedly or exit
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Market_Launch, StrictPartialOrder(nodes=[Feedback_Loop, Data_Monitor])]
)
# Feedback_Loop --> Data_Monitor inside loop
loop.children[1].order.add_edge(Feedback_Loop, Data_Monitor)

# Combine staff_pest and monitoring concurrency after installation and planning
op_phase = StrictPartialOrder(
    nodes=[staff_pest, monitoring, loop]
)
# Both staff_pest and monitoring start after installation and planning
# So the order edges are installation --> staff_pest, installation --> monitoring
op_phase.order.add_edge(staff_pest, loop)  # loop (market launch + feedback) after monitoring/staff
op_phase.order.add_edge(monitoring, loop)

# The overall root partial order:
# planning --> installation --> op_phase

root = StrictPartialOrder(
    nodes=[planning, installation, op_phase]
)
root.order.add_edge(planning, installation)
root.order.add_edge(installation, op_phase)