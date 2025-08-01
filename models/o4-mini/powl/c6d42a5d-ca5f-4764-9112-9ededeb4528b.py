# Generated from: c6d42a5d-ca5f-4764-9112-9ededeb4528b.json
# Description: This process outlines the detailed steps involved in establishing an urban rooftop farm on a commercial building. It begins with site evaluation and structural assessment to ensure the roof can support the load. Subsequent activities include soil testing, selecting appropriate crops for microclimate conditions, and designing irrigation systems tailored to limited water resources. The process also involves obtaining necessary permits, sourcing sustainable materials, and coordinating with local suppliers for organic seeds and fertilizers. Installation phases cover creating raised beds, integrating pest management solutions, and setting up renewable energy sources like solar panels to power automated watering. The final stages focus on staff training, marketing the farm's produce to local restaurants, and implementing a digital monitoring system for crop health and growth optimization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey      = Transition(label='Site Survey')
load_test        = Transition(label='Load Test')
soil_sample      = Transition(label='Soil Sample')
crop_select      = Transition(label='Crop Select')
irrigation_plan  = Transition(label='Irrigation Plan')
permit_apply     = Transition(label='Permit Apply')
material_order   = Transition(label='Material Order')
supplier_contact = Transition(label='Supplier Contact')
bed_install      = Transition(label='Bed Install')
pest_control     = Transition(label='Pest Control')
solar_setup      = Transition(label='Solar Setup')
staff_train      = Transition(label='Staff Train')
market_outreach  = Transition(label='Market Outreach')
system_setup     = Transition(label='System Setup')
health_monitor   = Transition(label='Health Monitor')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, load_test,
    soil_sample, crop_select, irrigation_plan,
    permit_apply, material_order, supplier_contact,
    bed_install, pest_control, solar_setup,
    staff_train, market_outreach, system_setup, health_monitor
])

# Sequence: Site Survey → Load Test → Soil Sample → Crop Select → Irrigation Plan
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(soil_sample, crop_select)
root.order.add_edge(crop_select, irrigation_plan)

# After Irrigation Plan: three concurrent preparatory tasks
root.order.add_edge(irrigation_plan, permit_apply)
root.order.add_edge(irrigation_plan, material_order)
root.order.add_edge(irrigation_plan, supplier_contact)

# Those three must finish before installation begins
root.order.add_edge(permit_apply, bed_install)
root.order.add_edge(material_order, bed_install)
root.order.add_edge(supplier_contact, bed_install)

# Installation sequence: Bed Install → Pest Control → Solar Setup
root.order.add_edge(bed_install, pest_control)
root.order.add_edge(pest_control, solar_setup)

# Final stages start after Solar Setup
root.order.add_edge(solar_setup, staff_train)
root.order.add_edge(solar_setup, market_outreach)
root.order.add_edge(solar_setup, system_setup)

# Health monitoring follows system setup
root.order.add_edge(system_setup, health_monitor)