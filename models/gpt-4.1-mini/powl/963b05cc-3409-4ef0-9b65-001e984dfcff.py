# Generated from: 963b05cc-3409-4ef0-9b65-001e984dfcff.json
# Description: This process outlines the detailed steps required to establish a sustainable urban rooftop farming operation. It involves initial site assessment, regulatory compliance checks, soil and structural analysis, procurement of specialized modular planting systems, installation of automated irrigation and nutrient delivery, integration of renewable energy sources, ongoing crop monitoring using IoT sensors, pest management with eco-friendly methods, periodic yield assessments, and community engagement for educational workshops. The goal is to maximize crop yield while maintaining environmental sustainability and building local food resilience in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Load_Testing = Transition(label='Load Testing')
Soil_Sampling = Transition(label='Soil Sampling')
System_Design = Transition(label='System Design')
Module_Assembly = Transition(label='Module Assembly')
Irrigation_Setup = Transition(label='Irrigation Setup')
Energy_Integration = Transition(label='Energy Integration')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Dosing = Transition(label='Nutrient Dosing')
Planting_Phase = Transition(label='Planting Phase')
Pest_Control = Transition(label='Pest Control')
Data_Monitoring = Transition(label='Data Monitoring')
Yield_Analysis = Transition(label='Yield Analysis')
Community_Outreach = Transition(label='Community Outreach')

# Create the partial order nodes list
nodes = [
    Site_Survey,
    Permit_Review,
    Load_Testing,
    Soil_Sampling,
    System_Design,
    Module_Assembly,
    Irrigation_Setup,
    Energy_Integration,
    Sensor_Install,
    Nutrient_Dosing,
    Planting_Phase,
    Pest_Control,
    Data_Monitoring,
    Yield_Analysis,
    Community_Outreach,
]

# Construct the StrictPartialOrder
root = StrictPartialOrder(nodes=nodes)

# Add edges to capture the sequential and partial ordering based on the description

# Phase 1: Initial assessments and design
root.order.add_edge(Site_Survey, Permit_Review)
root.order.add_edge(Permit_Review, Load_Testing)
root.order.add_edge(Load_Testing, Soil_Sampling)
root.order.add_edge(Soil_Sampling, System_Design)

# Phase 2: Procurement and assembly of systems
root.order.add_edge(System_Design, Module_Assembly)

# Phase 3: Installation of automated irrigation and energy integration (concurrent)
root.order.add_edge(Module_Assembly, Irrigation_Setup)
root.order.add_edge(Module_Assembly, Energy_Integration)

# Irrigation_Setup and Energy_Integration can happen concurrently, no order between them

# Both must precede sensor install and nutrient dosing (which happen in parallel)
root.order.add_edge(Irrigation_Setup, Sensor_Install)
root.order.add_edge(Energy_Integration, Sensor_Install)
root.order.add_edge(Irrigation_Setup, Nutrient_Dosing)
root.order.add_edge(Energy_Integration, Nutrient_Dosing)

# Sensor_Install and Nutrient_Dosing happen in parallel, both precede planting phase
root.order.add_edge(Sensor_Install, Planting_Phase)
root.order.add_edge(Nutrient_Dosing, Planting_Phase)

# Planting phase followed by pest control and data monitoring in parallel
root.order.add_edge(Planting_Phase, Pest_Control)
root.order.add_edge(Planting_Phase, Data_Monitoring)

# Pest control and data monitoring happen concurrently, both precede yield analysis
root.order.add_edge(Pest_Control, Yield_Analysis)
root.order.add_edge(Data_Monitoring, Yield_Analysis)

# Yield analysis precedes community outreach
root.order.add_edge(Yield_Analysis, Community_Outreach)