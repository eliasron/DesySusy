#!/usr/bin/python
import sys, os
import commands as com
from SetUpSample import SetUpSampleAndScript


#
#
def SampleFromSubSamples(SubSampleList):
    """dont know yet """
    
def cleanUpDir(outdir):
    #out=com.getoutput("rm -f merge_script.o*")
    file=open("cleanUpDir","w")
    out=com.getoutput('chmod u+x cleanUpDir')
    print outdir
    line='rm -f merge_script.o*'
    file.write(line+'\n')
    file.close()
    out=com.getoutput("mv cleanUpDir "+outdir+"/")
    
def MuHad():

    Scripts=[]
    Sample='MuHad'
    SubSample='Run2012A-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/data/MuHad/Run2012A-PromptReco-v1/190456-196531'
    Config='config_DATA_RA4b.txt'
    nFiles=3

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)


    Sample='MuHad'
    SubSample='Run2012B-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/data/MuHad/Run2012B-PromptReco-v1/SGE/190456-196531'
    Config='config_DATA_RA4b.txt'
    nFiles=7

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)


def ElectronHad():

    Scripts=[]
    Sample='ElectronHad'
    SubSample='Run2012A-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/data/ElectronHad/Run2012A-PromptReco-v1/190456-196531'
    Config='config_DATA_RA4b.txt'
    nFiles=3

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)

    Scripts=[]
    Sample='ElectronHad'
    SubSample='Run2012B-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/data/ElectronHad/Run2012B-PromptReco-v1/SGE/190456-196531'
    Config='config_DATA_RA4b.txt'
    nFiles=7
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)        


def SingleMu():

    Scripts=[]
    #Sample='SingleMu'
    #SubSample='Run2012A-PromptReco-v1'
    #FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/data/SingleMu/Run2012A-PromptReco-v1/190456-196531'
    #Config='config_DATA_RA4b.txt'
    #nFiles=3

    #
    #script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    #cleanUpDir('./'+Sample+'/'+SubSample)    
    #Scripts.append(script)


    Sample='SingleMu'
    SubSample='Run2012B-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/data/SingleMu/Run2012B-PromptReco-v1/'
    Config='config_DATA_RA4b.txt'
    nFiles=7

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)


def DoubleMu():

    Scripts=[]
    Sample='DoubleMu'
    SubSample='Run2012A-13Jul2012-v1'
    FilesDir='/scratch/hh/dust/naf/cms/user/schettle/nTuple12_v4c/data/DoubleMu/Run2012A-13Jul2012-v1'
    Config='config_DATA_RA4b.txt'
    nFiles=3

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)


    Sample='DoubleMu'
    SubSample='Run2012B-13Jul2012-v4'
    FilesDir='/scratch/hh/dust/naf/cms/user/schettle/nTuple12_v4c/data/DoubleMu/Run2012B-13Jul2012-v4'
    Config='config_DATA_RA4b.txt'
    nFiles=7

    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)    
    Scripts.append(script)



def TTJets():

    Scripts=[]
    Sample='TTJets'
    SubSample='SUMMER12'
    FilesDir='/scratch/hh/lustre/cms/user/sahin/nTuple12_v4b/mc/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)

    SubSample='SUMMER12POWHEG'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/schettle/nTuple12_v4b/mc/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)

def LM9():

    Scripts=[]
    Sample='LM9'
    SubSample='NoSub'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/SUSY_LM9_sftsht_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)

def LM6():

    Scripts=[]
    Sample='LM6'
    SubSample='NoSub'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/SUSY_LM6_sftsht_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)

def T2tt():

    Scripts=[]
    Sample='T2tt'
    SubSample='t500n100'
    FilesDir='/scratch/hh/current/cms/user/costanza/store/SMS-T2tt_FineBin_Mstop-225to1200_mLSP-0to1000_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=1
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    ########################################
    SubSample='t650n200'
    FilesDir='/scratch/hh/current/cms/user/costanza/store/SMS-T2tt_FineBin_Mstop-225to1200_mLSP-0to1000_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=1
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    ########################################
    SubSample='t750n400'
    FilesDir='/scratch/hh/current/cms/user/costanza/store/SMS-T2tt_FineBin_Mstop-225to1200_mLSP-0to1000_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=1
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)

def DYJetsToLL():

    Scripts=[]
    Sample='DYJets'
    SubSample='M-50'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12-PU_S7_START52_V9-v2/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    cleanUpDir('./'+Sample+'/'+SubSample)
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    Scripts.append(script)


def SingleTop():

    Scripts=[]
    Sample='SingleTop'
    SubSample='T-s-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/T_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    #============================================
    SubSample='T-t-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/T_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)                    
    #============================================
    SubSample='T-tW-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    #============================================
    SubSample='Tbar-s-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    #============================================
    SubSample='Tbar-t-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/eron/nTuple12_v2/mc/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    #============================================
    SubSample='Tbar-tW-channel'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1' 
    Config='config_MC_RA4b.txt'
    nFiles=3
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)
    #============================================    

    newscript=open('runall_'+Sample+'_All','w')
    for sc in Scripts:
        newline=sc+ ' $1 $2 '
        print newline
        newscript.write(newline+'\n')
    #

    
def WJetsToLNu():

    Scripts=[]
    Sample='WJetsToLNu'
    SubSample='NoSub'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12-PU_S7_START52_V9-v1'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)


def LM6():
    Scripts=[]
    Sample='LM6'
    SubSample='NoSub'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/SUSY_LM6_sftsht_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)



def LM9():
    Scripts=[]
    Sample='LM9'
    SubSample='NoSub'
    FilesDir=' /pnfs/desy.de/cms/tier2/store/user/msahin/nTuple12_v2/mc/SUSY_LM9_sftsht_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/'
    Config='config_MC_RA4b.txt'
    nFiles=3
    #
    script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)
    cleanUpDir('./'+Sample+'/'+SubSample)
    Scripts.append(script)


    
if __name__=='__main__':

    MuHad()
    ElectronHad()
    SingleMu()
    DoubleMu()
    TTJets()
    DYJetsToLL()
    WJetsToLNu()
    SingleTop()
    LM9()
    LM6()
    T2tt()
