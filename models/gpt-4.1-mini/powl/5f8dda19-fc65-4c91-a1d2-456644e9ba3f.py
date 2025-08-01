# Generated from: 5f8dda19-fc65-4c91-a1d2-456644e9ba3f.json
# Description: This process outlines the establishment of a fully automated urban vertical farming system that integrates IoT sensors, renewable energy sources, and AI-driven crop management. It begins with site assessment and design planning, followed by modular farm assembly and installation of hydroponic and aeroponic units. The system is then calibrated with environmental sensors for humidity, temperature, and nutrient monitoring. Renewable energy solutions like solar panels and wind turbines are integrated to ensure sustainable operation. AI algorithms are trained to optimize growth cycles and detect plant diseases early. The process concludes with staff training, compliance checks, and launch of a real-time monitoring dashboard for continuous performance analysis and yield forecasting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Design_Plan = Transition(label='Design Plan')
Module_Build = Transition(label='Module Build')
Unit_Install = Transition(label='Unit Install')
Sensor_Setup = Transition(label='Sensor Setup')
Energy_Integrate = Transition(label='Energy Integrate')
AI_Train = Transition(label='AI Train')
Calibrate_Enviro = Transition(label='Calibrate Enviro')
System_Test = Transition(label='System Test')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Disease_Detect = Transition(label='Disease Detect')
Growth_Optimize = Transition(label='Growth Optimize')
Dashboard_Launch = Transition(label='Dashboard Launch')
Yield_Forecast = Transition(label='Yield Forecast')

# The main partial order of the process:
# 1. Site Assess -> Design Plan (sequential)
# 2. Design Plan -> Module Build (sequential)
# 3. Module Build -> Unit Install (sequential)
# 4. Unit Install -> Sensor Setup (sequential)
# 5. Sensor Setup -> Calibrate Enviro (sequential)
# 6. Calibrate Enviro -> Energy Integrate (sequential)
# 7. Energy Integrate -> AI Train (sequential)
# 8. AI Train -> System Test (sequential)
# 9. System Test -> Staff Train (sequential)
# 10. Staff Train -> Compliance Check (sequential)
# 11. Compliance Check -> Dashboard Launch (sequential)
# 12. Dashboard Launch -> Yield Forecast (sequential)

# There are two AI-related activities after AI_Train:
# - Disease Detect and Growth Optimize are AI activities that can be viewed to happen concurrently or partially ordered.
# They have to occur before Dashboard Launch (as disease detect and growth optimize are AI-driven steps before Dashboard launch).

# Disease Detect and Growth Optimize should come after AI Train but before Dashboard Launch.
# Assume these two activities are concurrent.
# So:
# System Test -> Staff Train -> Compliance Check -> (Disease Detect and Growth Optimize concurrent) -> Dashboard Launch -> Yield Forecast

# Given that Disease Detect and Growth Optimize are AI-driven subtasks, they can be modeled as concurrent nodes that both depend on Compliance Check,
# and Dashboard Launch depends on both completing.

# Build a PO with all these nodes and edges:

# Final nodes:
# [
#   Site_Assess, Design_Plan, Module_Build, Unit_Install,
#   Sensor_Setup, Calibrate_Enviro, Energy_Integrate,
#   AI_Train, System_Test, Staff_Train, Compliance_Check,
#   Disease_Detect, Growth_Optimize,
#   Dashboard_Launch, Yield_Forecast
# ]

root = StrictPartialOrder(nodes=[
    Site_Assess, Design_Plan, Module_Build, Unit_Install,
    Sensor_Setup, Calibrate_Enviro, Energy_Integrate,
    AI_Train, System_Test, Staff_Train, Compliance_Check,
    Disease_Detect, Growth_Optimize,
    Dashboard_Launch, Yield_Forecast
])

root.order.add_edge(Site_Assess, Design_Plan)
root.order.add_edge(Design_Plan, Module_Build)
root.order.add_edge(Module_Build, Unit_Install)
root.order.add_edge(Unit_Install, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Calibrate_Enviro)
root.order.add_edge(Calibrate_Enviro, Energy_Integrate)
root.order.add_edge(Energy_Integrate, AI_Train)
root.order.add_edge(AI_Train, System_Test)
root.order.add_edge(System_Test, Staff_Train)
root.order.add_edge(Staff_Train, Compliance_Check)
# Compliance Check leads to Disease Detect and Growth Optimize concurrently
root.order.add_edge(Compliance_Check, Disease_Detect)
root.order.add_edge(Compliance_Check, Growth_Optimize)
# Dashboard Launch depends on both Disease Detect and Growth Optimize
root.order.add_edge(Disease_Detect, Dashboard_Launch)
root.order.add_edge(Growth_Optimize, Dashboard_Launch)
root.order.add_edge(Dashboard_Launch, Yield_Forecast)