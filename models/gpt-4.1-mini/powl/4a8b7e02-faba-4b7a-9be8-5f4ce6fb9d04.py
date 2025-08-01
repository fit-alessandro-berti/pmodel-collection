# Generated from: 4a8b7e02-faba-4b7a-9be8-5f4ce6fb9d04.json
# Description: This process involves the integration of vertical farming systems within urban infrastructure to optimize space and resource utilization. It encompasses site assessment, modular farm design, automated nutrient delivery, environmental monitoring, community engagement, crop rotation planning, waste recycling, pest management using AI, energy consumption optimization, and logistics coordination for local distribution. The process ensures sustainable food production by combining advanced technology, ecological practices, and urban planning, ultimately contributing to food security and reduced carbon footprint in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Design_Modules = Transition(label='Design Modules')
Install_Systems = Transition(label='Install Systems')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Set_Nutrients = Transition(label='Set Nutrients')
Monitor_Environment = Transition(label='Monitor Environment')
Engage_Community = Transition(label='Engage Community')
Plan_Rotation = Transition(label='Plan Rotation')
Recycle_Waste = Transition(label='Recycle Waste')
Manage_Pests = Transition(label='Manage Pests')
Optimize_Energy = Transition(label='Optimize Energy')
Schedule_Harvest = Transition(label='Schedule Harvest')
Coordinate_Logistics = Transition(label='Coordinate Logistics')
Train_Staff = Transition(label='Train Staff')
Report_Metrics = Transition(label='Report Metrics')

# Define modular system preparation partial order
modular_prep = StrictPartialOrder(
    nodes=[Design_Modules, Install_Systems, Calibrate_Sensors],
)
modular_prep.order.add_edge(Design_Modules, Install_Systems)
modular_prep.order.add_edge(Install_Systems, Calibrate_Sensors)

# Nutrients and monitoring partial order
nutrients_monitor = StrictPartialOrder(
    nodes=[Set_Nutrients, Monitor_Environment],
)

# Community engagement and training partial order (concurrent)
comm_train = StrictPartialOrder(
    nodes=[Engage_Community, Train_Staff],
)

# Plan rotation and recycle waste partial order
plan_recycle = StrictPartialOrder(
    nodes=[Plan_Rotation, Recycle_Waste],
)

# Pest management, energy optimization partial order (concurrent)
pests_energy = StrictPartialOrder(
    nodes=[Manage_Pests, Optimize_Energy],
)

# Harvest scheduling and logistics coordination
harvest_logistics = StrictPartialOrder(
    nodes=[Schedule_Harvest, Coordinate_Logistics],
)
harvest_logistics.order.add_edge(Schedule_Harvest, Coordinate_Logistics)

# Combine all prior steps (modular_prep must follow Site Assess)
after_assess = StrictPartialOrder(
    nodes=[
        modular_prep,
        nutrients_monitor,
        comm_train,
        plan_recycle,
        pests_energy,
        harvest_logistics,
        Report_Metrics,
    ],
)

# We add edges to represent control flow:
# Start after Site Assess:
after_assess.order.add_edge(modular_prep, nutrients_monitor)
after_assess.order.add_edge(modular_prep, comm_train)
after_assess.order.add_edge(modular_prep, plan_recycle)
after_assess.order.add_edge(modular_prep, pests_energy)
after_assess.order.add_edge(modular_prep, harvest_logistics)

# Report_Metrics depends on completion of all other activities except maybe comm_train (allow concurrent)
for node in [nutrients_monitor, comm_train, plan_recycle, pests_energy, harvest_logistics]:
    after_assess.order.add_edge(node, Report_Metrics)

# Root partial order: Site Assess before all others
root = StrictPartialOrder(
    nodes=[Site_Assess, after_assess],
)
root.order.add_edge(Site_Assess, after_assess)