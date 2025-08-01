# Generated from: f0aa953f-c018-4ac7-b91e-620bd8c0007a.json
# Description: This process involves establishing an urban vertical farm within a repurposed high-rise building. It includes site analysis, modular system design, environmental control calibration, nutrient solution formulation, seedling preparation, and automated monitoring integration. The setup ensures sustainable crop production through resource recycling, energy optimization, and waste management while complying with urban agricultural regulations. The process culminates in operational validation and community engagement to promote local food sourcing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SystemAssembly = Transition(label='System Assembly')
ClimateSetup = Transition(label='Climate Setup')
LightCalibration = Transition(label='Light Calibration')
SeedSelection = Transition(label='Seed Selection')
SeedlingPrep = Transition(label='Seedling Prep')
NutrientMix = Transition(label='Nutrient Mix')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorInstall = Transition(label='Sensor Install')
DataIntegration = Transition(label='Data Integration')
WasteRouting = Transition(label='Waste Routing')
EnergyAudit = Transition(label='Energy Audit')
RegulationCheck = Transition(label='Regulation Check')
OperationalTest = Transition(label='Operational Test')
CommunityOutreach = Transition(label='Community Outreach')

# Define partial orders for some concurrent tasks inside the process

# Modular system design after Site Survey
DesignPO = StrictPartialOrder(nodes=[DesignLayout, SystemAssembly])
DesignPO.order.add_edge(DesignLayout, SystemAssembly)

# Environmental controls after system assembly
EnvControlPO = StrictPartialOrder(nodes=[ClimateSetup, LightCalibration])
# These two are concurrent, no order edges

# Nutrient solution and seedling prep after environmental controls
NutSeedPO = StrictPartialOrder(nodes=[NutrientMix, SeedSelection, SeedlingPrep])
NutSeedPO.order.add_edge(SeedSelection, SeedlingPrep)  # Seedling Prep after Seed Selection
# NutrientMix can be concurrent with SeedSelection and SeedlingPrep

# Irrigation setup and sensor install concurrent after nutrient and seedling
IrrSensorPO = StrictPartialOrder(nodes=[IrrigationSetup, SensorInstall])
# concurrent, no edges

# Data integration after sensor install
# We will order SensorInstall -> DataIntegration

# Waste routing and energy audit concurrent after data integration
WasteEnergyPO = StrictPartialOrder(nodes=[WasteRouting, EnergyAudit])
# concurrent, no edges

# Regulation check concurrent with WasteRouting and EnergyAudit
# So combine WasteEnergyPO and RegulationCheck in partial order with all three nodes:
RegulationWasteEnergyPO = StrictPartialOrder(nodes=[WasteRouting, EnergyAudit, RegulationCheck])
# All three concurrent (no edges)

# Final validation and community outreach sequential after regulation check
FinalPO = StrictPartialOrder(nodes=[OperationalTest, CommunityOutreach])
FinalPO.order.add_edge(OperationalTest, CommunityOutreach)

# Now, connect all partial orders in the correct order

# Site Survey -> Design Layout
# Design Layout -> System Assembly (inside DesignPO)
# System Assembly -> Environmental Controls (ClimateSetup and LightCalibration)
# Environmental Controls -> Nutrient and Seedling Prep
# Nutrient and Seedling Prep -> IrrigationSetup and SensorInstall
# SensorInstall -> DataIntegration
# DataIntegration -> Waste, Energy, Regulation checks concurrent
# RegulationCheck and others -> OperationalTest
# OperationalTest -> CommunityOutreach

# Let's define top level nodes:
# site survey
# designPO (design layout -> system assembly)
# envControlPO (climate setup, light calibration concurrent)
# nutSeedPO (nutrient mix, seed selection -> seedling prep)
# irrSensorPO (irrigation setup, sensor install concurrent)
# dataIntegration
# regulationWasteEnergyPO (waste routing, energy audit, regulation check concurrent)
# finalPO (operational test -> community outreach)

# Construct top-level partial order nodes list
top_nodes = [
    SiteSurvey,
    DesignPO,
    SystemAssembly,   # SystemAssembly already in DesignPO, so no need separately
    EnvControlPO,
    NutSeedPO,
    IrrigationSetup,
    SensorInstall,
    DataIntegration,
    RegulationWasteEnergyPO,
    FinalPO,
]

# Wait: SystemAssembly is inside DesignPO already so do not put it in top-level nodes separately.

# The concurrency between IrrigationSetup and SensorInstall is represented by irrSensorPO,
# we want to have a PO with these two, not separated.

irrSensorPO = IrrSensorPO  # Reuse for clarity

top_nodes = [
    SiteSurvey,
    DesignPO,
    EnvControlPO,
    NutSeedPO,
    irrSensorPO,
    DataIntegration,
    RegulationWasteEnergyPO,
    FinalPO,
]

root = StrictPartialOrder(nodes=top_nodes)

# Add edges between top-level nodes according to described order:

# SiteSurvey --> DesignPO
root.order.add_edge(SiteSurvey, DesignPO)

# Last activity inside DesignPO is SystemAssembly.
# We must express that DesignPO finishes before EnvControlPO starts.
# Given SystemAssembly is last in DesignPO, just link DesignPO --> EnvControlPO 
root.order.add_edge(DesignPO, EnvControlPO)

# EnvControlPO --> NutSeedPO
root.order.add_edge(EnvControlPO, NutSeedPO)

# NutSeedPO --> irrSensorPO
root.order.add_edge(NutSeedPO, irrSensorPO)

# irrSensorPO nodes = IrrigationSetup, SensorInstall
# After SensorInstall comes DataIntegration (DataIntegration waits SensorInstall),
# IrrigationSetup and SensorInstall concurrent, so must ensure DataIntegration after SensorInstall and possibly after IrrigationSetup?
# Problem description specifies SensorInstall --> DataIntegration specifically.

root.order.add_edge(irrSensorPO, DataIntegration)

# Probably DataIntegration should wait for SensorInstall but not IrrigationSetup necessarily;
# can't express partial order inside irrSensorPO beyond nodes; we can just ensure DataIntegration after irrSensorPO.

# DataIntegration --> RegulationWasteEnergyPO
root.order.add_edge(DataIntegration, RegulationWasteEnergyPO)

# RegulationWasteEnergyPO --> FinalPO (OperationalTest, CommunityOutreach)
root.order.add_edge(RegulationWasteEnergyPO, FinalPO)

# Done.

# Make sure to add internal edges in partial orders defined earlier

# DesignPO already has DesignLayout->SystemAssembly

# EnvControlPO has no edges (concurrent)

# NutSeedPO has SeedSelection->SeedlingPrep

# IrrSensorPO no edges (concurrent)

# RegulationWasteEnergyPO no edges (concurrent)

# FinalPO has OperationalTest->CommunityOutreach

# That's the complete model.

# Assign root variable for output