# Generated from: 13f4ed83-8712-4494-b416-11cd79ef7042.json
# Description: This process involves the strategic deployment of autonomous underwater drones to collect rare mineral samples from deep-sea hydrothermal vents. It requires initial site surveying, remote vehicle calibration, and continuous environmental data analysis to adapt to changing ocean currents. Sample extraction is followed by secure transport via unmanned surface vessels to shore facilities, where material is cataloged, analyzed, and prepared for commercial use. Throughout the process, real-time communication with satellite networks ensures operational safety and data integrity under extreme conditions, while compliance with international maritime laws is maintained.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
site_survey     = Transition(label='Site Survey')
drone_deploy    = Transition(label='Drone Deploy')
sensor_check    = Transition(label='Sensor Check')
currents_monitor= Transition(label='Currents Monitor')
data_sync       = Transition(label='Data Sync')
sample_extract  = Transition(label='Sample Extract')
vessel_launch   = Transition(label='Vessel Launch')
transport_secure= Transition(label='Transport Secure')
material_catalog= Transition(label='Material Catalog')
quality_test    = Transition(label='Quality Test')
data_analyze    = Transition(label='Data Analyze')
satellite_link  = Transition(label='Satellite Link')
law_compliance  = Transition(label='Law Compliance')
report_compile  = Transition(label='Report Compile')
maintenance_chk = Transition(label='Maintenance Check')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for continuous environmental monitoring:
#   execute [Currents Monitor -> Data Sync], then either exit or repeat
env_seq = StrictPartialOrder(nodes=[currents_monitor, data_sync])
env_seq.order.add_edge(currents_monitor, data_sync)
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[env_seq, skip])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        drone_deploy,
        sensor_check,
        loop_env,
        sample_extract,
        vessel_launch,
        transport_secure,
        material_catalog,
        quality_test,
        data_analyze,
        report_compile,
        maintenance_chk,
        # these two run concurrently with the main flow
        satellite_link,
        law_compliance
    ]
)

# Sequential dependencies
root.order.add_edge(site_survey,      drone_deploy)
root.order.add_edge(drone_deploy,     sensor_check)
root.order.add_edge(sensor_check,     loop_env)
root.order.add_edge(loop_env,         sample_extract)
root.order.add_edge(sample_extract,   vessel_launch)
root.order.add_edge(vessel_launch,    transport_secure)
root.order.add_edge(transport_secure, material_catalog)
root.order.add_edge(material_catalog, quality_test)
root.order.add_edge(quality_test,     data_analyze)
root.order.add_edge(data_analyze,     report_compile)
root.order.add_edge(report_compile,   maintenance_chk)