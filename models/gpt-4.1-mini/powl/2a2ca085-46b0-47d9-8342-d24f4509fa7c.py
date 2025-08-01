# Generated from: 2a2ca085-46b0-47d9-8342-d24f4509fa7c.json
# Description: This process involves the intricate verification and authentication of rare antique assets for auction houses. It includes provenance research, material analysis, stylistic evaluation, condition reporting, and legal compliance checks. Each step requires collaboration between historians, scientists, legal experts, and auctioneers to ensure the asset's authenticity and market value before final cataloging and sale approval. Unexpected findings may trigger re-evaluation or legal hold, adding complexity to the workflow and requiring meticulous documentation and chain-of-custody management throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
AssetIntake = Transition(label='Asset Intake')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
StylisticReview = Transition(label='Stylistic Review')
ConditionReport = Transition(label='Condition Report')
LegalReview = Transition(label='Legal Review')
ExpertPanel = Transition(label='Expert Panel')
ScientificTest = Transition(label='Scientific Test')
ForgeryDetection = Transition(label='Forgery Detection')
ChainCustody = Transition(label='Chain Custody')
MarketAnalysis = Transition(label='Market Analysis')
CatalogEntry = Transition(label='Catalog Entry')
ReEvaluation = Transition(label='Re-Evaluation')
HoldNotification = Transition(label='Hold Notification')
FinalApproval = Transition(label='Final Approval')
AuctionSetup = Transition(label='Auction Setup')

skip = SilentTransition()

# Define forgery detection XOR node: either ForgeryDetection or skip 
# If forgery detected, go to ReEvaluation and HoldNotification
# We model the possible loop between initial analysis and re-analysis with a LOOP

# Scientific testing and forgery detection form a choice:
SciTestOrSkip = OperatorPOWL(operator=Operator.XOR, children=[ScientificTest, skip])
ForgeryDetectedChoice = OperatorPOWL(operator=Operator.XOR, children=[ForgeryDetection, skip])

# After ForgeryDetection, if detected, ReEvaluation and HoldNotification happen:
ReEvalHoldPO = StrictPartialOrder(nodes=[ReEvaluation, HoldNotification, ChainCustody])
ReEvalHoldPO.order.add_edge(ReEvaluation, HoldNotification)
ReEvalHoldPO.order.add_edge(HoldNotification, ChainCustody)

# ExpertPanel after ProvenanceCheck + MaterialScan + StylisticReview + ConditionReport
# We model the partial order of these four analyses before ExpertPanel

# PartialOrder of initial analyses
InitialAnalyses = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport])
# No order edges: concurrent analyses

# ExpertPanel after all these analyses
InitialAndExpert = StrictPartialOrder(nodes=[InitialAnalyses, ExpertPanel])
InitialAndExpert.order.add_edge(InitialAnalyses, ExpertPanel)

# BUT since these are POWL nodes, and InitialAnalyses is StrictPartialOrder and ExpertPanel is Transition,
# to be consistent with pm4py POWL, we need to flatten InitialAnalyses nodes into parent PO node.

# Actually pm4py expects nodes list of transitions/operatorPOWL or StrictPartialOrder; 
# However, POWL nodes are atomic, so to compose StrictPartialOrders, 
# we'd better create a PO of all initial + ExpertPanel nodes

# So let's create one PO with analyses + ExpertPanel, with order edges from each analysis to ExpertPanel

nodesInitialExpert = [ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport, ExpertPanel]
InitialExpertPO = StrictPartialOrder(nodes=nodesInitialExpert)
InitialExpertPO.order.add_edge(ProvenanceCheck, ExpertPanel)
InitialExpertPO.order.add_edge(MaterialScan, ExpertPanel)
InitialExpertPO.order.add_edge(StylisticReview, ExpertPanel)
InitialExpertPO.order.add_edge(ConditionReport, ExpertPanel)

# After ExpertPanel is ScientificTest or skip:
AfterExpertPO = StrictPartialOrder(nodes=[InitialExpertPO, SciTestOrSkip])
AfterExpertPO.order.add_edge(InitialExpertPO, SciTestOrSkip)

