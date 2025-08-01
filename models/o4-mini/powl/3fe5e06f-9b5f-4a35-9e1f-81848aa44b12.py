# Generated from: 3fe5e06f-9b5f-4a35-9e1f-81848aa44b12.json
# Description: This process outlines the integration of urban vertical farming systems within existing city infrastructure to optimize local food production, reduce transportation emissions, and promote sustainable agriculture. It involves site assessment, modular farm installation, IoT sensor deployment for environment monitoring, nutrient recycling, energy management, crop scheduling, automated harvesting, quality assurance, data analytics, community engagement, and regulatory compliance. The process ensures seamless coordination between technology providers, municipal authorities, and local communities, fostering innovation while addressing urban food security and ecological impact through continuous improvement and scalability planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
permit_review    = Transition(label='Permit Review')
modular_install  = Transition(label='Modular Install')
sensor_setup     = Transition(label='Sensor Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
energy_sync      = Transition(label='Energy Sync')
crop_plan        = Transition(label='Crop Plan')
irrigation_tune  = Transition(label='Irrigation Tune')
harvest_automate = Transition(label='Harvest Automate')
quality_check    = Transition(label='Quality Check')

# Define the loop body: data analysis and waste recycling
data_analysis  = Transition(label='Data Analysis')
waste_recycle  = Transition(label='Waste Recycle')
A = StrictPartialOrder(nodes=[data_analysis, waste_recycle])
A.order.add_edge(data_analysis, waste_recycle)

# Define the loop redo tasks: community meeting, compliance audit, scaling strategy
community_meet    = Transition(label='Community Meet')
compliance_audit  = Transition(label='Compliance Audit')
scale_strategy    = Transition(label='Scale Strategy')
B = StrictPartialOrder(nodes=[community_meet, compliance_audit, scale_strategy])
B.order.add_edge(community_meet,   compliance_audit)
B.order.add_edge(compliance_audit, scale_strategy)

# Construct the LOOP operator for continuous improvement and scalability
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, design_layout, permit_review,
        modular_install, sensor_setup,    nutrient_mix,
        energy_sync,  crop_plan,         irrigation_tune,
        harvest_automate, quality_check, loop
    ]
)

# Add the sequential control‐flow dependencies
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    permit_review)
root.order.add_edge(permit_review,    modular_install)
root.order.add_edge(modular_install,  sensor_setup)
root.order.add_edge(sensor_setup,     nutrient_mix)
root.order.add_edge(nutrient_mix,     energy_sync)
root.order.add_edge(energy_sync,      crop_plan)
root.order.add_edge(crop_plan,        irrigation_tune)
root.order.add_edge(irrigation_tune,  harvest_automate)
root.order.add_edge(harvest_automate, quality_check)
root.order.add_edge(quality_check,    loop)