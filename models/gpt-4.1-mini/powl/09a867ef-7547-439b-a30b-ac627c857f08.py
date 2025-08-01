# Generated from: 09a867ef-7547-439b-a30b-ac627c857f08.json
# Description: This process outlines the establishment of a custom urban farming system tailored to specific client locations and environmental conditions. It involves initial site assessment, soil and pollution testing, modular farm design, sourcing of specialized seeds and nutrients, installation of IoT sensors for real-time monitoring, integration of renewable energy sources, staff training on sustainable practices, and ongoing performance optimization. The process ensures maximized yield with minimal environmental impact, adapting to urban constraints while promoting local food production and community engagement through workshops and digital platforms for farm management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey = Transition(label='Site Survey')
soil_testing = Transition(label='Soil Testing')
pollution_check = Transition(label='Pollution Check')
farm_design = Transition(label='Farm Design')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
energy_integration = Transition(label='Energy Integration')
irrigation_install = Transition(label='Irrigation Install')
staff_training = Transition(label='Staff Training')
regulation_review = Transition(label='Regulation Review')
community_workshop = Transition(label='Community Workshop')
data_monitoring = Transition(label='Data Monitoring')
yield_analysis = Transition(label='Yield Analysis')
system_upgrade = Transition(label='System Upgrade')

# Initial site assessment as partial order with soil testing and pollution check in parallel after site survey
initial_assessment = StrictPartialOrder(nodes=[site_survey, soil_testing, pollution_check])
initial_assessment.order.add_edge(site_survey, soil_testing)
initial_assessment.order.add_edge(site_survey, pollution_check)

# Farm design after initial assessment
farm_design_partial = StrictPartialOrder(nodes=[initial_assessment, farm_design])
farm_design_partial.order.add_edge(initial_assessment, farm_design)

# Sourcing seeds and nutrient plan parallel after farm design
sourcing_and_nutrients = StrictPartialOrder(nodes=[seed_sourcing, nutrient_plan])
# No order edges: concurrent

# Installation partial order after sourcing and nutrients: sensor setup, energy integration and irrigation install can be concurrent
installation = StrictPartialOrder(nodes=[sensor_setup, energy_integration, irrigation_install])
# No order edges: concurrent

# Staff training and regulation review after installation
training_and_review = StrictPartialOrder(nodes=[staff_training, regulation_review])
# No order edges: concurrent

# Community workshop and data monitoring concurrent after training and review
community_and_monitoring = StrictPartialOrder(nodes=[community_workshop, data_monitoring])
# No order edges: concurrent

# Yield analysis after community & monitoring
yield_analysis_po = StrictPartialOrder(nodes=[community_and_monitoring, yield_analysis])
yield_analysis_po.order.add_edge(community_and_monitoring, yield_analysis)

# Loop with yield analysis and system upgrade: optimize ongoing performance
loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis_po, system_upgrade])

# Aggregate all in partial order
root = StrictPartialOrder(nodes=[farm_design_partial, sourcing_and_nutrients, installation, training_and_review, community_and_monitoring, yield_analysis_po, loop])

# Define edges to set the proper sequence of phases:
# farm_design_partial --> sourcing_and_nutrients
root.order.add_edge(farm_design_partial, sourcing_and_nutrients)
# sourcing_and_nutrients --> installation
root.order.add_edge(sourcing_and_nutrients, installation)
# installation --> training_and_review
root.order.add_edge(installation, training_and_review)
# training_and_review --> community_and_monitoring
root.order.add_edge(training_and_review, community_and_monitoring)
# community_and_monitoring --> yield_analysis_po
root.order.add_edge(community_and_monitoring, yield_analysis_po)
# yield_analysis_po --> loop (loop contains yield_analysis_po again)
root.order.add_edge(yield_analysis_po, loop)