# Then ForgeryDetection or skip:
AfterSciTestPO = StrictPartialOrder(nodes=[AfterExpertPO, ForgeryDetectedChoice])
AfterSciTestPO.order.add_edge(AfterExpertPO, ForgeryDetectedChoice)

# Now we define the loop body:

# Loop body B is the part executed again after ReEvaluation
# So loop body B includes ChainCustody, MarketAnalysis, CatalogEntry, LegalReview, FinalApproval, AuctionSetup

# We create partial order for final steps after chain custody

FinalStepsNodes = [MarketAnalysis, CatalogEntry, LegalReview, FinalApproval, AuctionSetup]
FinalStepsPO = StrictPartialOrder(nodes=FinalStepsNodes)
# define logical ordering:
FinalStepsPO.order.add_edge(MarketAnalysis, CatalogEntry)
FinalStepsPO.order.add_edge(CatalogEntry, LegalReview)
FinalStepsPO.order.add_edge(LegalReview, FinalApproval)
FinalStepsPO.order.add_edge(FinalApproval, AuctionSetup)

# ChainCustody happens before final steps:
FinalAfterChain = StrictPartialOrder(nodes=[ChainCustody, FinalStepsPO])
FinalAfterChain.order.add_edge(ChainCustody, FinalStepsPO)

# Now, the loop body B is FinalAfterChain
loop_body_B = FinalAfterChain

# Loop body A is the initial big part (from Asset Intake through forgery detection & re-eval)
# which must be done before final steps

# Create initial partial order nodes:
# AssetIntake before initial analyses (all 4 analyses)
# So AssetIntake --> ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport

InitialBigPO_nodes = [AssetIntake] + nodesInitialExpert[:-1]  # exclude ExpertPanel since already included below

# Let's build a PO that captures these constraints:

# However, nodesInitialExpert includes ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport, ExpertPanel

# We'll build a PO with nodes: AssetIntake, ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport, ExpertPanel, SciTestOrSkip, ForgeryDetectedChoice

loop_A_nodes = [AssetIntake, ProvenanceCheck, MaterialScan, StylisticReview, ConditionReport, ExpertPanel, SciTestOrSkip, ForgeryDetectedChoice]

loop_A = StrictPartialOrder(nodes=loop_A_nodes)

# Add ordering edges:

loop_A.order.add_edge(AssetIntake, ProvenanceCheck)
loop_A.order.add_edge(AssetIntake, MaterialScan)
loop_A.order.add_edge(AssetIntake, StylisticReview)
loop_A.order.add_edge(AssetIntake, ConditionReport)

loop_A.order.add_edge(ProvenanceCheck, ExpertPanel)
loop_A.order.add_edge(MaterialScan, ExpertPanel)
loop_A.order.add_edge(StylisticReview, ExpertPanel)
loop_A.order.add_edge(ConditionReport, ExpertPanel)

loop_A.order.add_edge(ExpertPanel, SciTestOrSkip)
loop_A.order.add_edge(SciTestOrSkip, ForgeryDetectedChoice)

# Now the loop structure:

# LOOP(* (A,B)): execute A, then choose to exit or execute B then A again repeatedly.

# In this workflow, after ForgeryDetectedChoice:
# - If ForgeryDetection branch was chosen, we must do ReEvaluation, HoldNotification, ChainCustody then loop again
# - If skip branch (no forgery), we skip Re-Eval/Hold/ChainCustody and proceed to final steps

# So B in the loop will be the steps: ReEvaluation, HoldNotification, ChainCustody (to represent re-work and hold), then loop back to A

# Create B as the PO for re-eval and hold with ChainCustody:

loop_B_nodes = [ReEvaluation, HoldNotification, ChainCustody]
loop_B = StrictPartialOrder(nodes=loop_B_nodes)
loop_B.order.add_edge(ReEvaluation, HoldNotification)
loop_B.order.add_edge(HoldNotification, ChainCustody)

# Create the loop operator:
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_A, loop_B])

# After the loop, the final steps follow:

root = StrictPartialOrder(nodes=[loop, FinalStepsPO])
root.order.add_edge(loop, FinalStepsPO)