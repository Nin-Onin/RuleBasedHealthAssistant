class HealthExpertSystem:
    def __init__(self, temperature, breathing, headache, cough, sore_throat, allergy):
        self.temperature = temperature
        self.breathing = breathing
        self.headache = headache
        self.cough = cough
        self.sore_throat = sore_throat
        self.allergy = allergy

    def get_diagnosis(self):
        if self.temperature < 37:
            return "No Fever"
        elif 37 <= self.temperature < 38:
            return "Low Fever"
        else:
            return "High Fever"

    def get_condition(self):
        if self.breathing == "light":
            return "Nasal Discharge"
        elif self.breathing == "heavy":
            return "Sinus Membranes Swelling"
        else:
            return "Normal"

    def get_treatment(self):
        if self.temperature >= 37 and self.headache and self.cough and self.sore_throat and not self.allergy:
            return "Take antibiotics and consult a doctor."
        elif self.allergy:
            return "Avoid antibiotics due to allergy. Use alternative treatment."
        else:
            return "Take rest and fluids."

    def is_abnormal(self, label, value):
        if label == "Diagnosis:" and value != "No Fever":
            return True
        if label == "Condition:" and value != "Normal":
            return True
        if label == "Treatment:" and value not in ["Take rest and fluids."]:
            return True
        return False
