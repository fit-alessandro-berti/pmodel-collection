# Generated from: 798a5975-311f-40f4-bc9e-6050c34aaadd.json
# Description: This process outlines the complex sequence of activities required to establish an urban vertical farming facility within a repurposed industrial building. It involves site analysis, environmental control design, hydroponic system installation, crop selection tailored for limited space and light, integration of IoT sensors for monitoring, and the development of a sustainable waste recycling loop. The process also includes securing permits, engaging local stakeholders, and implementing automated harvesting and packaging systems to optimize yield and reduce labor costs. Continuous data analysis and system calibration ensure adaptability to urban microclimates and consumer demand fluctuations, making this an atypical but highly sustainable agricultural business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Layout_Design = Transition(label='Layout Design')
Enviro_Setup = Transition(label='Enviro Setup')
Hydroponic_Install = Transition(label='Hydroponic Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
Waste_Loop = Transition(label='Waste Loop')
Irrigation_Tune = Transition(label='Irrigation Tune')
Climate_Control = Transition(label='Climate Control')
Automation_Setup = Transition(label='Automation Setup')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Line = Transition(label='Packaging Line')
Data_Review = Transition(label='Data Review')
Market_Align = Transition(label='Market Align')

# Model structure reasoning:
# 1) Site Survey leads to two parallel branches:
#    a) Permitting + Stakeholder engagement sequence
#    b) Design and setup loop

# Permitting sequence (linear order):
permits = StrictPartialOrder(nodes=[Permit_Filing, Stakeholder_Meet])
permits.order.add_edge(Permit_Filing, Stakeholder_Meet)

# Design and setup partial order with a loop for iterative calibration and tuning:
# After Layout Design and Enviro Setup, install Hydroponic and deploy sensors, then select crops.
# Waste Loop, Irrigation Tune, Climate Control form a loop with Layout Design (recalibration loop)
# Automation Setup, Harvest Plan, Packaging Line proceed in order
# Data Review and Market Align come at the end

# Base design/setup partial order nodes (excluding loop pieces for now)
design_base_nodes = [
    Layout_Design,
    Enviro_Setup,
    Hydroponic_Install,
    Sensor_Deploy,
    Crop_Select,
    Automation_Setup,
    Harvest_Plan,
    Packaging_Line,
    Data_Review,
    Market_Align
]

# Define partial order for design/setup linear parts before loop:
# Layout_Design --> Enviro_Setup
# Enviro_Setup --> Hydroponic_Install
# Hydroponic_Install --> Sensor_Deploy
# Sensor_Deploy --> Crop_Select
# Crop_Select --> Automation_Setup
# Automation_Setup --> Harvest_Plan --> Packaging_Line --> Data_Review --> Market_Align

design_setup = StrictPartialOrder(nodes=design_base_nodes)

design_setup.order.add_edge(Layout_Design, Enviro_Setup)
design_setup.order.add_edge(Enviro_Setup, Hydroponic_Install)
design_setup.order.add_edge(Hydroponic_Install, Sensor_Deploy)
design_setup.order.add_edge(Sensor_Deploy, Crop_Select)
design_setup.order.add_edge(Crop_Select, Automation_Setup)
design_setup.order.add_edge(Automation_Setup, Harvest_Plan)
design_setup.order.add_edge(Harvest_Plan, Packaging_Line)
design_setup.order.add_edge(Packaging_Line, Data_Review)
design_setup.order.add_edge(Data_Review, Market_Align)

# Define the loop:
# The loop is between Layout_Design and (Waste_Loop + Irrigation_Tune + Climate_Control)
# The loop body B = PO(Waste_Loop, Irrigation_Tune, Climate_Control) concurrent
# Loop is * (A=Layout_Design, B=the calibration activities)
calibration_nodes = [Waste_Loop, Irrigation_Tune, Climate_Control]
calibration_po = StrictPartialOrder(nodes=calibration_nodes)
# They are concurrent (no edges)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Layout_Design, calibration_po])

# Replace Layout_Design with loop in design_setup partial order; because Layout_Design is replaced by loop

# So we must create a new design partial order replacing Layout_Design with loop:

design_nodes_with_loop = [
    loop,
    Enviro_Setup,
    Hydroponic_Install,
    Sensor_Deploy,
    Crop_Select,
    Automation_Setup,
    Harvest_Plan,
    Packaging_Line,
    Data_Review,
    Market_Align
]

design_setup_with_loop = StrictPartialOrder(nodes=design_nodes_with_loop)

design_setup_with_loop.order.add_edge(loop, Enviro_Setup)
design_setup_with_loop.order.add_edge(Enviro_Setup, Hydroponic_Install)
design_setup_with_loop.order.add_edge(Hydroponic_Install, Sensor_Deploy)
design_setup_with_loop.order.add_edge(Sensor_Deploy, Crop_Select)
design_setup_with_loop.order.add_edge(Crop_Select, Automation_Setup)
design_setup_with_loop.order.add_edge(Automation_Setup, Harvest_Plan)
design_setup_with_loop.order.add_edge(Harvest_Plan, Packaging_Line)
design_setup_with_loop.order.add_edge(Packaging_Line, Data_Review)
design_setup_with_loop.order.add_edge(Data_Review, Market_Align)

# Now combine permits and design_setup_with_loop in parallel after Site Survey,
# both depend on Site Survey to complete first, but then run in parallel

# Combine permits and design_setup_with_loop in parallel, and connect Site Survey to both

root = StrictPartialOrder(nodes=[Site_Survey, permits, design_setup_with_loop])

root.order.add_edge(Site_Survey, permits)
root.order.add_edge(Site_Survey, design_setup_with_loop)