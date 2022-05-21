using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class gestionjeu : MonoBehaviour
{
    // le code principal ( qui lie les niveaux ect...)
    System.Random aleatoire = new System.Random();//pour aléatoire
   
    public static double somme,somme_pieceC,avant_somme,somme_depart;
    public static int test;
   public static int n=1, perso, perso_pre;
    public static float t_global; // temps pour inactivité
    static public int label20 = 0, label10 = 0, label5 = 0, label2 = 0, label1 = 0, label05 = 0, label02 = 0, label01 = 0;
    public GameObject im1, im2, im3, im4, im5;

    void Start () {
        if (parametre.niveaux == 1)
        {

            somme = aleatoire.Next(1, 11);// somme a rendre 
            somme = somme * 5;
            somme_depart = somme;//somme compris entre 5 et 50(multi de 5)
        }
       else if (parametre.niveaux == 2)
        {

            somme = aleatoire.Next(1, 50);// somme a rendre 
            somme_depart = somme;// comme compris entre 1 et 50
        }
       else if (parametre.niveaux == 3)
        {

            somme = aleatoire.Next(1, 50);// somme a rendre 
            somme_pieceC = aleatoire.Next(1, 11);
            somme_pieceC = somme_pieceC / 10;

            somme = somme + somme_pieceC;// somme compris de 1,1 a 51
            somme_depart = somme;// somme compris de 1,1 a 51
        }

        label01 = 0; label02 = 0; label05 = 0; label1 = 0; label2 = 0;
        label5 = 0; label10 = 0; label20 = 0;



        perso = aleatoire.Next(1, 5);
        Debug.Log("pers" + perso);
        if (perso == 1)
        {
            Image IM1 = im1.GetComponent<Image>();
            IM1.enabled = true;
            Image IM2 = im2.GetComponent<Image>();
            IM2.enabled = false;
            Image IM3 = im3.GetComponent<Image>();
            IM3.enabled = false;
            Image IM4 = im4.GetComponent<Image>();
            IM4.enabled = false;
            Image IM5 = im5.GetComponent<Image>();
            IM5.enabled = false;
        }
        if (perso == 2)
        {
            Image IM1 = im1.GetComponent<Image>();
            IM1.enabled = false;
            Image IM2 = im2.GetComponent<Image>();
            IM2.enabled = true;
            Image IM3 = im3.GetComponent<Image>();
            IM3.enabled = false;
            Image IM4 = im4.GetComponent<Image>();
            IM4.enabled = false;
            Image IM5 = im5.GetComponent<Image>();
            IM5.enabled = false;
        }
        if (perso == 3)
        {
            Image IM1 = im1.GetComponent<Image>();
            IM1.enabled = false;
            Image IM2 = im2.GetComponent<Image>();
            IM2.enabled = false;
            Image IM3 = im3.GetComponent<Image>();
            IM3.enabled = true;
            Image IM4 = im4.GetComponent<Image>();
            IM4.enabled = false;
            Image IM5 = im5.GetComponent<Image>();
            IM5.enabled = false;
        }
        if (perso == 4)
        {
            Image IM1 = im1.GetComponent<Image>();
            IM1.enabled = false;
            Image IM2 = im2.GetComponent<Image>();
            IM2.enabled = false;
            Image IM3 = im3.GetComponent<Image>();
            IM3.enabled = false;
            Image IM4 = im4.GetComponent<Image>();
            IM4.enabled = true;
            Image IM5 = im5.GetComponent<Image>();
            IM5.enabled = false;
        }
        if (perso == 5)
        {
            Image IM1 = im1.GetComponent<Image>();
            IM1.enabled = false;
            Image IM2 = im2.GetComponent<Image>();
            IM2.enabled = false;
            Image IM3 = im3.GetComponent<Image>();
            IM3.enabled = false;
            Image IM4 = im4.GetComponent<Image>();
            IM4.enabled = false;
            Image IM5 = im5.GetComponent<Image>();
            IM5.enabled = true;
        }


        perso_pre = perso;



    }

    void Update()
    {
 //------------programme pour le temp aide ------------
        t_global = t_global + Time.deltaTime;

//----------------------------------------------------
        if (somme == 0)//pour le 2eme client ou plus 
        {

            if (calcul.nombre_client< parametre.personne) //inferieur au nombre de client choisi en parametre
            {
                if (parametre.niveaux == 1)
                {

                     somme = aleatoire.Next(1, 11);// somme a rendre 
                    somme = somme * 5;
                    somme_depart = somme;

                }
                if (parametre.niveaux == 2)
                {

                    somme = aleatoire.Next(1, 50);// somme a rendre 
                    somme_depart = somme;

                }
                if (parametre.niveaux == 3)
                {

                    somme = aleatoire.Next(1, 50);// somme a rendre 
                    somme_pieceC = aleatoire.Next(1, 11);
                    somme_pieceC = somme_pieceC / 10;// somme a rendre 
               
                    somme = somme +somme_pieceC;
                    somme_depart = somme;

                }

                calcul.nombre_client = calcul.nombre_client + 1;

                

                while(perso == perso_pre) { perso = aleatoire.Next(1, 6);}
                
               if (perso == 1)
                    {
                    perso_pre = perso;
                    Image IM1 = im1.GetComponent<Image>();
                    IM1.enabled = true;
                    Image IM2 = im2.GetComponent<Image>();
                    IM2.enabled = false;
                    Image IM3 = im3.GetComponent<Image>();
                    IM3.enabled = false;
                    Image IM4 = im4.GetComponent<Image>();
                    IM4.enabled = false;
                    Image IM5 = im5.GetComponent<Image>();
                    IM5.enabled = false;
                }
                if (perso == 2)
                    {
                    perso_pre = perso;
                    Image IM1 = im1.GetComponent<Image>();
                    IM1.enabled = false;
                    Image IM2 = im2.GetComponent<Image>();
                    IM2.enabled = true;
                    Image IM3 = im3.GetComponent<Image>();
                    IM3.enabled = false;
                    Image IM4 = im4.GetComponent<Image>();
                    IM4.enabled = false;
                    Image IM5 = im5.GetComponent<Image>();
                    IM5.enabled = false;
                }
                if (perso == 3)
                    {
                    perso_pre = perso;
                    Image IM1 = im1.GetComponent<Image>();
                    IM1.enabled = false;
                    Image IM2 = im2.GetComponent<Image>();
                    IM2.enabled = false;
                    Image IM3 = im3.GetComponent<Image>();
                    IM3.enabled = true;
                    Image IM4 = im4.GetComponent<Image>();
                    IM4.enabled = false;
                    Image IM5 = im5.GetComponent<Image>();
                    IM5.enabled = false;
                }
                if (perso == 4)
                    {
                    perso_pre = perso;
                    Image IM1 = im1.GetComponent<Image>();
                    IM1.enabled = false;
                    Image IM2 = im2.GetComponent<Image>();
                    IM2.enabled = false;
                    Image IM3 = im3.GetComponent<Image>();
                    IM3.enabled = false;
                    Image IM4 = im4.GetComponent<Image>();
                    IM4.enabled = true;
                    Image IM5 = im5.GetComponent<Image>();
                    IM5.enabled = false;
                }
                if (perso == 5)
                    {

                    perso_pre = perso;
                    Image IM1 = im1.GetComponent<Image>();
                    IM1.enabled = false;
                    Image IM2 = im2.GetComponent<Image>();
                    IM2.enabled = false;
                    Image IM3 = im3.GetComponent<Image>();
                    IM3.enabled = false;
                    Image IM4 = im4.GetComponent<Image>();
                    IM4.enabled = false;
                    Image IM5 = im5.GetComponent<Image>();
                    IM5.enabled = true;
                }

                
                   
            }

            if (calcul.nombre_client == parametre.personne)
            {
                label20 = 0; label10 = 0; label5 = 0; label2 = 0; label1 = 0; label05 = 0; label02 = 0; label01 = 0;


            }
            

        }


    }
}


