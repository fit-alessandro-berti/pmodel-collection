# Generated from: 210ac66b-05ac-4b2f-8db3-d14107bf9873.json
# Description: This process involves the planning, construction, and operational launch of an urban vertical farm within a repurposed industrial building. It includes assessing structural integrity, designing modular grow systems, selecting crop varieties suited for vertical cultivation, installing automated climate controls, integrating renewable energy sources, training staff on hydroponic techniques, establishing supply chain logistics for fresh produce distribution, and implementing sustainability metrics for continuous improvement. The process ensures efficient use of limited urban space while maximizing yield and minimizing environmental impact through innovative farming technologies and data-driven management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Assess')
structure = Transition(label='Structure Check')
design = Transition(label='System Design')
crop = Transition(label='Crop Select')
module = Transition(label='Module Build')
climate = Transition(label='Climate Setup')
energy = Transition(label='Energy Integrate')
water = Transition(label='Water Install')
sensor = Transition(label='Sensor Deploy')
test = Transition(label='Automation Test')
train = Transition(label='Staff Train')
trial = Transition(label='Trial Cultivate')
harvest = Transition(label='Harvest Plan')
logistics = Transition(label='Logistics Setup')
monitor = Transition(label='Sustain Monitor')

# Planning phase: sequential
planning = StrictPartialOrder(nodes=[site, structure, design, crop])
planning.order.add_edge(site, structure)
planning.order.add_edge(structure, design)
planning.order.add_edge(design, crop)

# Construction phase: build then parallel installs then test
construction = StrictPartialOrder(nodes=[module, climate, energy, water, sensor, test])
construction.order.add_edge(module, climate)
construction.order.add_edge(module, energy)
construction.order.add_edge(module, water)
construction.order.add_edge(module, sensor)
construction.order.add_edge(climate, test)
construction.order.add_edge(energy, test)
construction.order.add_edge(water, test)
construction.order.add_edge(sensor, test)

# Loop body: trial cultivation then parallel harvest planning and logistics setup
loop_body = StrictPartialOrder(nodes=[trial, harvest, logistics])
loop_body.order.add_edge(trial, harvest)
loop_body.order.add_edge(trial, logistics)

# Loop operator: repeat trial+harvest+logistics until exit
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Compose the entire process
root = StrictPartialOrder(nodes=[planning, construction, train, loop, monitor])
root.order.add_edge(planning, construction)
root.order.add_edge(construction, train)
root.order.add_edge(train, loop)
root.order.add_edge(loop, monitor)