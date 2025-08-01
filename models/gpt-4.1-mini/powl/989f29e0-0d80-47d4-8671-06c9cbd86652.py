# Generated from: 989f29e0-0d80-47d4-8671-06c9cbd86652.json
# Description: This process outlines the comprehensive steps involved in launching a vertical farming business within an urban environment. It includes site selection under zoning constraints, modular infrastructure assembly, hydroponic system calibration, seed selection based on local climate adaptability, nutrient solution optimization, automated environmental monitoring setup, regulatory compliance verification, marketing campaign development targeting local consumers, staff recruitment with specialized agronomy skills, iterative yield testing, waste recycling integration, community engagement initiatives, and final launch event coordination. The process ensures sustainability, efficiency, and community integration in an atypical yet realistic urban agriculture venture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_selection = Transition(label='Site Selection')
zoning_review = Transition(label='Zoning Review')
modular_setup = Transition(label='Modular Setup')
system_calibration = Transition(label='System Calibration')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
compliance_check = Transition(label='Compliance Check')
market_analysis = Transition(label='Market Analysis')
hiring_staff = Transition(label='Hiring Staff')
yield_testing = Transition(label='Yield Testing')
waste_sorting = Transition(label='Waste Sorting')
community_meet = Transition(label='Community Meet')
promo_launch = Transition(label='Promo Launch')
feedback_loop = Transition(label='Feedback Loop')

# Build the feedback loop as a LOOP operator:
# after 'Yield Testing' decide to either exit or perform 'Feedback Loop' then 'Yield Testing' again
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[yield_testing, feedback_loop])

# Partial order of the core activities, reflecting dependencies following the description:

# First phase: site selection and zoning review must happen before modular setup
# Modular setup before system calibration
# Seed selection and nutrient mix can occur concurrently after system calibration
# Sensor install depends on calibration
# Compliance check after sensor install
# Market analysis and hiring staff can be done in parallel after compliance check
# Then comes the feedback/testing loop
# Waste sorting and community meet after testing loop completes
# Promo launch after community meet

# Nodes in the PO:
nodes = [
    site_selection,
    zoning_review,
    modular_setup,
    system_calibration,
    seed_selection,
    nutrient_mix,
    sensor_install,
    compliance_check,
    market_analysis,
    hiring_staff,
    loop_feedback,
    waste_sorting,
    community_meet,
    promo_launch,
]

root = StrictPartialOrder(nodes=nodes)

# Edges:

# Site Selection and Zoning Review start; modular setup after both
root.order.add_edge(site_selection, modular_setup)
root.order.add_edge(zoning_review, modular_setup)

# Modular Setup before System Calibration
root.order.add_edge(modular_setup, system_calibration)

# System Calibration before Sensor Install
root.order.add_edge(system_calibration, sensor_install)

# Seed Selection and Nutrient Mix happen after System Calibration (concurrent)
root.order.add_edge(system_calibration, seed_selection)
root.order.add_edge(system_calibration, nutrient_mix)

# Sensor Install and Seed Selection, Nutrient Mix all must happen before Compliance Check
root.order.add_edge(sensor_install, compliance_check)
root.order.add_edge(seed_selection, compliance_check)
root.order.add_edge(nutrient_mix, compliance_check)

# Compliance Check before Market Analysis and Hiring Staff (concurrent)
root.order.add_edge(compliance_check, market_analysis)
root.order.add_edge(compliance_check, hiring_staff)

# Market Analysis and Hiring Staff before feedback loop (yield testing with feedback)
root.order.add_edge(market_analysis, loop_feedback)
root.order.add_edge(hiring_staff, loop_feedback)

# Feedback loop completes before Waste Sorting
root.order.add_edge(loop_feedback, waste_sorting)

# Waste Sorting before Community Meet
root.order.add_edge(waste_sorting, community_meet)

# Community Meet before Promo Launch
root.order.add_edge(community_meet, promo_launch)