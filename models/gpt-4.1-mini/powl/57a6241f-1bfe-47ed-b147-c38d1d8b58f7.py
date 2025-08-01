# Generated from: 57a6241f-1bfe-47ed-b147-c38d1d8b58f7.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site assessment, environmental control design, modular system installation, nutrient cycling setup, and integration of AI-driven monitoring. The process ensures sustainable resource use by incorporating rainwater harvesting and waste biomass recycling. Stakeholder coordination includes local authorities, agronomists, and technology providers to optimize crop yield and minimize ecological impact. Continuous testing and adjustment phases guarantee optimal growth conditions and system efficiency before commercial production launch.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
SiteSurvey = Transition(label='Site Survey')
PermitsAcquire = Transition(label='Permits Acquire')
DesignLayout = Transition(label='Design Layout')
InstallFrame = Transition(label='Install Frame')
SetupHydroponics = Transition(label='Setup Hydroponics')
WaterHarvest = Transition(label='Water Harvest')
NutrientMix = Transition(label='Nutrient Mix')
LightingInstall = Transition(label='Lighting Install')
SensorCalibrate = Transition(label='Sensor Calibrate')
AIIntegration = Transition(label='AI Integration')
WasteProcess = Transition(label='Waste Process')
CropPlanting = Transition(label='Crop Planting')
GrowthMonitor = Transition(label='Growth Monitor')
YieldTesting = Transition(label='Yield Testing')
StakeholderMeet = Transition(label='Stakeholder Meet')
SystemAudit = Transition(label='System Audit')

# Build the partial order according to the process description:

# 1. Initial site and permit activities in sequence
# Site Survey --> Permits Acquire
# 2. Design Layout comes after site and permits
# 3. Installation phase: Install Frame --> Setup Hydroponics --> Lighting Install --> Sensor Calibrate
# 4. Environmental and resource setup can be concurrent with installation steps where applicable:
# Water Harvest and Nutrient Mix and Waste Process relate to sustainable resource use
# StakeholderMeet can be concurrent once Design Layout is done (to optimize)
# AI Integration is after Sensor Calibrate

# 5. Crop Planting after installation and setup
# 6. Growth Monitor and Yield Testing sequential, with possible loop on Growth Monitor and Yield Testing until satisfactory

# 7. System Audit at the end to finalize before commercial launch

# Create partial orders for setup:
install_sequence = StrictPartialOrder(nodes=[InstallFrame, SetupHydroponics, LightingInstall, SensorCalibrate])
install_sequence.order.add_edge(InstallFrame, SetupHydroponics)
install_sequence.order.add_edge(SetupHydroponics, LightingInstall)
install_sequence.order.add_edge(LightingInstall, SensorCalibrate)

# Sustainable setups (Water Harvest, Nutrient Mix, Waste Process) can be concurrent after Design Layout (parallel)
sustainable = StrictPartialOrder(
    nodes=[WaterHarvest, NutrientMix, WasteProcess]
)
# No ordering inside sustainable nodes (parallel)

# Stakeholder meeting after Design Layout, concurrent with sustainable setups
# So, these 4 nodes are concurrent after Design Layout:
# StakeholderMeet + sustainable nodes

# Partial order for those 4 concurrent nodes
stakeholders_and_sustain = StrictPartialOrder(
    nodes=[StakeholderMeet, WaterHarvest, NutrientMix, WasteProcess]
)
# No internal order, concurrent nodes

# Growth monitor and yield testing with loop:
# Loop over GrowthMonitor (A) and YieldTesting (B)
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[GrowthMonitor, YieldTesting]
)

# Now assemble the full process as a partial order:

# Nodes in the entire process:
# - SiteSurvey
# - PermitsAcquire
# - DesignLayout
# - install_sequence (composite node)
# - stakeholders_and_sustain (composite node)
# - AIIntegration
# - CropPlanting
# - growth_loop
# - SystemAudit

nodes = [
    SiteSurvey,
    PermitsAcquire,
    DesignLayout,
    install_sequence,
    stakeholders_and_sustain,
    AIIntegration,
    CropPlanting,
    growth_loop,
    SystemAudit,
]

root = StrictPartialOrder(nodes=nodes)

# Ordering edges according to dependencies:

# Site Survey --> Permits Acquire --> Design Layout
root.order.add_edge(SiteSurvey, PermitsAcquire)
root.order.add_edge(PermitsAcquire, DesignLayout)

# Design Layout --> install_sequence
root.order.add_edge(DesignLayout, install_sequence)

# Design Layout --> stakeholders_and_sustain (parallel branch)
root.order.add_edge(DesignLayout, stakeholders_and_sustain)

# install_sequence --> AI Integration
root.order.add_edge(install_sequence, AIIntegration)

# stakeholders_and_sustain --> AI Integration
root.order.add_edge(stakeholders_and_sustain, AIIntegration)

# AI Integration --> Crop Planting
root.order.add_edge(AIIntegration, CropPlanting)

# Crop Planting --> growth_loop
root.order.add_edge(CropPlanting, growth_loop)

# growth_loop --> System Audit
root.order.add_edge(growth_loop, SystemAudit)