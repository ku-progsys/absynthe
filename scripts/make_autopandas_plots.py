import PlotLinesDomain
import tablePandaResults
import tableSyGusResults





def main(): 


    # redefine these constants based upon the name of the csv's
    # change values for entropy vs no entropy tables
    files = {"global": "sygus_global.csv", "window3": "sygus_window3.csv", "window9" : "sygus_window9.csv",
             "window5": "sygus_window5.csv", "noentropy": "sygus_noheuristic.csv", "nodomains" : "sygus_nodomains.csv"}

    #change filenames for domains vs no domains line plot
    #domainsyg = [files["window5"], files["nodomains"]]

    #change filenames for window size line plot
    windocompsyg = [files["global"], files["window3"], files["window5"], files["window9"]]

    #Legends below
    sygwinlgnd = ["Global", "Window 3", "Window 5", "Window 9"]

    sygdomlgnd = ["Doms. Enabled" , "Doms. Disabled"]


    PlotLinesDomain.plotLines(windocompsyg, sygwinlgnd, "Effects of Window Size Sygus Benchmarks")

    #PlotLinesDomain.plotLines(domainsyg, sygdomlgnd, "Effects of Domains on Sygus Benchmarks", "sygus")

    tableSyGusResults.tableSygusResults(files["window5"], files["noentropy"])

    

if __name__ == "__main__": 

    main()