# Generated from: b9a32a0f-535f-41b9-84f1-1d07095c3ba2.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It involves site analysis, modular system design, environmental control calibration, nutrient cycling optimization, and integration of renewable energy sources. Stakeholder engagement, regulatory compliance, and sustainable waste management are also critical to ensure operational efficiency and minimize ecological impact. The process further includes technology installation, staff training, continuous monitoring, and iterative system adjustments to adapt to urban constraints and maximize crop yield in limited spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
stakeholder_meet   = Transition(label='Stakeholder Meet')
regulation_check   = Transition(label='Regulation Check')
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
modular_setup      = Transition(label='Modular Setup')
system_install     = Transition(label='System Install')
env_calibration    = Transition(label='Env Calibration')
nutrient_mix       = Transition(label='Nutrient Mix')
water_recycling    = Transition(label='Water Recycling')
energy_integrate   = Transition(label='Energy Integrate')
waste_process      = Transition(label='Waste Process')
staff_training     = Transition(label='Staff Training')
crop_planting      = Transition(label='Crop Planting')
monitoring         = Transition(label='Monitoring')
data_analysis      = Transition(label='Data Analysis')
yield_optimize     = Transition(label='Yield Optimize')
maintenance        = Transition(label='Maintenance')

# Parallel group for environmental & system calibration tasks
par_env = StrictPartialOrder(nodes=[
    env_calibration,
    nutrient_mix,
    water_recycling,
    energy_integrate,
    waste_process
])
# no edges => all five can run in parallel

# Loop for continuous monitoring, analysis and iterative optimization
# A = Monitoring -> Data Analysis -> Yield Optimize
A = StrictPartialOrder(nodes=[monitoring, data_analysis, yield_optimize])
A.order.add_edge(monitoring, data_analysis)
A.order.add_edge(data_analysis, yield_optimize)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[A, maintenance])

# Build the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    stakeholder_meet,
    regulation_check,
    site_survey,
    design_layout,
    modular_setup,
    system_install,
    par_env,
    staff_training,
    crop_planting,
    loop_monitor
])

# Add control-flow dependencies
root.order.add_edge(stakeholder_meet,   site_survey)
root.order.add_edge(regulation_check,   site_survey)
root.order.add_edge(site_survey,        design_layout)
root.order.add_edge(design_layout,      modular_setup)
root.order.add_edge(modular_setup,      system_install)
root.order.add_edge(system_install,     par_env)
root.order.add_edge(par_env,            staff_training)
root.order.add_edge(staff_training,     crop_planting)
root.order.add_edge(crop_planting,      loop_monitor)