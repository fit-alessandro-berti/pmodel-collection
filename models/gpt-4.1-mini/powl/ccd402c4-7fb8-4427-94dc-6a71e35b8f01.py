# Generated from: ccd402c4-7fb8-4427-94dc-6a71e35b8f01.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed high-rise building. It involves integrating IoT sensors for real-time monitoring of plant health, implementing hydroponic systems optimized for space and resource efficiency, and coordinating logistics for supply chain management of seeds, nutrients, and harvested crops. The process also includes securing permits, stakeholder engagement with local communities, and developing a renewable energy plan to ensure sustainability. Advanced data analytics are employed to predict yield and optimize growth cycles, while maintenance routines are scheduled to minimize downtime. Finally, marketing strategies are devised to position the farm as a local organic produce provider, emphasizing freshness and eco-friendliness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
StakeholderMeet = Transition(label='Stakeholder Meet')
DesignLayout = Transition(label='Design Layout')
IoTInstall = Transition(label='IoT Install')
SensorCalibrate = Transition(label='Sensor Calibrate')
HydroponicSetup = Transition(label='Hydroponic Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedSowing = Transition(label='Seed Sowing')
ClimateControl = Transition(label='Climate Control')
DataMonitor = Transition(label='Data Monitor')
YieldForecast = Transition(label='Yield Forecast')
EnergyPlan = Transition(label='Energy Plan')
MaintenancePlan = Transition(label='Maintenance Plan')
HarvestPrep = Transition(label='Harvest Prep')
SupplyDispatch = Transition(label='Supply Dispatch')
MarketLaunch = Transition(label='Market Launch')

# Step 1: Site Survey, Permit Filing, Stakeholder Meet (all concur)
initial_PO = StrictPartialOrder(nodes=[SiteSurvey, PermitFiling, StakeholderMeet])

# After initial, Design Layout depends on all three
# Use StrictPartialOrder to represent partial order with edges SiteSurvey --> DesignLayout etc.
design_PO = StrictPartialOrder(
    nodes=[DesignLayout, SiteSurvey, PermitFiling, StakeholderMeet]
)
design_PO.order.add_edge(SiteSurvey, DesignLayout)
design_PO.order.add_edge(PermitFiling, DesignLayout)
design_PO.order.add_edge(StakeholderMeet, DesignLayout)

# IoT Install and Hydroponic Setup depend on Design Layout, concurrently done:
iot_hydro_PO = StrictPartialOrder(
    nodes=[IoTInstall, HydroponicSetup, DesignLayout]
)
iot_hydro_PO.order.add_edge(DesignLayout, IoTInstall)
iot_hydro_PO.order.add_edge(DesignLayout, HydroponicSetup)

# Sensor Calibrate after IoT Install
sensor_PO = StrictPartialOrder(nodes=[SensorCalibrate, IoTInstall])
sensor_PO.order.add_edge(IoTInstall, SensorCalibrate)

# Nutrient Mix and Seed Sowing after Hydroponic Setup, concurrent:
nutrient_seed_PO = StrictPartialOrder(nodes=[NutrientMix, SeedSowing, HydroponicSetup])
nutrient_seed_PO.order.add_edge(HydroponicSetup, NutrientMix)
nutrient_seed_PO.order.add_edge(HydroponicSetup, SeedSowing)

# Climate Control after Nutrient Mix and Sensor Calibrate (both dependencies):
climate_PO = StrictPartialOrder(nodes=[ClimateControl, NutrientMix, SensorCalibrate])
climate_PO.order.add_edge(NutrientMix, ClimateControl)
climate_PO.order.add_edge(SensorCalibrate, ClimateControl)

# Data Monitor depends on Seed Sowing and Climate Control (both dependencies):
data_monitor_PO = StrictPartialOrder(nodes=[DataMonitor, SeedSowing, ClimateControl])
data_monitor_PO.order.add_edge(SeedSowing, DataMonitor)
data_monitor_PO.order.add_edge(ClimateControl, DataMonitor)

# Yield Forecast after Data Monitor
yield_PO = StrictPartialOrder(nodes=[YieldForecast, DataMonitor])
yield_PO.order.add_edge(DataMonitor, YieldForecast)

# Energy Plan and Maintenance Plan after Design Layout (can be concurrent with other activities that are later)
energy_maint_PO = StrictPartialOrder(nodes=[EnergyPlan, MaintenancePlan, DesignLayout])
energy_maint_PO.order.add_edge(DesignLayout, EnergyPlan)
energy_maint_PO.order.add_edge(DesignLayout, MaintenancePlan)

# Maintenance Plan loop: repeat Maintenance Plan and Data Monitor cycles before Harvest Prep
# Define loop: body=MaintenancePlan, redo=DataMonitor, exit=HarvestPrep
# POWL LOOP semantics: * (body, redo)
# We define the loop node as LOOP(MaintenancePlan, DataMonitor)
# But from description, "maintenance routines are scheduled to minimize downtime" while monitoring data
# For safe interpretation: loop cycles between DataMonitor and MaintenancePlan repeatedly until exit

# First, create loop with body MaintenancePlan, redo DataMonitor
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[MaintenancePlan, DataMonitor])

