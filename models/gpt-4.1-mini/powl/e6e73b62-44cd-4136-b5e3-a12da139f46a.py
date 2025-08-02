# Generated from: e6e73b62-44cd-4136-b5e3-a12da139f46a.json
# Description: This process describes the establishment of an urban vertical farming system that integrates advanced hydroponics, IoT sensors, and renewable energy management. It involves site evaluation, modular infrastructure assembly, nutrient solution calibration, environmental monitoring setup, and crop cycle optimization. The workflow also includes waste recycling, pest control without chemicals, real-time data analytics for yield prediction, and community engagement for local produce distribution. The process aims to maximize space efficiency and sustainability in densely populated areas by leveraging technology and innovative farming techniques, ensuring fresh, organic produce year-round while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Procure_Modules = Transition(label='Procure Modules')
Install_Framework = Transition(label='Install Framework')
Setup_Sensors = Transition(label='Setup Sensors')
Calibrate_Nutrients = Transition(label='Calibrate Nutrients')
Configure_IoT = Transition(label='Configure IoT')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Lighting = Transition(label='Manage Lighting')
Pest_Control = Transition(label='Pest Control')
Recycle_Waste = Transition(label='Recycle Waste')
Analyze_Data = Transition(label='Analyze Data')
Adjust_Environment = Transition(label='Adjust Environment')
Harvest_Crops = Transition(label='Harvest Crops')
Distribute_Produce = Transition(label='Distribute Produce')

# Phase 1: Setup and infrastructure partial order
setup_nodes = [
    Site_Survey,
    Design_Layout,
    Procure_Modules,
    Install_Framework,
    Setup_Sensors,
    Calibrate_Nutrients,
    Configure_IoT
]
setup = StrictPartialOrder(nodes=setup_nodes)
setup.order.add_edge(Site_Survey, Design_Layout)
setup.order.add_edge(Design_Layout, Procure_Modules)
setup.order.add_edge(Procure_Modules, Install_Framework)
setup.order.add_edge(Install_Framework, Setup_Sensors)
setup.order.add_edge(Setup_Sensors, Calibrate_Nutrients)
setup.order.add_edge(Calibrate_Nutrients, Configure_IoT)

# Phase 2: Crop cycle with monitoring loop and adjust environment
# Body of loop: 
# Plant_Seeding -> Monitor_Growth -> Manage_Lighting -> Analyze_Data -> Adjust_Environment
# loop structure: execute body and then choose to exit or loop again

crop_body_nodes = [
    Plant_Seeding,
    Monitor_Growth,
    Manage_Lighting,
    Analyze_Data,
    Adjust_Environment,
]

crop_body = StrictPartialOrder(nodes=crop_body_nodes)
crop_body.order.add_edge(Plant_Seeding, Monitor_Growth)
crop_body.order.add_edge(Monitor_Growth, Manage_Lighting)
crop_body.order.add_edge(Manage_Lighting, Analyze_Data)
crop_body.order.add_edge(Analyze_Data, Adjust_Environment)

crop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[crop_body, SilentTransition()])

# Phase 3: Pest control and waste recycling run concurrently (they are ongoing sustainability measures)
sustainability = StrictPartialOrder(nodes=[Pest_Control, Recycle_Waste])
# No order between to allow concurrency

# Phase 4: Harvest and distribute sequence
harvest_phase = StrictPartialOrder(nodes=[Harvest_Crops, Distribute_Produce])
harvest_phase.order.add_edge(Harvest_Crops, Distribute_Produce)

# Assemble the full process partial order:
# after setup, run sustainability concurrently with crop cycles, then harvest and distribute

# We combine sustainability and crop_cycle concurrently
mid_phase = StrictPartialOrder(nodes=[crop_cycle, sustainability])
# No edges between crop_cycle and sustainability for concurrency

# Final total order: setup --> mid_phase --> harvest_phase
root = StrictPartialOrder(nodes=[setup, mid_phase, harvest_phase])
root.order.add_edge(setup, mid_phase)
root.order.add_edge(mid_phase, harvest_phase)