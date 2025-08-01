# Generated from: 3e8eb1d4-f5f5-41c7-841e-42282a8bb617.json
# Description: This process outlines the complex steps required to establish a sustainable urban beekeeping operation within city limits. It involves selecting appropriate rooftop locations, obtaining legal permits, designing hive layouts that comply with local regulations, sourcing resilient bee colonies, implementing pollen monitoring systems, training staff in urban-specific hive management, scheduling regular health inspections, coordinating with local environmental groups, managing urban foraging resources, setting up honey extraction and packaging facilities on-site, integrating pest control measures that are safe for dense populations, marketing locally produced honey through community channels, and continuously adapting practices to evolving urban ecosystems and climate conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
HiveDesign = Transition(label='Hive Design')
ColonySourcing = Transition(label='Colony Sourcing')
PollenTesting = Transition(label='Pollen Testing')
StaffTraining = Transition(label='Staff Training')
HealthCheck = Transition(label='Health Check')
EnviroLiaison = Transition(label='Enviro Liaison')
ForageMapping = Transition(label='Forage Mapping')
ExtractionSetup = Transition(label='Extraction Setup')
PestControl = Transition(label='Pest Control')
HoneyPacking = Transition(label='Honey Packing')
LocalMarketing = Transition(label='Local Marketing')
ClimateAdapt = Transition(label='Climate Adapt')
DataLogging = Transition(label='Data Logging')

# Based on the description:
# 1) Site Survey
# 2) Permit Filing
# 3) Hive Design (requires compliance with regulations)
# 4) Colony Sourcing
# 5) Pollen Testing (monitoring system)
# 6) Staff Training
# 7) Health Check (regular inspections)
# 8) Enviro Liaison (coordination w/ groups)
# 9) Forage Mapping (manage resources)
# 10) Extraction Setup (on-site honey extraction/packaging)
# 11) Pest Control (safe pest control)
# 12) Honey Packing
# 13) Local Marketing
# 14) Climate Adapt and Data Logging (continuous adaptation)

# Logical structuring:
# Early steps are sequential: Site Survey -> Permit Filing -> Hive Design
# Colony Sourcing follows Hive Design (need design to know what to source)
# Pollen Testing and Staff Training can be concurrent after sourcing
# Health Check comes after staff is trained (they do inspections)
# Enviro Liaison and Forage Mapping are related and can be concurrent after Health Check
# Extraction Setup and Pest Control can start after Forage Mapping and Enviro Liaison
# Honey Packing and Local Marketing follow Extraction Setup and Pest Control
# Lastly, Climate Adapt and Data Logging run continuously and are concurrent - loop them

# Create partial orders inside a loop for continuous adaptation (ClimateAdapt and DataLogging)
adapt_loop = OperatorPOWL(operator=Operator.LOOP, children=[ClimateAdapt, DataLogging])

# Concurrent activities extracted as partial orders:
# Stage 1 (initial sequential): SiteSurvey -> PermitFiling -> HiveDesign -> ColonySourcing
stage1 = StrictPartialOrder(nodes=[SiteSurvey, PermitFiling, HiveDesign, ColonySourcing])
stage1.order.add_edge(SiteSurvey, PermitFiling)
stage1.order.add_edge(PermitFiling, HiveDesign)
stage1.order.add_edge(HiveDesign, ColonySourcing)

# Stage 2: PollenTesting and StaffTraining concurrent after ColonySourcing
stage2 = StrictPartialOrder(nodes=[PollenTesting, StaffTraining])
# No order edges => concurrent

# Stage 3: HealthCheck after StaffTraining
stage3 = StrictPartialOrder(nodes=[HealthCheck])
# Will add order edge from StaffTraining to HealthCheck via overall PO

# Stage 4: EnviroLiaison and ForageMapping concurrent after HealthCheck
stage4 = StrictPartialOrder(nodes=[EnviroLiaison, ForageMapping])

# Stage 5: ExtractionSetup and PestControl concurrent after EnviroLiaison and ForageMapping
stage5 = StrictPartialOrder(nodes=[ExtractionSetup, PestControl])

# Stage 6: HoneyPacking and LocalMarketing concurrent after ExtractionSetup and PestControl
stage6 = StrictPartialOrder(nodes=[HoneyPacking, LocalMarketing])

# Compose overall partial order combining all stages in sequence with dependencies added

nodes = [
    stage1,    # initial sequence block
    stage2,    # concurrent pollen testing & staff training
    stage3,    # health check
    stage4,    # enviro liaison & forage mapping
    stage5,    # extraction setup & pest control
    stage6,    # honey packing & local marketing
    adapt_loop # adaptation loop (continuous)
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to enforce order between stages
root.order.add_edge(stage1, stage2) # ColonySourcing done before PollenTesting+StaffTraining
# To enforce fine-grained order between ColonySourcing and stage2:
# Because stage1 ends with ColonySourcing, it must come before PollenTesting and StaffTraining
# (which are concurrent in stage2)
# Stage 3 (HealthCheck) after StaffTraining
root.order.add_edge(stage2, stage3)
# Stage 4 after HealthCheck
root.order.add_edge(stage3, stage4)
# Stage 5 after EnviroLiaison and ForageMapping
root.order.add_edge(stage4, stage5)
# Stage 6 after ExtractionSetup and PestControl
root.order.add_edge(stage5, stage6)
# The adaptation loop can run concurrently from the end, but logically it's continuous ongoing after main workflow
# We put it concurrent, but to ensure it starts after stage6, connect stage6 --> adapt_loop
root.order.add_edge(stage6, adapt_loop)