# Harvest Prep depends on yield forecast, maintenance loop, and energy plan
harvest_PO = StrictPartialOrder(
    nodes=[HarvestPrep, YieldForecast, maintenance_loop, EnergyPlan]
)
harvest_PO.order.add_edge(YieldForecast, HarvestPrep)
harvest_PO.order.add_edge(maintenance_loop, HarvestPrep)
harvest_PO.order.add_edge(EnergyPlan, HarvestPrep)

# Supply Dispatch after Harvest Prep
supply_PO = StrictPartialOrder(nodes=[SupplyDispatch, HarvestPrep])
supply_PO.order.add_edge(HarvestPrep, SupplyDispatch)

# Market Launch after Supply Dispatch and Stakeholder Meet (ensures community engagement and readiness)
market_PO = StrictPartialOrder(nodes=[MarketLaunch, SupplyDispatch, StakeholderMeet])
market_PO.order.add_edge(SupplyDispatch, MarketLaunch)
market_PO.order.add_edge(StakeholderMeet, MarketLaunch)

# Now combine all major parts in a partial order:
# Nodes: initial_PO nodes are included in design_PO nodes so we can use design_PO as start nodes
# Compose partial order for whole process:

# Let's collect all distinct nodes properly, we will build a big PO with these nodes:
nodes = [
    SiteSurvey, PermitFiling, StakeholderMeet, DesignLayout,
    IoTInstall, HydroponicSetup, SensorCalibrate,
    NutrientMix, SeedSowing, ClimateControl, DataMonitor,
    YieldForecast, EnergyPlan, MaintenancePlan,
    maintenance_loop,  # Instead of plain MaintenancePlan used in harvest_PO
    HarvestPrep, SupplyDispatch, MarketLaunch
]

root = StrictPartialOrder(nodes=nodes)

# Add edges reflecting dependencies:

# initial to design
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(PermitFiling, DesignLayout)
root.order.add_edge(StakeholderMeet, DesignLayout)

# design to IoTInstall and HydroponicSetup
root.order.add_edge(DesignLayout, IoTInstall)
root.order.add_edge(DesignLayout, HydroponicSetup)

# IoTInstall to SensorCalibrate
root.order.add_edge(IoTInstall, SensorCalibrate)

# HydroponicSetup to NutrientMix and SeedSowing
root.order.add_edge(HydroponicSetup, NutrientMix)
root.order.add_edge(HydroponicSetup, SeedSowing)

# NutrientMix and SensorCalibrate to ClimateControl
root.order.add_edge(NutrientMix, ClimateControl)
root.order.add_edge(SensorCalibrate, ClimateControl)

# SeedSowing and ClimateControl to DataMonitor
root.order.add_edge(SeedSowing, DataMonitor)
root.order.add_edge(ClimateControl, DataMonitor)

# DataMonitor to YieldForecast
root.order.add_edge(DataMonitor, YieldForecast)

# DesignLayout to EnergyPlan and MaintenancePlan (but maintenance replaced by loop)
root.order.add_edge(DesignLayout, EnergyPlan)
root.order.add_edge(DesignLayout, MaintenancePlan)

# Replace MaintenancePlan node with maintenance_loop for downstream edges:
# So link MaintenancePlan and DataMonitor as children of loop, but in root:
# MaintenanceLoop is node representing loop of (MaintenancePlan, DataMonitor)
# Assume MaintenancePlan and DataMonitor still nodes, but loop represents repeated execution

# For connections: MaintenanceLoop represents repeated MaintenancePlan and DataMonitor execution
# We will add edges from YieldForecast -> MaintenanceLoop (Maintenance should start after planning)
# But from original orders: MaintenancePlan started after DesignLayout; keep both edges

# To keep consistency, connect YieldForecast to MaintenanceLoop (delay maintenance until growth forecast):
root.order.add_edge(YieldForecast, maintenance_loop)

# MaintenanceLoop to HarvestPrep
root.order.add_edge(maintenance_loop, HarvestPrep)

# EnergyPlan to HarvestPrep
root.order.add_edge(EnergyPlan, HarvestPrep)

# HarvestPrep to SupplyDispatch
root.order.add_edge(HarvestPrep, SupplyDispatch)

# SupplyDispatch to MarketLaunch
root.order.add_edge(SupplyDispatch, MarketLaunch)

# StakeholderMeet is prerequisite for MarketLaunch as well (from initial stakeholder engagement)
root.order.add_edge(StakeholderMeet, MarketLaunch)

# Return the final root