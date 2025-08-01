# Generated from: 4cfad4ae-b22b-44ff-8612-a97da54e7574.json
# Description: This process outlines the end-to-end supply chain of urban beekeeping equipment and honey distribution. It begins with sourcing sustainable materials from local artisans, followed by custom manufacturing of eco-friendly hives. The process includes hive assembly, quality inspections, and seasonal bee colony integration. Parallel activities involve urban apiary site selection, environmental impact assessments, and regulatory compliance verification. Once hives are deployed, ongoing monitoring of bee health and hive conditions is conducted using IoT sensors. Honey extraction, purification, and packaging occur in small batches to maintain artisanal quality. The process concludes with direct-to-consumer marketing, urban farmer collaborations, and feedback loops for continuous product and process improvement, emphasizing sustainability and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
mat = Transition(label='Material Sourcing')
fab = Transition(label='Custom Fabrication')
assembly = Transition(label='Hive Assembly')
quality = Transition(label='Quality Check')
colony = Transition(label='Colony Integration')

site = Transition(label='Site Selection')
impact = Transition(label='Impact Assess')
compliance = Transition(label='Compliance Review')

sensor = Transition(label='Sensor Setup')
health = Transition(label='Health Monitoring')

extract = Transition(label='Honey Extract')
purify = Transition(label='Purify Batch')
package = Transition(label='Package Goods')

direct = Transition(label='Direct Marketing')
farmer = Transition(label='Farmer Partner')
feedback = Transition(label='Feedback Loop')

# 1. Manufacturing sequence
seq_manufacture = StrictPartialOrder(nodes=[mat, fab, assembly, quality, colony])
seq_manufacture.order.add_edge(mat, fab)
seq_manufacture.order.add_edge(fab, assembly)
seq_manufacture.order.add_edge(assembly, quality)
seq_manufacture.order.add_edge(quality, colony)

# 2. Parallel site/impact/compliance
par_site = StrictPartialOrder(nodes=[site, impact, compliance])
# no edges => fully parallel

# 3a. Monitoring sequence
seq_monitor = StrictPartialOrder(nodes=[sensor, health])
seq_monitor.order.add_edge(sensor, health)

# 3b. Honey processing sequence
seq_honey = StrictPartialOrder(nodes=[extract, purify, package])
seq_honey.order.add_edge(extract, purify)
seq_honey.order.add_edge(purify, package)

# 3. Parallel monitoring and honey processing
par_monitor_honey = StrictPartialOrder(nodes=[seq_monitor, seq_honey])

# 4. Marketing & feedback loop
seq_marketing = StrictPartialOrder(nodes=[direct, farmer])
seq_marketing.order.add_edge(direct, farmer)
loop = OperatorPOWL(operator=Operator.LOOP, children=[seq_marketing, feedback])

# Root POWL model
root = StrictPartialOrder(nodes=[seq_manufacture, par_site, par_monitor_honey, loop])
root.order.add_edge(seq_manufacture, par_site)
root.order.add_edge(par_site, par_monitor_honey)
root.order.add_edge(par_monitor_honey, loop)