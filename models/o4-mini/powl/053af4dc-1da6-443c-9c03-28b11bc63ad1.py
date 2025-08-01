# Generated from: 053af4dc-1da6-443c-9c03-28b11bc63ad1.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental control installation, hydroponic system setup, seed selection, and growth monitoring. The process also covers integration of IoT sensors for real-time data collection, automation of nutrient delivery, pest management protocols, and energy optimization strategies. Stakeholder coordination, regulatory compliance checks, and market launch planning ensure a sustainable and scalable urban agriculture solution that maximizes yield in limited space while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
structural_audit  = Transition(label='Structural Audit')
design_layout     = Transition(label='Design Layout')
install_hvac      = Transition(label='Install HVAC')
setup_hydro       = Transition(label='Setup Hydroponics')
seed_selection    = Transition(label='Seed Selection')
sensor_install    = Transition(label='Sensor Install')
data_integration  = Transition(label='Data Integration')
automation_setup  = Transition(label='Automation Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_control      = Transition(label='Pest Control')
energy_audit      = Transition(label='Energy Audit')
planting_cycle    = Transition(label='Planting Cycle')
compliance_check  = Transition(label='Compliance Check')
staff_training    = Transition(label='Staff Training')
market_launch     = Transition(label='Market Launch')

# Build the monitoring sub‐process (to be looped)
mon_data_int = Transition(label='Data Integration')
mon_nutr_mix = Transition(label='Nutrient Mix')
mon_pest     = Transition(label='Pest Control')
mon_energy   = Transition(label='Energy Audit')

monitorPO = StrictPartialOrder(
    nodes=[mon_data_int, mon_nutr_mix, mon_pest, mon_energy]
)
monitorPO.order.add_edge(mon_data_int, mon_nutr_mix)
monitorPO.order.add_edge(mon_nutr_mix, mon_pest)
monitorPO.order.add_edge(mon_pest, mon_energy)

# Build the loop around the planting cycle and monitoring
planting_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[planting_cycle, monitorPO]
)

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, structural_audit, design_layout,
        install_hvac, setup_hydro, seed_selection,
        sensor_install, data_integration, automation_setup,
        nutrient_mix, pest_control, energy_audit,
        planting_cycle, monitorPO, planting_loop,
        compliance_check, staff_training, market_launch
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(site_survey,       design_layout)
root.order.add_edge(structural_audit,  design_layout)
root.order.add_edge(design_layout,     install_hvac)
root.order.add_edge(install_hvac,      setup_hydro)
root.order.add_edge(setup_hydro,       seed_selection)
root.order.add_edge(seed_selection,    sensor_install)
root.order.add_edge(sensor_install,    data_integration)
root.order.add_edge(data_integration,  automation_setup)
root.order.add_edge(automation_setup,  nutrient_mix)
root.order.add_edge(nutrient_mix,      pest_control)
root.order.add_edge(pest_control,      energy_audit)
root.order.add_edge(energy_audit,      planting_loop)
root.order.add_edge(planting_loop,     compliance_check)
root.order.add_edge(compliance_check,  staff_training)
root.order.add_edge(staff_training,    market_launch)