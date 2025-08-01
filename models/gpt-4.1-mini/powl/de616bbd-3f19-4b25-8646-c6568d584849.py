# Generated from: de616bbd-3f19-4b25-8646-c6568d584849.json
# Description: This process involves establishing a fully automated urban vertical farm within a repurposed warehouse. It begins with site analysis and structural assessment, followed by environmental system design including hydroponics and LED lighting setup. Next, sensor installations for climate control and nutrient monitoring are integrated. Seed selection and germination protocols are developed alongside automated planting routines. Crop growth is continuously monitored using AI-driven analytics to optimize yield and resource usage. Harvesting is performed by robotic arms, and produce is packaged on-site with traceability labeling. Finally, logistics coordination ensures timely delivery to local markets, completing a sustainable urban agriculture cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
SiteAnalysis = Transition(label='Site Analysis')
StructuralCheck = Transition(label='Structural Check')

SystemDesign = Transition(label='System Design')
HydroponicsSetup = Transition(label='Hydroponics Setup')
LightingInstall = Transition(label='Lighting Install')

SensorInstall = Transition(label='Sensor Install')
ClimateControl = Transition(label='Climate Control')
NutrientMonitor = Transition(label='Nutrient Monitor')

SeedSelection = Transition(label='Seed Selection')
GerminationStart = Transition(label='Germination Start')
AutoPlanting = Transition(label='Auto Planting')

GrowthMonitoring = Transition(label='Growth Monitoring')
AIAnalytics = Transition(label='AI Analytics')

RoboticHarvest = Transition(label='Robotic Harvest')
Packaging = Transition(label='Packaging')
TraceLabeling = Transition(label='Trace Labeling')

LogisticsPlan = Transition(label='Logistics Plan')

# Build partial orders according to the process description:

# Site Analysis --> Structural Check
site_and_struct = StrictPartialOrder(nodes=[SiteAnalysis, StructuralCheck])
site_and_struct.order.add_edge(SiteAnalysis, StructuralCheck)

# System Design includes Hydroponics Setup & Lighting Install, which are sequential (design first, then setups)
system_design_po = StrictPartialOrder(nodes=[SystemDesign, HydroponicsSetup, LightingInstall])
system_design_po.order.add_edge(SystemDesign, HydroponicsSetup)
system_design_po.order.add_edge(HydroponicsSetup, LightingInstall)

# Sensor Install with Climate Control and Nutrient Monitor concurrent after Sensor Install
sensor_setup_po = StrictPartialOrder(nodes=[SensorInstall, ClimateControl, NutrientMonitor])
sensor_setup_po.order.add_edge(SensorInstall, ClimateControl)
sensor_setup_po.order.add_edge(SensorInstall, NutrientMonitor)

# Seed Selection --> Germination Start --> Auto Planting
seed_proc_po = StrictPartialOrder(
    nodes=[SeedSelection, GerminationStart, AutoPlanting])
seed_proc_po.order.add_edge(SeedSelection, GerminationStart)
seed_proc_po.order.add_edge(GerminationStart, AutoPlanting)

# Growth Monitoring and AI Analytics concurrent after Auto Planting
growth_monitoring_po = StrictPartialOrder(
    nodes=[GrowthMonitoring, AIAnalytics])
growth_monitoring_po.order.add_edge(GrowthMonitoring, AIAnalytics)  # AIAnalytics depends on GrowthMonitoring

# Harvesting, Packaging, Trace Labeling sequential
harvest_packaging_po = StrictPartialOrder(
    nodes=[RoboticHarvest, Packaging, TraceLabeling])
harvest_packaging_po.order.add_edge(RoboticHarvest, Packaging)
harvest_packaging_po.order.add_edge(Packaging, TraceLabeling)

# Build overall PO with all major partial orders plus LogisticsPlan at the end

# Combine all partial orders at top level nodes, define ordering according to the description:

# Overall sequence:
# (SiteAnalysis -> StructuralCheck) 
#   -> (SystemDesign -> HydroponicsSetup -> LightingInstall)
#   -> (SensorInstall -> ClimateControl & NutrientMonitor concurrent)
#   -> (SeedSelection -> GerminationStart -> AutoPlanting)
#   -> (GrowthMonitoring -> AIAnalytics)
#   -> (RoboticHarvest -> Packaging -> TraceLabeling)
#   -> LogisticsPlan

# First, create a list of all nodes:
all_nodes = [
    site_and_struct,
    system_design_po,
    sensor_setup_po,
    seed_proc_po,
    growth_monitoring_po,
    harvest_packaging_po,
    LogisticsPlan
]

root = StrictPartialOrder(nodes=all_nodes)

# Establish the overall ordering edges:
root.order.add_edge(site_and_struct, system_design_po)
root.order.add_edge(system_design_po, sensor_setup_po)
root.order.add_edge(sensor_setup_po, seed_proc_po)
root.order.add_edge(seed_proc_po, growth_monitoring_po)
root.order.add_edge(growth_monitoring_po, harvest_packaging_po)
root.order.add_edge(harvest_packaging_po, LogisticsPlan)