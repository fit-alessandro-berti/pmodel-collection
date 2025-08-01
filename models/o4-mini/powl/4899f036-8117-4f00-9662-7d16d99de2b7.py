# Generated from: 4899f036-8117-4f00-9662-7d16d99de2b7.json
# Description: This process details the complex orchestration required to establish a sustainable urban rooftop farm in a densely populated city. It involves evaluating structural integrity, securing permits, sourcing organic soil and seeds, designing efficient irrigation systems, integrating renewable energy solutions, coordinating with local suppliers, managing seasonal crop rotation, and implementing pest control without chemicals. Continuous monitoring of plant health and environmental data is essential. Additionally, the process requires community engagement initiatives and educational workshops to promote urban agriculture awareness and participation. The entire workflow balances regulatory compliance, environmental sustainability, and economic viability, ensuring the rooftop farm thrives as a model of urban green innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
siteSurvey      = Transition(label='Site Survey')
loadTesting     = Transition(label='Load Testing')
permitFiling    = Transition(label='Permit Filing')
soilSourcing    = Transition(label='Soil Sourcing')
seedSelection   = Transition(label='Seed Selection')
irrigationPlan  = Transition(label='Irrigation Plan')
energySetup     = Transition(label='Energy Setup')
supplierVetting = Transition(label='Supplier Vetting')
cropRotation    = Transition(label='Crop Rotation')
pestControl     = Transition(label='Pest Control')
healthMonitor   = Transition(label='Health Monitor')
dataLogging     = Transition(label='Data Logging')
communityMeet   = Transition(label='Community Meet')
workshopPlan    = Transition(label='Workshop Plan')
complianceCheck = Transition(label='Compliance Check')
harvestPrep     = Transition(label='Harvest Prep')
wasteManage     = Transition(label='Waste Manage')

# Define loops
# Seasonal loop: rotate crops, then pest control, repeat
seasonalLoop   = OperatorPOWL(operator=Operator.LOOP, children=[cropRotation, pestControl])
# Continuous monitoring loop: health monitoring and data logging
monitoringLoop = OperatorPOWL(operator=Operator.LOOP, children=[healthMonitor, dataLogging])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    siteSurvey, loadTesting, permitFiling,
    soilSourcing, seedSelection, supplierVetting,
    irrigationPlan, energySetup,
    seasonalLoop, monitoringLoop,
    communityMeet, workshopPlan,
    complianceCheck, harvestPrep, wasteManage
])

# Core sequence: site survey -> load testing -> permit filing
root.order.add_edge(siteSurvey, loadTesting)
root.order.add_edge(loadTesting, permitFiling)

# After permits, kick off parallel setup tasks and community initiatives
for t in [soilSourcing, seedSelection, supplierVetting, irrigationPlan, energySetup,
          communityMeet, workshopPlan]:
    root.order.add_edge(permitFiling, t)

# Once all setup tasks complete, start loops
for setup in [soilSourcing, seedSelection, supplierVetting, irrigationPlan, energySetup]:
    root.order.add_edge(setup, seasonalLoop)
    root.order.add_edge(setup, monitoringLoop)

# Community initiatives feed into compliance check as well
root.order.add_edge(communityMeet,   complianceCheck)
root.order.add_edge(workshopPlan,    complianceCheck)

# Both loops must finish (exit) before compliance check
root.order.add_edge(seasonalLoop,    complianceCheck)
root.order.add_edge(monitoringLoop,  complianceCheck)

# Final harvest and waste management
root.order.add_edge(complianceCheck, harvestPrep)
root.order.add_edge(harvestPrep,     wasteManage)