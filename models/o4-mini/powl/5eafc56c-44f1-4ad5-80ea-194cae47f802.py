# Generated from: 5eafc56c-44f1-4ad5-80ea-194cae47f802.json
# Description: This process outlines the complex and atypical steps required to establish an urban rooftop farm in a dense metropolitan area. It involves assessing rooftop structural integrity, navigating municipal permits, designing modular planting systems, sourcing sustainable materials, integrating IoT sensors for climate control, training staff on vertical farming techniques, and coordinating with local markets for produce distribution. Additional considerations include managing water recycling systems, implementing pest control without harmful chemicals, optimizing energy use via solar panels, and ensuring compliance with health and safety regulations. The process culminates in a launch event to promote community engagement and secure ongoing funding through local grants and partnerships, ensuring sustainability and long-term impact within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
permit_review   = Transition(label='Permit Review')
structural_test = Transition(label='Structural Test')
design_layout   = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
sensor_setup    = Transition(label='Sensor Setup')
water_system    = Transition(label='Water System')
pest_control    = Transition(label='Pest Control')
staff_training  = Transition(label='Staff Training')
energy_install  = Transition(label='Energy Install')
crop_planning   = Transition(label='Crop Planning')
market_liaison  = Transition(label='Market Liaison')
safety_audit    = Transition(label='Safety Audit')
launch_event    = Transition(label='Launch Event')
funding_apply   = Transition(label='Funding Apply')
community_meet  = Transition(label='Community Meet')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_review,
    structural_test,
    design_layout,
    material_sourcing,
    sensor_setup,
    water_system,
    pest_control,
    staff_training,
    energy_install,
    crop_planning,
    market_liaison,
    safety_audit,
    launch_event,
    funding_apply,
    community_meet
])

# Define ordering constraints
# 1. Survey → Permit Review & Structural Test
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(site_survey, structural_test)

# 2. Both Review & Test → Design Layout
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(structural_test, design_layout)

# 3. Design → Material Sourcing & Crop Planning
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(design_layout, crop_planning)

# 4. Crop Planning → Staff Training & Market Liaison
root.order.add_edge(crop_planning, staff_training)
root.order.add_edge(crop_planning, market_liaison)

# 5. Material Sourcing → Infrastructure setups
root.order.add_edge(material_sourcing, sensor_setup)
root.order.add_edge(material_sourcing, water_system)
root.order.add_edge(material_sourcing, pest_control)
root.order.add_edge(material_sourcing, energy_install)

# 6. Infrastructure setups → Safety Audit
for infra in [sensor_setup, water_system, pest_control, energy_install]:
    root.order.add_edge(infra, safety_audit)

# 7. Safety Audit, Staff Training, Market Liaison → Launch Event
root.order.add_edge(safety_audit, launch_event)
root.order.add_edge(staff_training, launch_event)
root.order.add_edge(market_liaison, launch_event)

# 8. Launch Event → Community Meet & Funding Apply
root.order.add_edge(launch_event, community_meet)
root.order.add_edge(launch_event, funding_apply)