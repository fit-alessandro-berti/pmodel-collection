# Generated from: 7f788fc5-115c-4554-adc1-e39c82d12ab1.json
# Description: This process details the comprehensive steps involved in establishing an urban rooftop farm on a commercial building. It includes assessing structural integrity, navigating local regulations, designing modular planting systems, sourcing sustainable materials, installing irrigation and solar-powered monitoring devices, training staff on urban agriculture techniques, implementing pest management strategies, and setting up a direct-to-consumer sales platform. The process ensures environmental compliance, maximizes crop yield in limited space, and integrates technology for efficient farm management while fostering community engagement through workshops and events.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_assess = Transition(label='Site Assess')
regulation_check = Transition(label='Regulation Check')
structural_survey = Transition(label='Structural Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
solar_install = Transition(label='Solar Install')
soil_prep = Transition(label='Soil Prep')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
monitoring_setup = Transition(label='Monitoring Setup')
harvest_plan = Transition(label='Harvest Plan')
sales_launch = Transition(label='Sales Launch')
community_event = Transition(label='Community Event')
waste_manage = Transition(label='Waste Manage')

# Model the process:
# Initial assessment phase: site assess -> (regulation check and structural survey in parallel)
# Then design layout
# Then material sourcing
# Then installation phase: irrigation setup and solar install in parallel
# Then soil preparation and seed selection in parallel
# Then planting phase
# Pest control and staff training run in parallel (both needed for healthy crops & trained staff)
# Monitoring setup to track crop growth
# Harvest plan
# Sales launch
# Community events and waste management run concurrently at the end to foster engagement and sustainability

root = StrictPartialOrder(nodes=[
    site_assess,
    regulation_check,
    structural_survey,
    design_layout,
    material_sourcing,
    irrigation_setup,
    solar_install,
    soil_prep,
    seed_selection,
    planting_phase,
    pest_control,
    staff_training,
    monitoring_setup,
    harvest_plan,
    sales_launch,
    community_event,
    waste_manage
])

order = root.order

# Site Assess -> Regulation Check and Structural Survey (concurrent)
order.add_edge(site_assess, regulation_check)
order.add_edge(site_assess, structural_survey)

# Both regulation_check and structural_survey done before design_layout
order.add_edge(regulation_check, design_layout)
order.add_edge(structural_survey, design_layout)

# Design layout before material sourcing
order.add_edge(design_layout, material_sourcing)

# Material sourcing before installation (both irrigation and solar install can be concurrent)
order.add_edge(material_sourcing, irrigation_setup)
order.add_edge(material_sourcing, solar_install)

# Both irrigation and solar installation before soil prep and seed selection (which are concurrent)
order.add_edge(irrigation_setup, soil_prep)
order.add_edge(solar_install, soil_prep)
order.add_edge(irrigation_setup, seed_selection)
order.add_edge(solar_install, seed_selection)

# Soil prep and seed selection before planting phase
order.add_edge(soil_prep, planting_phase)
order.add_edge(seed_selection, planting_phase)

# Planting phase before pest control and staff training (concurrent)
order.add_edge(planting_phase, pest_control)
order.add_edge(planting_phase, staff_training)

# Pest control and staff training before monitoring setup (both needed)
order.add_edge(pest_control, monitoring_setup)
order.add_edge(staff_training, monitoring_setup)

# Monitoring setup before harvest plan
order.add_edge(monitoring_setup, harvest_plan)

# Harvest plan before sales launch
order.add_edge(harvest_plan, sales_launch)

# Sales launch before community event and waste management (concurrent)
order.add_edge(sales_launch, community_event)
order.add_edge(sales_launch, waste_manage)