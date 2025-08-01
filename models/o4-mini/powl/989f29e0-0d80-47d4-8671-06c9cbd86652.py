# Generated from: 989f29e0-0d80-47d4-8671-06c9cbd86652.json
# Description: This process outlines the comprehensive steps involved in launching a vertical farming business within an urban environment. It includes site selection under zoning constraints, modular infrastructure assembly, hydroponic system calibration, seed selection based on local climate adaptability, nutrient solution optimization, automated environmental monitoring setup, regulatory compliance verification, marketing campaign development targeting local consumers, staff recruitment with specialized agronomy skills, iterative yield testing, waste recycling integration, community engagement initiatives, and final launch event coordination. The process ensures sustainability, efficiency, and community integration in an atypical yet realistic urban agriculture venture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_selection   = Transition(label='Site Selection')
zoning_review    = Transition(label='Zoning Review')
modular_setup    = Transition(label='Modular Setup')
system_cal       = Transition(label='System Calibration')
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_install   = Transition(label='Sensor Install')
compliance_check = Transition(label='Compliance Check')
market_analysis  = Transition(label='Market Analysis')
hiring_staff     = Transition(label='Hiring Staff')
yield_testing    = Transition(label='Yield Testing')
waste_sorting    = Transition(label='Waste Sorting')
community_meet   = Transition(label='Community Meet')
feedback_loop    = Transition(label='Feedback Loop')
promo_launch     = Transition(label='Promo Launch')

# Define the loop’s repeating part: Waste Sorting -> Community Meet -> Feedback Loop
loop_body = StrictPartialOrder(nodes=[waste_sorting, community_meet, feedback_loop])
loop_body.order.add_edge(waste_sorting, community_meet)
loop_body.order.add_edge(community_meet, feedback_loop)

# Define the loop: Yield Testing, then optionally (loop_body then Yield Testing) repeatedly
iterative_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_testing, loop_body]
)

# Build the overall partial order (strict sequence of major phases + the loop + final launch)
root = StrictPartialOrder(nodes=[
    site_selection,
    zoning_review,
    modular_setup,
    system_cal,
    seed_selection,
    nutrient_mix,
    sensor_install,
    compliance_check,
    market_analysis,
    hiring_staff,
    iterative_loop,
    promo_launch
])

# Add dependencies to enforce the sequence
root.order.add_edge(site_selection,   zoning_review)
root.order.add_edge(zoning_review,    modular_setup)
root.order.add_edge(modular_setup,    system_cal)
root.order.add_edge(system_cal,       seed_selection)
root.order.add_edge(seed_selection,   nutrient_mix)
root.order.add_edge(nutrient_mix,     sensor_install)
root.order.add_edge(sensor_install,   compliance_check)
root.order.add_edge(compliance_check, market_analysis)
root.order.add_edge(market_analysis,  hiring_staff)
root.order.add_edge(hiring_staff,     iterative_loop)
root.order.add_edge(iterative_loop,   promo_launch)