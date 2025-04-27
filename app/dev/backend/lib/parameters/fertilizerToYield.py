from .. import ParameterClassInterface
import plotly.express as plt
import pandas as pd

from .inference.universal_discourse import plantSpacing_universe_discourse, plantSpacing_membership_function

class Fertilizer():
    parameterValue: float
    def __init__(self, fetilizer, tune_fertilizer=False) -> None:
        self.parameterValue = fetilizer
        self.tune = tune_fertilizer


    """
        Fertilizer is designed differently
        No need for inference system
        It stores the quantity of ferilizer elements which is then used by the time series for final reading.
        This checks if fertilizer elements are sufficient
    """
    def inference(self) -> any:
        """
        fertilizer elements
        Phosphorus, Potasium, Calcium, Magnisium, Sodium, Nitrogen.
        All of this is stored in a dictionary and sent to the dataframe
        which is used to inflate the barchart
        """

        kvalue = 0
        Navalue = 0
        Mgvalue = 0
        CaValue = 0
        Pvalue = 0
        Nvalue = 0
        df = pd.DataFrame({
            "elements": ["K", "Na", "Mg", "Ca", "P", "N"],
            "values": [
                kvalue, 
                Navalue, 
                Mgvalue, 
                CaValue, 
                Pvalue, 
                Nvalue
                ]
        })
        df["index"] = df.index

        trace = plt.bar(df, x=df['elements'], y=df['values'],
                        text_auto=True, color=df['elements'],
                        title="Fertilizer"
                        )


        if self.tune:
            tunekvalue = self.tune["Tune_Potatium"] if self.tune["Tune_Potatium"] else kvalue
            tuneNavalue = self.tune["Tune_Sodium"] if self.tune["Tune_Sodium"] else Navalue
            tuneMgvalue = self.tune["Tune_Magnisium"] if self.tune["Tune_Magnisium"] else Mgvalue
            tuneCaValue = self.tune["Tune_Calcium"] if self.tune["Tune_Calcium"] else CaValue
            tunePvalue = self.tune["Tune_Phosphorus"] if self.tune["Tune_Phosphorus"] else Pvalue
            tuneNvalue = self.tune["Tune_Nitrogen"] if self.tune["Tune_Nitrogen"] else Nvalue

            df = pd.DataFrame({
                "elements": ["K", "Na", "Mg", "Ca", "P", "N"],
                "values": [
                tunekvalue, 
                tuneNavalue, 
                tuneMgvalue, 
                tuneCaValue, 
                tunePvalue, 
                tuneNvalue
                ]
            })

            df["index"] = df.index
            trace = plt.bar(df, x=df['elements'], y=df['values'],
                        text_auto=True, color=df['elements'],
                        title="Fertilizer"
                        )

        return trace
    
    
    async def updateGraph(self):
        pass







