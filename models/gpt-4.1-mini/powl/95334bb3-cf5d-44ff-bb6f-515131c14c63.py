# Generated from: 95334bb3-cf5d-44ff-bb6f-515131c14c63.json
# Description: This process outlines the complex steps involved in establishing a vertical farming system within an urban environment. It includes site analysis, modular infrastructure design, climatic control integration, nutrient cycle optimization, automated planting schedules, and energy-efficient lighting configurations. Additionally, it covers stakeholder coordination, regulatory compliance validation, waste recycling mechanisms, and data analytics for yield prediction, aiming to create a sustainable, high-yield urban agriculture solution that minimizes resource use and maximizes output within confined city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Scheduling = Transition(label='Plant Scheduling')
Light_Config = Transition(label='Light Config')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Permit_Check = Transition(label='Permit Check')
Waste_Setup = Transition(label='Waste Setup')
Data_Capture = Transition(label='Data Capture')
Yield_Model = Transition(label='Yield Model')
Energy_Audit = Transition(label='Energy Audit')
System_Testing = Transition(label='System Testing')
Harvest_Plan = Transition(label='Harvest Plan')
Maintenance_Log = Transition(label='Maintenance Log')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop on Feedback_Loop and Maintenance_Log: execute Maintenance_Log then choose to exit or do Feedback_Loop then Maintenance_Log again
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Log, Feedback_Loop])

# Data analytics branch: Data Capture -> Yield Model -> Energy Audit
data_analytics = StrictPartialOrder(nodes=[Data_Capture, Yield_Model, Energy_Audit])
data_analytics.order.add_edge(Data_Capture, Yield_Model)
data_analytics.order.add_edge(Yield_Model, Energy_Audit)

# Production setup sequence: Site Survey -> Design Modules -> Climate Setup -> Nutrient Mix -> Plant Scheduling -> Light Config
prod_setup = StrictPartialOrder(nodes=[Site_Survey, Design_Modules, Climate_Setup, Nutrient_Mix, Plant_Scheduling, Light_Config])
prod_setup.order.add_edge(Site_Survey, Design_Modules)
prod_setup.order.add_edge(Design_Modules, Climate_Setup)
prod_setup.order.add_edge(Climate_Setup, Nutrient_Mix)
prod_setup.order.add_edge(Nutrient_Mix, Plant_Scheduling)
prod_setup.order.add_edge(Plant_Scheduling, Light_Config)

# Regulation branch: Stakeholder Meet -> Permit Check
regulation = StrictPartialOrder(nodes=[Stakeholder_Meet, Permit_Check])
regulation.order.add_edge(Stakeholder_Meet, Permit_Check)

# Waste recycling concurrency node, no order within
waste_recycling = Waste_Setup

# System testing after setup & regulation branches completed before harvest plan
setup_and_regulation = StrictPartialOrder(
    nodes=[prod_setup, regulation, waste_recycling]
)
# Concurrent: prod_setup, regulation and waste_recycling parallel, no edges

# Merge dependencies: all three join then System Testing
merged_setup = StrictPartialOrder(nodes=[prod_setup, regulation, waste_recycling, System_Testing])
# Edges from each of the three to System Testing
merged_setup.order.add_edge(prod_setup, System_Testing)
merged_setup.order.add_edge(regulation, System_Testing)
merged_setup.order.add_edge(waste_recycling, System_Testing)

# Harvest plan after System Testing
harvest_process = StrictPartialOrder(nodes=[merged_setup, Harvest_Plan])
harvest_process.order.add_edge(merged_setup, Harvest_Plan)

# After harvest plan, maintenance loop runs concurrent with harvest plan finish
final_process = StrictPartialOrder(nodes=[harvest_process, maintenance_loop])
final_process.order.add_edge(harvest_process, maintenance_loop)

# Whole root includes final_process and data analytics in parallel (both independent)
root = StrictPartialOrder(nodes=[final_process, data_analytics])
# No edges between final_process and data_analytics => concurrent
