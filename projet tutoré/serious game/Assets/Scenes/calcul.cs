using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Events;
using UnityEngine.UI;
using System;

public class calcul : MonoBehaviour
{
 public GameObject NbilletC, ereur,er_global,NbilletD, NbilletV, prix_aide, Npiece2, Npiece1, Npiece01, Npiece02, Npiece05,prix_depart;
   public static int test;
    public Button b20, b10, b5, b2, b1, b05, b02, b01;
    private bool BILLETV, BILLETD, BILLETC, piece1, piece2, piece01, piece02, piece05;
      public static int nombre_client = 1;
    double n, pri = gestionjeu.somme, avant_pri;
    int erreur_global = 0, erreur = 0;// variable pour les erreur
    public float t = 0,total;// variable de temps 
    //------
    public bool etat=false;
    public float temp_avant = 0;
    public float intervalle = 1;
    int cligno=0;
    public ColorBlock cn20,cn10,cn5,cn2,cn1,cn05,cn02,cn01;
    static public int l20 = 0, l10 = 0, l5 = 0, l2 = 0, l1 = 0, l05 = 0, l02 = 0, l01 = 0, xx = 0;

    private void Start()
    {
        nombre_client = 1;

        Text prix = prix_aide.GetComponent<Text>();//pour la premier aide 
       prix.enabled = false;
        prix.text = gestionjeu.somme.ToString();

        Text ERREUR = ereur.GetComponent<Text>();// pour les erreur 
        ERREUR.enabled = false;
        Debug.Log("client=" + nombre_client);

        Text toto = prix_depart.GetComponent<Text>();
        toto.text = gestionjeu.somme_depart.ToString();

        //---------------------sauvegarde de toute les couleurs pour faire couleur (vert fluo) normal vert ect..
        if (parametre.niveaux == 1)
        {
        cn20 = b20.colors;
        cn10 = b10.colors;
        cn5 = b5.colors;
        }
        if (parametre.niveaux == 2)
        {
            cn20 = b20.colors;
            cn10 = b10.colors;
            cn5 = b5.colors;
            cn1 = b1.colors;
            cn2 = b2.colors;
        }
        if (parametre.niveaux == 3)
        {
            cn20 = b20.colors;
            cn10 = b10.colors;
            cn5 = b5.colors;
            cn2 = b2.colors;
            cn1 = b1.colors;
            cn05 = b05.colors;
            cn01 = b01.colors;
            cn02 = b02.colors;
        }

        //----------------------
    }

