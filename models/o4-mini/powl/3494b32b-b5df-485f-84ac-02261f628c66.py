# Generated from: 3494b32b-b5df-485f-84ac-02261f628c66.json
# Description: This process manages the unique supply chain for artisanal cheese production, starting from sourcing rare milk varieties from micro-dairies, through customized fermentation and aging procedures, to specialized packaging and direct distribution to niche markets. It incorporates quality control at every step, traceability of origin, and coordination with seasonal production cycles, ensuring product authenticity and maintaining the delicate balance between traditional methods and modern food safety standards. The process also involves managing limited edition batches, handling small-scale logistics, and engaging with artisan networks for collaborative innovation and market positioning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms    = Transition(label='Milk Sourcing')
qt    = Transition(label='Quality Testing')
mp    = Transition(label='Milk Pasteurize')
sc    = Transition(label='Starter Culture')
co    = Transition(label='Coagulation')
cc    = Transition(label='Curd Cutting')
wd    = Transition(label='Whey Drain')
mpres = Transition(label='Molding Press')
ss    = Transition(label='Salting Stage')
fer   = Transition(label='Fermentation')
am    = Transition(label='Aging Monitor')
ft    = Transition(label='Flavor Testing')
bl    = Transition(label='Batch Labeling')
cp    = Transition(label='Custom Packaging')
md    = Transition(label='Market Delivery')
tl    = Transition(label='Traceability Log')
ia    = Transition(label='Inventory Audit')

# Silent transition for choices and loop continuation
skip = SilentTransition()

# Choice for specialized vs. standard packaging (models limited-edition vs. regular batches)
pkg_choice = OperatorPOWL(operator=Operator.XOR, children=[cp, skip])

# Build the core pipeline as a strict partial order
pipeline = StrictPartialOrder(nodes=[
    ms, qt, mp, sc, co, cc, wd, mpres, ss, fer, am, ft, bl, pkg_choice, md, tl, ia
])

# Add ordering constraints
pipeline.order.add_edge(ms, qt)
pipeline.order.add_edge(ms, tl)
pipeline.order.add_edge(qt, mp)
pipeline.order.add_edge(qt, tl)
pipeline.order.add_edge(tl, mp)

pipeline.order.add_edge(mp, sc)
pipeline.order.add_edge(sc, co)
pipeline.order.add_edge(co, cc)
pipeline.order.add_edge(cc, wd)
pipeline.order.add_edge(wd, mpres)
pipeline.order.add_edge(mpres, ss)
pipeline.order.add_edge(ss, fer)
pipeline.order.add_edge(fer, am)
pipeline.order.add_edge(am, ft)

pipeline.order.add_edge(ft, bl)
pipeline.order.add_edge(bl, pkg_choice)
pipeline.order.add_edge(pkg_choice, md)

pipeline.order.add_edge(md, ia)

# Wrap the entire pipeline in a loop to model seasonal production cycles
root = OperatorPOWL(operator=Operator.LOOP, children=[pipeline, skip])