# L1TauAnalyzerPhase2

cmsrel CMSSW_11_1_2

cd CMSSW_11_1_2/src

cmsenv


git cms-init

git clone https://github.com/sandeepbhowmik1/L1TauProducerPhase2 $CMSSW_BASE/src/L1Trigger/Phase2L1Taus

git clone https://github.com/sandeepbhowmik1/L1TauProducerPhase2-DataFormats $CMSSW_BASE/src/DataFormats/Phase2L1Taus

git cms-addpkg DataFormats/L1TCorrelator

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_2/src/DataFormats/L1TCorrelator/interface/TkPrimaryVertex.h $CMSSW_BASE/src/DataFormats/L1TCorrelator/interface

cp /home/sbhowmik/HLTTau/HLTTauProducerPhase2/CMSSW_11_1_2/src/DataFormats/L1TCorrelator/src/classes_def.xml $CMSSW_BASE/src/DataFormats/L1TCorrelator/src


git clone https://github.com/sandeepbhowmik1/L1TauAnalyzerPhase2


scram b -j 8