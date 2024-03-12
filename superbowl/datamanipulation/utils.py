from pyairtable import Api

class Utils:

    #I accept a recordset from Airtable and group it by brand
    def groupByBrand(self,commercials):
        brands = {}
        for commercial in commercials:
            if commercial['fields']['brand'] in brands:
                brands[commercial['fields']['brand']] = brands[commercial['fields']['brand']] + 1
            else:
                brands[commercial['fields']['brand']] = 1
        return brands