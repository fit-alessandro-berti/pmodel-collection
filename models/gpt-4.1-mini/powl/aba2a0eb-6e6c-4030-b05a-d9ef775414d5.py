# Generated from: aba2a0eb-6e6c-4030-b05a-d9ef775414d5.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a constrained city environment. It starts with site assessment and zoning compliance, followed by modular infrastructure design and procurement. The process continues with climate system integration, hydroponic nutrient programming, and automated lighting calibration. Concurrently, staff training on biosecurity and crop monitoring is conducted. Post-installation, the process includes iterative testing of growth cycles, data analytics for yield optimization, pest control protocols, and community engagement for local distribution. Finally, the operation undergoes sustainability auditing and scalability planning to ensure long-term viability within urban agriculture paradigms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
design_layout = Transition(label='Design Layout')
material_order = Transition(label='Material Order')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
light_calibrate = Transition(label='Light Calibrate')
staff_training = Transition(label='Staff Training')
biosecurity_audit = Transition(label='Biosecurity Audit')
growth_testing = Transition(label='Growth Testing')
data_analysis = Transition(label='Data Analysis')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
sustain_audit = Transition(label='Sustain Audit')
scale_planning = Transition(label='Scale Planning')

# Step 1: Site Survey and Zoning Check sequential (site assessment + zoning compliance)
step1 = StrictPartialOrder(nodes=[site_survey, zoning_check])
step1.order.add_edge(site_survey, zoning_check)

# Step 2: Design Layout and Material Order sequential (modular infrastructure design + procurement)
step2 = StrictPartialOrder(nodes=[design_layout, material_order])
step2.order.add_edge(design_layout, material_order)

# Step 3: Climate Setup, Nutrient Mix, Light Calibrate sequential (climate system integration, hydroponic nutrient programming, lighting calibration)
step3 = StrictPartialOrder(nodes=[climate_setup, nutrient_mix, light_calibrate])
step3.order.add_edge(climate_setup, nutrient_mix)
step3.order.add_edge(nutrient_mix, light_calibrate)

# Step 4: Staff Training and Biosecurity Audit concurrent (staff training on biosecurity and crop monitoring - biosecurity audit modeled as audit of biosecurity)
step4 = StrictPartialOrder(nodes=[staff_training, biosecurity_audit])
# no order to model concurrency

# Step 5: Growth Testing looped with Data Analysis, Pest Control, Community Meet
# The description says iterative testing post-installation includes growth testing, data analytics, pest control, community engagement
# Model a loop with Growth Testing as the "body" and the choice to exit or do (Data Analysis, Pest Control, Community Meet) before next Growth Testing
post_installation_processing = StrictPartialOrder(
    nodes=[data_analysis, pest_control, community_meet]
)
# these three parallel as no order specified explicitly
# create a PO for concurrency
# no edges added

loop_body = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        SilentTransition(), 
        post_installation_processing
    ]
)
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_testing, loop_body]
)

# Step 6: Final step sequentially: Sustain Audit -> Scale Planning
final_steps = StrictPartialOrder(nodes=[sustain_audit, scale_planning])
final_steps.order.add_edge(sustain_audit, scale_planning)

# Now combine all steps sequentially:
# steps order:
# step1 -> step2 -> step3 -> step4 concurrent with step3? The text says "Concurrently, staff training on biosecurity and crop monitoring is conducted."
# So Staff Training and Biosecurity Audit run concurrently with step3 (climate setup, nutrient mix, light calibrate)
# So step3 and step4 run concurrently
# Then after that comes the loop, then final steps

# Combine step3 and step4 in parallel (no order)
step3_4 = StrictPartialOrder(
    nodes=[step3, step4]
)
# no edge between them for concurrency

# Combine all major sequential steps together:

root = StrictPartialOrder(
    nodes=[step1, step2, step3_4, loop, final_steps]
)
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3_4)
root.order.add_edge(step3_4, loop)
root.order.add_edge(loop, final_steps)