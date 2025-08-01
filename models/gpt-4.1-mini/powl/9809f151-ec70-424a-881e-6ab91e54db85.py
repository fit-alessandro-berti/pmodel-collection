# Generated from: 9809f151-ec70-424a-881e-6ab91e54db85.json
# Description: This process facilitates the systematic transfer and adaptation of innovative ideas and technologies between unrelated industries to foster breakthrough advancements. It involves identifying emerging trends, scouting potential partners from diverse sectors, conducting feasibility analyses, adapting concepts to new contexts, prototyping, iterative testing, regulatory alignment, intellectual property management, and finally, scaling through joint ventures or licensing agreements. The complexity lies in navigating unfamiliar domain constraints, aligning disparate stakeholder incentives, and ensuring the innovation remains viable and competitive across different market landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

TrendScan = Transition(label='Trend Scan')
PartnerScout = Transition(label='Partner Scout')
FeasibilityCheck = Transition(label='Feasibility Check')
ConceptAdapt = Transition(label='Concept Adapt')
PrototypeBuild = Transition(label='Prototype Build')
IterateTest = Transition(label='Iterate Test')
ComplianceAlign = Transition(label='Compliance Align')
IPSecure = Transition(label='IP Secure')
MarketMap = Transition(label='Market Map')
StakeholderSync = Transition(label='Stakeholder Sync')
ResourceAllocate = Transition(label='Resource Allocate')
RiskAssess = Transition(label='Risk Assess')
JointVenture = Transition(label='Joint Venture')
LicenseSetup = Transition(label='License Setup')
ScaleLaunch = Transition(label='Scale Launch')

# Build the iterative testing loop: (Prototype Build -> Iterate Test)*
# Loop = * (PrototypeBuild, IterateTest)
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, IterateTest])

# Scaling choice: Joint Venture or License Setup
scaling_choice = OperatorPOWL(operator=Operator.XOR, children=[JointVenture, LicenseSetup])

# Partial order for the first phase up to testing_loop
first_phase_nodes = [TrendScan, PartnerScout, FeasibilityCheck, ConceptAdapt, testing_loop, ComplianceAlign, IPSecure, MarketMap, StakeholderSync, ResourceAllocate, RiskAssess]
first_phase = StrictPartialOrder(nodes=first_phase_nodes)

# Define order edges for the first phase
first_phase.order.add_edge(TrendScan, PartnerScout)          # Identify partners after trends
first_phase.order.add_edge(PartnerScout, FeasibilityCheck)   # Check feasibility of partners
first_phase.order.add_edge(FeasibilityCheck, ConceptAdapt)   # Adapt concept after feasibility
first_phase.order.add_edge(ConceptAdapt, testing_loop)       # Prototype and test after adaptation
first_phase.order.add_edge(testing_loop, ComplianceAlign)    # Align compliance after testing
first_phase.order.add_edge(ComplianceAlign, IPSecure)        # Secure IP after compliance
first_phase.order.add_edge(IPSecure, MarketMap)              # Map market after securing IP
first_phase.order.add_edge(MarketMap, StakeholderSync)       # Sync stakeholders after market mapping
first_phase.order.add_edge(StakeholderSync, ResourceAllocate) # Allocate resources after stakeholder sync
first_phase.order.add_edge(ResourceAllocate, RiskAssess)     # Assess risk after resources allocated

# Final phase: scale launch after scaling choice
final_phase = StrictPartialOrder(nodes=[scaling_choice, ScaleLaunch])
final_phase.order.add_edge(scaling_choice, ScaleLaunch)

# Root model: first phase followed by final phase
root = StrictPartialOrder(nodes=[first_phase, final_phase])
root.order.add_edge(first_phase, final_phase)