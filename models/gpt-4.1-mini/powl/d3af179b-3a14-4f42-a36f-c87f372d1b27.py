# Generated from: d3af179b-3a14-4f42-a36f-c87f372d1b27.json
# Description: This process outlines the establishment of a vertical farming operation within an urban environment, focusing on integrating sustainable agriculture with smart technology. It involves site analysis, modular unit design, climate control optimization, nutrient solution formulation, LED spectrum tuning, automated seeding, growth monitoring via IoT sensors, pest management using biological agents, data-driven yield prediction, energy consumption assessment, waste recycling systems, community engagement programs, regulatory compliance audits, and final crop distribution logistics. The workflow ensures maximized space efficiency and minimized environmental impact while delivering fresh produce locally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
LED_Tuning = Transition(label='LED Tuning')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Waste_System = Transition(label='Waste System')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Crop_Packing = Transition(label='Crop Packing')
Logistics_Plan = Transition(label='Logistics Plan')

# Organize the process based on description into partially ordered segments:
#
# Basic ordering reflecting dependencies:
# Site Survey --> Design Modules --> Climate Setup
# Climate Setup and Nutrient Mix & LED Tuning are parallel (after Design Modules)
# Nutrient Mix and LED Tuning precede Seed Automation
# Seed Automation --> Growth Monitor --> Pest Control --> Yield Forecast
# Yield Forecast --> Energy Audit and Waste System (in parallel)
# Energy Audit, Waste System --> Community Meet and Compliance Check (both in parallel)
# Community Meet and Compliance Check --> Crop Packing --> Logistics Plan

# First PO with Site Survey, Design Modules and Climate Setup strictly ordered
po1 = StrictPartialOrder(
    nodes=[Site_Survey, Design_Modules, Climate_Setup],
)
po1.order.add_edge(Site_Survey, Design_Modules)
po1.order.add_edge(Design_Modules, Climate_Setup)

# Nutrient Mix and LED Tuning can be done in parallel and both must be done before Seed Automation
po2 = StrictPartialOrder(
    nodes=[Nutrient_Mix, LED_Tuning, Seed_Automation],
)
po2.order.add_edge(Nutrient_Mix, Seed_Automation)
po2.order.add_edge(LED_Tuning, Seed_Automation)

# Growth related sequence: Seed Automation -> Growth Monitor -> Pest Control -> Yield Forecast
po3 = StrictPartialOrder(
    nodes=[Seed_Automation, Growth_Monitor, Pest_Control, Yield_Forecast],
)
po3.order.add_edge(Seed_Automation, Growth_Monitor)
po3.order.add_edge(Growth_Monitor, Pest_Control)
po3.order.add_edge(Pest_Control, Yield_Forecast)

# After Yield Forecast: Energy Audit and Waste System run in parallel
po4 = StrictPartialOrder(
    nodes=[Yield_Forecast, Energy_Audit, Waste_System],
)
po4.order.add_edge(Yield_Forecast, Energy_Audit)
po4.order.add_edge(Yield_Forecast, Waste_System)

# Then Community Meet and Compliance Check run in parallel, both preceded by Energy Audit and Waste System
po5 = StrictPartialOrder(
    nodes=[Energy_Audit, Waste_System, Community_Meet, Compliance_Check],
)
po5.order.add_edge(Energy_Audit, Community_Meet)
po5.order.add_edge(Energy_Audit, Compliance_Check)
po5.order.add_edge(Waste_System, Community_Meet)
po5.order.add_edge(Waste_System, Compliance_Check)

# Final packing and logistics after Community Meet and Compliance Check
po6 = StrictPartialOrder(
    nodes=[Community_Meet, Compliance_Check, Crop_Packing, Logistics_Plan],
)
po6.order.add_edge(Community_Meet, Crop_Packing)
po6.order.add_edge(Compliance_Check, Crop_Packing)
po6.order.add_edge(Crop_Packing, Logistics_Plan)

# Combine all parts into one big PO
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5, po6]
)

# Add cross edges connecting the parts according to flow
root.order.add_edge(po1, po2)  # Climate Setup finishes before Nutrient Mix and LED Tuning start
root.order.add_edge(po2, po3)  # Seed Automation onwards
root.order.add_edge(po3, po4)  # Yield Forecast onwards
root.order.add_edge(po4, po5)  # Community Meet, Compliance Check start after Energy Audit and Waste System
root.order.add_edge(po5, po6)  # Final packing and logistics
