    <!--  2eme page de création du compte 
    elle sert a dire si oui ou non le copmpte a bien était crée -->
 
 <!DOCTYPE html>
 <html>
<body>
 <?php
    $var_t= 0;// variable servant de reference 

     $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $req=$bdd->query("SELECT* FROM utilisateur  GROUP BY e_mail");
                
      while($ligne=$req->fetch()) //test si un compte n'est pas crée 
          { 
           if($_POST['i_mail']==$ligne['e_mail'])// si yen a un alors varibale a 1
               {
                 $var_t= 1;
                }
          }
//-----------------------------------------------------
       if($var_t==1) // si variabla a 1 compte deja crée avec email donc ajout inpossible 
                    {
                        echo "Ajout est inpossbile car cette adresse e-mail existe déja";   
                    ?>  
                        <form method="post" action="création_dun_compte.php">
	                    <input type ="submit" value="retour" />
                        </form> 
                <?php
                    }
             else // sinon on ajout le compte 
                 {
                     // reference de premiere page 
                    $req=$bdd->exec("INSERT INTO utilisateur(nom,prenom,tel_portable,tel_service,e_mail,mot_de_passe,formation,accord,nom_de_jeune_fille) 
                    VALUES ('".$_POST['i_nom']."','".$_POST['i_prenom']."','".$_POST['i_telp']."','".$_POST['i_tels']."',
                    '".$_POST['i_mail']."','".$_POST['i_mp']."','".$_POST['formation']."','".$_POST['accord']."','".$_POST['i_nomj']."');");
                    echo "Création du compte réussi bonne naviguation ";
                // retour au menu principal ?>  
                    <form method="post" action="index.php">
                         <input type ="submit" value="retour au menu principal " />
                    </form> 
                    <?php
                 }     
                    ?>  
</body>
</html>