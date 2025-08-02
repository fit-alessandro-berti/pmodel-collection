# Generated from: b00bdfa0-37aa-4c6a-81c7-a503c203e6e5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponics, automated climate control, and AI-driven crop monitoring to maximize yield in limited spaces. The workflow involves site analysis, modular infrastructure assembly, nutrient solution formulation, lighting calibration, pest management, and real-time data analytics. Coordination with local authorities for zoning compliance and sustainability certifications is critical, alongside workforce training in specialized agricultural technology. The process also incorporates waste recycling strategies and market launch preparation, ensuring an eco-friendly, efficient, and scalable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
design_layout = Transition(label='Design Layout')
module_build = Transition(label='Module Build')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_lighting = Transition(label='Calibrate Lighting')
mix_nutrients = Transition(label='Mix Nutrients')
seed_planting = Transition(label='Seed Planting')
climate_setup = Transition(label='Climate Setup')
pest_control = Transition(label='Pest Control')
data_integration = Transition(label='Data Integration')
staff_training = Transition(label='Staff Training')
waste_recycling = Transition(label='Waste Recycling')
compliance_audit = Transition(label='Compliance Audit')
market_launch = Transition(label='Market Launch')

# Partial orders per logical grouping

# Initial site analysis group: Site Survey --> Zoning Check
site_analysis = StrictPartialOrder(nodes=[site_survey, zoning_check])
site_analysis.order.add_edge(site_survey, zoning_check)

# Design and build infrastructure group:
# Design Layout --> Module Build --> Install Hydroponics
design_build = StrictPartialOrder(nodes=[design_layout, module_build, install_hydroponics])
design_build.order.add_edge(design_layout, module_build)
design_build.order.add_edge(module_build, install_hydroponics)

# Calibration and nutrient preparation group:
# Calibrate Lighting and Mix Nutrients can be done concurrently
calib_mix = StrictPartialOrder(nodes=[calibrate_lighting, mix_nutrients])
# no edges, concurrent

# Planting and climate setup group:
# Seed Planting --> Climate Setup
plant_climate = StrictPartialOrder(nodes=[seed_planting, climate_setup])
plant_climate.order.add_edge(seed_planting, climate_setup)

# Pest Control --> Data Integration (monitoring)
pest_data = StrictPartialOrder(nodes=[pest_control, data_integration])
pest_data.order.add_edge(pest_control, data_integration)

# Staff Training can happen concurrently with pest_data
# Waste Recycling and Compliance Audit can happen after pest_data and staff training in any order
# Market Launch is last, after compliance audit

# staff_training concurrent with pest_data
staff_pest_data = StrictPartialOrder(nodes=[staff_training, pest_data])
# since pest_data is itself a StrictPartialOrder, we make sure to include its nodes and edges

# We flatten pest_data nodes and edges inside this PO to avoid nested PO inside PO nodes
staff_pest_data = StrictPartialOrder(nodes=[staff_training, pest_control, data_integration])
staff_pest_data.order.add_edge(pest_control, data_integration)

# Waste Recycling and Compliance Audit after that, can be concurrent between them but after pest_data and staff training
waste_compliance = StrictPartialOrder(nodes=[waste_recycling, compliance_audit])
# no edges, concurrent

# Final part: Market Launch at the end after waste_compliance
final_phase = StrictPartialOrder(nodes=[waste_recycling, compliance_audit, market_launch])
final_phase.order.add_edge(waste_recycling, market_launch)
final_phase.order.add_edge(compliance_audit, market_launch)

# Now combine all higher level phases in partial order representing entire process

# The big process PO nodes (sub-processes or activities):

# 1. site_analysis
# 2. design_build
# 3. calib_mix
# 4. plant_climate
# 5. staff_pest_data
# 6. waste_compliance
# 7. market_launch (but it's inside final_phase; include final_phase)

# We will build top level PO with nodes:
# site_analysis, design_build, calib_mix, plant_climate, staff_pest_data, waste_compliance, market_launch

# Actually since market_launch is last only, replace market_launch node by final_phase, which contains waste_compliance and market_launch.

root = StrictPartialOrder(
    nodes=[
        site_analysis,
        zoning_check,  # already included in site_analysis, do not re-add
        design_build,
        calib_mix,
        plant_climate,
        staff_pest_data,
        waste_compliance,
        final_phase
    ]
)

# Add top-level edges representing process flow and dependencies:

# site_analysis --> design_build
root.order.add_edge(site_analysis, design_build)

# design_build --> calib_mix
root.order.add_edge(design_build, calib_mix)

# calib_mix --> plant_climate
root.order.add_edge(calib_mix, plant_climate)

# plant_climate --> staff_pest_data
root.order.add_edge(plant_climate, staff_pest_data)

# staff_pest_data --> waste_compliance
root.order.add_edge(staff_pest_data, waste_compliance)

# waste_compliance --> final_phase
root.order.add_edge(waste_compliance, final_phase)

# Actually final_phase contains waste_recycling, compliance_audit, market_launch
# We already added waste_compliance and final_phase as separate nodes; to avoid duplication,
# let's remove waste_compliance node, and keep final_phase only:

# Refactor: remove waste_compliance node, keep final_phase as it contains waste_recycling, compliance audit, and market launch.

root = StrictPartialOrder(
    nodes=[
        site_analysis,
        design_build,
        calib_mix,
        plant_climate,
        staff_pest_data,
        final_phase,
    ]
)
root.order.add_edge(site_analysis, design_build)
root.order.add_edge(design_build, calib_mix)
root.order.add_edge(calib_mix, plant_climate)
root.order.add_edge(plant_climate, staff_pest_data)
root.order.add_edge(staff_pest_data, final_phase)