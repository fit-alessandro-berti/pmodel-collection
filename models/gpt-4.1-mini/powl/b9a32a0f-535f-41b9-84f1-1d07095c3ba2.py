# Generated from: b9a32a0f-535f-41b9-84f1-1d07095c3ba2.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It involves site analysis, modular system design, environmental control calibration, nutrient cycling optimization, and integration of renewable energy sources. Stakeholder engagement, regulatory compliance, and sustainable waste management are also critical to ensure operational efficiency and minimize ecological impact. The process further includes technology installation, staff training, continuous monitoring, and iterative system adjustments to adapt to urban constraints and maximize crop yield in limited spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
design_layout = Transition(label='Design Layout')
modular_setup = Transition(label='Modular Setup')
system_install = Transition(label='System Install')
env_calibration = Transition(label='Env Calibration')
nutrient_mix = Transition(label='Nutrient Mix')
water_recycling = Transition(label='Water Recycling')
energy_integrate = Transition(label='Energy Integrate')
waste_process = Transition(label='Waste Process')
staff_training = Transition(label='Staff Training')
crop_planting = Transition(label='Crop Planting')
monitoring = Transition(label='Monitoring')
data_analysis = Transition(label='Data Analysis')
yield_optimize = Transition(label='Yield Optimize')
maintenance = Transition(label='Maintenance')
stakeholder_meet = Transition(label='Stakeholder Meet')

# First partial order: initial steps, includes regulatory and stakeholder preparation
init_po = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    stakeholder_meet
])
# stakeholder_meet depends on regulation_check and site_survey (stakeholder engagement after site and regulation)
init_po.order.add_edge(site_survey, stakeholder_meet)
init_po.order.add_edge(regulation_check, stakeholder_meet)

# Design phase: design layout -> modular setup
design_po = StrictPartialOrder(nodes=[
    design_layout,
    modular_setup
])
design_po.order.add_edge(design_layout, modular_setup)

# Environmental systems partial order - can be partly concurrent:
# Env Calibration and Nutrient Mix and Water Recycling, Energy Integrate, Waste Process
env_nodes = [env_calibration, nutrient_mix, water_recycling, energy_integrate, waste_process]
env_po = StrictPartialOrder(nodes=env_nodes)
# Nutrient Mix likely needs water recycling
env_po.order.add_edge(water_recycling, nutrient_mix)

# Energy Integrate and Waste Process independent from others - so no orders added

# System install after modular setup, and after environmental calibration partial order
# We model system_install after modular_setup and all env steps
# Combine modular_setup and env_po in one PO with system_install after all

mod_env_po = StrictPartialOrder(nodes=[modular_setup, *env_nodes, system_install])
# modular_setup before system_install
mod_env_po.order.add_edge(modular_setup, system_install)
# All env nodes before system_install
for n in env_nodes:
    mod_env_po.order.add_edge(n, system_install)

# Training, crop planting and monitoring partial order
train_crop_monitor_po = StrictPartialOrder(nodes=[staff_training, crop_planting, monitoring])
train_crop_monitor_po.order.add_edge(staff_training, crop_planting)
train_crop_monitor_po.order.add_edge(crop_planting, monitoring)

# Analysis and optimization loop (data_analysis -> yield_optimize -> maintenance -> data_analysis loop)
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    data_analysis,
    OperatorPOWL(operator=Operator.XOR, children=[
        yield_optimize,
        maintenance
    ])
])

# Connect monitoring to analysis_loop (monitoring before data_analysis)
# Combine train_crop_monitor_po and analysis_loop in one PO to add monitoring -> data_analysis edge
train_monitor_analysis_po = StrictPartialOrder(nodes=[staff_training, crop_planting, monitoring, analysis_loop])
train_monitor_analysis_po.order.add_edge(staff_training, crop_planting)
train_monitor_analysis_po.order.add_edge(crop_planting, monitoring)
train_monitor_analysis_po.order.add_edge(monitoring, analysis_loop)

# Finally, merge all main parts:
# init_po -> design_po -> mod_env_po -> train_monitor_analysis_po
root = StrictPartialOrder(
    nodes=[
        init_po,
        design_po,
        mod_env_po,
        train_monitor_analysis_po
    ]
)
# The ordering dependencies between these sub-Po nodes
root.order.add_edge(init_po, design_po)
root.order.add_edge(design_po, mod_env_po)
root.order.add_edge(mod_env_po, train_monitor_analysis_po)