# Generated from: 1ed2da76-699d-4de0-98ac-7d18a0cc576b.json
# Description: This process outlines the complex setup and operational workflow for establishing an urban vertical farm that integrates hydroponics, renewable energy, and IoT sensor networks. It involves site assessment, modular structure assembly, nutrient solution formulation, environmental calibration, automated planting, real-time growth monitoring, pest detection via AI, adaptive lighting control, water recycling, harvest scheduling, quality analysis, packaging automation, and distribution logistics, ensuring sustainable and efficient fresh produce supply in metropolitan areas. Each step requires cross-disciplinary coordination among agronomists, engineers, and data scientists to optimize yield and minimize resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Design_Plan = Transition(label='Design Plan')
Permit_Acquire = Transition(label='Permit Acquire')
Structure_Build = Transition(label='Structure Build')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Setup = Transition(label='Plant Setup')
Env_Calibrate = Transition(label='Env Calibrate')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Light_Control = Transition(label='Light Control')
Water_Cycle = Transition(label='Water Cycle')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Test = Transition(label='Quality Test')
Pack_Goods = Transition(label='Pack Goods')
Logistics_Arrange = Transition(label='Logistics Arrange')

# First phase: setup sequence with partial concurrency
# Site Survey -> Design Plan -> Permit Acquire
# After permit: Structure Build and Sensor Install can proceed in parallel
# After that: Nutrient Mix and Env Calibrate can proceed in parallel
# Then Plant Setup

# Setup main PO with all these nodes
setup_nodes = [
    Site_Survey,
    Design_Plan,
    Permit_Acquire,
    Structure_Build,
    Sensor_Install,
    Nutrient_Mix,
    Env_Calibrate,
    Plant_Setup
]

setup_PO = StrictPartialOrder(nodes=setup_nodes)

# Define ordering of setup
setup_PO.order.add_edge(Site_Survey, Design_Plan)
setup_PO.order.add_edge(Design_Plan, Permit_Acquire)

# After Permit Acquire:
# Structure Build and Sensor Install concurrent (no order edge)

# After Structure Build and Sensor Install:
# Nutrient Mix and Env Calibrate concurrent (both require Structure Build and Sensor Install finished)
setup_PO.order.add_edge(Permit_Acquire, Structure_Build)
setup_PO.order.add_edge(Permit_Acquire, Sensor_Install)
setup_PO.order.add_edge(Structure_Build, Nutrient_Mix)
setup_PO.order.add_edge(Sensor_Install, Nutrient_Mix)
setup_PO.order.add_edge(Structure_Build, Env_Calibrate)
setup_PO.order.add_edge(Sensor_Install, Env_Calibrate)

# Both Nutrient Mix and Env Calibrate must finish before Plant Setup
setup_PO.order.add_edge(Nutrient_Mix, Plant_Setup)
setup_PO.order.add_edge(Env_Calibrate, Plant_Setup)

# Second phase: operational and monitoring (partially concurrent)
# Growth Monitoring is continuous and concurrent with Pest Detection, Light Control, Water Cycle
# These 4 are concurrent activities (Growth Monitor, Pest Detect, Light Control, Water Cycle)

monitor_nodes = [Growth_Monitor, Pest_Detect, Light_Control, Water_Cycle]

monitor_PO = StrictPartialOrder(nodes=monitor_nodes)
# No order edges between monitor nodes - concurrent

# Third phase: harvest and delivery sequence
# Harvest Plan -> Quality Test -> Pack Goods -> Logistics Arrange

harvest_nodes = [Harvest_Plan, Quality_Test, Pack_Goods, Logistics_Arrange]

harvest_PO = StrictPartialOrder(nodes=harvest_nodes)
harvest_PO.order.add_edge(Harvest_Plan, Quality_Test)
harvest_PO.order.add_edge(Quality_Test, Pack_Goods)
harvest_PO.order.add_edge(Pack_Goods, Logistics_Arrange)

# Now build the whole process partial order connecting the three phases
all_nodes = [setup_PO, monitor_PO, harvest_PO]

root = StrictPartialOrder(nodes=all_nodes)

# Link setup_PO --> monitor_PO and setup_PO --> harvest_PO (monitoring and harvesting after setup)
root.order.add_edge(setup_PO, monitor_PO)
root.order.add_edge(setup_PO, harvest_PO)

# It is plausible that harvest_PO needs monitoring to be completed? 
# Usually monitoring and harvest plan overlap but harvest depends on monitoring results.
# Model as: monitor_PO --> harvest_PO

root.order.add_edge(monitor_PO, harvest_PO)