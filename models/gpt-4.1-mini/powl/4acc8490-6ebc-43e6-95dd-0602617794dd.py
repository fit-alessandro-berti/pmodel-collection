# Generated from: 4acc8490-6ebc-43e6-95dd-0602617794dd.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It integrates environmental assessments, structural evaluations, community engagement, and regulatory compliance. Starting from site analysis to crop selection, irrigation planning, and installation of renewable energy systems, the process ensures optimized resource use and maximizes yield while fostering urban green spaces. The workflow also includes ongoing monitoring, pest management, and periodic yield assessment to maintain long-term productivity and environmental benefits within a city setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Soil_Sampling = Transition(label='Soil Sampling')
Water_Analysis = Transition(label='Water Analysis')
Crop_Research = Transition(label='Crop Research')
Energy_Audit = Transition(label='Energy Audit')
Permit_Filing = Transition(label='Permit Filing')
Design_Layout = Transition(label='Design Layout')
Irrigation_Setup = Transition(label='Irrigation Setup')
Solar_Install = Transition(label='Solar Install')
Community_Meet = Transition(label='Community Meet')
Supplier_Sourcing = Transition(label='Supplier Sourcing')
Planting_Plan = Transition(label='Planting Plan')
Pest_Control = Transition(label='Pest Control')
Yield_Monitor = Transition(label='Yield Monitor')
Waste_Manage = Transition(label='Waste Manage')
Harvest_Schedule = Transition(label='Harvest Schedule')

# Initial assessment: Site Survey leads to two parallel assessments Load Testing & Soil Sampling
assessment_PO = StrictPartialOrder(nodes=[Load_Testing, Soil_Sampling])
# concurrent means no order edges, so Load Testing & Soil Sampling concurrent; both follow Site Survey
assessment_root = StrictPartialOrder(nodes=[Site_Survey, assessment_PO])
assessment_root.order.add_edge(Site_Survey, assessment_PO)

# Water Analysis depends on Soil Sampling
water_PO = StrictPartialOrder(nodes=[Soil_Sampling, Water_Analysis])
water_PO.order.add_edge(Soil_Sampling, Water_Analysis)

# Crop Research depends on Soil Sampling and Water Analysis (both)
crop_PO = StrictPartialOrder(nodes=[Water_Analysis, Crop_Research])
crop_PO.order.add_edge(Water_Analysis, Crop_Research)

# Energy Audit independent but can start after Site Survey
energy_PO = StrictPartialOrder(nodes=[Site_Survey, Energy_Audit])
energy_PO.order.add_edge(Site_Survey, Energy_Audit)

# Permit Filing depends on Energy Audit and Load Testing (both)
permit_PO = StrictPartialOrder(nodes=[Load_Testing, Energy_Audit, Permit_Filing])
permit_PO.order.add_edge(Load_Testing, Permit_Filing)
permit_PO.order.add_edge(Energy_Audit, Permit_Filing)

# Design Layout depends on Crop Research and Permit Filing
design_PO = StrictPartialOrder(nodes=[Crop_Research, Permit_Filing, Design_Layout])
design_PO.order.add_edge(Crop_Research, Design_Layout)
design_PO.order.add_edge(Permit_Filing, Design_Layout)

# Community Meet and Supplier Sourcing can be done concurrently after Design Layout
community_supplier_PO = StrictPartialOrder(nodes=[Community_Meet, Supplier_Sourcing])
# They both depend on Design Layout
community_supplier_root = StrictPartialOrder(nodes=[Design_Layout, community_supplier_PO])
community_supplier_root.order.add_edge(Design_Layout, community_supplier_PO)

# Planting Plan depends on Community Meet and Supplier Sourcing
planting_PO = StrictPartialOrder(nodes=[Community_Meet, Supplier_Sourcing, Planting_Plan])
planting_PO.order.add_edge(Community_Meet, Planting_Plan)
planting_PO.order.add_edge(Supplier_Sourcing, Planting_Plan)

