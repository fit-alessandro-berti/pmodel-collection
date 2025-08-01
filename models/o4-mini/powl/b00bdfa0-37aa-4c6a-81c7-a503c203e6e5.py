# Generated from: b00bdfa0-37aa-4c6a-81c7-a503c203e6e5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponics, automated climate control, and AI-driven crop monitoring to maximize yield in limited spaces. The workflow involves site analysis, modular infrastructure assembly, nutrient solution formulation, lighting calibration, pest management, and real-time data analytics. Coordination with local authorities for zoning compliance and sustainability certifications is critical, alongside workforce training in specialized agricultural technology. The process also incorporates waste recycling strategies and market launch preparation, ensuring an eco-friendly, efficient, and scalable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities as POWL transitions
site_survey      = Transition(label='Site Survey')
zoning_check     = Transition(label='Zoning Check')
design_layout    = Transition(label='Design Layout')
module_build     = Transition(label='Module Build')
install_hydro    = Transition(label='Install Hydroponics')
calibrate_light  = Transition(label='Calibrate Lighting')
mix_nutrients    = Transition(label='Mix Nutrients')
climate_setup    = Transition(label='Climate Setup')
compliance_audit = Transition(label='Compliance Audit')
staff_training   = Transition(label='Staff Training')
seed_planting    = Transition(label='Seed Planting')
pest_control     = Transition(label='Pest Control')
data_integration = Transition(label='Data Integration')
waste_recycling  = Transition(label='Waste Recycling')
market_launch    = Transition(label='Market Launch')

# Build the partial order structure
root = StrictPartialOrder(nodes=[
    site_survey, zoning_check, design_layout, module_build,
    install_hydro, calibrate_light, mix_nutrients, climate_setup,
    compliance_audit, staff_training, seed_planting,
    pest_control, data_integration, waste_recycling, market_launch
])

# Sequence for site preparation and compliance
root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, module_build)

# Module assembly leads to infrastructure setup tasks in parallel
root.order.add_edge(module_build, install_hydro)
root.order.add_edge(module_build, calibrate_light)
root.order.add_edge(module_build, mix_nutrients)
root.order.add_edge(module_build, climate_setup)

# All setup tasks must complete before audit
root.order.add_edge(install_hydro, compliance_audit)
root.order.add_edge(calibrate_light, compliance_audit)
root.order.add_edge(mix_nutrients, compliance_audit)
root.order.add_edge(climate_setup, compliance_audit)

# After audit, train staff and start planting
root.order.add_edge(compliance_audit, staff_training)
root.order.add_edge(compliance_audit, seed_planting)
root.order.add_edge(staff_training, seed_planting)

# Planting leads to operational activities in parallel
root.order.add_edge(seed_planting, pest_control)
root.order.add_edge(seed_planting, data_integration)
root.order.add_edge(seed_planting, waste_recycling)

# Final launch after all operations
root.order.add_edge(pest_control, market_launch)
root.order.add_edge(data_integration, market_launch)
root.order.add_edge(waste_recycling, market_launch)