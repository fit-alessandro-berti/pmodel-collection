# Generated from: 2938294c-a1ca-4013-8751-9cd5bd84024e.json
# Description: This process outlines the intricate and atypical steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It combines elements of architectural retrofit, hydroponic system integration, climate control calibration, and sustainable resource management. The process begins with structural assessments and zoning clearances, followed by modular rack installation and nutrient solution formulation. Specialized tasks include LED spectrum tuning for various plant species, automated pest detection, and real-time data analytics for yield optimization. The workflow integrates cross-disciplinary teams coordinating logistics, technology deployment, and regulatory compliance to ensure a high-efficiency, eco-friendly urban agricultural production system that maximizes space utilization and minimizes environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Assess_Structure = Transition(label='Assess Structure')
Obtain_Permits = Transition(label='Obtain Permits')

Design_Layout = Transition(label='Design Layout')
Install_Racks = Transition(label='Install Racks')

Setup_Hydroponics = Transition(label='Setup Hydroponics')
Mix_Nutrients = Transition(label='Mix Nutrients')

Configure_Lighting = Transition(label='Configure Lighting')
Calibrate_Sensors = Transition(label='Calibrate Sensors')

Plant_Seeding = Transition(label='Plant Seeding')
Test_Irrigation = Transition(label='Test Irrigation')

Implement_Automation = Transition(label='Implement Automation')
Deploy_Analytics = Transition(label='Deploy Analytics')

Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Environment = Transition(label='Adjust Environment')

Conduct_Inspections = Transition(label='Conduct Inspections')
Manage_Waste = Transition(label='Manage Waste')

Train_Staff = Transition(label='Train Staff')
Launch_Operations = Transition(label='Launch Operations')

# Step 1: Structural assessments and permits (sequential)
step1 = StrictPartialOrder(nodes=[Assess_Structure, Obtain_Permits])
step1.order.add_edge(Assess_Structure, Obtain_Permits)

# Step 2: Modular rack installation and layout design
step2 = StrictPartialOrder(nodes=[Design_Layout, Install_Racks])
step2.order.add_edge(Design_Layout, Install_Racks)

# Step 3: Setup Hydroponics and Mix Nutrients (concurrent)
step3 = StrictPartialOrder(nodes=[Setup_Hydroponics, Mix_Nutrients])
# no order edges => concurrent

# Step 4: Lighting config and sensor calibration (concurrent)
step4 = StrictPartialOrder(nodes=[Configure_Lighting, Calibrate_Sensors])
# no edges => concurrent

# Step 5: Plant seeding and irrigation testing sequentially
step5 = StrictPartialOrder(nodes=[Plant_Seeding, Test_Irrigation])
step5.order.add_edge(Plant_Seeding, Test_Irrigation)

# Step 6: Automation implementation and analytics deployment sequentially
step6 = StrictPartialOrder(nodes=[Implement_Automation, Deploy_Analytics])
step6.order.add_edge(Implement_Automation, Deploy_Analytics)

# Step 7: Growth monitoring and environment adjustment loop
monitor_adjust_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Monitor_Growth, Adjust_Environment]
)

# Step 8: Inspections and waste management concurrent
step8 = StrictPartialOrder(nodes=[Conduct_Inspections, Manage_Waste])
# concurrent, no edges

# Step 9: Staff training preceding launch
step9 = StrictPartialOrder(nodes=[Train_Staff, Launch_Operations])
step9.order.add_edge(Train_Staff, Launch_Operations)

# Now build key partial orders and combine them respecting dependencies

# Combine the first steps sequentially:
init_stage = StrictPartialOrder(
    nodes=[step1, step2]
)
init_stage.order.add_edge(step1, step2)

# Combine hydroponics & nutrients with lighting & sensors concurrently
tech_setup = StrictPartialOrder(
    nodes=[step3, step4]
)
# no edges => concurrent

# Combine tech_setup before planting & irrigation (step5)
pre_plant = StrictPartialOrder(
    nodes=[tech_setup, step5]
)
pre_plant.order.add_edge(tech_setup, step5)

# Combine planting & irrigation before automation & analytics (step6)
automation_stage = StrictPartialOrder(
    nodes=[step5, step6]
)
automation_stage.order.add_edge(step5, step6)

# Combine automation before monitoring loop
monitor_stage = StrictPartialOrder(
    nodes=[step6, monitor_adjust_loop]
)
monitor_stage.order.add_edge(step6, monitor_adjust_loop)

# Combine monitoring with inspections & waste (step8) concurrent
inspect_waste_stage = StrictPartialOrder(
    nodes=[monitor_adjust_loop, step8]
)
# No order edges => concurrent

# Combine inspection/waste and staff training/launch sequenced
final_stage = StrictPartialOrder(
    nodes=[inspect_waste_stage, step9]
)
final_stage.order.add_edge(inspect_waste_stage, step9)

# Combine all top levels sequentially:
# init_stage -> pre_plant -> automation_stage -> monitor_stage -> inspect_waste_stage-> final_stage
# Note that some reuse of stages included, unify carefully

# To avoid duplication and to preserve order:
# We'll create a top partial order with these nodes:
root = StrictPartialOrder(
    nodes=[init_stage, pre_plant, automation_stage, monitor_stage, inspect_waste_stage, final_stage]
)
root.order.add_edge(init_stage, pre_plant)
root.order.add_edge(pre_plant, automation_stage)
root.order.add_edge(automation_stage, monitor_stage)
root.order.add_edge(monitor_stage, inspect_waste_stage)
root.order.add_edge(inspect_waste_stage, final_stage)