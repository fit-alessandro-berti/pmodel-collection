# Generated from: d9a71339-ce63-4af5-967e-8e55130c721e.json
# Description: This process outlines the establishment of an urban vertical farm integrating hydroponic systems and AI-driven environmental controls. Starting from site analysis and structural assessment, it involves modular unit installation, nutrient solution formulation, sensor calibration, and AI model training for growth optimization. The workflow includes ongoing data acquisition, predictive maintenance scheduling, pest detection via image recognition, and automated harvesting coordination. Final stages focus on yield quality assessment, packaging automation, and distribution logistics planning, ensuring sustainable urban agriculture with minimal resource consumption and maximized crop output.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
ModularInstall = Transition(label='Modular Install')
HydroponicSetup = Transition(label='Hydroponic Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AITraining = Transition(label='AI Training')
DataCapture = Transition(label='Data Capture')
MaintenancePlan = Transition(label='Maintenance Plan')
PestScan = Transition(label='Pest Scan')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestSync = Transition(label='Harvest Sync')
QualityTest = Transition(label='Quality Test')
PackagePrep = Transition(label='Package Prep')
LogisticsPlan = Transition(label='Logistics Plan')

# Prepare modular installation sequence
modular_and_setup = StrictPartialOrder(nodes=[ModularInstall, HydroponicSetup])
modular_and_setup.order.add_edge(ModularInstall, HydroponicSetup)

# Prepare nutrient mix and sensor setup parallel
nutrients_and_sensor = StrictPartialOrder(nodes=[NutrientMix, SensorSetup])
# no order between NutrientMix and SensorSetup – parallel

# AI training after sensor setup and nutrient mix (both)
ai_training_prep = StrictPartialOrder(
    nodes=[nutrients_and_sensor, AITraining]
)
ai_training_prep.order.add_edge(nutrients_and_sensor, AITraining)

# Build initial site analysis and structural check sequence
site_struct = StrictPartialOrder(nodes=[SiteSurvey, StructuralCheck])
site_struct.order.add_edge(SiteSurvey, StructuralCheck)

# Overall initialization sequence: site_struct -> modular_and_setup -> ai_training_prep
init_seq = StrictPartialOrder(
    nodes=[site_struct, modular_and_setup, ai_training_prep]
)
init_seq.order.add_edge(site_struct, modular_and_setup)
init_seq.order.add_edge(modular_and_setup, ai_training_prep)

# Loop body: DataCapture, then choice between MaintenancePlan or PestScan, then GrowthMonitor
maintenance_or_pest = OperatorPOWL(operator=Operator.XOR, children=[MaintenancePlan, PestScan])
loop_body = StrictPartialOrder(
    nodes=[DataCapture, maintenance_or_pest, GrowthMonitor]
)
loop_body.order.add_edge(DataCapture, maintenance_or_pest)
loop_body.order.add_edge(maintenance_or_pest, GrowthMonitor)

# Loop: execute loop_body repeatedly until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, GrowthMonitor])

# After loop ends: HarvestSync, QualityTest, PackagePrep, LogisticsPlan in sequence
post_loop_seq = StrictPartialOrder(
    nodes=[HarvestSync, QualityTest, PackagePrep, LogisticsPlan]
)
post_loop_seq.order.add_edge(HarvestSync, QualityTest)
post_loop_seq.order.add_edge(QualityTest, PackagePrep)
post_loop_seq.order.add_edge(PackagePrep, LogisticsPlan)

# Combine init_seq, loop, post_loop_seq
root = StrictPartialOrder(
    nodes=[init_seq, loop, post_loop_seq]
)
root.order.add_edge(init_seq, loop)
root.order.add_edge(loop, post_loop_seq)