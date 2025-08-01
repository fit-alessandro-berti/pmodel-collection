# Generated from: 36598120-a4a9-4fbc-90e5-28b3ed3c788e.json
# Description: This process outlines the complex steps involved in launching a vertical farming operation in an urban environment. It includes site selection considering zoning laws and sunlight access, modular infrastructure setup with hydroponic systems, climate control calibration, nutrient solution formulation, crop selection based on local demand, real-time environmental monitoring integration, pest management using bio-controls, workforce training on specialized equipment, marketing strategy focused on sustainability, distribution channel partnerships with local grocers, compliance with health and safety regulations, continuous yield optimization through data analytics, customer feedback loops for product improvement, and finally, scalability planning for future expansion into multiple urban sites.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
zoning_check     = Transition(label='Zoning Check')
infrastructure   = Transition(label='Infrastructure Setup')
calibration      = Transition(label='System Calibration')
nutrient_mix     = Transition(label='Nutrient Mix')
crop_selection   = Transition(label='Crop Selection')
enviro_monitor   = Transition(label='Enviro Monitoring')
pest_control     = Transition(label='Pest Control')
staff_training   = Transition(label='Staff Training')
marketing_plan   = Transition(label='Marketing Plan')
distributor_link = Transition(label='Distributor Link')
regulation_audit = Transition(label='Regulation Audit')
yield_analysis   = Transition(label='Yield Analysis')
feedback_review  = Transition(label='Feedback Review')
expansion_plan   = Transition(label='Expansion Plan')

# Build the feedback loop: perform yield analysis, then optionally review feedback and repeat
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_analysis, feedback_review]
)

# Assemble the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    zoning_check,
    infrastructure,
    calibration,
    nutrient_mix,
    crop_selection,
    enviro_monitor,
    pest_control,
    staff_training,
    marketing_plan,
    distributor_link,
    regulation_audit,
    feedback_loop,
    expansion_plan
])

# Define the control‐flow order
root.order.add_edge(site_survey,      zoning_check)
root.order.add_edge(zoning_check,     infrastructure)
root.order.add_edge(infrastructure,   calibration)
root.order.add_edge(calibration,      nutrient_mix)
root.order.add_edge(nutrient_mix,     crop_selection)
root.order.add_edge(crop_selection,   enviro_monitor)
root.order.add_edge(enviro_monitor,   pest_control)
root.order.add_edge(pest_control,     staff_training)
root.order.add_edge(staff_training,   marketing_plan)
root.order.add_edge(marketing_plan,   distributor_link)
root.order.add_edge(distributor_link, regulation_audit)
root.order.add_edge(regulation_audit, feedback_loop)
root.order.add_edge(feedback_loop,    expansion_plan)