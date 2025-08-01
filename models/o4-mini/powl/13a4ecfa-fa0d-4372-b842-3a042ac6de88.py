# Generated from: 13a4ecfa-fa0d-4372-b842-3a042ac6de88.json
# Description: This process outlines the complex journey of artisan coffee beans from remote high-altitude farms to exclusive urban cafes. It involves unique steps such as micro-lot selection, hand-picking quality checks, natural fermentation monitoring, and custom roasting profiles tailored for each batch. The process also integrates blockchain tracking to verify origin and fair trade certification, alongside dynamic demand forecasting based on seasonal consumer preferences. Packaging includes biodegradable materials with embedded NFC tags for consumer engagement. Finally, distribution leverages a mixed logistics network combining drone delivery for remote areas and traditional cold chain transport to preserve freshness, culminating in direct-to-customer subscription services with personalized brewing guides.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
farm_registration = Transition(label='Farm Registration')
lot_selection     = Transition(label='Lot Selection')
hand_picking      = Transition(label='Hand Picking')
fermentation_chk  = Transition(label='Fermentation Check')
quality_scoring   = Transition(label='Quality Scoring')
blockchain_tag    = Transition(label='Blockchain Tagging')
demand_forecast   = Transition(label='Demand Forecast')
roast_profiling   = Transition(label='Roast Profiling')
batch_roasting    = Transition(label='Batch Roasting')
nfc_embedding     = Transition(label='NFC Embedding')
eco_packaging     = Transition(label='Eco Packaging')
drone_dispatch    = Transition(label='Drone Dispatch')
cold_chain        = Transition(label='Cold Chain')
cafe_delivery     = Transition(label='Cafe Delivery')
subscription_setup= Transition(label='Subscription Setup')
brew_guide        = Transition(label='Brew Guide')

# Build the choice for distribution: either drone or cold‐chain
distribution_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[drone_dispatch, cold_chain]
)

# Build the choice for final delivery: either to cafes or subscription path
# The subscription path is a strict sequence: Subscription Setup -> Brew Guide
subscription_seq = StrictPartialOrder(nodes=[subscription_setup, brew_guide])
subscription_seq.order.add_edge(subscription_setup, brew_guide)

delivery_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[cafe_delivery, subscription_seq]
)

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    farm_registration,
    lot_selection,
    hand_picking,
    fermentation_chk,
    quality_scoring,
    blockchain_tag,
    demand_forecast,
    roast_profiling,
    batch_roasting,
    nfc_embedding,
    eco_packaging,
    distribution_choice,
    delivery_choice
])

# Define the control‐flow / partial‐order edges
root.order.add_edge(farm_registration, lot_selection)
root.order.add_edge(lot_selection, hand_picking)
root.order.add_edge(hand_picking, fermentation_chk)
root.order.add_edge(fermentation_chk, quality_scoring)

# After scoring, blockchain tagging and demand forecasting run in parallel
root.order.add_edge(quality_scoring, blockchain_tag)
root.order.add_edge(quality_scoring, demand_forecast)

# Both must finish before profiling & roasting
root.order.add_edge(blockchain_tag, roast_profiling)
root.order.add_edge(demand_forecast, roast_profiling)

# Continue the linear roast & packaging steps
root.order.add_edge(roast_profiling, batch_roasting)
root.order.add_edge(batch_roasting, nfc_embedding)
root.order.add_edge(nfc_embedding, eco_packaging)

# Then choose distribution, then choose final delivery
root.order.add_edge(eco_packaging, distribution_choice)
root.order.add_edge(distribution_choice, delivery_choice)