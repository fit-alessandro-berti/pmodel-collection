# Generated from: d1f09626-ee36-41c4-a545-6b9e24255b42.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil testing, and microclimate evaluation to ensure optimal plant growth conditions. The process also covers selecting appropriate crop varieties, designing irrigation systems, installing renewable energy sources, and integrating pest management strategies. Community engagement and regulatory compliance are addressed to foster local support and legal operation. Finally, ongoing maintenance protocols and yield monitoring are implemented to maximize productivity and sustainability over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Sample = Transition(label='Soil Sample')
Climate_Check = Transition(label='Climate Check')

Crop_Select = Transition(label='Crop Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Energy_Setup = Transition(label='Energy Setup')
Pest_Control = Transition(label='Pest Control')

Permit_Obtain = Transition(label='Permit Obtain')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

Bed_Construction = Transition(label='Bed Construction')
Seed_Planting = Transition(label='Seed Planting')
Water_Schedule = Transition(label='Water Schedule')

Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Yield_Report = Transition(label='Yield Report')

# Phase 1: Assessments in parallel (Site Survey -> Load Test, Soil Sample, Climate Check all concurrent after Load Test)
# Order: Site Survey --> Load Test, then Load Test --> Soil Sample, Load Test --> Climate Check concurrent
phase1 = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Soil_Sample, Climate_Check])
phase1.order.add_edge(Site_Survey, Load_Test)
phase1.order.add_edge(Load_Test, Soil_Sample)
phase1.order.add_edge(Load_Test, Climate_Check)

# Phase 2: Selection and Design after all assessments (Crop Select then irrigation, energy, pest control in parallel)
selection = Transition(label='Crop Select')
irrigation = Transition(label='Irrigation Plan')
energy = Transition(label='Energy Setup')
pest = Transition(label='Pest Control')

phase2 = StrictPartialOrder(nodes=[Crop_Select, Irrigation_Plan, Energy_Setup, Pest_Control])
phase2.order.add_edge(Crop_Select, Irrigation_Plan)
phase2.order.add_edge(Crop_Select, Energy_Setup)
phase2.order.add_edge(Crop_Select, Pest_Control)

# Phase 3: Permits and community engagement in parallel after phase 2
phase3 = StrictPartialOrder(nodes=[Permit_Obtain, Stakeholder_Meet])
# no internal order, both concurrent

# Phase 4: Bed Construction and planting after phases 2 and 3 completed
phase4 = StrictPartialOrder(nodes=[Bed_Construction, Seed_Planting, Water_Schedule])
phase4.order.add_edge(Bed_Construction, Seed_Planting)
phase4.order.add_edge(Seed_Planting, Water_Schedule)

# Phase 5: Ongoing Maintenance and monitoring - loop of (Growth Monitor), then choice of (Harvest Plan or Waste Recycle), then Yield Report
# Model loop: execute Growth Monitor, then choose exit or execute Harvest Plan or Waste Recycle then Growth Monitor again repeated until exit, finally Yield Report
harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Waste_Recycle])
loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, harvest_choice])

phase5 = StrictPartialOrder(nodes=[loop_maintenance, Yield_Report])
phase5.order.add_edge(loop_maintenance, Yield_Report)

# Compose big partial order for entire process
# Overall order:
# phase1 --> phase2 --> phase3 (parallel with phase2, so phase3 after phase2) --> phase4 --> phase5

# So: phase1 before phase2
#     phase2 before phase3 and phase4 (phase3 concurrent with phase4 ? Not stated explicitly; assume phase3 before phase4 to reflect permit and engagement before construction)
#     phase3 before phase4
#     phase4 before phase5

root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5])

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)