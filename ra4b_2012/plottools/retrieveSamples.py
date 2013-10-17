import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import readySamples as samples


#sys.path.append('

#from .. import readySamples as samples
#import ra4b_2012.readySamples as samples


#Gets/creates the reweighted and/or merged files from the samples
#stated in readySamples

def getSample(sampleSelectionDict,mergeRWOptions):
    '''select the samples to plot'''
    dataSample=sampleSelectionDict['Sample']
    dataEstimation=sampleSelectionDict['Estimation']
    dataTail=sampleSelectionDict['Tail']
    dataSampleString='samples.'+dataSample+'_'+dataEstimation+'_'+dataTail+'(mergeRWOptions)'
    print 'the string is ',dataSampleString
    datSample=eval(dataSampleString)
    return datSample

def retrieveSamples(dataValues,dataMergeRWOptions):
    dataTags=['Sample','Estimation','Tail']
    dataSelectionDict=dict(zip(dataTags,dataValues))
    sample=getSample(dataSelectionDict,dataMergeRWOptions)
    return sample
    


if __name__=='__main__':


    #EXAMPLE ON HOW TO USE THIS:
    #
    #in readySamples, there is a function called TTJetsMG_CR1_NoTail
    # which a set of root files are specified:
    #
    #
    #
    #def TTJetsMG_CR1_NoTail(options):
    #
    #Samp=Sample()
    #Samp.isData=False
    #Samp.AddRootFile('TTJetsMG/SemiLept/TTJetsMG_SemiLept_CR1_NoTail.root')
    #Samp.AddRootFile('TTJetsMG/DiLept/TTJetsMG_DiLept_CR1_NoTail.root')
    #Samp.AddRootFile('TTJetsMG/FullyHad/TTJetsMG_FullyHad_CR1_NoTail.root')
    #Samp.ReweightAndMerge(options)
    #return Samp    


    #the argument options is a dictionary in which we specify if we would like to reweight the files,
    #and if we would like to merge them after the reweighting.

    #Suppose we have a data file with a lumi of 10000, we would like to reweight each of the
    #ttjets samples to 10000 and then merge them, this can be accomplished easily like this:
    #
    #
    #
    mcMergeRWOptions={} #---defines it to be a directory
    mcMergeRWOptions['RW']=True #--defines that they should be reweighted
    mcMergeRWOptions['dataLumi']=[10000] #defines the lumi to which to reweight the files, it has
    # to be on a list!
    mcMergeRWOptions['Merge']=True # we would like to merge them afterwards
    #
    #
    #
    print 'going to retrieve'
    ttjets=retrieveSamples(['TTJetsMG','CR1','NoTail'],mcMergeRWOptions)
    








