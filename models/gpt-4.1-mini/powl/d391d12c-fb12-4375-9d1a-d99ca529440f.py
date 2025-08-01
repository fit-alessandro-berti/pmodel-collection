# Generated from: d391d12c-fb12-4375-9d1a-d99ca529440f.json
# Description: This process outlines the steps involved in establishing a bespoke urban farming system tailored to small rooftop spaces in densely populated cities. It includes site analysis, microclimate assessment, soil-less media selection, modular hydroponic design, nutrient cycling optimization, and automated environmental controls. The workflow integrates stakeholder coordination, regulatory compliance checks, and community engagement programs to ensure sustainability and scalability. Continuous monitoring and adaptive management strategies are embedded to respond to seasonal variations and urban pollution factors, enabling year-round crop production with minimal resource waste while fostering local food security and green urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Build partial orders for initial analysis: Site Survey -> Climate Check -> Soil Testing -> Media Select
init_analysis = StrictPartialOrder(
    nodes=[site_survey, climate_check, soil_testing, media_select])
init_analysis.order.add_edge(site_survey, climate_check)
init_analysis.order.add_edge(climate_check, soil_testing)
init_analysis.order.add_edge(soil_testing, media_select)

# Design & Setup: Design Layout -> Hydro Setup -> Nutrient Mix -> Sensor Install
design_setup = StrictPartialOrder(
    nodes=[design_layout, hydro_setup, nutrient_mix, sensor_install])
design_setup.order.add_edge(design_layout, hydro_setup)
design_setup.order.add_edge(hydro_setup, nutrient_mix)
design_setup.order.add_edge(nutrient_mix, sensor_install)

# Regulatory & Stakeholder: Regulation Review -> Permit Apply and Stakeholder Meet -> Community Train in parallel with the two chains; Stakeholder Meet concur with permit apply steps
regulation_permit = StrictPartialOrder(
    nodes=[regulation_review, permit_apply])
regulation_permit.order.add_edge(regulation_review, permit_apply)
stakeholder_training = StrictPartialOrder(
    nodes=[stakeholder_meet, community_train])
stakeholder_training.order.add_edge(stakeholder_meet, community_train)

# Merge regulatory and stakeholder branches with concurrency
reg_stakeholder = StrictPartialOrder(
    nodes=[regulation_permit, stakeholder_training])
# no edges between regulation_permit and stakeholder_training mean concurrency

# Planting and continuous management loop:
# Plant Seed -> loop(Monitor Growth and Adjust Controls) -> Harvest Plan -> Waste Recycle -> Feedback Loop
# The loop contains Monitor Growth -> Adjust Controls (simple sequence)
monitor_adjust = StrictPartialOrder(
    nodes=[monitor_growth, adjust_controls])
monitor_adjust.order.add_edge(monitor_growth, adjust_controls)

loop_monitor_adjust = OperatorPOWL(
    operator=Operator.LOOP,
    children=[plant_seed, monitor_adjust]
)

post_harvest = StrictPartialOrder(
    nodes=[harvest_plan, waste_recycle, feedback_loop])
post_harvest.order.add_edge(harvest_plan, waste_recycle)
post_harvest.order.add_edge(waste_recycle, feedback_loop)

# Compose the overall process as partial order:
# init_analysis -> design_setup -> reg_stakeholder -> loop_monitor_adjust -> post_harvest
root = StrictPartialOrder(
    nodes=[init_analysis, design_setup, reg_stakeholder, loop_monitor_adjust, post_harvest])
root.order.add_edge(init_analysis, design_setup)
root.order.add_edge(design_setup, reg_stakeholder)
root.order.add_edge(reg_stakeholder, loop_monitor_adjust)
root.order.add_edge(loop_monitor_adjust, post_harvest)