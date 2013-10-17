from Plot_RootObjects import *
from Plot_SetRootObjectsOptions import *
from ROOT import SetOwnership,gROOT,gPad,gDirectory,TCanvas,TLine, TF1,TH1F,TH1D,TH1I,TFile,TKey,TString,THStack,TList,TLegend,TPaveText,TIter,TPad
from ROOT import TLine
import copy
#======================================
class SimpleStack:
    """a class to plot stacks and a ratio plot"""

    #def __init__(self,dataLumi,xT,yST,yRT,optDict):
    def __init__(self,Properties):
        #
        #
        self.rebOff=0  # rebinning offset
        self.rebN=0  # # bins to rebin
        #self.lumi=Properties.get('dataLumi')  # guess what
        self.xmin=0.0
        self.xmax=0.0
        self.pad1=0.0
        self.pad2=0.0
        self.theStack=BuildTHStack(Properties)        
        self.sumMC=0
        self.dataHistograms=[]
        self.signalHistograms=[]
        self.Properties=Properties
    #======================================





        
    #======================================
    #ADD BACKGROUND TO THE STACK
    #======================================
    def AddStack(self,histo):
        """it adds a certain histogram to the background stack """
        #dont forget about the rebinning
        if str(histo).find('nil') != -1:
            raise NameError('You are trying to add a null pointer to the stack')
        #
        self.theStack.Add(histo)

        if(self.sumMC==0):
            self.sumMC=histo.Clone()
        else:
            self.sumMC.Add(histo)
    #==========================================



    #======================================
    #ADD THE DATA
    #======================================
    def AddData(self,histo):
        """it simply adds a data histogram to the list"""
        self.dataHistograms.append(histo)
    #======================================


    #======================================
    #ADD THE SIGNAL
    #======================================
    def AddSignal(self,histo):
        """add a signal histogram to the list"""
        #print 'line width ',histo.GetLineWidth()
        self.signalHistograms.append(histo)
    #======================================        


    #======================================
    #DRAW THE OBJECTS
    #======================================
    def Draw(self):
        """draws the whole thing, stack + data + signals"""
        
        #if self.sumMC==0:
        #    print "WARNING: no stack plot"
        #if len(self.dataHistograms)==0:
        #    print "WARNING: no data plots have been added"
        #if len(self.signalHistograms)==0:
        #    pass
            #print "WARNING: no signal plots have been added"

        if str(gPad).find('nil')==0:
            raise NameError('No Canvas has been defined at this point')
        #
        #=====GET DATA HISTOGRAM
        if len(self.dataHistograms)>0:
            datah=self.dataHistograms[0]
        else:
            datah=False
        #
        #
        #=========TPAD1===========
        #pad1_logy=self.Properties.get('pad1_logy',1)

        pad1=BuildTPad(self.Properties,'pad1',0.1,0.3,0.9,0.9)
        #
        #
        #=======DRAW THE PADS=====
        self.pad1=pad1
        pad1.Draw()
        pad1.cd()
        pad1.DrawFrame(0.001,0.001,1.,1.)
        #
        #
        #
        #
        #
        #
        #
        #
        #===============================
        #=======ON THE FIRST PAD
        #===============================
        pad1.cd()
        #pad1.DrawFrame(0.,0.,1.,1.)
        #
        #
        #
        #=========SET AND DRAW THE STACK
        self.theStack.Draw(self.Properties.get('drawingOptions_stack','h'))
        #self.theStack.Draw('h')
        SetTHStackOptions(self.theStack,self.Properties)
        self.theStack.SetMinimum(self.Properties.get('StackMinimum',0.1))
        stackmaximum=self.Properties.get('StackMaximum')
        if stackmaximum != None:
            currentmax=self.theStack.GetMaximum()
            self.theStack.SetMaximum(currentmax*self.Properties.get('StackMaximum'))
        #
        #=========DRAW THE DATA
        if datah:
            datah.Draw(self.Properties.get('drawingOptions_data','same p e1'))
        gPad.Update()        
        #raw_input('before signal')        
        

        #=========DRAW THE SIGNALS
        for sig in self.signalHistograms:
            sig.Draw(self.Properties.get('drawingOptions_sig','same '))
            gPad.Update()
            #raw_input('signal added')
        #==========================
        #
        pad1.cd()

        

        
