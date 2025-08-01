# Generated from: abbba611-d6ff-4635-a027-a152683b7407.json
# Description: This process outlines the comprehensive setup of an urban vertical farm integrating advanced hydroponics and IoT technologies to maximize crop yield in limited city spaces. It begins with site assessment and resource analysis, followed by modular system design and procurement of specialized equipment. Installation involves precise environmental control calibration, nutrient solution formulation, and sensor network deployment. Continuous monitoring and adaptive management optimize plant growth cycles, while automated harvesting and post-harvest processing ensure quality and efficiency. The process concludes with sustainability evaluation and scalability planning to expand operations in urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Resource_Audit = Transition(label='Resource Audit')
System_Design = Transition(label='System Design')
Equipment_Order = Transition(label='Equipment Order')
Structure_Build = Transition(label='Structure Build')
Install_Pumps = Transition(label='Install Pumps')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Mix_Nutrients = Transition(label='Mix Nutrients')
Deploy_IoT = Transition(label='Deploy IoT')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Lighting = Transition(label='Adjust Lighting')
Harvest_Crops = Transition(label='Harvest Crops')
Process_Yield = Transition(label='Process Yield')
Evaluate_Impact = Transition(label='Evaluate Impact')
Plan_Expansion = Transition(label='Plan Expansion')

# Step 1: Site Survey and Resource Audit are concurrent initial assessments
initial_assessment = StrictPartialOrder(nodes=[Site_Survey, Resource_Audit])

# Step 2: System Design and Equipment Order (System Design first, then Equipment Order)
design_procurement = StrictPartialOrder(nodes=[System_Design, Equipment_Order])
design_procurement.order.add_edge(System_Design, Equipment_Order)

# Step 3: Installation steps - Structure Build, Install Pumps, Calibrate Sensors, Mix Nutrients, Deploy IoT
# Assuming Structure Build precedes all other installation activities that can be concurrent among themselves
installation = StrictPartialOrder(nodes=[Structure_Build, Install_Pumps, Calibrate_Sensors, Mix_Nutrients, Deploy_IoT])
installation.order.add_edge(Structure_Build, Install_Pumps)
installation.order.add_edge(Structure_Build, Calibrate_Sensors)
installation.order.add_edge(Structure_Build, Mix_Nutrients)
installation.order.add_edge(Structure_Build, Deploy_IoT)
# Install Pumps, Calibrate Sensors, Mix Nutrients, Deploy IoT can be concurrent

# Step 4: Planting after installation
# Plant Seeding follows installation complete
planting = StrictPartialOrder(nodes=[Plant_Seeding])
# To connect: installation --> Plant Seeding

# Step 5: Monitoring and Adjust Lighting (Adjust Lighting depends on Monitor Growth, can loop)
# Model loop: monitor growth cycle then decide to adjust lighting or end monitoring

loop_monitoring = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Monitor_Growth,
        Adjust_Lighting
    ]
)

# Step 6: Harvest Crops and Process Yield sequential
harvest_processing = StrictPartialOrder(nodes=[Harvest_Crops, Process_Yield])
harvest_processing.order.add_edge(Harvest_Crops, Process_Yield)

# Step 7: Final evaluation and planning sequential
final_steps = StrictPartialOrder(nodes=[Evaluate_Impact, Plan_Expansion])
final_steps.order.add_edge(Evaluate_Impact, Plan_Expansion)

# Compose full process partial order:

# First compose initial assessment --> design_procurement
phase1 = StrictPartialOrder(nodes=[initial_assessment, design_procurement])
phase1.order.add_edge(initial_assessment, design_procurement)

# Then design_procurement --> installation
phase2 = StrictPartialOrder(nodes=[design_procurement, installation])
phase2.order.add_edge(design_procurement, installation)

# installation --> Plant Seeding
phase3 = StrictPartialOrder(nodes=[installation, planting])
phase3.order.add_edge(installation, planting)

# planting --> loop_monitoring
phase4 = StrictPartialOrder(nodes=[planting, loop_monitoring])
phase4.order.add_edge(planting, loop_monitoring)

# loop_monitoring --> harvest_processing
phase5 = StrictPartialOrder(nodes=[loop_monitoring, harvest_processing])
phase5.order.add_edge(loop_monitoring, harvest_processing)

# harvest_processing --> final_steps
phase6 = StrictPartialOrder(nodes=[harvest_processing, final_steps])
phase6.order.add_edge(harvest_processing, final_steps)

# Now chain all phases:
root = StrictPartialOrder(nodes=[initial_assessment, design_procurement, installation,
                                planting, loop_monitoring, harvest_processing, final_steps])
root.order.add_edge(initial_assessment, design_procurement)
root.order.add_edge(design_procurement, installation)
root.order.add_edge(installation, planting)
root.order.add_edge(planting, loop_monitoring)
root.order.add_edge(loop_monitoring, harvest_processing)
root.order.add_edge(harvest_processing, final_steps)