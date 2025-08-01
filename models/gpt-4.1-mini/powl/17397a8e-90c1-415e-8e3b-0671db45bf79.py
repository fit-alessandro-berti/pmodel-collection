# Generated from: 17397a8e-90c1-415e-8e3b-0671db45bf79.json
# Description: This process outlines the comprehensive steps required to establish a sustainable urban rooftop farm. It involves evaluating roof conditions, securing permits, designing modular growing units, sourcing organic soil and seeds, installing irrigation and lighting systems, implementing pest control measures, training local staff, and creating a distribution framework for fresh produce. The workflow ensures compliance with safety regulations, maximizes space utilization, and promotes community engagement through workshops and seasonal events. Continuous monitoring and maintenance guarantee optimal plant growth and yield, supporting urban food security and environmental benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Roof_Survey = Transition(label='Roof Survey')
Permit_Check = Transition(label='Permit Check')
Design_Layout = Transition(label='Design Layout')
Module_Build = Transition(label='Module Build')
Soil_Sourcing = Transition(label='Soil Sourcing')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Install = Transition(label='Irrigation Install')
Lighting_Setup = Transition(label='Lighting Setup')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Safety_Audit = Transition(label='Safety Audit')
Planting_Phase = Transition(label='Planting Phase')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Community_Event = Transition(label='Community Event')
Produce_Delivery = Transition(label='Produce Delivery')

# Create the partial order nodes
nodes = [
    Roof_Survey,
    Permit_Check,
    Safety_Audit,
    Design_Layout,
    Module_Build,
    Soil_Sourcing,
    Seed_Selection,
    Irrigation_Install,
    Lighting_Setup,
    Pest_Control,
    Staff_Training,
    Planting_Phase,
    Growth_Monitor,
    Harvest_Plan,
    Community_Event,
    Produce_Delivery
]

root = StrictPartialOrder(nodes=nodes)

# Add edges representing process dependencies:

# Initial evaluation steps to be done in sequence:
root.order.add_edge(Roof_Survey, Permit_Check)      # Roof Survey --> Permit Check
root.order.add_edge(Permit_Check, Safety_Audit)     # Permit Check --> Safety Audit

# Safety audit must finish before design + build modules:
root.order.add_edge(Safety_Audit, Design_Layout)
root.order.add_edge(Safety_Audit, Soil_Sourcing)    # Soil Sourcing depends on safety compliance as well
root.order.add_edge(Safety_Audit, Seed_Selection)

# Design flows into building modules:
root.order.add_edge(Design_Layout, Module_Build)

# Soil and Seed sourcing can be done in parallel, but both must complete before planting:
root.order.add_edge(Soil_Sourcing, Planting_Phase)
root.order.add_edge(Seed_Selection, Planting_Phase)

# Install irrigation and lighting after module build:
root.order.add_edge(Module_Build, Irrigation_Install)
root.order.add_edge(Module_Build, Lighting_Setup)

# Irrigation and Lighting must finish before planting:
root.order.add_edge(Irrigation_Install, Planting_Phase)
root.order.add_edge(Lighting_Setup, Planting_Phase)

# Pest control and Staff training after planting starts but before growth monitoring:
root.order.add_edge(Planting_Phase, Pest_Control)
root.order.add_edge(Planting_Phase, Staff_Training)

# Pest control and Staff training must complete before growth monitoring:
root.order.add_edge(Pest_Control, Growth_Monitor)
root.order.add_edge(Staff_Training, Growth_Monitor)

# Growth monitoring before harvest planning:
root.order.add_edge(Growth_Monitor, Harvest_Plan)

# Harvest planning before community event and produce delivery:
root.order.add_edge(Harvest_Plan, Community_Event)
root.order.add_edge(Harvest_Plan, Produce_Delivery)

# Community event and produce delivery can be concurrent:
# No edge between Community_Event and Produce_Delivery

# The above partial order models the overall dependencies and concurrency.
