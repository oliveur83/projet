using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

// code pour les parametre -----------------------------

public class parametre : MonoBehaviour
{
    public GameObject niveau1,client1,aide1,aide2,visuel1,erreur;// variable pour changer le texte 
   public static int niveaux = 1;//variable pour la fonction niveaux
   public static int personne = 1;// variable pour la fonction client
    public static bool audi=false,audi2=false;// variable pour la fonction aide 1 et aide 2
    public static bool visuel=false;// variable pour la fonction visuel 

    void Start()
    {
        
        if (niveaux == 1) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Facile"; }
        if (niveaux == 2) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Moyen"; }
        if (niveaux == 3) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Difficile"; }
        if (personne == 1) { Text txt = client1.GetComponent<Text>(); txt.text = "1"; }
        if (personne == 2) { Text txt = client1.GetComponent<Text>(); txt.text = "2"; }
        if (personne == 3) { Text txt = client1.GetComponent<Text>(); txt.text = "3"; }
        if (personne == 4) { Text txt = client1.GetComponent<Text>(); txt.text = "4"; }
        if (personne == 5) { Text txt = client1.GetComponent<Text>(); txt.text = "5"; }
        if (audi == false) { Text txt = aide1.GetComponent<Text>(); txt.text = "Non"; }
        if (audi == true) { Text txt = aide1.GetComponent<Text>(); txt.text = "Oui"; }
        if (audi2 == false) { Text txt = aide2.GetComponent<Text>(); txt.text = "Non"; }
        if (audi2 == true) { Text txt = aide2.GetComponent<Text>(); txt.text = "Oui"; }
        if (visuel == false) { Text txt = visuel1.GetComponent<Text>(); txt.text = "Non"; }
        if (visuel == true) { Text txt = visuel1.GetComponent<Text>(); txt.text = "Oui"; }
    }
    public void niveau()//fonction pour choisir le niveaux 
    {
        
        niveaux = niveaux + 1;
        if (niveaux == 4) { niveaux = 1; }
      
        if (niveaux == 1) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Facile"; }
        if (niveaux == 2) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Moyen"; }
        if (niveaux == 3) { Text txt = niveau1.GetComponent<Text>(); txt.text = "Difficile"; }
    }

    public void nombre_personne()//fonciton pour choisir le nombre de personne
    {
        personne = personne+ 1;
        if (personne == 6) { personne = 1; }
        if (personne == 1) { Text txt = client1.GetComponent<Text>(); txt.text = "1"; }
        if (personne== 2) { Text txt = client1.GetComponent<Text>(); txt.text = "2"; }
        if (personne== 3) { Text txt = client1.GetComponent<Text>(); txt.text = "3"; }
        if (personne== 4) { Text txt = client1.GetComponent<Text>(); txt.text = "4"; }
        if (personne== 5) { Text txt = client1.GetComponent<Text>(); txt.text = "5"; }

    }
    public void audioO() //fonction pour choisir laide
    {
        if (audi == false) { audi= true; }
        else if (audi == true) { audi = false; }
        if (audi==false) { Text txt = aide1.GetComponent<Text>(); txt.text = "Non"; }
        if (audi==true) { Text txt = aide1.GetComponent<Text>(); txt.text = "Oui"; }

    }
    public void audio2() //fonction pour choisir laide
    {
        if (audi2 == false) { audi2 = true; }
        else if (audi2 == true) { audi2 = false; }

        if (audi2 == false) { Text txt = aide2.GetComponent<Text>(); txt.text = "Non"; }
        if (audi2 == true) { Text txt = aide2.GetComponent<Text>(); txt.text = "Oui"; }
        Debug.Log("Il manque : " + gestionjeu.somme);
        
    }
    public void visuell()//fonction pour choisir laide
    {
            if (visuel ==false) { visuel = true; }
        else if (visuel == true) { visuel = false; }

        if (visuel== false) { Text txt = visuel1.GetComponent<Text>(); txt.text = "Non"; }
        if (visuel== true) { Text txt = visuel1.GetComponent<Text>(); txt.text = "Oui"; }
    }
}
