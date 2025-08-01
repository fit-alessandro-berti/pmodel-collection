# Generated from: b4a918a9-b0a3-4add-b384-6ee0f12a12b9.json
# Description: This process outlines the comprehensive steps required to launch a vertical farming operation within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and community engagement initiatives. The process begins with site acquisition and feasibility analysis, followed by modular farm design and procurement of specialized equipment. Installation involves setting up climate sensors, nutrient delivery systems, and automated harvesting robots. Concurrently, regulatory compliance and sustainability certification are secured. Marketing strategies focus on local partnerships and transparent supply chain communication. Training programs for staff emphasize technology operation and crop management. The process concludes with pilot harvests, data-driven optimization, and phased scaling to meet urban food demands sustainably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_acquire      = Transition(label="Site Acquire")
feasibility       = Transition(label="Feasibility Check")
design_farm       = Transition(label="Design Farm")
equipment_order   = Transition(label="Equipment Order")
install_sensors   = Transition(label="Install Sensors")
setup_hydroponics = Transition(label="Setup Hydroponics")
integrate_ai      = Transition(label="Integrate AI")
robot_deploy      = Transition(label="Robot Deploy")
compliance_review = Transition(label="Compliance Review")
certify_sustain   = Transition(label="Certify Sustain")
launch_marketing  = Transition(label="Launch Marketing")
partner_outreach  = Transition(label="Partner Outreach")
staff_training    = Transition(label="Staff Training")
pilot_harvest     = Transition(label="Pilot Harvest")
data_optimize     = Transition(label="Data Optimize")
scale_operations  = Transition(label="Scale Operations")

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_acquire, feasibility, design_farm, equipment_order,
    install_sensors, setup_hydroponics, integrate_ai, robot_deploy,
    compliance_review, certify_sustain,
    launch_marketing, partner_outreach,
    staff_training, pilot_harvest, data_optimize, scale_operations
])

# 1) Site Acquire -> Feasibility Check -> Design Farm -> Equipment Order
root.order.add_edge(site_acquire, feasibility)
root.order.add_edge(feasibility, design_farm)
root.order.add_edge(design_farm, equipment_order)

# 2) After Equipment Order, four installation activities run in parallel:
#    Install Sensors, Setup Hydroponics, Integrate AI, Robot Deploy
for install_task in [install_sensors, setup_hydroponics, integrate_ai, robot_deploy]:
    root.order.add_edge(equipment_order, install_task)

# 3) Concurrently with installation, secure Compliance Review and Certify Sustain
for compliance_task in [compliance_review, certify_sustain]:
    root.order.add_edge(equipment_order, compliance_task)

# 4) After both compliance steps, launch marketing and partner outreach in parallel
for marketing_task in [launch_marketing, partner_outreach]:
    root.order.add_edge(compliance_review, marketing_task)
    root.order.add_edge(certify_sustain, marketing_task)

# 5) Staff Training follows completion of both marketing branches
root.order.add_edge(launch_marketing, staff_training)
root.order.add_edge(partner_outreach, staff_training)

# 6) Final sequence: Pilot Harvest -> Data Optimize -> Scale Operations
root.order.add_edge(staff_training, pilot_harvest)
root.order.add_edge(pilot_harvest, data_optimize)
root.order.add_edge(data_optimize, scale_operations)