    public void Update()
    {
      
        Text toto = prix_depart.GetComponent<Text>();
        toto.text = gestionjeu.somme_depart.ToString();


       // Debug.Log("Ref lab" + gestionjeu.label20);

      //  Debug.Log("lab pre" + l20);
       
        
        //--------------------------programme aide dans le jeu ----------------------------------------------
        // premier aides 

        if (gestionjeu.t_global > 55)
        {

            if (parametre.audi == true)// afficher le ce qui nous reste pendant tout la partie
            {
                 Text prix = prix_aide.GetComponent<Text>();
                 prix.text = gestionjeu.somme.ToString();
                 prix.enabled = true;
            }

        }
// deuxieme aides 
        if (gestionjeu.t_global > 90)
        {


            if (parametre.audi2 == true)
            {           
                //--------------intervalle
                    if (gestionjeu.t_global - temp_avant >= intervalle)
                      {
                           temp_avant = gestionjeu.t_global;
                             cligno = cligno + 1;

                             if (etat == false)
                                 {
                                 etat = true;
                                  }
                             else if (etat == true)
                                {
                                  etat = false;
                                }

                       
                // tout les cas pour intervalle 
                if (gestionjeu.somme >= 20)//prix plus grand que 20
                {
                    if (etat == true)
                    {
                        ColorBlock c20;
                        c20 = b20.colors;
                        c20.normalColor = Color.green;
                        b20.colors = c20;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c20;
                        c20 = b20.colors;
                        c20.normalColor = cn20.normalColor;
                        b20.colors = c20;

                    }
                }
                else if (gestionjeu.somme >= 10)//prix plus grand que 10
                {
                    if (etat == true)
                    {
                        ColorBlock c10;
                        c10 = b10.colors;
                        c10.normalColor = Color.green;
                        b10.colors = c10;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c10;
                        c10 = b10.colors;
                        c10.normalColor = cn10.normalColor;
                        b10.colors = c10;

                    }
                }
                else if (gestionjeu.somme >= 5)//prix plus grand que 5
                {
                    if (etat == true)
                    {
                        ColorBlock c5;
                        c5 = b5.colors;
                        c5.normalColor = Color.green;
                        b5.colors = c5;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c5;
                        c5 = b5.colors;
                        c5.normalColor = cn5.normalColor;
                        b5.colors = c5;

                    }
                }
                else if (gestionjeu.somme >= 2)//prix plus grand que 2
                {
                    if (etat == true)
                    {
                        ColorBlock c2;
                        c2 = b2.colors;
                        c2.normalColor = Color.green;
                        b2.colors = c2;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c2;
                        c2 = b2.colors;
                        c2.normalColor = cn2.normalColor;
                        b2.colors = c2;

                    }
                }
                else if (gestionjeu.somme >= 1)//prix plus grand que 1
                {
                    if (etat == true)
                    {
                        ColorBlock c1;
                        c1 = b1.colors;
                        c1.normalColor = Color.green;
                        b1.colors = c1;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c1;
                        c1 = b1.colors;
                        c1.normalColor = cn1.normalColor;
                        b1.colors = c1;

                    }
                }
                else if (gestionjeu.somme >= 0.5)//prix plus grand que 50 centime
                {
                    if (etat == true)
                    {
                        ColorBlock c05;
                        c05 = b05.colors;
                        c05.normalColor = Color.green;
                        b05.colors = c05;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c05;
                        c05 = b05.colors;
                        c05.normalColor = cn05.normalColor;
                        b05.colors = c05;

                    }
                }
                else if (gestionjeu.somme >= 0.2)//prix plus grand que 20 centime
                {
                    if (etat == true)
                    {
                        ColorBlock c02;
                        c02 = b20.colors;
                        c02.normalColor = Color.green;
                        b02.colors = c02;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c02;
                        c02 = b02.colors;
                        c02.normalColor = cn02.normalColor;
                        b02.colors = c02;

                    }
                }
                else if (gestionjeu.somme >= 0.1)//prix plus grand que 10 centime
                {
                    if (etat == true)
                    {
                        ColorBlock c01;
                        c01 = b01.colors;
                        c01.normalColor = Color.green;
                        b01.colors = c01;

                    }
                    else if (etat == false)
                    {
                        ColorBlock c01;
                        c01 = b01.colors;
                        c01.normalColor = cn01.normalColor;
                        b01.colors = c01;

                    }
                }
                }
            }
           if (cligno == 10)// clignotemment 10 fois
            {
                cligno = 0;
                gestionjeu.t_global = 0;
                temp_avant = 0;
            }
           
        }

        //----------------fin du programme aides------------------
        //-------------programme terminer la partie ------------------------------

        

        
        if (gestionjeu.somme == 0)
        {
         
            if (nombre_client == parametre.personne)
            {
               

                SceneManager.LoadScene("menu principal");

                chargement_level.dema = 0;


                gestionjeu.label20 = 0;
                gestionjeu.label10 = 0;
                gestionjeu.label5 = 0;
                gestionjeu.label2 = 0;
                gestionjeu.label1 = 0;
                gestionjeu.label05 = 0;
                gestionjeu.label02 = 0;
                gestionjeu.label01 = 0;

     
            }

    


        }
        
 //------------------------------------------------------ ---------------------
 //-------programme de calcul quand on clik sur un bouton ---------------------
        if (BILLETV == true)//calcul du prix pour 20
        {
            l20  = gestionjeu.label20;
            Text txt = NbilletV.GetComponent<Text>();
            gestionjeu.label20 = gestionjeu.label20 + 1;
            test = gestionjeu.label20;
            txt.text = test.ToString();
            
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            BILLETV = false;// pour desactivé
            gestionjeu.t_global = 0;//car on a activé 
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label20 = l20;
                test = gestionjeu.label20;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
            if(gestionjeu.somme == 0)
            {
                gestionjeu.label20 = 0;
                gestionjeu.label10 = 0;
                gestionjeu.label5 = 0;
                gestionjeu.label2 = 0;
                gestionjeu.label1 = 0;
                gestionjeu.label05 = 0;
                gestionjeu.label02 = 0;
                gestionjeu.label01 = 0;


                Text txt55 = NbilletV.GetComponent<Text>();
                txt55.text = gestionjeu.label20.ToString();

                Text txt2 = NbilletD.GetComponent<Text>();
                txt2.text = gestionjeu.label10.ToString();

                Text txt3 = NbilletC.GetComponent<Text>();
                txt3.text = gestionjeu.label5.ToString();

                Text txt4 = Npiece2.GetComponent<Text>();
                txt4.text = gestionjeu.label2.ToString();

                Text txt5 = Npiece1.GetComponent<Text>();
                txt5.text = gestionjeu.label1.ToString();

                Text txt6 = Npiece05.GetComponent<Text>();
                txt6.text = gestionjeu.label05.ToString();

                Text txt7 = Npiece02.GetComponent<Text>();
                txt7.text = gestionjeu.label02.ToString();

                Text txt8 = Npiece01.GetComponent<Text>();
                txt8.text = gestionjeu.label01.ToString();
            }
           

               
        }

        if (BILLETD == true) //calcul du prix pour 10
        {
            
            l10 = gestionjeu.label10;
            
            Text txt = NbilletD.GetComponent<Text>();
            gestionjeu.label10 = gestionjeu.label10 + 1;
            txt.text = gestionjeu.label10.ToString();
            //----------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            BILLETD = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();

            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 
            if (gestionjeu.somme < 0)
            {
                gestionjeu.label10 = l10;
                test = gestionjeu.label10;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
            if (gestionjeu.somme == 0)
            {
                gestionjeu.label20 = 0;
                gestionjeu.label10 = 0;
                gestionjeu.label5 = 0;
                gestionjeu.label2 = 0;
                gestionjeu.label1 = 0;
                gestionjeu.label05 = 0;
                gestionjeu.label02 = 0;
                gestionjeu.label01 = 0;


                Text txt55 = NbilletV.GetComponent<Text>();
                txt55.text = gestionjeu.label20.ToString();

                Text txt2 = NbilletD.GetComponent<Text>();
                txt2.text = gestionjeu.label10.ToString();

                Text txt3 = NbilletC.GetComponent<Text>();
                txt3.text = gestionjeu.label5.ToString();

                Text txt4 = Npiece2.GetComponent<Text>();
                txt4.text = gestionjeu.label2.ToString();

                Text txt5 = Npiece1.GetComponent<Text>();
                txt5.text = gestionjeu.label1.ToString();

                Text txt6 = Npiece05.GetComponent<Text>();
                txt6.text = gestionjeu.label05.ToString();

                Text txt7 = Npiece02.GetComponent<Text>();
                txt7.text = gestionjeu.label02.ToString();

                Text txt8 = Npiece01.GetComponent<Text>();
                txt8.text = gestionjeu.label01.ToString();
            }
        }

        else if (BILLETC == true) //calcul du prix pour 5
        {
           
            l5 = gestionjeu.label5;
           
            Text txt = NbilletC.GetComponent<Text>();
            gestionjeu.label5 = gestionjeu.label5 + 1;
            txt.text = gestionjeu.label5.ToString();
            //-----------------------------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            BILLETC = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label5 = l5;
                test = gestionjeu.label5;
                txt.text = test.ToString();

                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
            if (gestionjeu.somme == 0)
            {
                gestionjeu.label20 = xx ;
                gestionjeu.label10 = xx;
                gestionjeu.label5 = xx;
                gestionjeu.label2 = xx;
                gestionjeu.label1 = xx;
                gestionjeu.label05 = xx;
                gestionjeu.label02 = xx;
                gestionjeu.label01 = xx;


                Text txt55 = NbilletV.GetComponent<Text>();
                txt55.text = gestionjeu.label20.ToString();

                Text txt2 = NbilletD.GetComponent<Text>();
                txt2.text = gestionjeu.label10.ToString();

                Text txt3 = NbilletC.GetComponent<Text>();
                txt3.text = gestionjeu.label5.ToString();

                Text txt4 = Npiece2.GetComponent<Text>();
                txt4.text = gestionjeu.label2.ToString();

                Text txt5 = Npiece1.GetComponent<Text>();
                txt5.text = gestionjeu.label1.ToString();

                Text txt6 = Npiece05.GetComponent<Text>();
                txt6.text = gestionjeu.label05.ToString();

                Text txt7 = Npiece02.GetComponent<Text>();
                txt7.text = gestionjeu.label02.ToString();

                Text txt8 = Npiece01.GetComponent<Text>();
                txt8.text = gestionjeu.label01.ToString();
            }

        }
        else if (piece2 == true) //calcul du prix pour 0.20
        {

            l2 = gestionjeu.label2;
           
            Text txt = Npiece2.GetComponent<Text>();
            gestionjeu.label2 = gestionjeu.label2 + 1;
            txt.text = gestionjeu.label2.ToString();
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            piece2 = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label2 = l2;
                test = gestionjeu.label2;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }

        }
        else if (piece1 == true) //calcul du prix pour 0.10
        {
         
            l1 = gestionjeu.label1;
            
            Text txt = Npiece1.GetComponent<Text>();
            gestionjeu.label1 = gestionjeu.label1 + 1;
            txt.text = gestionjeu.label1.ToString();
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            piece1 = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label1 = l1;
                test = gestionjeu.label1;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
        }
        else if (piece05 == true) //calcul du prix pour 0.50
        {
           
            l05 = gestionjeu.label05;
           
            Text txt = Npiece05.GetComponent<Text>();
            gestionjeu.label05 = gestionjeu.label05 + 1;
            txt.text = gestionjeu.label05.ToString();
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            piece05 = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label05 = l05;
                test = gestionjeu.label05;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
        }
        else if (piece02 == true) //calcul du prix pour 5
        {
            l02 = gestionjeu.label02;
           
            Text txt = Npiece02.GetComponent<Text>();
            gestionjeu.label02 = gestionjeu.label02 + 1;
            txt.text = gestionjeu.label02.ToString();
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            piece02 = false;
            gestionjeu.t_global = 0;
            Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label02 = l02;
                test = gestionjeu.label02;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
        }
        else if (piece01 == true) //calcul du prix pour 5
        {
            l01 = gestionjeu.label01;
            Text txt = Npiece01.GetComponent<Text>();
            gestionjeu.label01 = gestionjeu.label01 + 1;
            txt.text = gestionjeu.label01.ToString();
            //------------------------
            gestionjeu.avant_somme = gestionjeu.somme;
            pri = Calcul(n);
            piece01 = false;
            gestionjeu.t_global = 0;
          Text prix = prix_aide.GetComponent<Text>();
            prix.text = gestionjeu.somme.ToString();
            Text ERREUR = ereur.GetComponent<Text>();// lie au code
            ERREUR.enabled = false; //on l'efface pour que utilisateur ne le voit pas 

            if (gestionjeu.somme < 0)
            {
                gestionjeu.label01 = l01;
                test = gestionjeu.label01;
                txt.text = test.ToString();
                Text ERREUR2 = ereur.GetComponent<Text>();// lie unity au code 
                ERREUR2.enabled = true;// visible 
                gestionjeu.somme = gestionjeu.avant_somme;// somme avant 0
                erreur = erreur + 1;// on ajoute 
            }
        }
      
    }
 //---------------------------------------------------------------
 //---------------------------------------------------------
        public void Demare01()   // cliquer sur bouton 0.10
        {
            piece01 = true;
            n = 0.1; //utilixer dans la fonction calcul  
        }
        public void Demare02()   // cliquer sur bouton 0.20
        {

            piece02 = true;
            n = 0.2; //utilixer dans la fonction calcul  
        }
        public void Demare05()   // cliquer sur bouton 0.50
        {
            piece05 = true;
            n = 0.5; //utilixer dans la fonction calcul  
        }
        public void demare1()   // cliquer sur bouton 1
        {
            piece1 = true;
            n = 1; //utilixer dans la fonction calcul  
        }

        public void demare2()   // cliquer sur bouton 2
        {
            piece2 = true;
            n = 2; //utilixer dans la fonction calcul  
        }

        public void demare5()   //cliquer sur bouton 5 
        {
            BILLETC = true;
            n = 5; //utilixer dans la fonction calcul  

        }

        public void demare10()   // cliquer sur bouton 10
        {
            BILLETD = true;
            n = 10; //utilixer dans la fonction calcul  
        }

        public void demare20()  //cliquer sur le bouton 20
        {
            BILLETV = true;
            n = 20;      //utilixer dans la fonction calcul  
        }
    

    public static double Calcul(double n) //focntion calcul
    {
        gestionjeu.somme = gestionjeu.somme - n;
        gestionjeu.somme = Math.Round(gestionjeu.somme * 100f) / 100f;
        return gestionjeu.somme;
    }
}

     