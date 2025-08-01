# Generated from: 13f4ed83-8712-4494-b416-11cd79ef7042.json
# Description: This process involves the strategic deployment of autonomous underwater drones to collect rare mineral samples from deep-sea hydrothermal vents. It requires initial site surveying, remote vehicle calibration, and continuous environmental data analysis to adapt to changing ocean currents. Sample extraction is followed by secure transport via unmanned surface vessels to shore facilities, where material is cataloged, analyzed, and prepared for commercial use. Throughout the process, real-time communication with satellite networks ensures operational safety and data integrity under extreme conditions, while compliance with international maritime laws is maintained.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
DroneDeploy = Transition(label='Drone Deploy')
SensorCheck = Transition(label='Sensor Check')
CurrentsMonitor = Transition(label='Currents Monitor')
SampleExtract = Transition(label='Sample Extract')
DataSync = Transition(label='Data Sync')
VesselLaunch = Transition(label='Vessel Launch')
TransportSecure = Transition(label='Transport Secure')
MaterialCatalog = Transition(label='Material Catalog')
QualityTest = Transition(label='Quality Test')
DataAnalyze = Transition(label='Data Analyze')
SatelliteLink = Transition(label='Satellite Link')
LawCompliance = Transition(label='Law Compliance')
ReportCompile = Transition(label='Report Compile')
MaintenanceCheck = Transition(label='Maintenance Check')

# Loop node for continuous environmental data analysis to adapt currents:
# Loop body:
# A = CurrentsMonitor
# B = SensorCheck (recalibration before next monitor)
loop_env_adapt = OperatorPOWL(operator=Operator.LOOP, children=[CurrentsMonitor, SensorCheck])

# Initial part: SiteSurvey --> DroneDeploy --> loop_env_adapt
init_po = StrictPartialOrder(nodes=[SiteSurvey, DroneDeploy, loop_env_adapt])
init_po.order.add_edge(SiteSurvey, DroneDeploy)
init_po.order.add_edge(DroneDeploy, loop_env_adapt)

# Sample extraction and transport partial order:
# SampleExtract --> DataSync --> VesselLaunch --> TransportSecure
sample_transport_po = StrictPartialOrder(nodes=[SampleExtract, DataSync, VesselLaunch, TransportSecure])
sample_transport_po.order.add_edge(SampleExtract, DataSync)
sample_transport_po.order.add_edge(DataSync, VesselLaunch)
sample_transport_po.order.add_edge(VesselLaunch, TransportSecure)

# At shore: MaterialCatalog --> QualityTest --> DataAnalyze
shore_processing_po = StrictPartialOrder(nodes=[MaterialCatalog, QualityTest, DataAnalyze])
shore_processing_po.order.add_edge(MaterialCatalog, QualityTest)
shore_processing_po.order.add_edge(QualityTest, DataAnalyze)

# Concurrent with shore processing:
# LawCompliance and SatelliteLink run concurrently and precede ReportCompile
concurrent_cons = StrictPartialOrder(nodes=[LawCompliance, SatelliteLink, ReportCompile])
concurrent_cons.order.add_edge(LawCompliance, ReportCompile)
concurrent_cons.order.add_edge(SatelliteLink, ReportCompile)

# Combine shore_processing_po and concurrent_cons in partial order with ReportCompile after them
# Also, MaintenanceCheck happens at some point - let's model it as concurrent with SampleExtract (maintenance check before sample extraction)
# So we add MaintenanceCheck before SampleExtract (to be safe)

# Add MaintenanceCheck --> SampleExtract
sample_transport_with_maintenance = StrictPartialOrder(nodes=[MaintenanceCheck, SampleExtract, DataSync, VesselLaunch, TransportSecure])
sample_transport_with_maintenance.order.add_edge(MaintenanceCheck, SampleExtract)
sample_transport_with_maintenance.order.add_edge(SampleExtract, DataSync)
sample_transport_with_maintenance.order.add_edge(DataSync, VesselLaunch)
sample_transport_with_maintenance.order.add_edge(VesselLaunch, TransportSecure)

# Combine sample_transport_with_maintenance and shore_processing_po, and concurrent_cons, all in a partial order.
# TransportSecure precedes MaterialCatalog
# TransportSecure precedes LawCompliance and SatelliteLink (to ensure secure transport before compliance and satellite comms for reporting)
# ReportCompile is last

final_po1 = StrictPartialOrder(
    nodes=[sample_transport_with_maintenance, shore_processing_po, concurrent_cons]
)
final_po1.order.add_edge(sample_transport_with_maintenance, shore_processing_po)
final_po1.order.add_edge(sample_transport_with_maintenance, concurrent_cons)
final_po1.order.add_edge(shore_processing_po, concurrent_cons)  # Ensure ReportCompile after shore processing

# The whole final process: initial part (site survey etc.) --> final_po1
root = StrictPartialOrder(nodes=[init_po, final_po1])
root.order.add_edge(init_po, final_po1)