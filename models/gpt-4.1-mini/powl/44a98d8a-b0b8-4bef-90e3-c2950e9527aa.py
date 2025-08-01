# Generated from: 44a98d8a-b0b8-4bef-90e3-c2950e9527aa.json
# Description: This process outlines the comprehensive onboarding of a new urban vertical farm into a city's sustainable food supply network. It involves site evaluation, modular system installation, environmental calibration, crop selection tailored to local demand, integration with renewable energy sources, staff training on automated systems, real-time monitoring setup, waste recycling integration, and compliance verification with urban agricultural regulations. The process also includes community engagement initiatives to promote local awareness and partnerships with retailers for direct-to-consumer distribution, ensuring a seamless launch and operational sustainability within a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Module_Setup = Transition(label='Module Setup')
Env_Calibration = Transition(label='Env Calibration')
Crop_Planning = Transition(label='Crop Planning')
Energy_Sync = Transition(label='Energy Sync')
Staff_Training = Transition(label='Staff Training')
Sensor_Install = Transition(label='Sensor Install')
Data_Integration = Transition(label='Data Integration')
Waste_Setup = Transition(label='Waste Setup')
Reg_Review = Transition(label='Reg Review')
Community_Meet = Transition(label='Community Meet')
Retail_Align = Transition(label='Retail Align')
System_Testing = Transition(label='System Testing')
Launch_Prep = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')

# The process is:
# 1. Site Survey --> Module Setup --> Env Calibration
# 2. Crop Planning after Env Calibration
# 3. Parallel branches after Crop Planning:
#    a) Energy Sync --> Staff Training --> Sensor Install --> Data Integration
#    b) Waste Setup --> Reg Review
#    c) Community Meet --> Retail Align
# So (a), (b), (c) run in partial order (concurrent)
# 4. After all concurrent branches finish, System Testing --> Launch Prep
# 5. Feedback Loop is a looping structure after Launch Prep:
#    loop body: Feedback Loop then back to System Testing and Launch Prep again
#    modeled as LOOP(System Testing + Launch Prep, Feedback Loop)

# Steps 1-3 modeled as strict partial order with concurrency for branches a,b,c:

# Branch a PO
branch_a_nodes = [Energy_Sync, Staff_Training, Sensor_Install, Data_Integration]
branch_a_po = StrictPartialOrder(nodes=branch_a_nodes)
branch_a_po.order.add_edge(Energy_Sync, Staff_Training)
branch_a_po.order.add_edge(Staff_Training, Sensor_Install)
branch_a_po.order.add_edge(Sensor_Install, Data_Integration)

# Branch b PO
branch_b_nodes = [Waste_Setup, Reg_Review]
branch_b_po = StrictPartialOrder(nodes=branch_b_nodes)
branch_b_po.order.add_edge(Waste_Setup, Reg_Review)

# Branch c PO
branch_c_nodes = [Community_Meet, Retail_Align]
branch_c_po = StrictPartialOrder(nodes=branch_c_nodes)
branch_c_po.order.add_edge(Community_Meet, Retail_Align)

# Merge branches a,b,c as concurrent nodes
branches_abc_nodes = [branch_a_po, branch_b_po, branch_c_po]

# First build the PO from Crop Planning to the concurrent branches
crop_and_branches_nodes = [Crop_Planning] + branches_abc_nodes
crop_branches_po = StrictPartialOrder(nodes=crop_and_branches_nodes)
crop_branches_po.order.add_edge(Crop_Planning, branch_a_po)
crop_branches_po.order.add_edge(Crop_Planning, branch_b_po)
crop_branches_po.order.add_edge(Crop_Planning, branch_c_po)

# Steps 1-3 started with initial steps:
# Site Survey --> Module Setup --> Env Calibration --> (Crop Planning -> branches)
initial_nodes = [Site_Survey, Module_Setup, Env_Calibration, crop_branches_po]

initial_po = StrictPartialOrder(nodes=initial_nodes)
initial_po.order.add_edge(Site_Survey, Module_Setup)
initial_po.order.add_edge(Module_Setup, Env_Calibration)
initial_po.order.add_edge(Env_Calibration, crop_branches_po)

# After branches, System Testing --> Launch Prep
# So define testing_prep_po:
testing_prep_po = StrictPartialOrder(nodes=[System_Testing, Launch_Prep])
testing_prep_po.order.add_edge(System_Testing, Launch_Prep)

# Connect branches to testing_prep_po
final_before_loop_nodes = [initial_po, testing_prep_po]
final_before_loop_po = StrictPartialOrder(nodes=final_before_loop_nodes)
final_before_loop_po.order.add_edge(initial_po, testing_prep_po)

# Loop: * (testing_prep_po, Feedback_Loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[testing_prep_po, Feedback_Loop])

# Replace testing_prep_po in final_before_loop_po with loop
# The final root is initial_po --> loop

root = StrictPartialOrder(nodes=[initial_po, loop])
root.order.add_edge(initial_po, loop)