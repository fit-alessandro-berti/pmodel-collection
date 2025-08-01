# Generated from: 47e0a57b-e9a4-45fe-8df5-fd1cba8954f0.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city. It includes site selection based on environmental factors, modular infrastructure design, integration of IoT sensors for climate control, hydroponic system assembly, automated nutrient delivery calibration, energy sourcing from renewables, pest management through biological agents, crop selection for optimal yield, staff training on technology use, regulatory compliance checks, real-time monitoring setup, harvest scheduling, packaging with sustainable materials, distribution logistics coordination, and continuous system optimization using AI analytics to maximize productivity and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Select = Transition(label='Site Select')
Design_Modules = Transition(label='Design Modules')
Install_Sensors = Transition(label='Install Sensors')
Assemble_Hydroponics = Transition(label='Assemble Hydroponics')
Calibrate_Nutrients = Transition(label='Calibrate Nutrients')
Source_Energy = Transition(label='Source Energy')
Manage_Pests = Transition(label='Manage Pests')
Select_Crops = Transition(label='Select Crops')
Train_Staff = Transition(label='Train Staff')
Check_Compliance = Transition(label='Check Compliance')
Setup_Monitoring = Transition(label='Setup Monitoring')
Schedule_Harvest = Transition(label='Schedule Harvest')
Package_Produce = Transition(label='Package Produce')
Coordinate_Logistics = Transition(label='Coordinate Logistics')
Optimize_Systems = Transition(label='Optimize Systems')

# Create partial orders modeling logical flow and concurrency:

# Initial site selection done before design
# Design modules precedes installation of sensors & assembly of hydroponics & sourcing energy
# Installation of sensors, assembly of hydroponics, and energy sourcing can be done concurrently after design
# Calibrate nutrients depends on assembly hydroponics
# Manage pests and select crops can be done in parallel after nutrient calibration and sourcing energy
# Train staff and check compliance depend on manage pests and select crops (all)
# Setup monitoring depends on install sensors and train staff
# Schedule harvest after setup monitoring and check compliance
# Package produce after schedule harvest, coordinate logistics after package produce
# Optimize systems can run concurrently after coordinate logistics (continuous optimization)

nodes = [
    Site_Select, Design_Modules,
    Install_Sensors, Assemble_Hydroponics, Source_Energy,
    Calibrate_Nutrients,
    Manage_Pests, Select_Crops,
    Train_Staff, Check_Compliance,
    Setup_Monitoring,
    Schedule_Harvest,
    Package_Produce,
    Coordinate_Logistics,
    Optimize_Systems
]

root = StrictPartialOrder(nodes=nodes)

o = root.order.add_edge

# Site Select -> Design Modules
o(Site_Select, Design_Modules)

# Design Modules -> concurrent: Install Sensors, Assemble Hydroponics, Source Energy
o(Design_Modules, Install_Sensors)
o(Design_Modules, Assemble_Hydroponics)
o(Design_Modules, Source_Energy)

# Assemble Hydroponics -> Calibrate Nutrients
o(Assemble_Hydroponics, Calibrate_Nutrients)

# Calibrate Nutrients and Source Energy -> Manage Pests and Select Crops (both depend on calibrated system and energy)
o(Calibrate_Nutrients, Manage_Pests)
o(Calibrate_Nutrients, Select_Crops)
o(Source_Energy, Manage_Pests)
o(Source_Energy, Select_Crops)

# Manage Pests and Select Crops -> Train Staff and Check Compliance (both depend on these two)
o(Manage_Pests, Train_Staff)
o(Select_Crops, Train_Staff)
o(Manage_Pests, Check_Compliance)
o(Select_Crops, Check_Compliance)

# Install Sensors and Train Staff -> Setup Monitoring
o(Install_Sensors, Setup_Monitoring)
o(Train_Staff, Setup_Monitoring)

# Setup Monitoring and Check Compliance -> Schedule Harvest
o(Setup_Monitoring, Schedule_Harvest)
o(Check_Compliance, Schedule_Harvest)

# Schedule Harvest -> Package Produce
o(Schedule_Harvest, Package_Produce)

# Package Produce -> Coordinate Logistics
o(Package_Produce, Coordinate_Logistics)

# Coordinate Logistics -> Optimize Systems (continuous optimization after logistics)
o(Coordinate_Logistics, Optimize_Systems)