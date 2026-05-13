# Rule - Based Health Assistant

## 📖 About
Rule-Based Medical Assistant is a simple expert system developed as Laboratory Exercise - 2 in CSci 141 Intelligent Systems. It processes inputs such as temperature, breathing, symptoms, and allergies through rule-based logic, then delivers a diagnosis, condition, and treatment using Python’s Tkinter GUI.

## ✨ Features/Demo
#### Welcome Interface
<img src="./assets/Welcome-UI.png" alt="LS" width="600" height="400">

#### Main Interface
<img src="./assets/Main-UI.png" alt="LS" width="600" height="400">

#### Result Interface
<img src="./assets/Result-UI.png" alt="LS" width="600" height="400">

## 🛠️ Tech stack
* Python 3.x <br>
* Tkinter / ttk <br>
* Pillow (PIL) <br>

## ⚙️ Getting Started
### Prerequisites
* Python 3.x <br>
* pip <br>
### Installation & Run
1. Installation & Run <br>
   &nbsp; &nbsp; git clone https://github.com/Nin-Onin/RuleBasedHealthAssistant.git <br>
   &nbsp; &nbsp; cd RuleBasedHealthAssistant
2. Install the required dependency <br>
   &nbsp; &nbsp; pip install pillow <br>
3. Run the application <br>
   &nbsp; &nbsp; python RuleBasedHealthAssistant.py

## 🚀 Usage
1. Click Get Started on the welcome screen.
2. Fill in the patient's name, temperature (°C), breathing type, symptoms, and allergy status.
3. Click Evaluate to see the diagnosis result.

| Output | Rule |
|---|---|
| No Fever | Temperature < 37°C |
| Low Fever | 37°C ≤ Temperature < 38°C |
| High Fever | Temperature ≥ 38°C |
| Nasal Discharge | Breathing = Light |
| Sinus Membranes Swelling | Breathing = Heavy |
| Take antibiotics and consult a doctor | Fever + all symptoms + no allergy |
| Avoid antibiotics, use alternative treatment | Allergy = Yes |
| Take rest and fluids | No fever or no symptoms |

## 👤 Author
**Niño M. Austria**
- Course: CSci 141 – Intelligent Systems
- GitHub: [@Nin-Onin](https://github.com/Nin-Onin)
