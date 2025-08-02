# Generated from: 70dd875c-8039-49b4-9e9a-9ea55d9b03e2.json
# Description: This complex process involves the design, implementation, and ongoing optimization of urban farming systems tailored to specific city environments. It starts with site analysis to assess sunlight, soil quality, and local climate, followed by modular farm design incorporating vertical farming, hydroponics, and aquaponics tailored to available spaces. The process continues with sourcing sustainable materials and specialized equipment, installation of automated irrigation and nutrient delivery systems, and integration of IoT sensors for real-time monitoring of crop health and environmental conditions. Subsequent activities include staff training on unique urban farming techniques, ongoing maintenance and pest management using eco-friendly methods, data analysis for yield optimization, and community engagement programs to promote urban agriculture awareness. The final stages involve scaling the model to multiple sites while maintaining quality control and adapting the design based on evolving urban policies and technological advancements, ensuring a sustainable and profitable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SiteSurvey = Transition(label='Site Survey')
ClimateStudy = Transition(label='Climate Study')
SoilTesting = Transition(label='Soil Testing')

DesignLayout = Transition(label='Design Layout')

MaterialSourcing = Transition(label='Material Sourcing')
EquipmentSetup = Transition(label='Equipment Setup')

IrrigationInstall = Transition(label='Irrigation Install')
SensorDeploy = Transition(label='Sensor Deploy')
SystemConfig = Transition(label='System Config')

StaffTraining = Transition(label='Staff Training')

CropPlanting = Transition(label='Crop Planting')
PestControl = Transition(label='Pest Control')

DataCapture = Transition(label='Data Capture')
YieldReview = Transition(label='Yield Review')

CommunityOutreach = Transition(label='Community Outreach')

ScaleExpansion = Transition(label='Scale Expansion')
PolicyAdapt = Transition(label='Policy Adapt')

# 1) Site analysis: Site Survey, Climate Study, Soil Testing concurrently (no order)
site_analysis = StrictPartialOrder(nodes=[SiteSurvey, ClimateStudy, SoilTesting])

# 2) Modular farm design (single node)
design = DesignLayout

# 3) Sourcing materials and equipment concurrently
sourcing = StrictPartialOrder(nodes=[MaterialSourcing, EquipmentSetup])

# 4) Installation: Irrigation Install -> Sensor Deploy -> System Config (sequence)
installation = StrictPartialOrder(nodes=[IrrigationInstall, SensorDeploy, SystemConfig])
installation.order.add_edge(IrrigationInstall, SensorDeploy)
installation.order.add_edge(SensorDeploy, SystemConfig)

# 5) Staff training (single node)
training = StaffTraining

# 6) Crop Planting and Pest Control (pest control is ongoing maintenance, so no strict order implied; assume planting then pest control)
crop_and_pest = StrictPartialOrder(nodes=[CropPlanting, PestControl])
crop_and_pest.order.add_edge(CropPlanting, PestControl)

# 7) Data analysis: Data Capture -> Yield Review (sequence)
data_analysis = StrictPartialOrder(nodes=[DataCapture, YieldReview])
data_analysis.order.add_edge(DataCapture, YieldReview)

# 8) Community engagement (single node)
community = CommunityOutreach

# 9) Scaling and adaptation concurrently
scaling_adapt = StrictPartialOrder(nodes=[ScaleExpansion, PolicyAdapt])

# Connect all major steps partially ordered (sequential flow between main phases)
# site_analysis -> design -> sourcing -> installation -> training -> crop_and_pest -> data_analysis -> community -> scaling_adapt

nodes = [
    site_analysis, design, sourcing, installation, training, crop_and_pest, data_analysis, community, scaling_adapt
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(site_analysis, design)
root.order.add_edge(design, sourcing)
root.order.add_edge(sourcing, installation)
root.order.add_edge(installation, training)
root.order.add_edge(training, crop_and_pest)
root.order.add_edge(crop_and_pest, data_analysis)
root.order.add_edge(data_analysis, community)
root.order.add_edge(community, scaling_adapt)