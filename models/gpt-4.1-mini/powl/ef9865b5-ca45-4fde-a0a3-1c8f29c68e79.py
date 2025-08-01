# Generated from: ef9865b5-ca45-4fde-a0a3-1c8f29c68e79.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm on a commercial building. It includes site assessment for structural integrity and sunlight exposure, obtaining necessary permits, designing modular planting systems, sourcing sustainable materials, installing irrigation and sensor networks, recruiting skilled urban farmers, conducting soil-less planting trials, implementing pest management strategies, and setting up a digital monitoring platform. The process concludes with initial harvest planning and community engagement activities aimed at promoting urban agriculture benefits and local food sourcing awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
structural_test = Transition(label='Structural Test')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
soilless_prep = Transition(label='Soilless Prep')
pest_control = Transition(label='Pest Control')
system_calibrate = Transition(label='System Calibrate')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

# Build partial order
# Logical ordering:
# Site Survey consists of Structural Test and Permit Review after it.
# Then Design Layout.
# Then Material Sourcing.
# Then concurrent irrigation and sensor install.
# Then Recruit Farmers.
# Then Trial Planting and Soilless Prep concurrently.
# Then Pest Control and System Calibrate concurrently.
# Then Data Monitor.
# Then Harvest Plan.
# Then Community Outreach.

root = StrictPartialOrder(nodes=[
    site_survey,
    structural_test,
    permit_review,
    design_layout,
    material_sourcing,
    irrigation_setup,
    sensor_install,
    recruit_farmers,
    trial_planting,
    soilless_prep,
    pest_control,
    system_calibrate,
    data_monitor,
    harvest_plan,
    community_outreach
])

order = root.order
# Site Survey -> Structural Test and Permit Review
order.add_edge(site_survey, structural_test)
order.add_edge(site_survey, permit_review)

# Structural Test and Permit Review must complete before Design Layout
order.add_edge(structural_test, design_layout)
order.add_edge(permit_review, design_layout)

# Design Layout -> Material Sourcing
order.add_edge(design_layout, material_sourcing)

# Material Sourcing -> Irrigation Setup and Sensor Install concurrently
order.add_edge(material_sourcing, irrigation_setup)
order.add_edge(material_sourcing, sensor_install)

# Irrigation Setup and Sensor Install -> Recruit Farmers
order.add_edge(irrigation_setup, recruit_farmers)
order.add_edge(sensor_install, recruit_farmers)

# Recruit Farmers -> Trial Planting and Soilless Prep concurrently
order.add_edge(recruit_farmers, trial_planting)
order.add_edge(recruit_farmers, soilless_prep)

# Trial Planting and Soilless Prep -> Pest Control and System Calibrate concurrently
order.add_edge(trial_planting, pest_control)
order.add_edge(trial_planting, system_calibrate)
order.add_edge(soilless_prep, pest_control)
order.add_edge(soilless_prep, system_calibrate)

# Pest Control and System Calibrate -> Data Monitor
order.add_edge(pest_control, data_monitor)
order.add_edge(system_calibrate, data_monitor)

# Data Monitor -> Harvest Plan
order.add_edge(data_monitor, harvest_plan)

# Harvest Plan -> Community Outreach
order.add_edge(harvest_plan, community_outreach)