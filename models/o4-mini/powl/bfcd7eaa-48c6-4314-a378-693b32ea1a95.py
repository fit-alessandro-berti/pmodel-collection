# Generated from: bfcd7eaa-48c6-4314-a378-693b32ea1a95.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, modular structure design, climate control integration, hydroponic system installation, nutrient solution calibration, automated lighting setup, crop selection, growth monitoring, pest management, yield forecasting, energy optimization, waste recycling, market analysis, and finally, distribution logistics to ensure fresh produce reaches local markets efficiently. Each step requires coordination across engineering, agricultural science, and logistics teams to maximize space utilization and sustainability in a densely populated environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey         = Transition(label='Site Survey')
design_layout       = Transition(label='Design Layout')
structure_build     = Transition(label='Structure Build')
climate_setup       = Transition(label='Climate Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_prep       = Transition(label='Nutrient Prep')
lighting_config     = Transition(label='Lighting Config')
crop_select         = Transition(label='Crop Select')
growth_monitor      = Transition(label='Growth Monitor')
pest_control        = Transition(label='Pest Control')
yield_forecast      = Transition(label='Yield Forecast')
energy_audit        = Transition(label='Energy Audit')
waste_manage        = Transition(label='Waste Manage')
market_study        = Transition(label='Market Study')
logistics_plan      = Transition(label='Logistics Plan')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, structure_build,
    climate_setup, hydroponics_install, nutrient_prep, lighting_config,
    crop_select, growth_monitor, pest_control, yield_forecast,
    energy_audit, waste_manage, market_study, logistics_plan
])

# 1. Core sequential flow: Site Survey → Design Layout → Structure Build
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)

# 2. After structure build, four engineering tasks can execute in parallel:
for eng in [climate_setup, hydroponics_install, nutrient_prep, lighting_config]:
    root.order.add_edge(structure_build, eng)
    # They all must finish before Crop Select
    root.order.add_edge(eng, crop_select)

# 3. Crop Select leads to concurrent Growth Monitor and Pest Control
root.order.add_edge(crop_select, growth_monitor)
root.order.add_edge(crop_select, pest_control)

# 4. Yield Forecast depends on both monitoring and pest management
root.order.add_edge(growth_monitor, yield_forecast)
root.order.add_edge(pest_control, yield_forecast)

# 5. After forecasting, three tasks run in parallel, all feeding into Logistics Plan
for post in [energy_audit, waste_manage, market_study]:
    root.order.add_edge(yield_forecast, post)
    root.order.add_edge(post, logistics_plan)