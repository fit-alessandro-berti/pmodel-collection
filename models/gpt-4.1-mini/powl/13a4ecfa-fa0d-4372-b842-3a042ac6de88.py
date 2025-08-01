# Generated from: 13a4ecfa-fa0d-4372-b842-3a042ac6de88.json
# Description: This process outlines the complex journey of artisan coffee beans from remote high-altitude farms to exclusive urban cafes. It involves unique steps such as micro-lot selection, hand-picking quality checks, natural fermentation monitoring, and custom roasting profiles tailored for each batch. The process also integrates blockchain tracking to verify origin and fair trade certification, alongside dynamic demand forecasting based on seasonal consumer preferences. Packaging includes biodegradable materials with embedded NFC tags for consumer engagement. Finally, distribution leverages a mixed logistics network combining drone delivery for remote areas and traditional cold chain transport to preserve freshness, culminating in direct-to-customer subscription services with personalized brewing guides.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
farm_reg = Transition(label='Farm Registration')
lot_sel = Transition(label='Lot Selection')
hand_pick = Transition(label='Hand Picking')
ferm_check = Transition(label='Fermentation Check')
qual_score = Transition(label='Quality Scoring')
block_tag = Transition(label='Blockchain Tagging')
roast_prof = Transition(label='Roast Profiling')
batch_roast = Transition(label='Batch Roasting')
nfc_embed = Transition(label='NFC Embedding')
eco_pack = Transition(label='Eco Packaging')
drone_disp = Transition(label='Drone Dispatch')
cold_chain = Transition(label='Cold Chain')
demand_forecast = Transition(label='Demand Forecast')
cafe_deliv = Transition(label='Cafe Delivery')
subs_setup = Transition(label='Subscription Setup')
brew_guide = Transition(label='Brew Guide')

# Packaging parallel tasks node: NFC Embedding and Eco Packaging concurrent
packaging = StrictPartialOrder(nodes=[nfc_embed, eco_pack])

# Distribution choice: either Drone Dispatch or Cold Chain
distribution = OperatorPOWL(operator=Operator.XOR, children=[drone_disp, cold_chain])

# Delivery parallel tasks node: Cafe Delivery and Subscription Setup concurrently
delivery_parallel = StrictPartialOrder(nodes=[cafe_deliv, subs_setup])
# Subscription Setup followed by Brew Guide (sequential)
subs_seq = StrictPartialOrder(nodes=[subs_setup, brew_guide])
subs_seq.order.add_edge(subs_setup, brew_guide)

# Replace delivery_parallel nodes with Subscription sequence to preserve Brew Guide after Subscription Setup
delivery = StrictPartialOrder(nodes=[cafe_deliv, subs_seq])
# No order between cafe_deliv and subs_seq (concurrent)

# Loop for demand forecasting activity - assuming it loops continuously after roasting till distribution
# Loop: execute demand_forecast, then choose to exit or continue (simulate repeated forecasting)
demand_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, SilentTransition()])

# Build the process partial order
root = StrictPartialOrder(
    nodes=[
        farm_reg,       # start
        lot_sel,
        hand_pick,
        ferm_check,
        qual_score,
        block_tag,
        roast_prof,
        batch_roast,
        packaging,      # NFC Embedding & Eco Packaging
        demand_loop,    # loop for demand forecasting
        distribution,   # XOR between drone and cold chain
        delivery        # cafe delivery and subscription+bvg concurrent
    ]
)

# Define order of activities reflecting the described workflow

root.order.add_edge(farm_reg, lot_sel)
root.order.add_edge(lot_sel, hand_pick)
root.order.add_edge(hand_pick, ferm_check)
root.order.add_edge(ferm_check, qual_score)
root.order.add_edge(qual_score, block_tag)
root.order.add_edge(block_tag, roast_prof)
root.order.add_edge(roast_prof, batch_roast)
root.order.add_edge(batch_roast, packaging)
root.order.add_edge(packaging, demand_loop)  # after packaging start demand forecasting loop

root.order.add_edge(demand_loop, distribution)  # after demand forecasting loop, distribution

root.order.add_edge(distribution, delivery)    # distribution precedes delivery tasks

# No order constraints inside packaging (concurrent)

# No order constraints between cafe_delivery and subs_seq inside delivery (concurrent)

# Brew Guide is after Subscription Setup inside subs_seq

# The LOOP node demand_loop: semantic usage as per definition (execute demand_forecast then silent exit or repeat)

# All set with concurrency and choices per description

# Return root as final model