# Irrigation Setup and Solar Install can run in parallel after Planting Plan and Design Layout (assume irrigation depends on Planting Plan, solar on Design Layout)
irrigation_PO = StrictPartialOrder(nodes=[Planting_Plan, Irrigation_Setup])
irrigation_PO.order.add_edge(Planting_Plan, Irrigation_Setup)

solar_PO = StrictPartialOrder(nodes=[Design_Layout, Solar_Install])
solar_PO.order.add_edge(Design_Layout, Solar_Install)

# Combine Irrigation and Solar as concurrent nodes
install_PO = StrictPartialOrder(nodes=[irrigation_PO, solar_PO])

# Pest Control depends on Planting Plan and Supplier Sourcing (pests occur after planting and supply)
pest_PO = StrictPartialOrder(nodes=[Planting_Plan, Supplier_Sourcing, Pest_Control])
pest_PO.order.add_edge(Planting_Plan, Pest_Control)
pest_PO.order.add_edge(Supplier_Sourcing, Pest_Control)

# Yield Monitor, Waste Manage, Harvest Schedule are ongoing/terminal activities
# Yield Monitor and Waste Manage can run concurrently after Pest Control and Irrigation Setup & Solar Install
monitoring_PO = StrictPartialOrder(nodes=[Yield_Monitor, Waste_Manage])
# Monitoring depends on installations and pest control
monitoring_root = StrictPartialOrder(
    nodes=[install_PO, pest_PO, monitoring_PO]
)
monitoring_root.order.add_edge(install_PO, monitoring_PO)
monitoring_root.order.add_edge(pest_PO, monitoring_PO)

# Harvest Schedule depends on Planting Plan and Yield Monitor (can't harvest before planting and monitoring)
harvest_PO = StrictPartialOrder(nodes=[Planting_Plan, Yield_Monitor, Harvest_Schedule])
harvest_PO.order.add_edge(Planting_Plan, Harvest_Schedule)
harvest_PO.order.add_edge(Yield_Monitor, Harvest_Schedule)

# Combine all to root, as a large partial order:
root = StrictPartialOrder(
    nodes=[
        Site_Survey,
        Load_Testing,
        Soil_Sampling,
        Water_Analysis,
        Crop_Research,
        Energy_Audit,
        Permit_Filing,
        Design_Layout,
        Community_Meet,
        Supplier_Sourcing,
        Planting_Plan,
        Irrigation_Setup,
        Solar_Install,
        Pest_Control,
        Yield_Monitor,
        Waste_Manage,
        Harvest_Schedule,
    ]
)

# Add edges for dependencies as per above
root.order.add_edge(Site_Survey, Load_Testing)
root.order.add_edge(Site_Survey, Soil_Sampling)

root.order.add_edge(Soil_Sampling, Water_Analysis)
root.order.add_edge(Water_Analysis, Crop_Research)

root.order.add_edge(Site_Survey, Energy_Audit)

root.order.add_edge(Load_Testing, Permit_Filing)
root.order.add_edge(Energy_Audit, Permit_Filing)

root.order.add_edge(Crop_Research, Design_Layout)
root.order.add_edge(Permit_Filing, Design_Layout)

root.order.add_edge(Design_Layout, Community_Meet)
root.order.add_edge(Design_Layout, Supplier_Sourcing)

root.order.add_edge(Community_Meet, Planting_Plan)
root.order.add_edge(Supplier_Sourcing, Planting_Plan)

root.order.add_edge(Planting_Plan, Irrigation_Setup)
root.order.add_edge(Design_Layout, Solar_Install)

root.order.add_edge(Planting_Plan, Pest_Control)
root.order.add_edge(Supplier_Sourcing, Pest_Control)

root.order.add_edge(Irrigation_Setup, Yield_Monitor)
root.order.add_edge(Solar_Install, Yield_Monitor)
root.order.add_edge(Pest_Control, Yield_Monitor)
root.order.add_edge(Irrigation_Setup, Waste_Manage)
root.order.add_edge(Solar_Install, Waste_Manage)
root.order.add_edge(Pest_Control, Waste_Manage)

root.order.add_edge(Planting_Plan, Harvest_Schedule)
root.order.add_edge(Yield_Monitor, Harvest_Schedule)