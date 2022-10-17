import pandas  
import numpy as npy
#import sklearn
import matplotlib.pyplot as plt
from scipy import stats as st
#from sklearn import linear_model
from scipy import stats


class TempManger:
    
    #Atributos
    df = pandas.read_excel("TempFilter.xlsx")
    
    

    @classmethod
    def AnnualAvgAnnoMax(cls,anno: int):
        """Devuelve el promedio de las temperaturas máximas registradas en el año 
        especificado por parámetro

        Args:
            anno (int)

        Returns:
            _type_: float
        """
        var = 0
        cont = 0
        for i in range (len(cls.df)):
            if cls.df["Año"][i] == anno:
                var += cls.df["Maxima Media"][i]
                cont +=1
        return (var/cont) 
    
    @classmethod
    def AnnualAvgAnnoMin(cls,anno: int):
        """Devuelve el promedio de las temperaturas minimas registradas en el año 
        especificado por parámetro

        Args:
            anno (int)

        Returns:
            _type_: float
        """
        var = 0
        cont = 0
        for i in range (len(cls.df)):
            if cls.df["Año"][i] == anno:
                var += cls.df["Minima Media"][i]
                cont +=1
        return (var/cont) 
    
    
    @classmethod
    def AnnualAvgProvsegunAnnoMax(cls, prov: str, anno: int):
        """Devuelve el promedio anual de la temperatura máxima de la provincia especificada por parámetro
        en el año especificado por parámetro

        Args:
            prov (str): 
            anno (int):

        Returns:
            _type_: float
        """
        var = 0
        cont = 0
        for i in range (len(cls.df)):
            if cls.df['Provincia'][i] == prov and cls.df["Año"][i] == anno:
                var += cls.df["Maxima Media"][i]
                cont +=1
        return (var/cont)
    
    @classmethod
    def AnnualAvgProvsegunAnnoMin(cls, prov: str, anno: int):
        """Devuelve el promedio anual de la temperatura mínima de la provincia especificada por parámetro
        en el año especificado por parámetro

        Args:
            prov (str): 
            anno (int):

        Returns:
            _type_: float
        """
        var = 0
        cont = 0
        for i in range (len(cls.df)):
            if cls.df['Provincia'][i] == prov and cls.df["Año"][i] == anno:
                var += cls.df["Minima Media"][i]
                cont +=1
        return (var/cont)
    
        
    @classmethod
    def FullAnnualAvgAnnoallProvMax(cls):
        """Devuelve el promedio anual de las temperaturas maximas de cada año registrado en la base de 
        datos

        Returns:
            _type_: DataFrame
        """
        lista = []
        listaaux = []
        for i in cls.df["Año"]:
            if i not in listaaux:
                lista.append(cls.AnnualAvgAnnoMax(i))
                listaaux.append(i)
        dfresult = pandas.DataFrame({"Años": listaaux, "Maxima Media" : lista })
        return dfresult
    
    @classmethod
    def FullAnnualAvgAnnoallProvMin(cls):
        """Devuelve el promedio anual de las temperaturas mínimas de cada año registrado en la base de 
        datos

        Returns:
            _type_: DataFrame
        """
        lista = []
        listaaux = []
        for i in cls.df["Año"]:
            if i not in listaaux:
                lista.append(cls.AnnualAvgAnnoMin(i))
                listaaux.append(i)
        dfresult = pandas.DataFrame({"Años": listaaux, "Minima Media" : lista })
        return dfresult
    
    
    @classmethod
    def FullAnnualAvgProvsegunAnnoMax(cls, anno: int ):
        """ 
        Devuelve la máxima media de temperaturas de 
        todas las provincias segun el año
        pasado por parámetro  
        
        Args: año(int)
        
        Return: list(int)
        """
        lista = []
        listaaux = []
        for i in range (len(cls.df)):
            if cls.df["Año"][i] == anno and cls.df["Provincia"][i] not in listaaux :
                lista.append(cls.AnnualAvgProvsegunAnnoMax(cls.df["Provincia"][i], anno))
                listaaux.append(cls.df["Provincia"][i])
        dfresult = pandas.DataFrame({"Provincias": listaaux, "Maxima Media": lista})
        return dfresult
    
    @classmethod
    def FullAnnualAvgProvsegunAnnoMin(cls, anno: int ):
        """ 
        Devuelve la mínima media de temperaturas de 
        todas las provincias segun el año
        pasado por parámetro  
        
        Args: año(int)
        
        Return: list(int)
        """
        lista = []
        listaaux = []
        for i in range (len(cls.df)):
            if cls.df["Año"][i] == anno and cls.df["Provincia"][i] not in listaaux :
                lista.append(cls.AnnualAvgProvsegunAnnoMin(cls.df["Provincia"][i], anno))
                listaaux.append(cls.df["Provincia"][i])
        dfresult = pandas.DataFrame({"Provincias": listaaux, "Minima Media": lista})
        return dfresult
    
    
    @classmethod
    def FullAnnualAvgAnnosegunProvMax(cls, prov: str):
        """ 
        Devuelve la máxima media de temperaturas de 
        de la povincia pasada por parámetro durante todos 
        los años que se alamacenan en BD
        
        Args: 
            año(int)
        
        Returns: 
            __type__: list
        """
        lista = []
        listaaux = []
        for i in range (len(cls.df)):
            if cls.df["Provincia"][i] == prov and cls.df["Año"][i] not in listaaux :
                lista.append(cls.AnnualAvgProvsegunAnnoMax(prov, cls.df["Año"][i]))
                listaaux.append(cls.df["Año"][i])
        dfresult = pandas.DataFrame({"Años": listaaux, "Maxima Media": lista})
        return dfresult

   

    
    @classmethod
    def FullAnnualAvgAnnosegunProvMin(cls, prov: str):
        """Devuelve la mínima media de temperaturas de 
        de la povincia pasada por parámetro durante todos 
        los años que se alamacenan en BD
        
        Args: 
            año(int)
        
        Returns: 
            __type__: list
        """
        lista = []
        listaaux = []
        for i in range (len(cls.df)):
            if cls.df["Provincia"][i] == prov and cls.df["Año"][i] not in listaaux :
                lista.append(cls.AnnualAvgProvsegunAnnoMin(prov, cls.df["Año"][i]))
                listaaux.append(cls.df["Año"][i])
        dfresult = pandas.DataFrame({"Años": listaaux, "Minima Media": lista})
        return dfresult
    
    
    #@classmethod
    #def PredictionAnnualMax_Media(cls, listaux: list):
        """Devuelve los resultados de las predicciones de la maxima media de las temperaturas 
        durante los años especificados por parámetro
        Args:
            listaux (list)
        Returns:
            _type_: DataFrame
        """
        df = pandas.read_excel("TempFilter.xlsx")
        a = npy.array([cls.FullAnnualAvgAnnoallProvMax()["Años"]]).reshape(-1,1) 
        b = npy.array([cls.FullAnnualAvgAnnoallProvMax()["Maxima Media"]]).reshape(-1,1)
        regr = linear_model.LinearRegression()
        regr.fit(a, b)
        list = []
        for i in listaux:
            list.append(regr.predict([[i]])[0][0])
        df1 = pandas.DataFrame({"Años":listaux , "Prediction_Max_Media":list})   
        return df1
    
    #@classmethod
    #def PredictionAnnualMin_Media(cls, listaux: list):
        """Devuelve los resultados de las predicciones de la minima media de las temperaturas 
        durante los años especificados por parámetro
        Args:
            listaux (list)
        Returns:
            _type_: DataFrame
        """
        df = pandas.read_excel("TempFilter.xlsx")
        a = npy.array([cls.FullAnnualAvgAnnoallProvMin()["Años"]]).reshape(-1,1) 
        b = npy.array([cls.FullAnnualAvgAnnoallProvMin()["Minima Media"]]).reshape(-1,1)
        regr = linear_model.LinearRegression()
        regr.fit(a, b)
        list = []
        for i in listaux:
            list.append(regr.predict([[i]])[0][0])
        df1 = pandas.DataFrame({"Años":listaux , "Prediction_Min_Media":list})   
        return df1
    
    
    
    
    #@classmethod
    #def PredictionbyProvencieMax_Media(cls, prov: str , listaux: list):
        """Devuelve los resultados de las predicciones de la maxima media de las temperaturas
        de las provician especificada porcparámetro durante los años especificados por parámetro

        Args:
            prov (str)
            listaux (list)

        Returns:
            _type_: DataFrame
        """
        df = pandas.read_excel("TempFilter.xlsx")
        a = npy.array([cls.FullAnnualAvgAnnosegunProvMax(prov)["Años"]]).reshape(-1,1) 
        b = npy.array([cls.FullAnnualAvgAnnosegunProvMax(prov)["Maxima Media"]]).reshape(-1,1)
        regr = linear_model.LinearRegression()
        regr.fit(a, b)
        list = []
        for i in listaux:
            list.append(regr.predict([[i]])[0][0])
            
    #@classmethod
    #def PredictionbyProvencieMin_Media(cls, prov: str , listaux: list):
        """Devuelve los resultados de las predicciones de la minima media de las temperaturas
        de las provician especificada porcparámetro durante los años especificados por parámetro

        Args:
            prov (str)
            listaux (list)

        Returns:
            _type_: DataFrame
        """
        df = pandas.read_excel("TempFilter.xlsx")
        a = npy.array([cls.FullAnnualAvgAnnosegunProvMin(prov)["Años"]]).reshape(-1,1) 
        b = npy.array([cls.FullAnnualAvgAnnosegunProvMin(prov)["Maxima Media"]]).reshape(-1,1)
        regr = linear_model.LinearRegression()
        regr.fit(a, b)
        list = []
        for i in listaux:
            list.append(regr.predict([[i]])[0][0])
            
        df1 = pandas.DataFrame({"Años":listaux , "Prediction_Min_Media":list})   
        return df1


    @classmethod
    def Total_DataFrame(cls):
        
        lista = []
        for element in cls.df['Anno']:
            if element not in cls.df['Anno']:
                newdf =cls.FullAnnualAvgProvsegunAnnoMax(element)
                lista.append(element)
        newdf.aggregate({'Anno':lista})

        return newdf

"""     
list = [2008,2009,2010]
df = TempManger.PredictionAnnualMax_Media(list)
df1 = TempManger.FullAnnualAvgAnnosegunProvMax(prov="Holguín")
print(df)
"""

class RainfallManager():
    #Atributos
    df = pandas.read_excel("RainfallFilter.xlsx")
    
    @classmethod
    def Describe(cls):
        print(cls.df.describe())

