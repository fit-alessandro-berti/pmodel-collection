# Generated from: 45eed133-7dd3-43ef-be2d-9e9a89843f70.json
# Description: This process outlines the establishment of a sustainable urban vertical farm within a repurposed industrial building. It involves site analysis, structural assessment, installation of hydroponic systems, climate control setup, automation integration, and continuous monitoring. The process ensures optimized space utilization, resource efficiency, and year-round crop production. Collaborative efforts between architects, engineers, agronomists, and IT specialists are essential to address challenges such as lighting optimization, water recycling, pest control, and yield forecasting. The process also includes regulatory compliance checks, community engagement, and supply chain coordination for distribution and marketing of produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
design_layout = Transition(label='Design Layout')
install_frames = Transition(label='Install Frames')
setup_hydroponics = Transition(label='Setup Hydroponics')
climate_setup = Transition(label='Climate Setup')
lighting_config = Transition(label='Lighting Config')
automation_install = Transition(label='Automation Install')
sensor_deploy = Transition(label='Sensor Deploy')
water_cycle = Transition(label='Water Cycle')
pest_control = Transition(label='Pest Control')
system_testing = Transition(label='System Testing')
plant_seeding = Transition(label='Plant Seeding')
growth_monitor = Transition(label='Growth Monitor')
yield_forecast = Transition(label='Yield Forecast')
regulation_audit = Transition(label='Regulation Audit')
community_meet = Transition(label='Community Meet')
supply_chain = Transition(label='Supply Chain')

# Phase 1: Initial building and site assessment (Site Survey -> Structure Check -> Design Layout)
phase1 = StrictPartialOrder(nodes=[site_survey, structure_check, design_layout])
phase1.order.add_edge(site_survey, structure_check)
phase1.order.add_edge(structure_check, design_layout)

# Phase 2: Installation (Install Frames -> Setup Hydroponics -> Climate Setup)
install_phase = StrictPartialOrder(nodes=[install_frames, setup_hydroponics, climate_setup])
install_phase.order.add_edge(install_frames, setup_hydroponics)
install_phase.order.add_edge(setup_hydroponics, climate_setup)

# Phase 3: Configuration & automation done in parallel (Lighting Config, Automation Install, Sensor Deploy)
config_phase = StrictPartialOrder(nodes=[lighting_config, automation_install, sensor_deploy])
# No order edges, fully concurrent

# Phase 4: Resource efficiency & environment management (Water Cycle, Pest Control)
env_phase = StrictPartialOrder(nodes=[water_cycle, pest_control])
# no order edge, concurrent

# Phase 5: Testing and validation (System Testing)
testing_phase = system_testing

# Phase 6: Planting and monitoring loop
# The loop: (Plant Seeding) then choose to exit or (Growth Monitor and Yield Forecast) then repeat Plant Seeding again
growth_monitoring = StrictPartialOrder(nodes=[growth_monitor, yield_forecast])
growth_monitoring.order.add_edge(growth_monitor, yield_forecast)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP,
                              children=[plant_seeding, growth_monitoring])

# Phase 7: Compliance, Community & Supply Chain coordination (Regulation Audit -> Community Meet -> Supply Chain)
closing_phase = StrictPartialOrder(nodes=[regulation_audit, community_meet, supply_chain])
closing_phase.order.add_edge(regulation_audit, community_meet)
closing_phase.order.add_edge(community_meet, supply_chain)

# Compose overall process partial order
# Ordering the phases:
# phase1 -> install_phase -> config_phase & env_phase (concurrent) -> testing_phase -> monitoring_loop -> closing_phase

# Combine config_phase and env_phase in parallel (no edges)
config_env_phase = StrictPartialOrder(
    nodes=[lighting_config, automation_install, sensor_deploy, water_cycle, pest_control]
)
# config_phase and env_phase nodes with no inter-order edges -> all concurrent

# Build overall nodes list
all_nodes = [
    phase1,
    install_phase,
    config_env_phase,
    testing_phase,
    monitoring_loop,
    closing_phase
]

root = StrictPartialOrder(nodes=all_nodes)

# Add ordering edges between high-level phases
root.order.add_edge(phase1, install_phase)
root.order.add_edge(install_phase, config_env_phase)
root.order.add_edge(config_env_phase, testing_phase)
root.order.add_edge(testing_phase, monitoring_loop)
root.order.add_edge(monitoring_loop, closing_phase)