# Generated from: ef48ab64-c3e6-42bb-a647-3d0c5b63037d.json
# Description: This process outlines the comprehensive steps involved in establishing a high-tech urban vertical farm in a dense metropolitan area. It begins with site selection and initial environmental assessment, followed by modular structure design and hydroponic system integration. The process includes automation software development for climate and nutrient control, seed selection optimized for vertical growth, and installation of LED grow lights. It further covers workforce training on specialized equipment, regulatory compliance checks, and community engagement programs to promote sustainability awareness. Finally, it concludes with phased crop planting, real-time monitoring setup, and optimization cycles to maximize yield within limited urban space while reducing carbon footprint and water usage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_select      = Transition(label='Site Select')
env_assess       = Transition(label='Env Assess')
design_modules   = Transition(label='Design Modules')
hydroponics_setup= Transition(label='Hydroponics Setup')
software_dev     = Transition(label='Software Dev')
seed_choose      = Transition(label='Seed Choose')
led_install      = Transition(label='LED Install')
train_staff      = Transition(label='Train Staff')
compliance_check = Transition(label='Compliance Check')
engage_community = Transition(label='Engage Community')
plant_crops      = Transition(label='Plant Crops')
monitor_growth   = Transition(label='Monitor Growth')
optimize_yields  = Transition(label='Optimize Yields')
waste_manage     = Transition(label='Waste Manage')
energy_audit     = Transition(label='Energy Audit')
water_recycle    = Transition(label='Water Recycle')

# Loop for monitoring and optimization cycles
monitor_opt_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, optimize_yields]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_select,
    env_assess,
    design_modules,
    hydroponics_setup,
    software_dev,
    seed_choose,
    led_install,
    train_staff,
    compliance_check,
    engage_community,
    plant_crops,
    monitor_opt_loop,
    waste_manage,
    energy_audit,
    water_recycle
])

# Linear dependencies up to planting
root.order.add_edge(site_select,       env_assess)
root.order.add_edge(env_assess,        design_modules)
root.order.add_edge(design_modules,    hydroponics_setup)
root.order.add_edge(hydroponics_setup, software_dev)
root.order.add_edge(software_dev,      seed_choose)
root.order.add_edge(seed_choose,       led_install)
root.order.add_edge(led_install,       train_staff)
root.order.add_edge(train_staff,       compliance_check)
root.order.add_edge(compliance_check,  engage_community)
root.order.add_edge(engage_community,  plant_crops)

# After planting, start loop and concurrent sustainability tasks
root.order.add_edge(plant_crops, monitor_opt_loop)
root.order.add_edge(plant_crops, waste_manage)
root.order.add_edge(plant_crops, energy_audit)
root.order.add_edge(plant_crops, water_recycle)