# Generated from: d460587c-54a1-4a67-bbc5-b48e55b72949.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes initial structural assessments, securing permits, soil and water testing, installation of hydroponic systems, integration of renewable energy sources, crop selection based on microclimate data, stakeholder coordination, ongoing environmental monitoring, and market launch strategies. The process ensures compliance with city regulations, maximizes yield efficiency, and incorporates community engagement initiatives to promote urban agriculture awareness and education. It requires interdisciplinary collaboration among engineers, agronomists, architects, and local authorities to successfully transform unused rooftop spaces into productive green environments that contribute to local food security and urban ecosystem enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Load_Testing = Transition(label='Load Testing')
Soil_Sampling = Transition(label='Soil Sampling')
Water_Testing = Transition(label='Water Testing')
System_Design = Transition(label='System Design')
Solar_Setup = Transition(label='Solar Setup')
Crop_Planning = Transition(label='Crop Planning')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Material_Order = Transition(label='Material Order')
System_Install = Transition(label='System Install')
Environmental_Audit = Transition(label='Environmental Audit')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Market_Launch = Transition(label='Market Launch')

# Structural assessments sequence
structural_assessment = StrictPartialOrder(
    nodes=[Site_Survey, Load_Testing, Permit_Filing],
)
structural_assessment.order.add_edge(Site_Survey, Load_Testing)
structural_assessment.order.add_edge(Load_Testing, Permit_Filing)

# Soil and water testing partial order (can be concurrent)
soil_water_tests = StrictPartialOrder(
    nodes=[Soil_Sampling, Water_Testing],
    # no order edges means concurrent
)

# System preparation - system design after soil/water testing
system_design_phase = StrictPartialOrder(
    nodes=[soil_water_tests, System_Design],
)
system_design_phase.order.add_edge(soil_water_tests, System_Design)

# Solar setup (renewable energy integration) concurrent with material order
solar_material = StrictPartialOrder(
    nodes=[Solar_Setup, Material_Order],
)
# no order edges means concurrent

# Installation sequence: system install after system design, solar setup and material order
installation_phase = StrictPartialOrder(
    nodes=[system_design_phase, solar_material, System_Install],
)
installation_phase.order.add_edge(system_design_phase, System_Install)
installation_phase.order.add_edge(solar_material, System_Install)

# Crop planning and stakeholder meet concurrent after installation
crop_and_stakeholder = StrictPartialOrder(
    nodes=[Crop_Planning, Stakeholder_Meet],
)
# no order edges means concurrent

# Environmental audit as a loop:
# Loop body: Growth Monitoring and Pest Control concurrently,
# then Environmental Audit
growth_pest = StrictPartialOrder(
    nodes=[Growth_Monitoring, Pest_Control],
)
# no order edges, concurrent

body_loop = StrictPartialOrder(
    nodes=[growth_pest, Environmental_Audit],
)
body_loop.order.add_edge(growth_pest, Environmental_Audit)

# Loop node * (Environmental Audit, growth_pest)
env_loop = OperatorPOWL(operator=Operator.LOOP, children=[Environmental_Audit, growth_pest])

# Overall monitoring phase: perform first Environmental Audit, then loop growth/pest then audit repeated
# To reflect the logic: execute Environmental_Audit first, then loop growth_pest + Environmental_Audit repeatedly
monitoring_phase = StrictPartialOrder(
    nodes=[Environmental_Audit, env_loop],
)
monitoring_phase.order.add_edge(Environmental_Audit, env_loop)

# Market launch after monitoring, stakeholder meet and crop planning
final_phase = StrictPartialOrder(
    nodes=[crop_and_stakeholder, monitoring_phase, Market_Launch],
)
final_phase.order.add_edge(crop_and_stakeholder, Market_Launch)
final_phase.order.add_edge(monitoring_phase, Market_Launch)

# Connect initial structural assessment to system design phase
start_to_design = StrictPartialOrder(
    nodes=[structural_assessment, system_design_phase],
)
start_to_design.order.add_edge(structural_assessment, system_design_phase)

# Connect installation phase after system design phase and solar_material is inside installation_phase already

# Final root partial order with all main nodes:
# structural_assessment --> soil_water_tests --> system_design_phase --> installation_phase --> crop_and_stakeholder --> monitoring_phase --> Market_Launch
root = StrictPartialOrder(
    nodes=[
        structural_assessment,
        soil_water_tests,
        system_design_phase,
        solar_material,
        installation_phase,
        crop_and_stakeholder,
        monitoring_phase,
        Market_Launch,
    ]
)

# Add edges to preserve overall flow
root.order.add_edge(structural_assessment, soil_water_tests)
root.order.add_edge(soil_water_tests, system_design_phase)
root.order.add_edge(system_design_phase, solar_material)
root.order.add_edge(solar_material, installation_phase)
root.order.add_edge(installation_phase, crop_and_stakeholder)
root.order.add_edge(crop_and_stakeholder, monitoring_phase)
root.order.add_edge(monitoring_phase, Market_Launch)