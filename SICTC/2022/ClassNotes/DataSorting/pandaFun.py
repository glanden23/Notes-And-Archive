import matplotlib.pyplot as plt
import pandas

def readCSV(file, header):
    """readCSV Function
    
    Arguments:
        file: String of file path
        header: Line number of your headers
    
    Returns: CSV data set
    """
    return pandas.read_csv(file,header=header)

def getStats(data):
    """getStats Function
    
    Arguments:
        data: Pandas column data
    
    Returns: [Min, Max, Mean, Sum, Count]
    """
    return [data.min(), data.max(), data.mean(), data.sum(), data.count()]

def createGraph(data1,data2,graphTitle,title1,title2):
    """createGraph Function
    
    Arguments:
        data1: Pandas column data (x)
        data2: Pandas column data (y)
        graphTitle: Title of the graph
        title1: Title of the x axis
        title2: Title of the y axis
    
    Returns: Doesn't return, shows graph
    """
    plt.plot(data1, data2)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.title(graphTitle)
    plt.show()

def createBarGraph(data1,data2,graphTitle,title1,title2):
    """createBarGraph Function
    
    Arguments:
        data1: Pandas column data (x)
        data2: Pandas column data (y)
        graphTitle: Title of the graph
        title1: Title of the x axis
        title2: Title of the y axis
    
    Returns: Doesn't return, shows graph
    """
    plt.bar(data1, data2)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.title(graphTitle)
    plt.show()

def createPieGraph(data1,data2,graphTitle,title1,title2):
    """createPieGraph Function
    
    Arguments:
        data1: Pandas column data (x)
        data2: Pandas column data (y)
        graphTitle: Title of the graph
        title1: Title of the x axis
        title2: Title of the y axis
    
    Returns: Doesn't return, shows graph
    """
    plt.pie(data1, data2)
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.title(graphTitle)
    plt.show()

def getMinIndex(data):
    """getMinIndex Function
    
    Arguments:
        data: Pandas column data
    
    Returns: [minData, index]
    """
    minData=0
    for i in range(len(data)):
        if (data[i] < minData):
            minData = data[i]
            index = i
    return [minData,index]

def getMaxIndex(data):
    """getMaxIndex Function
    
    Arguments:
        data: Pandas column data
    
    Returns: [maxData, index]
    """
    maxData=0
    for i in range(len(data)):
        if (data[i] > maxData):
            maxData = data[i]
            index = i
    return [maxData,index]

def replaceData(data,target,replacement):
    """replaceData Function
    
    Arguments:
        data: Pandas column data
        target: value being replaced
        replacement: what value is being replaced with
    
    Returns: Pandas column data
    """
    return data.replace(target,replacement)

def dropData(data,subnet,inplace):
    """dropData Function
    
    Arguments:
        data: Panda ENTIRE data set
        subset: header string value for column data
        inplace: True/False
    """
    data.dropna(subset=[subnet],inplace=inplace)