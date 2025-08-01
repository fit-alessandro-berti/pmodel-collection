# Generated from: 963b05cc-3409-4ef0-9b65-001e984dfcff.json
# Description: This process outlines the detailed steps required to establish a sustainable urban rooftop farming operation. It involves initial site assessment, regulatory compliance checks, soil and structural analysis, procurement of specialized modular planting systems, installation of automated irrigation and nutrient delivery, integration of renewable energy sources, ongoing crop monitoring using IoT sensors, pest management with eco-friendly methods, periodic yield assessments, and community engagement for educational workshops. The goal is to maximize crop yield while maintaining environmental sustainability and building local food resilience in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label="Site Survey")
permit_review    = Transition(label="Permit Review")
load_testing     = Transition(label="Load Testing")
soil_sampling    = Transition(label="Soil Sampling")
system_design    = Transition(label="System Design")
module_assembly  = Transition(label="Module Assembly")
irrigation_setup = Transition(label="Irrigation Setup")
energy_integration = Transition(label="Energy Integration")
sensor_install   = Transition(label="Sensor Install")
nutrient_dosing  = Transition(label="Nutrient Dosing")
planting_phase   = Transition(label="Planting Phase")
pest_control     = Transition(label="Pest Control")
data_monitoring  = Transition(label="Data Monitoring")
yield_analysis   = Transition(label="Yield Analysis")
community_outreach = Transition(label="Community Outreach")

# Parallel installation of irrigation, energy and sensor systems
install_po = StrictPartialOrder(nodes=[irrigation_setup, energy_integration, sensor_install])
# (no edges = they are concurrent)

# Loop for ongoing monitoring, pest control and yield analysis
monitor_seq = StrictPartialOrder(nodes=[data_monitoring, pest_control, yield_analysis])
monitor_seq.order.add_edge(data_monitoring, pest_control)
monitor_seq.order.add_edge(pest_control, yield_analysis)
skip = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_seq, skip])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, permit_review, load_testing, soil_sampling,
        system_design, module_assembly, install_po,
        nutrient_dosing, planting_phase,
        monitor_loop, community_outreach
    ]
)

# Define the sequencing constraints
root.order.add_edge(site_survey,      permit_review)
root.order.add_edge(permit_review,    load_testing)
root.order.add_edge(load_testing,     soil_sampling)
root.order.add_edge(soil_sampling,    system_design)
root.order.add_edge(system_design,    module_assembly)
root.order.add_edge(module_assembly,  install_po)
root.order.add_edge(install_po,       nutrient_dosing)
root.order.add_edge(nutrient_dosing,  planting_phase)
root.order.add_edge(planting_phase,   monitor_loop)
root.order.add_edge(planting_phase,   community_outreach)