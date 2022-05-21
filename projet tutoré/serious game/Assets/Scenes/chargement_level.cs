using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;
using UnityEngine.UI;
using System;

public class chargement_level: MonoBehaviour
{

public static int dema=0;

        public  void  Level()  // chargement de niveaux 
    {       if(parametre.niveaux==1) {SceneManager.LoadScene("facile");dema = 1; }
        if (parametre.niveaux== 2) { SceneManager.LoadScene("moyen");dema = 1; }
        if (parametre.niveaux == 3) { SceneManager.LoadScene("difficile");dema = 1; }
    }
    public void menu_parametre()   // cliquer boutoon parametre ouvre parametre
    {
        SceneManager.LoadScene("parametre");

    }
    public void creation_compte() // cliquer boutoon crétion ouvre création
    {
        SceneManager.LoadScene("creation");
    }
    public void retour()    // cliquer boutoon retour ouvre menu principal
    {
        SceneManager.LoadScene("menu principal");
    }

    public void creation()
    {
        SceneManager.LoadScene("menu principal");
    }

}
