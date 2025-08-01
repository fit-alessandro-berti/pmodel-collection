# Generated from: 467abb53-7670-436c-9632-e65d632913ac.json
# Description: This process involves the complex orchestration of urban vertical farm development, integrating architectural design, environmental control systems, and agricultural science to optimize crop yield in constrained city spaces. It starts with site assessment and feasibility analysis, followed by modular farm design and structural adaptation to existing buildings. Subsequently, it includes installing hydroponic and aeroponic systems, integrating IoT sensors for real-time monitoring, and implementing automated nutrient delivery and climate regulation. The process also covers workforce training, supply chain coordination for seed and resource procurement, and establishing waste recycling protocols. Continuous data collection and AI-driven crop management optimize growth cycles, while marketing strategies are aligned to promote locally grown produce. This atypical business process blends technology, sustainability, and urban planning to revolutionize food production in metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess     = Transition(label='Site Assess')
feas_eval       = Transition(label='Feasibility Eval')
mod_design      = Transition(label='Modular Design')
struct_adapt    = Transition(label='Structure Adapt')
sys_install     = Transition(label='System Install')
sensor_deploy   = Transition(label='Sensor Deploy')
nutrient_setup  = Transition(label='Nutrient Setup')
climate_control = Transition(label='Climate Control')
worker_train    = Transition(label='Worker Train')
seed_procure    = Transition(label='Seed Procure')
resource_manage = Transition(label='Resource Manage')
waste_recycle   = Transition(label='Waste Recycle')
supply_sync     = Transition(label='Supply Sync')
data_collect    = Transition(label='Data Collect')
ai_optimize     = Transition(label='AI Optimize')
market_launch   = Transition(label='Market Launch')

# Loop for continuous data collection and AI optimization
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, ai_optimize])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess, feas_eval,
    mod_design, struct_adapt,
    sys_install, sensor_deploy, nutrient_setup, climate_control,
    worker_train, seed_procure, resource_manage, waste_recycle, supply_sync,
    data_loop, market_launch
])

# Define control-flow dependencies
root.order.add_edge(site_assess,     feas_eval)
root.order.add_edge(feas_eval,       mod_design)
root.order.add_edge(mod_design,      struct_adapt)
root.order.add_edge(struct_adapt,    sys_install)
root.order.add_edge(sys_install,     sensor_deploy)
root.order.add_edge(sensor_deploy,   nutrient_setup)
root.order.add_edge(nutrient_setup,  climate_control)

# After climate control, four tasks in parallel
root.order.add_edge(climate_control, worker_train)
root.order.add_edge(climate_control, seed_procure)
root.order.add_edge(climate_control, resource_manage)
root.order.add_edge(climate_control, waste_recycle)

# Synchronize seed and resource activities before supply sync
root.order.add_edge(seed_procure,    supply_sync)
root.order.add_edge(resource_manage, supply_sync)

# All setup tasks complete before entering the data loop
root.order.add_edge(worker_train,    data_loop)
root.order.add_edge(waste_recycle,   data_loop)
root.order.add_edge(supply_sync,     data_loop)

# After the continuous loop, launch marketing
root.order.add_edge(data_loop,       market_launch)