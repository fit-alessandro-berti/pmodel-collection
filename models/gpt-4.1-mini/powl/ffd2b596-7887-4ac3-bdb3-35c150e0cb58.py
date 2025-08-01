# Generated from: ffd2b596-7887-4ac3-bdb3-35c150e0cb58.json
# Description: This process outlines the complex and highly customized assembly of drones tailored for specific environmental conditions and client requirements. It begins with detailed component sourcing, followed by precision calibration of sensors and motors. Quality assurance is integrated at multiple stages to ensure durability under varied weather conditions. Software integration involves adaptive flight algorithms that adjust to real-time data inputs. Final testing simulates extreme operational scenarios before packaging and logistics coordination for global distribution. Throughout, cross-functional teams collaborate closely to manage supply chain variability and maintain compliance with international aviation standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Component_Sourcing = Transition(label='Component Sourcing')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Motor_Assembly = Transition(label='Motor Assembly')
Frame_Build = Transition(label='Frame Build')
Software_Install = Transition(label='Software Install')
Algorithm_Tune = Transition(label='Algorithm Tune')
Battery_Integrate = Transition(label='Battery Integrate')
Signal_Test = Transition(label='Signal Test')
Durability_Check = Transition(label='Durability Check')
Flight_Simulate = Transition(label='Flight Simulate')
Quality_Inspect = Transition(label='Quality Inspect')
Compliance_Review = Transition(label='Compliance Review')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Client_Feedback = Transition(label='Client Feedback')

# Partial order for component sourcing and calibration
sourcing_and_calibrate = StrictPartialOrder(nodes=[
    Component_Sourcing, Sensor_Calibrate, Motor_Assembly, Frame_Build
])
sourcing_and_calibrate.order.add_edge(Component_Sourcing, Sensor_Calibrate)
sourcing_and_calibrate.order.add_edge(Component_Sourcing, Motor_Assembly)
sourcing_and_calibrate.order.add_edge(Component_Sourcing, Frame_Build)

# Quality Inspect depends on assemblies (Motor Assembly, Frame Build, Sensor Calibrate)
quality_stage = StrictPartialOrder(nodes=[
    Motor_Assembly, Frame_Build, Sensor_Calibrate, Quality_Inspect, Durability_Check
])
quality_stage.order.add_edge(Motor_Assembly, Quality_Inspect)
quality_stage.order.add_edge(Frame_Build, Quality_Inspect)
quality_stage.order.add_edge(Sensor_Calibrate, Quality_Inspect)
quality_stage.order.add_edge(Quality_Inspect, Durability_Check)

# Software installation and tuning
software_stage = StrictPartialOrder(nodes=[
    Software_Install, Algorithm_Tune
])
software_stage.order.add_edge(Software_Install, Algorithm_Tune)

# Testing stage: Signal Test and Flight Simulate, parallel but Flight Simulate after Algorithm Tune
testing_stage = StrictPartialOrder(nodes=[
    Algorithm_Tune, Signal_Test, Flight_Simulate
])
testing_stage.order.add_edge(Algorithm_Tune, Flight_Simulate)

# Compliance stage after durability check and testing
compliance_stage = StrictPartialOrder(nodes=[
    Durability_Check, Flight_Simulate, Quality_Inspect, Compliance_Review
])
compliance_stage.order.add_edge(Durability_Check, Compliance_Review)
compliance_stage.order.add_edge(Flight_Simulate, Compliance_Review)
compliance_stage.order.add_edge(Quality_Inspect, Compliance_Review)

# Packaging and logistics after compliance review and battery integrate
packaging_logistics = StrictPartialOrder(nodes=[
    Battery_Integrate, Packaging_Prep, Logistics_Plan
])
packaging_logistics.order.add_edge(Battery_Integrate, Packaging_Prep)
packaging_logistics.order.add_edge(Packaging_Prep, Logistics_Plan)

# Combine all as a large partial order with appropriate edges
root = StrictPartialOrder(nodes=[
    sourcing_and_calibrate, quality_stage, software_stage,
    testing_stage, compliance_stage, packaging_logistics, Client_Feedback
])

# Define dependencies between big stages
root.order.add_edge(sourcing_and_calibrate, quality_stage)
root.order.add_edge(quality_stage, software_stage)
root.order.add_edge(software_stage, testing_stage)
root.order.add_edge(testing_stage, compliance_stage)
root.order.add_edge(compliance_stage, packaging_logistics)

# Client feedback happens last after packaging and logistics
root.order.add_edge(packaging_logistics, Client_Feedback)