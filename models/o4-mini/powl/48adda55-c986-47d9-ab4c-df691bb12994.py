# Generated from: 48adda55-c986-47d9-ab4c-df691bb12994.json
# Description: This process outlines the adaptive urban farming cycle designed for maximizing crop yield within limited city spaces while integrating sustainable practices and community involvement. It involves site analysis, modular bed assembly, soil enrichment through organic composting, real-time environmental monitoring with IoT devices, automated irrigation adjustment, pest control using biological agents, crop rotation planning based on historical data, community harvesting events, waste recycling into biochar, and continuous feedback loops to optimize growth parameters. The process also includes stakeholder coordination, urban policy compliance checks, and expansion feasibility studies to ensure scalability and environmental impact mitigation in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey       = Transition(label='Site Survey')
bed_setup         = Transition(label='Bed Setup')
soil_prep         = Transition(label='Soil Prep')
compost_mix       = Transition(label='Compost Mix')
sensor_install    = Transition(label='Sensor Install')
irrigation_adjust = Transition(label='Irrigation Adjust')
pest_control      = Transition(label='Pest Control')
crop_rotate       = Transition(label='Crop Rotate')
harvest_event     = Transition(label='Harvest Event')
waste_convert     = Transition(label='Waste Convert')
data_analyze      = Transition(label='Data Analyze')
feedback_loop     = Transition(label='Feedback Loop')
stakeholder_meet  = Transition(label='Stakeholder Meet')
policy_check      = Transition(label='Policy Check')
expansion_plan    = Transition(label='Expansion Plan')

# Define the core cycle body (one iteration of the adaptive farming cycle)
cycle_body = StrictPartialOrder(
    nodes=[
        irrigation_adjust,
        pest_control,
        crop_rotate,
        harvest_event,
        waste_convert,
        data_analyze
    ]
)
# Sequence within one cycle iteration
cycle_body.order.add_edge(irrigation_adjust, pest_control)
cycle_body.order.add_edge(pest_control, crop_rotate)
cycle_body.order.add_edge(crop_rotate, harvest_event)
cycle_body.order.add_edge(harvest_event, waste_convert)
cycle_body.order.add_edge(waste_convert, data_analyze)

# Define the loop: do one cycle, then either exit or invoke feedback and repeat
loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle_body, feedback_loop]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        bed_setup,
        soil_prep,
        compost_mix,
        sensor_install,
        stakeholder_meet,
        policy_check,
        loop_cycle,
        expansion_plan
    ]
)
# Initial setup sequence
root.order.add_edge(site_survey, bed_setup)
root.order.add_edge(bed_setup, soil_prep)
root.order.add_edge(soil_prep, compost_mix)
root.order.add_edge(compost_mix, sensor_install)

# After sensor install, coordinate stakeholders, policy check, and start the cycle concurrently
root.order.add_edge(sensor_install, stakeholder_meet)
root.order.add_edge(sensor_install, policy_check)
root.order.add_edge(sensor_install, loop_cycle)

# All three must complete before expansion planning
root.order.add_edge(stakeholder_meet, expansion_plan)
root.order.add_edge(policy_check, expansion_plan)
root.order.add_edge(loop_cycle, expansion_plan)