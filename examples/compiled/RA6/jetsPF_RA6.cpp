#include "NtupleTools2_h.h"
#include "../tools/ConfigReader.h"
#include "../tools/CutFlow.h"
#include "../tools/THTools.h"
#include "TDirectory.h"

using namespace std;


bool jetsPF_RA6(EasyChain* tree, vector<unsigned>& selJet, CutSet& selCut) {

  ConfigReader config;
  // static since we read only once
  static float jet_pt_min      = config.getFloat("jet_pt_min", 40);
  static float jet_eta_max      = config.getDouble("jet_eta_max",   2.5);
  static bool  quick           = config.getBool("quick",false);
  static bool  isOldNtuple     = config.getBool("isOldNtuple",false);
  // the muon collection

  typedef LorentzM LOR;
  //if(isOldNtuple) 
  //typedef LorentzV LOR;
  
  vector<LOR>& JetsPF = tree->Get(&JetsPF, "ak5JetPF2PATCorrectedP4Pat");

  float HTPF = 0; 
  for( unsigned jet=0; jet<JetsPF.size(); ++jet ) {
    TString ptCut = "pt>";
    ptCut += jet_pt_min;
    if( !selCut.keepIf( ptCut          , JetsPF.at(jet).pt()         >  jet_pt_min     ) && quick ) continue;
    TString etaCut = "|eta|<";
    etaCut += jet_eta_max;
    if( !selCut.keepIf( etaCut         , fabs(JetsPF.at(jet).eta())  <  jet_eta_max    ) && quick ) continue;

    vector<int>&      Jets_IDloosePF            = tree->Get( &Jets_IDloosePF,  "ak5JetPF2PATPFJetIDloosePat" );
    if( !selCut.keepIf( "looseID"      , Jets_IDloosePF.at(jet)                        ) && quick ) continue;


    if( quick || selCut.applyCuts(ptCut+" "+etaCut+" looseID" ) )
      selJet.push_back(jet);

  }// jet loop


}//main

