# Generated from: 4c4219c2-e95f-4111-8c82-cb0d638883d6.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental impact assessment, modular hydroponic system design, installation of climate control units, integration of IoT sensors for real-time monitoring, and automated nutrient delivery setup. The process further includes staff training on system operation, regulatory compliance checks, pilot crop cultivation, data-driven yield optimization, waste recycling implementation, energy consumption analysis, marketing strategy development for local produce, and continuous system maintenance planning to ensure sustainability and scalability of the farm operation in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey = Transition(label="Site Survey")
impact_review = Transition(label="Impact Review")
system_design = Transition(label="System Design")
climate_setup = Transition(label="Climate Setup")
sensor_install = Transition(label="Sensor Install")
nutrient_setup = Transition(label="Nutrient Setup")
staff_training = Transition(label="Staff Training")
compliance_check = Transition(label="Compliance Check")
pilot_grow = Transition(label="Pilot Grow")
yield_analyze = Transition(label="Yield Analyze")
waste_manage = Transition(label="Waste Manage")
energy_audit = Transition(label="Energy Audit")
marketing_plan = Transition(label="Marketing Plan")
maintenance_plan = Transition(label="Maintenance Plan")
scale_strategy = Transition(label="Scale Strategy")

# Build a strict partial order for the linear flow
nodes = [
    site_survey,
    impact_review,
    system_design,
    climate_setup,
    sensor_install,
    nutrient_setup,
    staff_training,
    compliance_check,
    pilot_grow,
    yield_analyze,
    waste_manage,
    energy_audit,
    marketing_plan,
    maintenance_plan,
    scale_strategy
]

root = StrictPartialOrder(nodes=nodes)

# Add sequential dependencies
for i in range(len(nodes) - 1):
    root.order.add_edge(nodes[i], nodes[i + 1])