# Generated from: 22c6027b-62f9-4e9c-a553-d2ec8b47ecbf.json
# Description: This process outlines an adaptive urban farming cycle designed to optimize crop yield within constrained city environments by integrating real-time environmental monitoring, dynamic resource allocation, and community engagement. Initially, sensor data is collected and analyzed to determine microclimate variations. Based on these insights, planting schedules and nutrient delivery are adjusted dynamically to suit specific crop requirements. Community volunteers participate in maintenance and harvesting, while waste products undergo bio-conversion to generate compost and energy. The entire system undergoes continuous feedback loops involving AI-driven predictions and manual expert interventions, ensuring sustainable production, minimal waste, and enhanced social cohesion in urban neighborhoods.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
SensorDeploy      = Transition(label='Sensor Deploy')
DataCapture       = Transition(label='Data Capture')
MicroclimateMap   = Transition(label='Microclimate Map')
AnalyzeTrends     = Transition(label='Analyze Trends')
AdjustSchedule    = Transition(label='Adjust Schedule')
AllocateNutrients = Transition(label='Allocate Nutrients')
PlantCrops        = Transition(label='Plant Crops')
VolunteerBrief    = Transition(label='Volunteer Brief')
MaintenanceRound  = Transition(label='Maintenance Round')
HarvestCrops      = Transition(label='Harvest Crops')
WasteCollect      = Transition(label='Waste Collect')
BioConvertWaste   = Transition(label='Bio-Convert Waste')
CompostApply      = Transition(label='Compost Apply')
EnergyStore       = Transition(label='Energy Store')
FeedbackReview    = Transition(label='Feedback Review')
ExpertConsult     = Transition(label='Expert Consult')

# Define the feedback loop: do FeedbackReview at least once, then optionally ExpertConsult then FeedbackReview etc.
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackReview, ExpertConsult])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    SensorDeploy, DataCapture, MicroclimateMap, AnalyzeTrends,
    AdjustSchedule, AllocateNutrients, PlantCrops,
    VolunteerBrief, MaintenanceRound, HarvestCrops,
    WasteCollect, BioConvertWaste, CompostApply, EnergyStore,
    loop_node
])

# Add the control‐flow edges
root.order.add_edge(SensorDeploy,      DataCapture)
root.order.add_edge(DataCapture,       MicroclimateMap)
root.order.add_edge(MicroclimateMap,   AnalyzeTrends)
root.order.add_edge(AnalyzeTrends,     AdjustSchedule)
root.order.add_edge(AnalyzeTrends,     AllocateNutrients)
root.order.add_edge(AdjustSchedule,    PlantCrops)
root.order.add_edge(AllocateNutrients, PlantCrops)
root.order.add_edge(PlantCrops,        VolunteerBrief)
root.order.add_edge(VolunteerBrief,    MaintenanceRound)
root.order.add_edge(MaintenanceRound,  HarvestCrops)
root.order.add_edge(HarvestCrops,      WasteCollect)
root.order.add_edge(WasteCollect,      BioConvertWaste)
root.order.add_edge(BioConvertWaste,   CompostApply)
root.order.add_edge(BioConvertWaste,   EnergyStore)
root.order.add_edge(CompostApply,      loop_node)
root.order.add_edge(EnergyStore,       loop_node)