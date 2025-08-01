# Generated from: 82c7bb20-1887-47ca-af33-3e9835c913b3.json
# Description: This process details the intricate supply chain of artisanal cheese production from sourcing rare milk varieties through microscopic bacterial culture preparation, carefully timed aging in controlled environments, to bespoke packaging and niche market distribution. Each step requires precision to maintain quality and heritage, including quality sampling, microbial testing, seasonal adjustments, and artisan collaboration, culminating in a high-value product favored by connoisseurs and specialty retailers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk = Transition(label='Milk Sourcing')
culture = Transition(label='Culture Prep')
curd = Transition(label='Curd Cutting')
whey = Transition(label='Whey Draining')
mold = Transition(label='Mold Inoculation')
press = Transition(label='Pressing Cheese')
salting = Transition(label='Salting Phase')
aging_setup = Transition(label='Aging Setup')
humidity = Transition(label='Humidity Control')
microbial = Transition(label='Microbial Check')
flavor = Transition(label='Flavor Testing')
batch = Transition(label='Batch Tracking')
packaging = Transition(label='Packaging Design')
market = Transition(label='Market Research')
distribution = Transition(label='Distribution Plan')
retail = Transition(label='Retail Partnering')
feedback = Transition(label='Customer Feedback')

# Model the aging loop: repeat microbial check & flavor testing after humidity control
body = StrictPartialOrder(nodes=[microbial, flavor])
body.order.add_edge(microbial, flavor)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk, culture, curd, whey, mold, press, salting,
    aging_setup, aging_loop, batch,
    packaging, market, distribution, retail, feedback
])

# Sequential flow up to aging
root.order.add_edge(milk, culture)
root.order.add_edge(culture, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, mold)
root.order.add_edge(mold, press)
root.order.add_edge(press, salting)
root.order.add_edge(salting, aging_setup)
root.order.add_edge(aging_setup, aging_loop)

# After aging loop, batch tracking
root.order.add_edge(aging_loop, batch)

# Parallel packaging and market research after batch tracking
root.order.add_edge(batch, packaging)
root.order.add_edge(batch, market)

# Both packaging and market research must finish before distribution
root.order.add_edge(packaging, distribution)
root.order.add_edge(market, distribution)

# Then retail partnering and finally customer feedback
root.order.add_edge(distribution, retail)
root.order.add_edge(retail, feedback)