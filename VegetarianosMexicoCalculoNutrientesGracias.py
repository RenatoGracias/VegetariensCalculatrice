from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from VegetarianosNutricionProgramaGracias import *

class BoxLayoutTest(BoxLayout):
    # Definir la variable pour l'objet texte "bienvenue"
    bienvenue_texte= StringProperty("Bienvenue!") # une fois cree on va l'assigner a l'objet texte correspondant dans le Kivy file en disant "text.bienvenuetexte" tout simplement
    # retrouver le nom utilizateur dans la variablenombre, text input object id "idnom"
    variable_nombre= ObjectProperty()
    #  fonction pour actualizer l'objet text "Bienvenue" en ajoutant le nom utilisateur de la variablenombre
    def accueillir(self):
        self.bienvenue_texte= "Bienvenue " + self.variable_nombre.text + "!"

    # Variable pour montrer la IMC
    resultat_IMC = StringProperty("IMC")
    # variables pour recuperer les dates de base del utilisateur
    age= ObjectProperty()
    poids= ObjectProperty()
    taille= ObjectProperty()

    # definir la fonction pour calculer IMC a partir des variables age, poids et taille et assigner le resultat a la variable IMC
    def ActionCalculerIMC(self):
        try:
            IMC = (float(self.poids.text)) / (float(self.taille.text) * float(self.taille.text))
            if IMC > 18.5 and IMC < 24.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Peso Normal 'Normopeso' tambien conocido como 'peso ideal' ¡felicitaciones!"
            elif IMC < 18.5:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "bajo peso"
            elif IMC > 18.5 and IMC < 26.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Posible sobrepeso grado 1"
            elif IMC > 27 and IMC < 29.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Sobrepeso tipo 1 (preobesidad), se sugiere ejercicio y dieta hipocalorica, Nota: porfavor consulte a un especialista nutriologo o bien medico antes de considerar la sugerencia"
            elif IMC > 30 and IMC < 34.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Obesidad tipo 1 (leve), se sugiere ejercicio y dieta hipocalorica, Nota: porfavor consulte a un especialista nutriologo o bien medico antes de considerar la sugerencia"
            elif IMC > 35 and IMC < 39.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Obesidad tipo 2 (moderada), se sugiere ejercicio y dieta hipocalorica, Nota: porfavor consulte a un especialista nutriologo o bien medico antes de considerar la sugerencia"
            elif IMC > 40 and IMC < 49.9:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Obesidad tipo 3 (morbida Nota: de la etimologia latina 'morbidus' capaz de generar enfermedad), Porfavor consulte a su medico"
            elif IMC > 50:
                self.resultat_IMC = "Tu IMC es: " + str(IMC) + "Obesidad Extrema, porfavor consulte con el medico urgentemente"
        except:
            self.resultat_IMC = "Si-il vous plait rentrez-vous un nombre"
