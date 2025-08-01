# Generated from: 82273a9a-e0e4-419a-953d-fad931e90b35.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farm on a commercial building. It involves initial structural assessments, environmental impact studies, selection of appropriate crops, installation of modular soil beds, irrigation systems, and solar-powered sensors. The process integrates community engagement for educational workshops, pest control using organic methods, and a logistics plan for weekly harvesting and distribution to local markets. Continuous monitoring and maintenance ensure optimal growth conditions, while data analytics optimize yield and resource usage, promoting a closed-loop urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activity transitions
site_survey      = Transition(label='Site Survey')
load_testing     = Transition(label='Load Testing')
impact_study     = Transition(label='Impact Study')
crop_selection   = Transition(label='Crop Selection')
soil_prep        = Transition(label='Soil Prep')
bed_install      = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_deploy    = Transition(label='Sensor Deploy')
solar_config     = Transition(label='Solar Config')
community_meet   = Transition(label='Community Meet')
workshop_plan    = Transition(label='Workshop Plan')
pest_control     = Transition(label='Pest Control')
harvest_plan     = Transition(label='Harvest Plan')
supply_route     = Transition(label='Supply Route')
data_monitor     = Transition(label='Data Monitor')
yield_analysis   = Transition(label='Yield Analysis')
maintenance      = Transition(label='Maintenance')

# Group the maintenance & analysis into a small partial order for the loop body
maintenance_analysis = StrictPartialOrder(nodes=[maintenance, yield_analysis])
maintenance_analysis.order.add_edge(maintenance, yield_analysis)

# Define the continuous monitoring & maintenance loop
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitor, maintenance_analysis]
)

# Build the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, impact_study, crop_selection,
    soil_prep, bed_install,
    irrigation_setup, sensor_deploy, solar_config,
    community_meet, workshop_plan,
    pest_control, harvest_plan, supply_route,
    monitoring_loop
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey,      load_testing)
root.order.add_edge(load_testing,     impact_study)
root.order.add_edge(impact_study,     crop_selection)
root.order.add_edge(crop_selection,   soil_prep)
root.order.add_edge(soil_prep,        bed_install)

# After bed installation, set up irrigation, sensors, and solar in parallel
root.order.add_edge(bed_install,      irrigation_setup)
root.order.add_edge(bed_install,      sensor_deploy)
root.order.add_edge(bed_install,      solar_config)

# Community engagement follows full setup
root.order.add_edge(irrigation_setup, community_meet)
root.order.add_edge(sensor_deploy,    community_meet)
root.order.add_edge(solar_config,     community_meet)
root.order.add_edge(community_meet,   workshop_plan)

# Pest control, harvesting and distribution
root.order.add_edge(workshop_plan,    pest_control)
root.order.add_edge(pest_control,     harvest_plan)
root.order.add_edge(harvest_plan,     supply_route)

# After distribution, enter the continuous monitoring & maintenance loop
root.order.add_edge(supply_route,     monitoring_loop)