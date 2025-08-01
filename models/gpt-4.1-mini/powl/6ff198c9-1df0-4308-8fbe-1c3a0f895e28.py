# Generated from: 6ff198c9-1df0-4308-8fbe-1c3a0f895e28.json
# Description: This process outlines the establishment of a fully operational urban vertical farm within a metropolitan environment. It involves site evaluation, modular infrastructure assembly, environmental control calibration, automated nutrient delivery configuration, pest monitoring integration, crop selection based on microclimate data, real-time growth analytics setup, waste recycling incorporation, energy optimization, workforce training on smart farming tools, regulatory compliance checks, community engagement programs, and supply chain alignment for direct-to-consumer distribution, ensuring sustainability and high yield in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
module_build = Transition(label='Module Build')
env_control = Transition(label='Env Control')
nutrient_setup = Transition(label='Nutrient Setup')
pest_monitor = Transition(label='Pest Monitor')
crop_select = Transition(label='Crop Select')
growth_analytics = Transition(label='Growth Analytics')
waste_recycle = Transition(label='Waste Recycle')
energy_audit = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
supply_align = Transition(label='Supply Align')
market_launch = Transition(label='Market Launch')
data_review = Transition(label='Data Review')

# Create partial order reflecting a logical sequence (with concurrency where reasonable)
# Interpretation based on the description:
# 1. Site Survey
# 2. Module Build
# 3. Parallel Environmental control calibration, Nutrient setup, Pest monitoring integration
# 4. Crop select (based on microclimate data from env control)
# 5. Growth analytics and Waste recycle and Energy audit (concurrent)
# 6. Staff training and Compliance check (can run in parallel)
# 7. Community meet and Supply align (can run in parallel)
# 8. Data Review before Market Launch
# 9. Market Launch final

nodes = [
    site_survey,
    module_build,
    env_control,
    nutrient_setup,
    pest_monitor,
    crop_select,
    growth_analytics,
    waste_recycle,
    energy_audit,
    staff_training,
    compliance_check,
    community_meet,
    supply_align,
    data_review,
    market_launch
]

root = StrictPartialOrder(nodes=nodes)

order = root.order.add_edge
# Sequential edges
order(site_survey, module_build)
order(module_build, env_control)
order(module_build, nutrient_setup)
order(module_build, pest_monitor)

# Crop Select depends on Env Control (microclimate data)
order(env_control, crop_select)

# Growth Analytics, Waste Recycle, Energy Audit parallel after Crop Select and Nutrient Setup and Pest Monitor
order(crop_select, growth_analytics)
order(crop_select, waste_recycle)
order(crop_select, energy_audit)

order(nutrient_setup, growth_analytics)
order(nutrient_setup, waste_recycle)
order(nutrient_setup, energy_audit)

order(pest_monitor, growth_analytics)
order(pest_monitor, waste_recycle)
order(pest_monitor, energy_audit)

# Staff training and Compliance check after those three complete - concurrency allowed
order(growth_analytics, staff_training)
order(waste_recycle, staff_training)
order(energy_audit, staff_training)

order(growth_analytics, compliance_check)
order(waste_recycle, compliance_check)
order(energy_audit, compliance_check)

# Community meet and Supply align after Staff training and Compliance check - concurrency allowed
order(staff_training, community_meet)
order(compliance_check, community_meet)

order(staff_training, supply_align)
order(compliance_check, supply_align)

# Data Review after Community meet and Supply align (both must finish)
order(community_meet, data_review)
order(supply_align, data_review)

# Market launch after Data Review
order(data_review, market_launch)