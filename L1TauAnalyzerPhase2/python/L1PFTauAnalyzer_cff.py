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

L1PFTauAnalyzer = cms.EDAnalyzer("L1PFTauAnalyzer",
                                        debug              = cms.untracked.bool(False),
                                        isReco             = cms.untracked.bool(False),
                                        min_pt             = cms.untracked.double(20),
                                        max_eta            = cms.untracked.double(2.4),
                                        genTagToken        = cms.InputTag("generator"),
                                        genVertexToken     = cms.InputTag("genVertexProducer", "z0"),
                                        l1VertexToken      = cms.InputTag("VertexProducer", "l1vertices"),
                                        genTauToken        = cms.InputTag("tauGenJetsSelectorAllHadrons"),
                                        l1TauToken         = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
                                        #l1PFTauToken       = cms.InputTag("L1PFTauProducer","L1PFTaus"),
                                        #l1PFTauToken       = cms.InputTag("L1NNTauProducer","L1PFTausNN"), # _3
                                        l1PFTauToken       = cms.InputTag("L1NNTauProducerPuppi","L1PFTausNN"), # _4
                                        recoVertexToken    = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        recoTauToken       = cms.InputTag("slimmedTaus"),
                                        recoGMTauToken     = cms.InputTag("goodTaus"),
                                        treeName           = cms.string("L1PFTauAnalyzer"),
                                        fillBDT            = cms.untracked.bool(False),
                                        bdtRootFileName    = cms.string("bdt_test_L1PFTauAnalyzer.root"),
                                        treeBDTName        = cms.string("L1PFTauAnalyzer"),
                                        createHistRoorFile = cms.untracked.bool(True),
                                        histRootFileName   = cms.string("hist_test_L1PFTauAnalyzer.root"),
                                        applyBDT           = cms.untracked.bool(False),
                                        )


AnalyzerSeq = cms.Sequence(
    genVertexProducer +
    #genMatchedTaus +
    #goodTaus       +
    L1PFTauAnalyzer
)
