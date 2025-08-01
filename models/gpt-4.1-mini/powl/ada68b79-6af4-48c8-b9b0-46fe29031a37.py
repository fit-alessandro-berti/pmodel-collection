# Generated from: ada68b79-6af4-48c8-b9b0-46fe29031a37.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed warehouse, integrating hydroponic systems and AI-driven climate controls. It involves site analysis, modular structure assembly, nutrient solution preparation, crop selection based on market trends, continuous environmental monitoring, pest detection using image recognition, automated harvesting scheduling, and supply chain synchronization with local retailers to ensure freshness and reduce carbon footprint. The process also includes waste recycling, energy optimization, and data analytics for yield improvement, making it a complex but sustainable agricultural innovation in city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Install_Hydroponics = Transition(label='Install Hydroponics')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Select_Crops = Transition(label='Select Crops')
Setup_Sensors = Transition(label='Setup Sensors')
Configure_AI = Transition(label='Configure AI')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Detect_Pests = Transition(label='Detect Pests')
Schedule_Harvest = Transition(label='Schedule Harvest')
Sort_Produce = Transition(label='Sort Produce')
Pack_Orders = Transition(label='Pack Orders')
Coordinate_Delivery = Transition(label='Coordinate Delivery')
Recycle_Waste = Transition(label='Recycle Waste')
Analyze_Data = Transition(label='Analyze Data')
Optimize_Energy = Transition(label='Optimize Energy')

# Subprocess 1: Site preparation sequence
site_prep = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Structure_Build,
    Install_Hydroponics,
    Prepare_Nutrients,
    Select_Crops
])
site_prep.order.add_edge(Site_Survey, Design_Layout)
site_prep.order.add_edge(Design_Layout, Structure_Build)
site_prep.order.add_edge(Structure_Build, Install_Hydroponics)
site_prep.order.add_edge(Install_Hydroponics, Prepare_Nutrients)
site_prep.order.add_edge(Prepare_Nutrients, Select_Crops)

# Subprocess 2: Sensor setup and configuration
sensor_setup = StrictPartialOrder(nodes=[Setup_Sensors, Configure_AI])
sensor_setup.order.add_edge(Setup_Sensors, Configure_AI)

# Subprocess 3: Planting and monitoring sequence
plant_mon = StrictPartialOrder(nodes=[Plant_Seeding, Monitor_Growth])
plant_mon.order.add_edge(Plant_Seeding, Monitor_Growth)

# Subprocess 4: Pest detection feeding back into monitoring (loop)
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Detect_Pests])

# Subprocess 5: Harvesting and order processing partial order
harvest_proc = StrictPartialOrder(nodes=[
    Schedule_Harvest,
    Sort_Produce,
    Pack_Orders,
    Coordinate_Delivery
])
harvest_proc.order.add_edge(Schedule_Harvest, Sort_Produce)
harvest_proc.order.add_edge(Sort_Produce, Pack_Orders)
harvest_proc.order.add_edge(Pack_Orders, Coordinate_Delivery)

# Subprocess 6: Sustainability and analytics tasks (concurrent)
sustain_analytics = StrictPartialOrder(nodes=[
    Recycle_Waste,
    Analyze_Data,
    Optimize_Energy
])
# no dependencies => all concurrent

# Combine sensor setup with plant seeding (planting depends after sensor setup)
planting = StrictPartialOrder(nodes=[sensor_setup, plant_mon])
planting.order.add_edge(sensor_setup, plant_mon)

# Combine plant monitoring with pest loop (monitor growth will be replaced by pest_loop)
monitoring_with_pests = StrictPartialOrder(nodes=[pest_loop])
# no edges since loop here manages itself

# Combine planting followed by monitoring with pests
planting_and_monitoring = StrictPartialOrder(nodes=[planting, monitoring_with_pests])
planting_and_monitoring.order.add_edge(planting, monitoring_with_pests)

# Top level partial order combining all main subprocesses:
# site_prep must precede planting_and_monitoring and harvesting
# harvesting depends on monitoring_with_pests finishing (harvest proc happens after pest loop)
# sustainability tasks run concurrently with harvesting

root = StrictPartialOrder(nodes=[
    site_prep,
    planting_and_monitoring,
    harvest_proc,
    sustain_analytics
])
root.order.add_edge(site_prep, planting_and_monitoring)
root.order.add_edge(planting_and_monitoring, harvest_proc)
# sustain_analytics concurrent with harvest_proc => no order edges
