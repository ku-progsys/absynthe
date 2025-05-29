import PlotLinesDomain
import tablePandaResults
import tableSyGusResults





def main(): 


    # redefine these constants based upon the name of the csv's
    # change values for entropy vs no entropy tables
    sygcompare = {"entropy": "table1-entropy.csv", "noentropy": "table1-noabs.csv"}
    pandacompare = {"entropy": "table2-entropy.csv", "noentropy": "table2-noabs.csv"}

    #change filenames for domains vs no domains line plot
    domainsyg = ["table1-entropycopy2.csv", "table1-entropycopy.csv"]
    domainpnd = ["table2-entropy.csv", "table2-noabs.csv"]

    #change filenames for window size line plot
    windocompsyg = ["table1-entropycopy.csv", "table1-entropycopy2.csv", "table1-entropycopy3.csv", "table1-entropycopy4.csv"]
    windowcomppnd = ["table2-entropy.csv", "table2-entropy.csv", "table1-entropycopy.csv", "table1-entropycopy2.csv"]

    #Legends below
    sygwinlgnd = ["Global", "Window 3", "Window 5", "Window 9"]
    pndwinlgnd = ["Global", "Window 3", "Window 5", "Window 9"]

    sygdomlgnd = ["Doms. Enabled" , "Doms. Disabled"]
    pnddomlgnd = ["Doms. Enabled" , "Doms. Disabled"]


    PlotLinesDomain.plotLines(windocompsyg, sygwinlgnd, "Effects of Window Size Sygus Benchmarks")
    PlotLinesDomain.plotLines(windowcomppnd, pndwinlgnd, "Effects of Window Size Pandas Benchmarks")

    PlotLinesDomain.plotLines(domainsyg, sygdomlgnd, "Effects of Domains on Sygus Benchmarks")
    PlotLinesDomain.plotLines(domainpnd, pnddomlgnd, "Effects of Domains on Pandas Benchmarks")

    tablePandaResults.tablePandasResults(pandacompare["entropy"], pandacompare["noentropy"])
    tableSyGusResults.tableSygusResults(sygcompare["entropy"], sygcompare["noentropy"])

    





if __name__ == "__main__": 

    main()