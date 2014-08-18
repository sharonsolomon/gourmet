from sqlalchemy import Integer, String, Float, Column, Text

from gourmet.models import meta

class Nutrition (meta.Base):
    __tablename__ = 'nutrition'

    ndbno = Column(Integer, primary_key=True, info={'label': "Nutrient Databank Number"})
    desc = Column(String(100), info={'label': "Short Description"})
    water = Column(Float, info={'label': _("Water")})
    kcal = Column(Float, info={'label': _("Kilocalories")})
    protein = Column(Float, info={'label': _("g protein")})
    lipid = Column(Float, info={'label': _("g lipid")})
    ash = Column(Float, info={'label': _("g ash")})
    carb = Column(Float, info={'label': _("g carbohydrates")})
    fiber = Column(Float, info={'label': _("g fiber")})
    sugar = Column(Float, info={'label': _("g sugar")})
    calcium = Column(Float, info={'label': _("mg calcium")})
    iron = Column(Float, info={'label': _("mg iron")})
    magnesium = Column(Float, info={'label': _("mg magnesium")})
    phosphorus = Column(Float, info={'label': _("mg phosphorus")})
    potassium = Column(Float, info={'label': _("mg potassium")})
    sodium = Column(Float, info={'label': _("mg sodium")})
    zinc = Column(Float, info={'label': _("mg zinc")})
    copper = Column(Float, info={'label': _("mg copper")})
    manganese = Column(Float, info={'label': _("mg manganese")})
    selenium = Column(Float, info={'label': _("microgram selenium")})
    vitaminc = Column(Float, info={'label': _("mg vitamin c")})
    thiamin = Column(Float, info={'label': _("mg thiamin")})
    riboflavin = Column(Float, info={'label': _("mg riboflavin")})
    niacin = Column(Float, info={'label': _("mg niacin")})
    pantoacid = Column(Float, info={'label': _("mg pantothenic acid")})
    vitaminb6 = Column(Float, info={'label': _("mg vitamin B6")})
    folatetotal = Column(Float, info={'label': _("microgram Folate Total")})
    folateacid = Column(Float, info={'label': _("microgram Folic acid")})
    foodfolate = Column(Float, info={'label': _("microgram Food Folate")})
    folatedfe = Column(Float, info={'label': _("microgram dietary folate equivalents")})
    choline = Column(Float, info={'label': _("Choline, total")})
    vitb12 = Column(Float, info={'label': _("microgram Vitamin B12")})
    vitaiu = Column(Float, info={'label': _("Vitamin A IU")})
    vitarae = Column(Float, info={'label': _("Vitamin A (microgram Retinal Activity Equivalents")})
    retinol = Column(Float, info={'label': _("microgram Retinol")})
    alphac = Column(Float, info={'label': _("microgram Alpha-carotene")})
    betac = Column(Float, info={'label': _("microgram Beta-carotene")})
    betacrypt = Column(Float, info={'label': _("microgram Beta Cryptoxanthin")})
    lypocene = Column(Float, info={'label': _("microgram Lycopene")})
    lutzea = Column(Float, info={'label': _("microgram Lutein+Zeazanthin")})
    vite = Column(Float, info={'label': _("mg Vitamin E")})
    vitk = Column(Float, info={'label': _("mg Vitamin K")})
    fasat = Column(Float, info={'label': _("g Saturated Fatty Acid")})
    famono = Column(Float, info={'label': _("g Monounsaturated Fatty Acids")})
    fapoly = Column(Float, info={'label': _("g Polyunsaturated Fatty Acids")})
    cholestrl = Column(Float, info={'label': _("mg Cholesterol")})
    gramwt1 = Column(Float, info={'label': "Gram Weight 1"})
    gramdsc1 = Column(String(100), info={'label': "Gram Weight Description 1"})
    gramwt2 = Column(Float, info={'label': "Gram Weight 2"})
    gramdsc2 = Column(String(100), info={'label': "Gram Weight Description 2"})
    refusepct = Column(Float, info={'label': _("Percent refuse")})
    foodgroup = Column(Text, info={'label': ''})

    not_summable = ['refusepct', 'gramwt1', 'gramwt2']
    # Not sure about gramwt1 and gramwt2...

    def __add__ (self, other):
        result = Nutrition()
        for c in Nutrition.__table__.columns:
            if isinstance (c.type, Float) and not c.name in self.not_summable:
                self_col = getattr(self, c.name) or 0
                other_col = getattr(other, c.name) or 0
                setattr(result, c.name, self_col+other_col)
        return result

    def __mul__ (self, other):
        result = Nutrition()
        for c in Nutrition.__table__.columns:
            if isinstance (c.type, Float) and not c.name in self.not_summable:
                self_col = getattr(self, c.name) or 0
                setattr(result, c.name, other*self_col)
        return result

    def __rmul__ (self, other):
        return self.__mul__(other)