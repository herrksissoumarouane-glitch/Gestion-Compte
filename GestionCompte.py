class SoldeNegatifError(Exception):
    def __str__(self):
        return "le solde ne doit pas etre negatif"

class MontantInvalideError(Exception):
    def __str__(self):
        return "le montant doit etre un entier positif"

class Compte:
    def __init__(self, solde=0):
        self.solde = solde
        self.historique = []

    def afficher_solde(self):
        return self.solde

    def deposer(self, montant):
        if montant <= 0:
            raise MontantInvalideError()
        self.solde += montant
        self.historique.append(f"Depot: +{montant} -> solde: {self.solde}")

    def retirer(self, montant):
        if montant <= 0:
            raise MontantInvalideError()
        if montant > self.solde:
            raise SoldeNegatifError()
        self.solde -= montant
        self.historique.append(f"Retrait: -{montant} -> solde: {self.solde}")

def menu():
    print("\n1. Afficher le solde")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Historique")
    print("5. Quitter")

def run():
    compte = Compte()
    while True:
        try:
            menu()
            choix = int(input("Choix: "))
            if choix == 1:
                print(f"Solde actuel: {compte.afficher_solde()}")
            elif choix == 2:
                m = int(input("Montant à déposer: "))
                compte.deposer(m)
                print(f"Déposé: {m}. Nouveau solde: {compte.afficher_solde()}")
            elif choix == 3:
                m = int(input("Montant à retirer: "))
                compte.retirer(m)
                print(f"Retiré: {m}. Nouveau solde: {compte.afficher_solde()}")
            elif choix == 4:
                if not compte.historique:
                    print("Aucune opération pour l'instant.")
                else:
                    for ligne in compte.historique:
                        print(ligne)
            elif choix == 5:
                print("Au revoir.")
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
        except MontantInvalideError as mie:
            print(mie)
        except SoldeNegatifError as sne:
            print(sne)
        except Exception as e:
            print("Erreur inattendue:", e)

if __name__ == "__main__":
    run()
