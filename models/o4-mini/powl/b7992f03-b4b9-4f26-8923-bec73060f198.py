# Generated from: b7992f03-b4b9-4f26-8923-bec73060f198.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed commercial building. It begins with site assessment and structural analysis, followed by environmental control installation and nutrient cycling design. The process includes selecting appropriate crop varieties optimized for vertical growth, integrating IoT sensors for real-time monitoring, and implementing automated irrigation and lighting schedules. Staff training on system maintenance and crop management is conducted alongside regulatory compliance checks. The final stages involve pilot cultivation, yield analysis, and continuous optimization to ensure sustainable production and minimal resource consumption in a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define atomic activities
site_survey       = Transition(label='Site Survey')
structure_check   = Transition(label='Structure Check')
design_layout     = Transition(label='Design Layout')
install_hvac      = Transition(label='Install HVAC')
set_lighting      = Transition(label='Set Lighting')
deploy_sensors    = Transition(label='Deploy Sensors')
select_crops      = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
nutrient_setup    = Transition(label='Nutrient Setup')
staff_training    = Transition(label='Staff Training')
compliance_audit  = Transition(label='Compliance Audit')
pilot_cultivation = Transition(label='Pilot Cultivation')
data_monitoring   = Transition(label='Data Monitoring')
yield_analysis    = Transition(label='Yield Analysis')
process_review    = Transition(label='Process Review')

# Phase 1: Site assessment and structural analysis
phase1 = StrictPartialOrder(nodes=[site_survey, structure_check])
phase1.order.add_edge(site_survey, structure_check)

# Phase 2: Design layout, then environmental control installation and nutrient setup
phase2 = StrictPartialOrder(nodes=[design_layout, install_hvac, set_lighting, nutrient_setup])
phase2.order.add_edge(design_layout, install_hvac)
phase2.order.add_edge(install_hvac, set_lighting)
phase2.order.add_edge(design_layout, nutrient_setup)

# Phase 3: Crop selection, sensor deployment, irrigation configuration (concurrent)
phase3 = StrictPartialOrder(nodes=[select_crops, deploy_sensors, configure_irrigation])

# Phase 4: Staff training and compliance audit (concurrent)
phase4 = StrictPartialOrder(nodes=[staff_training, compliance_audit])

# Phase 5: Pilot cultivation & data monitoring -> yield analysis -> process review
phase5 = StrictPartialOrder(nodes=[pilot_cultivation, data_monitoring, yield_analysis, process_review])
phase5.order.add_edge(pilot_cultivation, yield_analysis)
phase5.order.add_edge(data_monitoring,   yield_analysis)
phase5.order.add_edge(yield_analysis,    process_review)

# Root model: sequential chaining of the five phases
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)