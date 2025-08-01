# Generated from: ef5ec26b-e0aa-476c-b68c-0a7ef159cc72.json
# Description: This process outlines the complex coordination required to establish and maintain a collaborative urban farming initiative involving multiple stakeholders such as local governments, community groups, and technology providers. It includes site selection, soil testing, resource allocation, crop planning, volunteer recruitment, real-time monitoring, and yield optimization using IoT devices and data analytics. The process also integrates conflict resolution mechanisms, educational workshops, seasonal market planning, and sustainability assessments to ensure long-term viability and community engagement. Each activity is designed to balance technological integration with social dynamics to create a resilient urban agriculture ecosystem in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
soil_testing = Transition(label='Soil Testing')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_plan = Transition(label='Resource Plan')
crop_selection = Transition(label='Crop Selection')
volunteer_signup = Transition(label='Volunteer Sign-up')
tech_setup = Transition(label='Tech Setup')
irrigation_check = Transition(label='Irrigation Check')
data_collection = Transition(label='Data Collection')
growth_monitoring = Transition(label='Growth Monitoring')
conflict_mediate = Transition(label='Conflict Mediate')
workshop_prep = Transition(label='Workshop Prep')
community_feedback = Transition(label='Community Feedback')
market_forecast = Transition(label='Market Forecast')
yield_analysis = Transition(label='Yield Analysis')
sustainability_audit = Transition(label='Sustainability Audit')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage = Transition(label='Waste Manage')

# Silent skip for XOR
skip = SilentTransition()

# Define the monitoring loop:
#  A = Data Collection -> Growth Monitoring
monitorA = StrictPartialOrder(nodes=[data_collection, growth_monitoring])
monitorA.order.add_edge(data_collection, growth_monitoring)
#  B = Irrigation Check -> Equipment Maintain
monitorB = StrictPartialOrder(nodes=[irrigation_check, equipment_maintain])
monitorB.order.add_edge(irrigation_check, equipment_maintain)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitorA, monitorB])

# Define conflict resolution choice: either Conflict Mediate or skip
conflict_xor = OperatorPOWL(operator=Operator.XOR, children=[conflict_mediate, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    soil_testing,
    stakeholder_meet,
    resource_plan,
    crop_selection,
    volunteer_signup,
    tech_setup,
    monitor_loop,
    conflict_xor,
    workshop_prep,
    community_feedback,
    market_forecast,
    yield_analysis,
    sustainability_audit,
    waste_manage
])

# Define ordering relations
# Initial site survey
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(site_survey, stakeholder_meet)

# After soil testing and stakeholder meeting: resource planning
root.order.add_edge(soil_testing, resource_plan)
root.order.add_edge(stakeholder_meet, resource_plan)

# Crop selection after resource plan
root.order.add_edge(resource_plan, crop_selection)

# Volunteer sign-up and tech setup in parallel after crop selection
root.order.add_edge(crop_selection, volunteer_signup)
root.order.add_edge(crop_selection, tech_setup)

# Monitoring loop starts after both volunteer signup and tech setup
root.order.add_edge(volunteer_signup, monitor_loop)
root.order.add_edge(tech_setup, monitor_loop)

# After the monitoring loop, do conflict resolution or skip
root.order.add_edge(monitor_loop, conflict_xor)

# After conflict resolution, run the educational workshop and feedback
root.order.add_edge(conflict_xor, workshop_prep)
root.order.add_edge(workshop_prep, community_feedback)

# Then plan market and analyze yield
root.order.add_edge(community_feedback, market_forecast)
root.order.add_edge(market_forecast, yield_analysis)

# Finally sustainability audits and waste management
root.order.add_edge(yield_analysis, sustainability_audit)
root.order.add_edge(sustainability_audit, waste_manage)