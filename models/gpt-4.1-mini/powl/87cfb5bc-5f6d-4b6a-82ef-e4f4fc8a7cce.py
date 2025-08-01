# Generated from: 87cfb5bc-5f6d-4b6a-82ef-e4f4fc8a7cce.json
# Description: This process outlines the end-to-end implementation of a bespoke urban farming system tailored for high-density city environments. It involves initial site assessment, soil and air quality analysis, modular design planning, sourcing sustainable materials, installing smart irrigation systems, integrating sensor networks for real-time monitoring, establishing vertical planting modules, implementing pest control using bioengineering methods, training local staff on system maintenance, conducting pilot crop cycles, optimizing nutrient delivery based on AI analytics, coordinating community engagement for shared farming spaces, managing harvest logistics with urban transport considerations, and finally evaluating overall yield performance for continuous improvement and scalability in constrained urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
site_assess = Transition(label='Site Assess')
soil_test = Transition(label='Soil Test')
air_analyze = Transition(label='Air Analyze')
design_plan = Transition(label='Design Plan')
material_source = Transition(label='Material Source')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
vertical_plant = Transition(label='Vertical Plant')
pest_control = Transition(label='Pest Control')
staff_train = Transition(label='Staff Train')
pilot_crop = Transition(label='Pilot Crop')
nutrient_adjust = Transition(label='Nutrient Adjust')
community_engage = Transition(label='Community Engage')
harvest_manage = Transition(label='Harvest Manage')
yield_review = Transition(label='Yield Review')

# Construct the partial order corresponding to the described process:
# Order reflects the typical end-to-end flow:
# Site Assess --> Soil Test and Air Analyze (parallel)
# Both Soil Test and Air Analyze --> Design Plan
# Design Plan --> Material Source --> Irrigation Setup --> Sensor Install
# Sensor Install --> Vertical Plant --> Pest Control --> Staff Train
# Staff Train --> Pilot Crop --> Nutrient Adjust
# Nutrient Adjust --> Community Engage --> Harvest Manage --> Yield Review

root = StrictPartialOrder(
    nodes=[
        site_assess, soil_test, air_analyze, design_plan, material_source,
        irrigation_setup, sensor_install, vertical_plant, pest_control,
        staff_train, pilot_crop, nutrient_adjust, community_engage,
        harvest_manage, yield_review
    ]
)

# Define edges of partial order
root.order.add_edge(site_assess, soil_test)
root.order.add_edge(site_assess, air_analyze)
root.order.add_edge(soil_test, design_plan)
root.order.add_edge(air_analyze, design_plan)
root.order.add_edge(design_plan, material_source)
root.order.add_edge(material_source, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, vertical_plant)
root.order.add_edge(vertical_plant, pest_control)
root.order.add_edge(pest_control, staff_train)
root.order.add_edge(staff_train, pilot_crop)
root.order.add_edge(pilot_crop, nutrient_adjust)
root.order.add_edge(nutrient_adjust, community_engage)
root.order.add_edge(community_engage, harvest_manage)
root.order.add_edge(harvest_manage, yield_review)