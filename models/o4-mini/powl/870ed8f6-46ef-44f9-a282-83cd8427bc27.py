# Generated from: 870ed8f6-46ef-44f9-a282-83cd8427bc27.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site analysis, environmental impact assessments, selecting appropriate crops, structural reinforcements, irrigation system design, soil preparation, installation of climate control technologies, integration of renewable energy sources, pest management strategies, community engagement, ongoing maintenance scheduling, yield monitoring, and finally, produce distribution logistics. The process ensures maximization of limited space, compliance with local regulations, and creation of a resilient urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
load_analysis     = Transition(label='Load Analysis')
permits_request   = Transition(label='Permits Request')
crop_selection    = Transition(label='Crop Selection')
soil_testing      = Transition(label='Soil Testing')
irrigation_setup  = Transition(label='Irrigation Setup')
structural_reinf  = Transition(label='Structural Reinforce')
climate_control   = Transition(label='Climate Control')
energy_integration= Transition(label='Energy Integration')
pest_management   = Transition(label='Pest Management')
community_outreach= Transition(label='Community Outreach')
maintenance_plan  = Transition(label='Maintenance Plan')
yield_monitoring  = Transition(label='Yield Monitoring')
harvest_schedule  = Transition(label='Harvest Schedule')
distribution_plan = Transition(label='Distribution Plan')

# Build the POWL partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_analysis, permits_request, crop_selection,
    soil_testing, irrigation_setup, structural_reinf, climate_control,
    energy_integration, pest_management, community_outreach,
    maintenance_plan, yield_monitoring, harvest_schedule, distribution_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      load_analysis)
root.order.add_edge(site_survey,      soil_testing)
root.order.add_edge(load_analysis,    permits_request)
root.order.add_edge(soil_testing,     permits_request)
root.order.add_edge(soil_testing,     crop_selection)
root.order.add_edge(permits_request, community_outreach)
root.order.add_edge(permits_request, structural_reinf)
root.order.add_edge(structural_reinf, irrigation_setup)
root.order.add_edge(structural_reinf, climate_control)
root.order.add_edge(structural_reinf, energy_integration)
root.order.add_edge(crop_selection,   pest_management)
root.order.add_edge(irrigation_setup, maintenance_plan)
root.order.add_edge(climate_control,  maintenance_plan)
root.order.add_edge(energy_integration, maintenance_plan)
root.order.add_edge(maintenance_plan, yield_monitoring)
root.order.add_edge(yield_monitoring, harvest_schedule)
root.order.add_edge(harvest_schedule, distribution_plan)