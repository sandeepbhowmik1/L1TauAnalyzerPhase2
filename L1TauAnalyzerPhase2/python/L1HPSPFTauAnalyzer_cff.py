import FWCore.ParameterSet.Config as cms

genMatchedTaus = cms.EDFilter("genMatchTauFilter",
        taus = cms.InputTag("slimmedTaus")
    )

goodTaus = cms.EDFilter("PATTauRefSelector",
        #src = cms.InputTag("slimmedTaus"),
        src = cms.InputTag("genMatchedTaus"),
        cut = cms.string(
        'pt > 20 && abs(eta) < 2.4 '
        '&& abs(charge) > 0 && abs(charge) < 2 '
        '&& tauID("decayModeFinding") > 0.5 '
        #'&& tauID("chargedIsoPtSum") < 2.5'
        '&& tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5'
        #'&& tauID("byMediumIsolationMVArun2v1DBoldDMwLT") > 0.5 '
        #'&& tauID("againstMuonTight3") > 0.5 '
        #'&& tauID("againstElectronVLooseMVA6") > 0.5 '
        ),
        filter = cms.bool(False)
)

genVertexProducer = cms.EDProducer("GenVertexProducer",
  #src = cms.InputTag('prunedGenParticles'),
  src = cms.InputTag('genParticles'),
  pdgIds = cms.vint32(-15, +15) # CV: use { -15, +15 } for signal, empty list for background                                    
) 

L1HPSPFTauAnalyzer = cms.EDAnalyzer("L1HPSPFTauAnalyzer",
                                        debug              = cms.untracked.bool(False),
                                        isReco             = cms.untracked.bool(False),
                                        min_pt             = cms.untracked.double(20),
                                        #max_eta            = cms.untracked.double(2.4),
                                        max_eta            = cms.untracked.double(3.0),
                                        genTagToken        = cms.InputTag("generator"),
                                        genVertexToken     = cms.InputTag("genVertexProducer", "z0"),
                                        #l1VertexToken      = cms.InputTag("VertexProducer", "l1vertices"),
                                        l1VertexToken      = cms.InputTag("L1TkPrimaryVertex"),
                                        genTauToken        = cms.InputTag("tauGenJetsSelectorAllHadrons"),
                                        l1TauToken         = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithStripsAndPreselectionPF"),        # _1
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithStripsAndPreselectionPuppi"),     # _2
                                        l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithStripsWithoutPreselectionPF"),    # _3
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithStripsPF"),    # _3 
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithStripsWithoutPreselectionPuppi"), # _4
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithoutStripsAndPreselectionPF"),     # _5
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithoutStripsAndPreselectionPuppi"),  # _6
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithoutStripsWithPreselectionPF"),    # _7
                                        #l1PFTauToken       = cms.InputTag("L1HPSPFTauProducerWithoutStripsWithPreselectionPuppi"), # _8
                                        recoVertexToken    = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        recoTauToken       = cms.InputTag("slimmedTaus"),
                                        recoGMTauToken     = cms.InputTag("goodTaus"),
                                        treeName           = cms.string("L1PFTauAnalyzer"),
                                        fillBDT            = cms.untracked.bool(False),
                                        bdtRootFileName    = cms.string("bdt_test_L1HPSPFTauAnalyzer.root"),
                                        treeBDTName        = cms.string("L1PFTauAnalyzer"),
                                        createHistRoorFile = cms.untracked.bool(False),
                                        histRootFileName   = cms.string("hist_test_L1HPSPFTauAnalyzer.root"),
                                        applyBDT           = cms.untracked.bool(False),
                                        #bdtInputFileName   = cms.string("L1TauAnalyzerPhase2/L1TauAnalyzerPhase2/data/L1HPSPFTau_XGB_testVars_default_7Var_20200219_3.xml"),  # _3
                                        #bdtInputFileName   = cms.string("L1TauAnalyzerPhase2/L1TauAnalyzerPhase2/data/L1HPSPFTau_XGB_testVars_default_7Var_20200219_4.xml"),  # _4 
                                        bdtInputFileName   = cms.string("L1TauAnalyzerPhase2/L1TauAnalyzerPhase2/data/L1HPSPFTau_XGB_testVars_default_6Var_20200304_4.xml"),  # _4
                                        )


AnalyzerSeq = cms.Sequence(
    #genVertexProducer +
    #genMatchedTaus +
    #goodTaus       +
    L1HPSPFTauAnalyzer
)
