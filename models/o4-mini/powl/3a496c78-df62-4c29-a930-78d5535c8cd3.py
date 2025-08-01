# Generated from: 3a496c78-df62-4c29-a930-78d5535c8cd3.json
# Description: This process details the establishment of an urban vertical farming system within a repurposed commercial building. It involves site evaluation, structural modifications, installation of hydroponic systems, climate control setup, automated nutrient delivery configuration, and integration of AI-driven monitoring tools. Additionally, it includes staff training, regulatory compliance verification, crop planning, and marketing strategy development to ensure sustainable and efficient production of fresh produce in limited urban spaces while minimizing environmental impact and maximizing yield.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
struct_eval      = Transition(label='Structural Eval')
permit_obtain    = Transition(label='Permit Obtain')
system_design    = Transition(label='System Design')
hydroponic_install = Transition(label='Hydroponic Install')
climate_setup    = Transition(label='Climate Setup')
lighting_config  = Transition(label='Lighting Config')
nutrient_setup   = Transition(label='Nutrient Setup')
automation_setup = Transition(label='Automation Setup')
ai_integration   = Transition(label='AI Integration')
staff_training   = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
crop_planning    = Transition(label='Crop Planning')
yield_testing    = Transition(label='Yield Testing')
market_launch    = Transition(label='Market Launch')

# Loop for iterative crop planning & yield testing
loop_crop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_planning, yield_testing]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, struct_eval, permit_obtain, system_design,
    hydroponic_install, climate_setup, lighting_config,
    nutrient_setup, automation_setup, ai_integration,
    staff_training, compliance_check, loop_crop, market_launch
])

# Define sequencing
root.order.add_edge(site_survey, struct_eval)
root.order.add_edge(struct_eval, permit_obtain)
root.order.add_edge(permit_obtain, system_design)

# After design, all installation/config steps can proceed in parallel
for install in [hydroponic_install, climate_setup, lighting_config, nutrient_setup, automation_setup]:
    root.order.add_edge(system_design, install)

# All installations/configurations precede AI integration
for install in [hydroponic_install, climate_setup, lighting_config, nutrient_setup, automation_setup]:
    root.order.add_edge(install, ai_integration)

# AI integration precedes staff training and compliance check
root.order.add_edge(ai_integration, staff_training)
root.order.add_edge(ai_integration, compliance_check)

# Training & compliance must finish before the crop planning loop
root.order.add_edge(staff_training, loop_crop)
root.order.add_edge(compliance_check, loop_crop)

# Once the crop planning loop completes, proceed to market launch
root.order.add_edge(loop_crop, market_launch)