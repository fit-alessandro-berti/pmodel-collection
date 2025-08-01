# Generated from: f71ac55f-f1b1-4593-8db6-fdf046f64277.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, climate control integration, nutrient delivery setup, automated monitoring installation, and crop scheduling. The workflow includes securing permits, sourcing sustainable materials, integrating renewable energy, and establishing waste recycling protocols. The process ensures efficient space utilization, maximizes crop yield, and supports community engagement through educational tours and local partnerships, fostering urban agriculture innovation and sustainability in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey      = Transition(label='Site Survey')
PermitReview    = Transition(label='Permit Review')
DesignLayout    = Transition(label='Design Layout')
SystemAssembly  = Transition(label='System Assembly')
ClimateSetup    = Transition(label='Climate Setup')
NutrientPrep    = Transition(label='Nutrient Prep')
IrrigationTest  = Transition(label='Irrigation Test')
LightingConfig  = Transition(label='Lighting Config')
EnergyInstall   = Transition(label='Energy Install')
SensorSetup     = Transition(label='Sensor Setup')
AutomationDeploy= Transition(label='Automation Deploy')
CropSeeding     = Transition(label='Crop Seeding')
WastePlan       = Transition(label='Waste Plan')
StaffTraining   = Transition(label='Staff Training')
CommunityOutreach = Transition(label='Community Outreach')
YieldMonitor    = Transition(label='Yield Monitor')
MaintenanceCheck= Transition(label='Maintenance Check')

# Loop for ongoing monitoring and maintenance
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[YieldMonitor, MaintenanceCheck]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, PermitReview,
    DesignLayout, SystemAssembly,
    ClimateSetup, NutrientPrep,
    IrrigationTest, LightingConfig, EnergyInstall, SensorSetup,
    AutomationDeploy, CropSeeding,
    WastePlan, StaffTraining, CommunityOutreach,
    monitoring_loop
])

# Add sequencing dependencies
o = root.order
o.add_edge(SiteSurvey,      PermitReview)
o.add_edge(PermitReview,    DesignLayout)
o.add_edge(DesignLayout,    SystemAssembly)
o.add_edge(SystemAssembly,  ClimateSetup)
o.add_edge(ClimateSetup,    NutrientPrep)

# After nutrient prep, tests and installs can proceed in parallel
for nxt in [IrrigationTest, LightingConfig, EnergyInstall, SensorSetup]:
    o.add_edge(NutrientPrep, nxt)

# All tests/installs must finish before automation deployment
for prev in [IrrigationTest, LightingConfig, EnergyInstall, SensorSetup]:
    o.add_edge(prev, AutomationDeploy)

o.add_edge(AutomationDeploy, CropSeeding)

# After seeding, plan waste, train staff, and do outreach in parallel
for nxt in [WastePlan, StaffTraining, CommunityOutreach]:
    o.add_edge(CropSeeding, nxt)

# After all of those, enter the monitoring & maintenance loop
for prev in [WastePlan, StaffTraining, CommunityOutreach]:
    o.add_edge(prev, monitoring_loop)