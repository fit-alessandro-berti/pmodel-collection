# Generated from: 7b1a9edd-8c90-4d84-8749-609e2667fee5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, focusing on integrating advanced hydroponic systems, renewable energy sources, and AI-driven crop management. It begins with site analysis and urban zoning compliance, followed by modular structure assembly and environmental control installation. Crop selection is tailored for urban consumer demand, optimizing yield and nutrient density. The process includes water recycling system setup and renewable energy integration to minimize environmental impact. Continuous AI monitoring adjusts lighting, nutrients, and climate to maximize growth efficiency. Finally, harvested produce undergoes quality assessment before packaging and distribution to local markets, ensuring freshness and sustainability throughout the urban supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Zoning_Review = Transition(label='Zoning Review')
Modular_Build = Transition(label='Modular Build')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Energy_Install = Transition(label='Energy Install')
AI_Calibration = Transition(label='AI Calibration')
Crop_Select = Transition(label='Crop Select')
Water_Recycling = Transition(label='Water Recycling')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Growth_Monitor = Transition(label='Growth Monitor')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Dispatch = Transition(label='Market Dispatch')
Waste_Manage = Transition(label='Waste Manage')

# Partial order 1: Site Analysis --> Zoning Review (site prep)
site_prep = StrictPartialOrder(nodes=[Site_Analysis, Zoning_Review])
site_prep.order.add_edge(Site_Analysis, Zoning_Review)

# Partial order 2: Modular Build --> Hydroponic Setup and Energy Install in parallel after modular build
# Hydroponic Setup and Energy Install are concurrent after Modular Build
modular_and_install = StrictPartialOrder(
    nodes=[Modular_Build, Hydroponic_Setup, Energy_Install]
)
modular_and_install.order.add_edge(Modular_Build, Hydroponic_Setup)
modular_and_install.order.add_edge(Modular_Build, Energy_Install)

# AI Calibration occurs after Hydroponic Setup and Energy Install both finish
ai_cal = StrictPartialOrder(nodes=[Hydroponic_Setup, Energy_Install, AI_Calibration])
ai_cal.order.add_edge(Hydroponic_Setup, AI_Calibration)
ai_cal.order.add_edge(Energy_Install, AI_Calibration)

# Crop Select next
crop_select = Transition(label='Crop Select')

# Water Recycling setup concurrent with Climate Control and Nutrient Mix after AI Calibration and Crop Select
# AI Calibration and Crop Select run sequentially, then these three concurrent
crop_select_phase = StrictPartialOrder(nodes=[AI_Calibration, Crop_Select])
crop_select_phase.order.add_edge(AI_Calibration, Crop_Select)

post_crop_parallel = StrictPartialOrder(
    nodes=[Water_Recycling, Climate_Control, Nutrient_Mix]
)  # concurrent nodes

# Growth Monitor after all three concurrent finish
growth_monitor = Transition(label='Growth Monitor')

post_modern_grow = StrictPartialOrder(
    nodes=[Water_Recycling, Climate_Control, Nutrient_Mix, growth_monitor]
)
post_modern_grow.order.add_edge(Water_Recycling, growth_monitor)
post_modern_grow.order.add_edge(Climate_Control, growth_monitor)
post_modern_grow.order.add_edge(Nutrient_Mix, growth_monitor)

# Quality check after growth monitoring
quality_check = Quality_Check

# Packaging prep concurrent with Waste Manage after Quality Check
pack_waste = StrictPartialOrder(nodes=[Packaging_Prep, Waste_Manage, quality_check])
pack_waste.order.add_edge(quality_check, Packaging_Prep)
pack_waste.order.add_edge(quality_check, Waste_Manage)

# Market Dispatch after Packaging Prep
final_dispatch = StrictPartialOrder(nodes=[Packaging_Prep, Market_Dispatch])
final_dispatch.order.add_edge(Packaging_Prep, Market_Dispatch)

# Combine pack_waste and final_dispatch, noting Packaging_Prep is in both so we reuse the same node(s)
# We need to compose pack_waste and final_dispatch carefully; include Waste_Manage and Market_Dispatch, order Packaging_Prep -> Market_Dispatch
pack_waste_dispatch = StrictPartialOrder(
    nodes=[Packaging_Prep, Waste_Manage, Market_Dispatch]
)
pack_waste_dispatch.order.add_edge(Packaging_Prep, Market_Dispatch)

