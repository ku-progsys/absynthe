import PlotLinesDomain
import tablePandasResults





def main(): 


    # redefine these constants based upon the name of the csv's
    # change values for entropy vs no entropy tables
    files = {"global": "./Results/pandas_global.csv", "window3": "./Results/pandas_window3.csv", "window7" : "./Results/pandas_window7.csv",
             "window5": "./Results/pandas_window5.csv", "noentropy": "./Results/pandas_size.csv", "nodomains" : "./Results/pandas_ent_nodoms.csv"}

    #change filenames for domains vs no domains line plot
    pandadomain = [files["window5"], files["nodomains"]]

    #change filenames for window size line plot
    pandawindocomp = [files["global"], files["window3"], files["window5"], files["window7"]]

    #Legends below
    pandawinlgnd = ["Global", "Window 3", "Window 5", "Window 7"]

    pandadomlgnd = ["Doms. Enabled" , "Doms. Disabled"]

    try: 
        PlotLinesDomain.plotLines(pandawindocomp, pandawinlgnd, "Effects of Window Size panda Benchmarks")
    except: 
        print("Error: Could Not Make Size Comparison Chart")
    try: 
        PlotLinesDomain.plotLines(pandadomain, pandadomlgnd, "Effects of Domains on panda Benchmarks")
    except: 
        print("Error: Could Not Make Domain Comparison Chart")
    try: 
        tablePandasResults.tablePandasResults(files["window5"], files["noentropy"])
    except: 
        print("Error: Could Not Make Table")
    

if __name__ == "__main__": 

    main()