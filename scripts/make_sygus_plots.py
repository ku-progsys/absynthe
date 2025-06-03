import PlotLinesDomain
import tableSyGusResults





def main(): 


    # redefine these constants based upon the name of the csv's
    # change values for entropy vs no entropy tables
    files = {"global": "./Results/sygus_global.csv", "window3": "./Results/sygus_window3.csv", "window7" : "./Results/sygus_window7.csv",
             "window5": "./Results/sygus_window5.csv", "noentropy": "./Results/sygus_size.csv", "nodomains" : "./Results/sygus_ent_nodoms.csv"}

    #change filenames for domains vs no domains line plot
    sygdomain = [files["window5"], files["nodomains"]]

    #change filenames for window size line plot
    sygwindocomp = [files["global"], files["window3"], files["window5"], files["window7"]]

    #Legends below
    sygwinlgnd = ["Global", "Window 3", "Window 5", "Window 7"]

    sygdomlgnd = ["Doms. Enabled" , "Doms. Disabled"]


    PlotLinesDomain.plotLines(sygwindocomp, sygwinlgnd, "Effects of Window Size Sygus Benchmarks")

    PlotLinesDomain.plotLines(sygdomain, sygdomlgnd, "Effects of Domains on Sygus Benchmarks")

    tableSyGusResults.tableSygusResults(files["window5"], files["noentropy"])

    

if __name__ == "__main__": 

    main()