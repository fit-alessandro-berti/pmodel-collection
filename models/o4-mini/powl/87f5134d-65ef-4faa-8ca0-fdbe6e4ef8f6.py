# Generated from: 87f5134d-65ef-4faa-8ca0-fdbe6e4ef8f6.json
# Description: This process outlines the complex setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, modular farm design, equipment procurement, and installation of hydroponic and aeroponic systems. The process includes environmental control calibration, integration of IoT sensors for real-time monitoring, and development of automated nutrient delivery schedules. Staff training on system operation and safety protocols is conducted, followed by initial trial planting and iterative optimization of growth parameters. The final steps focus on establishing supply chain logistics, marketing strategies for local produce, and ongoing maintenance scheduling to ensure sustainability and productivity in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
survey = Transition(label='Site Survey')
design = Transition(label='Design Plan')
procure = Transition(label='Procure Equipment')
install = Transition(label='Install Modules')
hydro = Transition(label='Setup Hydroponics')
calibrate = Transition(label='Calibrate Sensors')
integrate = Transition(label='Integrate IoT')
program = Transition(label='Program Automation')
train = Transition(label='Train Staff')
trial = Transition(label='Trial Planting')
optimize = Transition(label='Optimize Growth')
logistics = Transition(label='Logistics Setup')
marketing = Transition(label='Marketing Plan')
maintenance = Transition(label='Maintenance Plan')
launch = Transition(label='Launch Operations')

# Loop for iterative trial and optimization
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[trial, optimize])

# Build the partial order
root = StrictPartialOrder(nodes=[
    survey, design, procure, install, hydro, calibrate,
    integrate, program, train, loop_node,
    logistics, marketing, maintenance, launch
])

# Add ordering dependencies
root.order.add_edge(survey, design)
root.order.add_edge(design, procure)
root.order.add_edge(procure, install)
root.order.add_edge(install, hydro)
root.order.add_edge(hydro, calibrate)
root.order.add_edge(calibrate, integrate)
root.order.add_edge(integrate, program)
root.order.add_edge(program, train)
root.order.add_edge(train, loop_node)
root.order.add_edge(loop_node, logistics)
root.order.add_edge(logistics, marketing)
root.order.add_edge(marketing, maintenance)
root.order.add_edge(maintenance, launch)