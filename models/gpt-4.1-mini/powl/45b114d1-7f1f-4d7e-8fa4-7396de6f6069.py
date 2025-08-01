# Generated from: 45b114d1-7f1f-4d7e-8fa4-7396de6f6069.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, structural modifications, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, calibration of nutrient delivery systems, implementation of energy-efficient LED lighting, and automation of climate control. The process further includes staff training on smart farming techniques, development of crop scheduling algorithms, pest management protocols without pesticides, and establishing partnerships with local markets for produce distribution. Continuous data collection and system optimization ensure sustainable and scalable urban agriculture in constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
StructureAssess = Transition(label='Structure Assess')
LayoutDesign = Transition(label='Layout Design')
InstallFrames = Transition(label='Install Frames')
SetupHydroponics = Transition(label='Setup Hydroponics')
AddSensors = Transition(label='Add Sensors')
CalibrateNutrients = Transition(label='Calibrate Nutrients')
InstallLighting = Transition(label='Install Lighting')
ConfigureClimate = Transition(label='Configure Climate')
DevelopSoftware = Transition(label='Develop Software')
TrainStaff = Transition(label='Train Staff')
PestMonitor = Transition(label='Pest Monitor')
CropScheduling = Transition(label='Crop Scheduling')
MarketLiaison = Transition(label='Market Liaison')
DataAnalysis = Transition(label='Data Analysis')

# Step 1: Site Survey --> Structure Assess --> Layout Design
po1 = StrictPartialOrder(nodes=[SiteSurvey, StructureAssess, LayoutDesign])
po1.order.add_edge(SiteSurvey, StructureAssess)
po1.order.add_edge(StructureAssess, LayoutDesign)

# Step 2: Structural modifications and installation frame: Layout Design --> Install Frames
po2 = StrictPartialOrder(nodes=[InstallFrames])
# will connect po1 to po2 later

# Step 3: Installation of hydroponic and aeroponic systems and sensors.
po3 = StrictPartialOrder(nodes=[SetupHydroponics, AddSensors])
# presumably SetupHydroponics before AddSensors because sensors depend on installation
po3.order.add_edge(SetupHydroponics, AddSensors)

# Step 4: Calibration of nutrients, lighting installation, climate configuration.
po4 = StrictPartialOrder(nodes=[CalibrateNutrients, InstallLighting, ConfigureClimate])
# assuming calibration -> lighting -> configure climate (somewhat sequential)
po4.order.add_edge(CalibrateNutrients, InstallLighting)
po4.order.add_edge(InstallLighting, ConfigureClimate)

# Step 5: Software development, staff training (can be concurrent)
po5 = StrictPartialOrder(nodes=[DevelopSoftware, TrainStaff])
# No order edges = concurrent

# Step 6: Pest monitoring, crop scheduling, market liaison (can start after staff training and software)
po6 = StrictPartialOrder(nodes=[PestMonitor, CropScheduling, MarketLiaison])
# No order edges = concurrent

# Step 7: Data analysis - continuous, but here model as last activity depending on pest monitor, crop scheduling, market liaison
po7 = StrictPartialOrder(nodes=[DataAnalysis])
# Connect po6 to po7 later

# Compose installation phase partial order: install frames -> setup hydroponics & add sensors -> calibration, lighting, climate
po_install_phase = StrictPartialOrder(
    nodes=[InstallFrames, SetupHydroponics, AddSensors, CalibrateNutrients, InstallLighting, ConfigureClimate]
)
po_install_phase.order.add_edge(InstallFrames, SetupHydroponics)
po_install_phase.order.add_edge(SetupHydroponics, AddSensors)
po_install_phase.order.add_edge(AddSensors, CalibrateNutrients)
po_install_phase.order.add_edge(CalibrateNutrients, InstallLighting)
po_install_phase.order.add_edge(InstallLighting, ConfigureClimate)

# Compose training & development phase PO with pest, crop scheduling, market liaison
po_training_dev = StrictPartialOrder(
    nodes=[DevelopSoftware, TrainStaff, PestMonitor, CropScheduling, MarketLiaison]
)
po_training_dev.order.add_edge(DevelopSoftware, PestMonitor)
po_training_dev.order.add_edge(TrainStaff, PestMonitor)
po_training_dev.order.add_edge(DevelopSoftware, CropScheduling)
po_training_dev.order.add_edge(TrainStaff, CropScheduling)
po_training_dev.order.add_edge(DevelopSoftware, MarketLiaison)
po_training_dev.order.add_edge(TrainStaff, MarketLiaison)

# Compose the last stage: Pest/Crop/Market -> Data Analysis
po_final = StrictPartialOrder(nodes=[PestMonitor, CropScheduling, MarketLiaison, DataAnalysis])
po_final.order.add_edge(PestMonitor, DataAnalysis)
po_final.order.add_edge(CropScheduling, DataAnalysis)
po_final.order.add_edge(MarketLiaison, DataAnalysis)

# Now connect the phases partially ordered:
# po1 (survey, structure, layout) --> install phase
po_top = StrictPartialOrder(
    nodes=[SiteSurvey, StructureAssess, LayoutDesign,
           InstallFrames, SetupHydroponics, AddSensors, CalibrateNutrients, InstallLighting, ConfigureClimate,
           DevelopSoftware, TrainStaff,
           PestMonitor, CropScheduling, MarketLiaison,
           DataAnalysis]
)

# Add edges from po1
po_top.order.add_edge(SiteSurvey, StructureAssess)
po_top.order.add_edge(StructureAssess, LayoutDesign)

# Layout Design --> Install Frames
po_top.order.add_edge(LayoutDesign, InstallFrames)

# Install Frames -> Setup Hydroponics -> Add Sensors -> Calibrate Nutrients -> Install Lighting -> Configure Climate
po_top.order.add_edge(InstallFrames, SetupHydroponics)
po_top.order.add_edge(SetupHydroponics, AddSensors)
po_top.order.add_edge(AddSensors, CalibrateNutrients)
po_top.order.add_edge(CalibrateNutrients, InstallLighting)
po_top.order.add_edge(InstallLighting, ConfigureClimate)

# After Configure Climate finishes, Develop Software and Train Staff in parallel
po_top.order.add_edge(ConfigureClimate, DevelopSoftware)
po_top.order.add_edge(ConfigureClimate, TrainStaff)

# Develop Software + Train Staff --> Pest Monitor, Crop Scheduling, Market Liaison (all three start after both are done)
po_top.order.add_edge(DevelopSoftware, PestMonitor)
po_top.order.add_edge(DevelopSoftware, CropScheduling)
po_top.order.add_edge(DevelopSoftware, MarketLiaison)
po_top.order.add_edge(TrainStaff, PestMonitor)
po_top.order.add_edge(TrainStaff, CropScheduling)
po_top.order.add_edge(TrainStaff, MarketLiaison)

# Pest Monitor, Crop Scheduling, Market Liaison --> Data Analysis
po_top.order.add_edge(PestMonitor, DataAnalysis)
po_top.order.add_edge(CropScheduling, DataAnalysis)
po_top.order.add_edge(MarketLiaison, DataAnalysis)

root = po_top