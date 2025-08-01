# Generated from: 6ff198c9-1df0-4308-8fbe-1c3a0f895e28.json
# Description: This process outlines the establishment of a fully operational urban vertical farm within a metropolitan environment. It involves site evaluation, modular infrastructure assembly, environmental control calibration, automated nutrient delivery configuration, pest monitoring integration, crop selection based on microclimate data, real-time growth analytics setup, waste recycling incorporation, energy optimization, workforce training on smart farming tools, regulatory compliance checks, community engagement programs, and supply chain alignment for direct-to-consumer distribution, ensuring sustainability and high yield in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define the atomic activities
site_survey      = Transition(label='Site Survey')
module_build     = Transition(label='Module Build')
env_control      = Transition(label='Env Control')
nutrient_setup   = Transition(label='Nutrient Setup')
pest_monitor     = Transition(label='Pest Monitor')
crop_select      = Transition(label='Crop Select')
growth_analytics = Transition(label='Growth Analytics')
data_review      = Transition(label='Data Review')
waste_recycle    = Transition(label='Waste Recycle')
energy_audit     = Transition(label='Energy Audit')
staff_training   = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
community_meet   = Transition(label='Community Meet')
supply_align     = Transition(label='Supply Align')
market_launch    = Transition(label='Market Launch')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, module_build, env_control, nutrient_setup, pest_monitor,
    crop_select, growth_analytics, data_review,
    waste_recycle, energy_audit, staff_training,
    compliance_check, community_meet,
    supply_align, market_launch
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, module_build)

root.order.add_edge(module_build, env_control)
root.order.add_edge(module_build, nutrient_setup)
root.order.add_edge(module_build, pest_monitor)

root.order.add_edge(env_control, crop_select)
root.order.add_edge(nutrient_setup, crop_select)
root.order.add_edge(pest_monitor, crop_select)

root.order.add_edge(env_control, growth_analytics)
root.order.add_edge(nutrient_setup, growth_analytics)
root.order.add_edge(pest_monitor, growth_analytics)

root.order.add_edge(crop_select, data_review)
root.order.add_edge(growth_analytics, data_review)

root.order.add_edge(data_review, waste_recycle)
root.order.add_edge(data_review, energy_audit)
root.order.add_edge(data_review, staff_training)
root.order.add_edge(data_review, compliance_check)
root.order.add_edge(data_review, community_meet)

root.order.add_edge(data_review, supply_align)
root.order.add_edge(compliance_check, supply_align)
root.order.add_edge(community_meet, supply_align)

root.order.add_edge(supply_align, market_launch)