# Generated from: 3193313d-84b4-4769-b323-b2256ce16595.json
# Description: This process outlines the complex sequence required to establish an urban vertical farm within a metropolitan environment. It involves site selection based on environmental factors, designing multi-level hydroponic systems, sourcing sustainable materials, integrating IoT sensors for climate control, securing permits from local authorities, installing energy-efficient LED lighting, implementing automated nutrient delivery, training staff on plant care and system maintenance, and launching a market outreach campaign focused on local produce. The process also includes establishing partnerships with local restaurants and grocery stores, continuous monitoring of crop health through data analytics, and adapting operations based on seasonal changes and consumer feedback to maximize yield and sustainability in a highly regulated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition('Site Assess')
Design_Layout = Transition('Design Layout')
Material_Source = Transition('Material Source')
Permit_Obtain = Transition('Permit Obtain')
System_Install = Transition('System Install')
Sensor_Setup = Transition('Sensor Setup')
Lighting_Configure = Transition('Lighting Configure')
Nutrient_Program = Transition('Nutrient Program')
Staff_Train = Transition('Staff Train')
Crop_Planting = Transition('Crop Planting')
Data_Monitor = Transition('Data Monitor')
Market_Launch = Transition('Market Launch')
Partnership_Build = Transition('Partnership Build')
Feedback_Collect = Transition('Feedback Collect')
Yield_Adjust = Transition('Yield Adjust')

# Partial Order for Setup Phase:
# Site Assess -> Design Layout -> Material Source
#                            |
#                            -> Permit Obtain (concurrent to Material Source)
setup_phase = StrictPartialOrder(nodes=[Site_Assess, Design_Layout, Material_Source, Permit_Obtain])
setup_phase.order.add_edge(Site_Assess, Design_Layout)
setup_phase.order.add_edge(Design_Layout, Material_Source)
setup_phase.order.add_edge(Design_Layout, Permit_Obtain)

# Partial Order for Installation Phase:
# Material Source & Permit Obtain must finish before System Install and Sensor Setup
# Sensor Setup -> Lighting Configure -> Nutrient Program -> Staff Train
installation_phase = StrictPartialOrder(nodes=[Material_Source, Permit_Obtain, System_Install,
                                              Sensor_Setup, Lighting_Configure, Nutrient_Program, Staff_Train])
installation_phase.order.add_edge(Material_Source, System_Install)
installation_phase.order.add_edge(Permit_Obtain, System_Install)
installation_phase.order.add_edge(System_Install, Sensor_Setup)
installation_phase.order.add_edge(Sensor_Setup, Lighting_Configure)
installation_phase.order.add_edge(Lighting_Configure, Nutrient_Program)
installation_phase.order.add_edge(Nutrient_Program, Staff_Train)

# Crop Planting after staff trained
# Market Launch and Partnership Build can run concurrently after Crop Planting
crop_and_market_phase = StrictPartialOrder(nodes=[Staff_Train, Crop_Planting,
                                                 Market_Launch, Partnership_Build])
crop_and_market_phase.order.add_edge(Staff_Train, Crop_Planting)
crop_and_market_phase.order.add_edge(Crop_Planting, Market_Launch)
crop_and_market_phase.order.add_edge(Crop_Planting, Partnership_Build)

# Monitoring and feedback cycle is a loop:
# LOOP(
#    Data Monitor,
#    Sequence: Feedback Collect -> Yield Adjust
# )
feedback_cycle_body = StrictPartialOrder(nodes=[Feedback_Collect, Yield_Adjust])
feedback_cycle_body.order.add_edge(Feedback_Collect, Yield_Adjust)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Monitor, feedback_cycle_body])

# Final partial order combining main phases and feedback loop
root = StrictPartialOrder(nodes=[setup_phase, installation_phase, crop_and_market_phase, feedback_loop])
root.order.add_edge(setup_phase, installation_phase)
root.order.add_edge(installation_phase, crop_and_market_phase)
root.order.add_edge(crop_and_market_phase, feedback_loop)