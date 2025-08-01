# Generated from: 10ccdc94-f10b-4ea9-a3e4-f30868651ae4.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It begins with structural assessment and legal compliance checks, followed by soil and water testing. Selection of plant varieties suitable for rooftop conditions is critical, alongside the installation of irrigation and drainage systems. The process also includes microclimate monitoring, pest control strategies tailored to urban environments, and community engagement for educational programs. Finally, ongoing maintenance schedules and yield optimization through data analytics complete the setup, ensuring a sustainable and productive rooftop farm in a dense cityscape.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
structure_check = Transition(label='Structure Check')
legal_review = Transition(label='Legal Review')
soil_testing = Transition(label='Soil Testing')
water_analysis = Transition(label='Water Analysis')
plant_selection = Transition(label='Plant Selection')
irrigation_setup = Transition(label='Irrigation Setup')
drainage_install = Transition(label='Drainage Install')
climate_monitor = Transition(label='Climate Monitor')
pest_control = Transition(label='Pest Control')
community_engage = Transition(label='Community Engage')
education_plan = Transition(label='Education Plan')
maintenance_plan = Transition(label='Maintenance Plan')
yield_tracking = Transition(label='Yield Tracking')
data_analytics = Transition(label='Data Analytics')
harvest_schedule = Transition(label='Harvest Schedule')
waste_manage = Transition(label='Waste Manage')

# Partial order for structural and legal checks (both must be done, order assumed structure_check → legal_review)
# This is initial assessment phase
initial_assessment = StrictPartialOrder(
    nodes=[structure_check, legal_review],
)
initial_assessment.order.add_edge(structure_check, legal_review)

# Soil and water testing are presumably parallel after the initial checks
soil_water_testing = StrictPartialOrder(
    nodes=[soil_testing, water_analysis],
)

# Plant selection comes after soil and water tests
plant_selection_po = StrictPartialOrder(
    nodes=[plant_selection],
)

# Irrigation and drainage setup logically parallel after plant selection
irrigation_and_drainage = StrictPartialOrder(
    nodes=[irrigation_setup, drainage_install],
)

# Microclimate monitoring and pest control likely run concurrently after irrigation and drainage
climate_and_pest = StrictPartialOrder(
    nodes=[climate_monitor, pest_control],
)

# Community engagement and education plan are related and likely sequential
community_education = StrictPartialOrder(
    nodes=[community_engage, education_plan],
)
community_education.order.add_edge(community_engage, education_plan)

# Maintenance plan and yield tracking and data analytics and harvest and waste manage are last steps
# Assume maintenance plan first, then yield tracking, data analytics, harvest schedule, and waste manage in partial order where yield tracking < data analytics < harvest schedule, waste manage concurrent or last
final_steps = StrictPartialOrder(
    nodes=[maintenance_plan, yield_tracking, data_analytics, harvest_schedule, waste_manage],
)
final_steps.order.add_edge(maintenance_plan, yield_tracking)
final_steps.order.add_edge(yield_tracking, data_analytics)
final_steps.order.add_edge(data_analytics, harvest_schedule)
# waste_manage concurrent, no order edges forced

# Compose these segments with the partial order edges to represent the entire process ordering

# Now generate the full PO step by step

# 1) initial_assessment → soil_water_testing
# 2) soil_water_testing → plant_selection_po
# 3) plant_selection_po → irrigation_and_drainage
# 4) irrigation_and_drainage → climate_and_pest
# 5) climate_and_pest → community_education
# 6) community_education → final_steps

# Create top node that includes all sub-POs and add edges between them
root = StrictPartialOrder(
    nodes=[
        initial_assessment, 
        soil_water_testing, 
        plant_selection_po, 
        irrigation_and_drainage, 
        climate_and_pest, 
        community_education,
        final_steps
    ],
)

# Add edges to enforce the described ordering
root.order.add_edge(initial_assessment, soil_water_testing)
root.order.add_edge(soil_water_testing, plant_selection_po)
root.order.add_edge(plant_selection_po, irrigation_and_drainage)
root.order.add_edge(irrigation_and_drainage, climate_and_pest)
root.order.add_edge(climate_and_pest, community_education)
root.order.add_edge(community_education, final_steps)