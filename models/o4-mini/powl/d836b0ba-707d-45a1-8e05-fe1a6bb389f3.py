# Generated from: d836b0ba-707d-45a1-8e05-fe1a6bb389f3.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a dense metropolitan area. It includes site selection based on sunlight and accessibility, modular system design tailored to limited space, integration of IoT sensors for environmental monitoring, selection of crop varieties suited for vertical growth, soil and nutrient solution preparation, automated irrigation setup, pest management using biocontrol agents, energy-efficient LED lighting installation, staff training on system maintenance, regulatory compliance checks, market analysis for local distribution, packaging design for freshness retention, logistics planning for rapid delivery, data analytics for yield optimization, and continuous improvement through feedback loops. This atypical process requires coordination across agronomy, technology, logistics, and marketing disciplines to create a sustainable, productive urban farm that minimizes resource use while maximizing output and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_select       = Transition(label='Site Select')
design_layout     = Transition(label='Design Layout')
sensor_integrate  = Transition(label='Sensor Integrate')
crop_choose       = Transition(label='Crop Choose')
soil_prepare      = Transition(label='Soil Prepare')
irrigation_setup  = Transition(label='Irrigation Setup')
pest_control      = Transition(label='Pest Control')
lighting_install  = Transition(label='Lighting Install')
staff_train       = Transition(label='Staff Train')
compliance_check  = Transition(label='Compliance Check')
market_analyze    = Transition(label='Market Analyze')
package_design    = Transition(label='Package Design')
logistics_plan    = Transition(label='Logistics Plan')
data_analyze      = Transition(label='Data Analyze')
feedback_loop     = Transition(label='Feedback Loop')

# Define the feedback loop: perform data analysis, then optionally feedback and re‐analyze
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, feedback_loop])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_select, design_layout,
    sensor_integrate, crop_choose,
    soil_prepare, irrigation_setup,
    pest_control, lighting_install,
    staff_train, compliance_check,
    market_analyze, package_design,
    logistics_plan, data_loop
])

# Define sequencing and concurrency constraints
# Initial planning
root.order.add_edge(site_select, design_layout)

# Branch into agronomy, technology, regulatory, marketing
root.order.add_edge(design_layout, crop_choose)
root.order.add_edge(design_layout, sensor_integrate)
root.order.add_edge(design_layout, compliance_check)
root.order.add_edge(design_layout, market_analyze)

# Agronomy line
root.order.add_edge(crop_choose, soil_prepare)
root.order.add_edge(soil_prepare, pest_control)

# Technology line
root.order.add_edge(sensor_integrate, irrigation_setup)
root.order.add_edge(irrigation_setup, lighting_install)
root.order.add_edge(lighting_install, staff_train)

# Marketing line
root.order.add_edge(market_analyze, package_design)
root.order.add_edge(package_design, logistics_plan)

# Synchronize end‐of‐phase tasks into the continuous improvement loop
root.order.add_edge(pest_control, data_loop)
root.order.add_edge(staff_train, data_loop)
root.order.add_edge(logistics_plan, data_loop)
root.order.add_edge(compliance_check, data_loop)