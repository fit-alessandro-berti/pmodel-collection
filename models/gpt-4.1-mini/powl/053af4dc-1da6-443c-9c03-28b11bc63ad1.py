# Generated from: 053af4dc-1da6-443c-9c03-28b11bc63ad1.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental control installation, hydroponic system setup, seed selection, and growth monitoring. The process also covers integration of IoT sensors for real-time data collection, automation of nutrient delivery, pest management protocols, and energy optimization strategies. Stakeholder coordination, regulatory compliance checks, and market launch planning ensure a sustainable and scalable urban agriculture solution that maximizes yield in limited space while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
design_layout = Transition(label='Design Layout')

install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')

seed_selection = Transition(label='Seed Selection')
planting_cycle = Transition(label='Planting Cycle')

sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')

nutrient_mix = Transition(label='Nutrient Mix')
automation_setup = Transition(label='Automation Setup')

pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')

compliance_check = Transition(label='Compliance Check')
market_launch = Transition(label='Market Launch')

staff_training = Transition(label='Staff Training')

# Model each logical sub-process as a partial order or sequence

# 1. Initial site assessment phase: Site Survey then Structural Audit then Design Layout
site_assessment = StrictPartialOrder(nodes=[site_survey, structural_audit, design_layout])
site_assessment.order.add_edge(site_survey, structural_audit)
site_assessment.order.add_edge(structural_audit, design_layout)

# 2. Installation phase: Install HVAC then Setup Hydroponics (sequential)
installation = StrictPartialOrder(nodes=[install_hvac, setup_hydroponics])
installation.order.add_edge(install_hvac, setup_hydroponics)

# 3. Plant preparation: Seed Selection then looping Planting Cycle (model planting cycle as a loop to reflect repeated growth monitoring and planting)
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, staff_training])  
# Loop: execute planting_cycle, then choose to exit or do staff_training then again planting_cycle

plant_preparation = StrictPartialOrder(nodes=[seed_selection, planting_loop])
plant_preparation.order.add_edge(seed_selection, planting_loop)

# 4. IoT & data integration: Sensor Install then Data Integration
iot_integration = StrictPartialOrder(nodes=[sensor_install, data_integration])
iot_integration.order.add_edge(sensor_install, data_integration)

# 5. Nutrient and automation phase: Nutrient Mix then Automation Setup
nutrient_automation = StrictPartialOrder(nodes=[nutrient_mix, automation_setup])
nutrient_automation.order.add_edge(nutrient_mix, automation_setup)

# 6. Pest and energy management, these can be done concurrently after automation setup
pest_energy = StrictPartialOrder(nodes=[pest_control, energy_audit])
# No order edges, concurrent

# 7. Compliance and Market Launch phase: Compliance Check then Market Launch
compliance_market = StrictPartialOrder(nodes=[compliance_check, market_launch])
compliance_market.order.add_edge(compliance_check, market_launch)

# Combine phases respecting their logical order:
# site_assessment --> installation --> plant_preparation --> iot_integration --> nutrient_automation --> pest_energy --> compliance_market
# Using a top-level partial order connecting these phases

root = StrictPartialOrder(
    nodes=[
        site_assessment,
        installation,
        plant_preparation,
        iot_integration,
        nutrient_automation,
        pest_energy,
        compliance_market
    ]
)

root.order.add_edge(site_assessment, installation)
root.order.add_edge(installation, plant_preparation)
root.order.add_edge(plant_preparation, iot_integration)
root.order.add_edge(iot_integration, nutrient_automation)
root.order.add_edge(nutrient_automation, pest_energy)
root.order.add_edge(pest_energy, compliance_market)