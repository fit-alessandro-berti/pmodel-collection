# Generated from: ef48ab64-c3e6-42bb-a647-3d0c5b63037d.json
# Description: This process outlines the comprehensive steps involved in establishing a high-tech urban vertical farm in a dense metropolitan area. It begins with site selection and initial environmental assessment, followed by modular structure design and hydroponic system integration. The process includes automation software development for climate and nutrient control, seed selection optimized for vertical growth, and installation of LED grow lights. It further covers workforce training on specialized equipment, regulatory compliance checks, and community engagement programs to promote sustainability awareness. Finally, it concludes with phased crop planting, real-time monitoring setup, and optimization cycles to maximize yield within limited urban space while reducing carbon footprint and water usage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_select = Transition(label='Site Select')
env_assess = Transition(label='Env Assess')
design_modules = Transition(label='Design Modules')
hydroponics_setup = Transition(label='Hydroponics Setup')
software_dev = Transition(label='Software Dev')
seed_choose = Transition(label='Seed Choose')
led_install = Transition(label='LED Install')
train_staff = Transition(label='Train Staff')
compliance_check = Transition(label='Compliance Check')
engage_community = Transition(label='Engage Community')
plant_crops = Transition(label='Plant Crops')
monitor_growth = Transition(label='Monitor Growth')
optimize_yields = Transition(label='Optimize Yields')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
water_recycle = Transition(label='Water Recycle')

# Step 1: Site selection and environmental assessment are sequential
step1 = StrictPartialOrder(nodes=[site_select, env_assess])
step1.order.add_edge(site_select, env_assess)

# Step 2: Modular design and hydroponics setup sequential
step2 = StrictPartialOrder(nodes=[design_modules, hydroponics_setup])
step2.order.add_edge(design_modules, hydroponics_setup)

# Step 3: Software dev and seed choosing can be done concurrently before LED install
concurrent_sw_seed = StrictPartialOrder(nodes=[software_dev, seed_choose])
# No edges => concurrent

step3 = StrictPartialOrder(nodes=[concurrent_sw_seed, led_install])
step3.order.add_edge(concurrent_sw_seed, led_install)

# Step 4: Staff training, compliance check, community engagement - all concurrent
step4 = StrictPartialOrder(nodes=[train_staff, compliance_check, engage_community])
# No order edges => concurrent

# Step 5: Plant crops, monitoring growth, and optimize yields in a LOOP:
# Loop(body=Plant Crops, redo= Optimize Yields + Monitor Growth)
# But Monitor Growth and Optimize Yields can be concurrent in redo

redo_part = StrictPartialOrder(nodes=[monitor_growth, optimize_yields])
# concurrent, no order edges

loop_part = OperatorPOWL(operator=Operator.LOOP, children=[plant_crops, redo_part])

# Step 6: Waste Manage, Energy Audit, and Water Recycle after loop, all concurrent
step6 = StrictPartialOrder(nodes=[waste_manage, energy_audit, water_recycle])

# Combine all major steps in a partial order representing the full workflow:

# Nodes of the root PO: step1, step2, step3, step4, loop_part, step6
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, loop_part, step6])

# Define the partial order edges between these phases:

# step1 --> step2
root.order.add_edge(step1, step2)

# step2 --> step3
root.order.add_edge(step2, step3)

# step3 --> step4
root.order.add_edge(step3, step4)

# step4 --> loop_part
root.order.add_edge(step4, loop_part)

# loop_part --> step6
root.order.add_edge(loop_part, step6)