# Build overall process partial orders and edges between them:
# site_prep --> modular_and_install
# modular_and_install --> ai_cal (covered within ai_cal)
# ai_cal + crop_select_phase --> post_crop_parallel (concurrent Water_Recycling etc)
# post_crop_parallel --> growth_monitor (covered)
# growth_monitor --> quality_check
# quality_check --> packaging & waste manage
# packaging --> market dispatch

# Compose main parts step-wise:

# Step 1 + 2: site_prep --> modular_and_install
step1_2 = StrictPartialOrder(
    nodes=[site_prep, modular_and_install]
)
step1_2.order.add_edge(site_prep, modular_and_install)

# But to keep consistency, site_prep and modular_and_install are themselves partial orders
# so we treat them as nodes, but for POWL, nodes are transitions or operators
# We must flatten or treat them as nodes only if we embed partially ordered nodes or as children of root

# To simplify, build a layered model using OperatorPOWL and StrictPartialOrder

# Build modular_and_install as PO
modular_install_po = modular_and_install

# Build ai_cal + crop_select_phase sequentially:
ai_crop_seq = StrictPartialOrder(nodes=[ai_cal, crop_select])
ai_crop_seq.order.add_edge(ai_cal, crop_select)

# post_crop_parallel + growth_monitor
post_crop_gm = post_modern_grow

# quality + packaging+waste + market dispatch
pack_waste_dispatch_po = StrictPartialOrder(
    nodes=[quality_check, Packaging_Prep, Waste_Manage, Market_Dispatch]
)
pack_waste_dispatch_po.order.add_edge(quality_check, Packaging_Prep)
pack_waste_dispatch_po.order.add_edge(quality_check, Waste_Manage)
pack_waste_dispatch_po.order.add_edge(Packaging_Prep, Market_Dispatch)

# Build full sequence combining all parts:

# Create a partial order of all major steps as nodes and add edges representing causal relations

root = StrictPartialOrder(
    nodes=[
        Site_Analysis,
        Zoning_Review,
        Modular_Build,
        Hydroponic_Setup,
        Energy_Install,
        AI_Calibration,
        Crop_Select,
        Water_Recycling,
        Climate_Control,
        Nutrient_Mix,
        Growth_Monitor,
        Quality_Check,
        Packaging_Prep,
        Market_Dispatch,
        Waste_Manage
    ]
)

# order edges as per process description:

# Site Analysis --> Zoning Review
root.order.add_edge(Site_Analysis, Zoning_Review)

# Zoning Review --> Modular Build
root.order.add_edge(Zoning_Review, Modular_Build)

# Modular Build --> Hydroponic Setup
root.order.add_edge(Modular_Build, Hydroponic_Setup)

# Modular Build --> Energy Install (parallel after Modular Build)
root.order.add_edge(Modular_Build, Energy_Install)

# Hydroponic Setup --> AI Calibration
root.order.add_edge(Hydroponic_Setup, AI_Calibration)

# Energy Install --> AI Calibration (AI Calibration waits for both setups)
root.order.add_edge(Energy_Install, AI_Calibration)

# AI Calibration --> Crop Select
root.order.add_edge(AI_Calibration, Crop_Select)

# Crop Select --> Water Recycling (concurrent branch start)
root.order.add_edge(Crop_Select, Water_Recycling)

# Crop Select --> Climate Control
root.order.add_edge(Crop_Select, Climate_Control)

# Crop Select --> Nutrient Mix
root.order.add_edge(Crop_Select, Nutrient_Mix)

# Water Recycling --> Growth Monitor
root.order.add_edge(Water_Recycling, Growth_Monitor)

# Climate Control --> Growth Monitor
root.order.add_edge(Climate_Control, Growth_Monitor)

# Nutrient Mix --> Growth Monitor
root.order.add_edge(Nutrient_Mix, Growth_Monitor)

# Growth Monitor --> Quality Check
root.order.add_edge(Growth_Monitor, Quality_Check)

# Quality Check --> Packaging Prep
root.order.add_edge(Quality_Check, Packaging_Prep)

# Quality Check --> Waste Manage
root.order.add_edge(Quality_Check, Waste_Manage)

# Packaging Prep --> Market Dispatch
root.order.add_edge(Packaging_Prep, Market_Dispatch)