#     definition de la fonction pour calculer la TMB + facteur d'activite
    sexe = ObjectProperty()
    resultat_TMB= StringProperty("Resultado TMB")
    nivel_de_actividad= ObjectProperty()
    Resultat_TMB_et_facteur_d_activite= StringProperty("Resultado TMB + Facteur d'activite")
    selecciona_nivel=StringProperty("Selecciona tu nivel de actividad:")
    def Calculer_TMB(self):
        try:
            if float(self.sexe.text) == 1:
                TMBhombre = float(66) + (13.7 * float(self.poids.text)) + (float(5) * float(self.taille.text)) - (6.8 * float(self.age.text))
                self.resultat_TMB= "Tu TMB para 1 día es: " + str(TMBhombre)
            #variables pour la formule par le facteur d'activite
                actividadmuyligera = 1.2
                actividadligera = 1.375
                actividadmoderada = 1.55
                actividadactiva = 1.725
                actividadmuyactiva = 1.9
                if self.nivel_de_actividad.text == "1":
                    TMB_et_facteur_d_activite = float(TMBhombre) * actividadmuyligera
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "2":
                    TMB_et_facteur_d_activite = float(TMBhombre) * actividadligera
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "3":
                    TMB_et_facteur_d_activite = float(TMBhombre) * actividadmoderada
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "4":
                    TMB_et_facteur_d_activite = float(TMBhombre) * actividadactiva
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "5":
                    TMB_et_facteur_d_activite = float(TMBhombre) * actividadmuyactiva
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                else:
                    self.selecciona_nivel= "¡ORA ORA ORA ORA! elige entre el 1 y el 5"
            elif float(self.sexe.text) == 2:
                TMBfemme = float(655) + (9.6 * float(self.poids.text)) + (float(1.8) * float(self.taille.text)) - (4.7 * float(self.age.text))
                self.resultat_TMB= "Tu TMB para 1 día es: " + str(TMBfemme)
                actividadmuyligera = 1.2
                actividadligera = 1.375
                actividadmoderada = 1.55
                actividadactiva = 1.725
                actividadmuyactiva = 1.9
                if self.nivel_de_actividad.text == "1":
                    TMB_et_facteur_d_activite = float(TMBfemme) * actividadmuyligera
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "2":
                    TMB_et_facteur_d_activite = float(TMBfemme) * actividadligera
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "3":
                    TMB_et_facteur_d_activite = float(TMBfemme) * actividadmoderada
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "4":
                    TMB_et_facteur_d_activite = float(TMBfemme) * actividadactiva
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                elif self.nivel_de_actividad.text == "5":
                    TMB_et_facteur_d_activite = float(TMBfemme) * actividadmuyactiva
                    self.Resultat_TMB_et_facteur_d_activite = str(TMB_et_facteur_d_activite)
                else:
                    self.selecciona_nivel = "¡ORA ORA ORA ORA! elige entre el 1 y el 5"
        except:
            self.selecciona_nivel = "¡ORA ORA ORA ORA! elige entre el 1 y el 5"
#             On va a definir la variable pour conaitre la decision pour le type de diete soit it cetogenique ou regulier
    tipo_de_dieta=ObjectProperty()
    elige_tipo_de_dieta_label=StringProperty("Elige tipo de dieta: 1. Regular (alta en carbohidratos),")
    quantite_de_proteines_en_grames=StringProperty()
    quantite_de_lipides_en_grames = StringProperty()
    quantite_de_carbohidrates_en_grames = StringProperty()
    def calculer_les_grames_de_nutriments(self):
        try:
            if float(self.tipo_de_dieta.text) == 1:
                Cantidad_de_proteinas_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite) * 15 / 100
                Cantidad_de_proteinas_en_gramos = Cantidad_de_proteinas_en_kilocalorias / 4
                self.quantite_de_proteines_en_grames = str(int(Cantidad_de_proteinas_en_gramos))
                Cantidad_de_lipidos_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite) * 35 / 100
                Cantidad_de_lipidos_en_gramos = Cantidad_de_lipidos_en_kilocalorias / 9
                self.quantite_de_lipides_en_grames = str(int(Cantidad_de_lipidos_en_gramos))
                Cantidad_de_carbohidratos_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite) * 50 / 100
                Cantidad_de_carbohidratos_en_gramos = Cantidad_de_carbohidratos_en_kilocalorias / 4
                self.quantite_de_carbohidrates_en_grames = str(int(Cantidad_de_carbohidratos_en_gramos))
            if float(self.tipo_de_dieta.text) == 2:
                Cantidad_de_proteinas_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite)  * 15 / 100
                Cantidad_de_proteinas_en_gramos = Cantidad_de_proteinas_en_kilocalorias / 4
                self.quantite_de_proteines_en_grames = str(int(Cantidad_de_proteinas_en_gramos))
                Cantidad_de_lipidos_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite)  * 75 / 100
                Cantidad_de_lipidos_en_gramos = Cantidad_de_lipidos_en_kilocalorias / 9
                self.quantite_de_lipides_en_grames = str(int(Cantidad_de_lipidos_en_gramos))
                Cantidad_de_carbohidratos_en_kilocalorias = float(self.Resultat_TMB_et_facteur_d_activite)  * 10 / 100
                Cantidad_de_carbohidratos_en_gramos = Cantidad_de_carbohidratos_en_kilocalorias / 4
                self.quantite_de_carbohidrates_en_grames = str(int(Cantidad_de_carbohidratos_en_gramos))
        except:
            self.elige_tipo_de_dieta_label = "Elige un numero: 1 para dieta basada en carbohidratos o"


class InterfazApp(App):

    pass

InterfazApp().run()
#¡Benedictions! Merci mon Dieu. aaaaaaaaammmeeeeeennn



