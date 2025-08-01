# Generated from: bdf44922-22c8-46e4-82a6-f7f0a9347bb3.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site evaluation, structural modifications for weight support, installation of hydroponic and aeroponic systems, integration of automated climate control, and implementation of AI-driven nutrient delivery. The process also includes staff training on system maintenance, daily crop monitoring, pest management with minimal chemicals, and data analysis for yield optimization. Finally, it covers packaging logistics and coordination with local markets to ensure fresh produce distribution, emphasizing sustainability and resource efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
structural_mod = Transition(label='Structural Mod')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
ai_integration = Transition(label='AI Integration')
nutrient_mix = Transition(label='Nutrient Mix')
crop_planting = Transition(label='Crop Planting')
staff_training = Transition(label='Staff Training')
sensor_setup = Transition(label='Sensor Setup')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
data_analysis = Transition(label='Data Analysis')
packaging_prep = Transition(label='Packaging Prep')
market_sync = Transition(label='Market Sync')

# High-level process partial orders and structure
# Phase 1: Building preparation (site_survey -> load_testing -> structural_mod)
phase1 = StrictPartialOrder(nodes=[site_survey, load_testing, structural_mod])
phase1.order.add_edge(site_survey, load_testing)
phase1.order.add_edge(load_testing, structural_mod)

# Phase 2: System installation (system_install -> climate_setup -> ai_integration)
phase2 = StrictPartialOrder(nodes=[system_install, climate_setup, ai_integration])
phase2.order.add_edge(system_install, climate_setup)
phase2.order.add_edge(climate_setup, ai_integration)

# Phase 3: Nutrient and planting setup (nutrient_mix -> crop_planting)
phase3 = StrictPartialOrder(nodes=[nutrient_mix, crop_planting])
phase3.order.add_edge(nutrient_mix, crop_planting)

# Phase 4: Staff training and sensor setup (staff_training and sensor_setup concurrent)
phase4 = StrictPartialOrder(nodes=[staff_training, sensor_setup])
# no ordering: concurrent

# Phase 5: Monitoring and pest control loop:
# loop node with body: (growth_monitor -> data_analysis) 
# and redo pest_control after each cycle, until exit
monitor_seq = StrictPartialOrder(nodes=[growth_monitor, data_analysis])
monitor_seq.order.add_edge(growth_monitor, data_analysis)

monitor_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    monitor_seq,
    pest_control
])

# Phase 6: Packaging and market syncing
phase6 = StrictPartialOrder(nodes=[packaging_prep, market_sync])
phase6.order.add_edge(packaging_prep, market_sync)

# Assemble phases in partial order - phases are sequential in order:
# phase1 -> phase2 -> phase3 -> phase4 -> monitor_pest_loop -> phase6
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, monitor_pest_loop, phase6])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, monitor_pest_loop)
root.order.add_edge(monitor_pest_loop, phase6)