# Generated from: d391d12c-fb12-4375-9d1a-d99ca529440f.json
# Description: This process outlines the steps involved in establishing a bespoke urban farming system tailored to small rooftop spaces in densely populated cities. It includes site analysis, microclimate assessment, soil-less media selection, modular hydroponic design, nutrient cycling optimization, and automated environmental controls. The workflow integrates stakeholder coordination, regulatory compliance checks, and community engagement programs to ensure sustainability and scalability. Continuous monitoring and adaptive management strategies are embedded to respond to seasonal variations and urban pollution factors, enabling year-round crop production with minimal resource waste while fostering local food security and green urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
climate_check     = Transition(label='Climate Check')
soil_testing      = Transition(label='Soil Testing')
media_select      = Transition(label='Media Select')
design_layout     = Transition(label='Design Layout')
hydro_setup       = Transition(label='Hydro Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_install    = Transition(label='Sensor Install')

regulation_review = Transition(label='Regulation Review')
permit_apply      = Transition(label='Permit Apply')

stakeholder_meet  = Transition(label='Stakeholder Meet')
community_train   = Transition(label='Community Train')

plant_seed        = Transition(label='Plant Seed')
monitor_growth    = Transition(label='Monitor Growth')
adjust_controls   = Transition(label='Adjust Controls')
waste_recycle     = Transition(label='Waste Recycle')

harvest_plan      = Transition(label='Harvest Plan')
feedback_loop     = Transition(label='Feedback Loop')

# Compliance check: Regulation Review -> Permit Apply
compliance = StrictPartialOrder(nodes=[regulation_review, permit_apply])
compliance.order.add_edge(regulation_review, permit_apply)

# Stakeholder coordination (concurrent)
stakeholder = StrictPartialOrder(nodes=[stakeholder_meet, community_train])

# Growing loop: Monitor Growth is A; body B = {Adjust Controls, Waste Recycle} executed concurrently
grow_body = StrictPartialOrder(nodes=[adjust_controls, waste_recycle])
grow_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, grow_body])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_check, soil_testing,
    media_select, design_layout, hydro_setup, nutrient_mix, sensor_install,
    compliance, stakeholder,
    plant_seed,
    grow_loop,
    harvest_plan, feedback_loop
])

# Initial site analysis sequence
root.order.add_edge(site_survey,    climate_check)
root.order.add_edge(climate_check,  soil_testing)

# Design & setup sequence
root.order.add_edge(soil_testing,   media_select)
root.order.add_edge(media_select,   design_layout)
root.order.add_edge(design_layout,  hydro_setup)
root.order.add_edge(hydro_setup,    nutrient_mix)
root.order.add_edge(nutrient_mix,   sensor_install)

# After setup, do compliance and stakeholder tasks in parallel
root.order.add_edge(sensor_install, compliance)
root.order.add_edge(sensor_install, stakeholder)

# Both compliance and stakeholder must finish before planting
root.order.add_edge(compliance,     plant_seed)
root.order.add_edge(stakeholder,    plant_seed)

# Planting precedes the growth loop
root.order.add_edge(plant_seed,     grow_loop)

# After growth loop, plan harvest and then feedback
root.order.add_edge(grow_loop,      harvest_plan)
root.order.add_edge(harvest_plan,   feedback_loop)