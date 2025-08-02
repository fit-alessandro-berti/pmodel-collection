# Generated from: 1528ad7c-bd53-464f-94b3-4c36be12f57d.json
# Description: This process describes the complex and atypical steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It encompasses site assessment, modular structure design, climate control calibration, advanced hydroponic system installation, sensor network deployment for real-time monitoring, and integration with renewable energy sources. The process also includes staff training on specialized equipment, compliance with urban agriculture regulations, yield forecasting using AI analytics, and establishing distribution channels targeting local markets. This ensures sustainable food production in limited city spaces while optimizing resource efficiency and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Install_Framework = Transition(label='Install Framework')
Setup_HVAC = Transition(label='Setup HVAC')
Deploy_Sensors = Transition(label='Deploy Sensors')
Configure_Lighting = Transition(label='Configure Lighting')
Install_Hydroponics = Transition(label='Install Hydroponics')
Energy_Integration = Transition(label='Energy Integration')
Staff_Training = Transition(label='Staff Training')
Compliance_Check = Transition(label='Compliance Check')
System_Testing = Transition(label='System Testing')
AI_Forecasting = Transition(label='AI Forecasting')
Optimize_Workflow = Transition(label='Optimize Workflow')
Market_Setup = Transition(label='Market Setup')
Launch_Operations = Transition(label='Launch Operations')

# Build the partial order reflecting dependencies and concurrency

root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Modules, Install_Framework, Setup_HVAC,
    Deploy_Sensors, Configure_Lighting, Install_Hydroponics,
    Energy_Integration, Staff_Training, Compliance_Check, System_Testing,
    AI_Forecasting, Optimize_Workflow, Market_Setup, Launch_Operations
])

# Site Survey is the initial step
# Design Modules depends on Site Survey
root.order.add_edge(Site_Survey, Design_Modules)
# Install Framework depends on Design Modules
root.order.add_edge(Design_Modules, Install_Framework)

# Setup HVAC, Deploy Sensors, Configure Lighting, Install Hydroponics and Energy Integration
# can start only after Install Framework (building infrastructure)
root.order.add_edge(Install_Framework, Setup_HVAC)
root.order.add_edge(Install_Framework, Deploy_Sensors)
root.order.add_edge(Install_Framework, Configure_Lighting)
root.order.add_edge(Install_Framework, Install_Hydroponics)
root.order.add_edge(Install_Framework, Energy_Integration)

# Staff Training and Compliance Check can only start after all installation (all 5 activities above) are completed
# So they depend on the 5 installation/configuration activities
root.order.add_edge(Setup_HVAC, Staff_Training)
root.order.add_edge(Deploy_Sensors, Staff_Training)
root.order.add_edge(Configure_Lighting, Staff_Training)
root.order.add_edge(Install_Hydroponics, Staff_Training)
root.order.add_edge(Energy_Integration, Staff_Training)

root.order.add_edge(Setup_HVAC, Compliance_Check)
root.order.add_edge(Deploy_Sensors, Compliance_Check)
root.order.add_edge(Configure_Lighting, Compliance_Check)
root.order.add_edge(Install_Hydroponics, Compliance_Check)
root.order.add_edge(Energy_Integration, Compliance_Check)

# System Testing depends on Staff Training and Compliance Check
root.order.add_edge(Staff_Training, System_Testing)
root.order.add_edge(Compliance_Check, System_Testing)

# AI Forecasting and Optimize Workflow can start after System Testing
root.order.add_edge(System_Testing, AI_Forecasting)
root.order.add_edge(System_Testing, Optimize_Workflow)

# Market Setup depends on Compliance Check (to verify regulations) and can run concurrently with AI Forecasting and Optimize Workflow
root.order.add_edge(Compliance_Check, Market_Setup)

# Launch Operations depends on AI Forecasting, Optimize Workflow and Market Setup
root.order.add_edge(AI_Forecasting, Launch_Operations)
root.order.add_edge(Optimize_Workflow, Launch_Operations)
root.order.add_edge(Market_Setup, Launch_Operations)