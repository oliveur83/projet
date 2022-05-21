    <!-- page pour reiniatlisé sont mot de pass  -->
    <!DOCTYPE html>
    <html>
            <body><FONT size="5">

                 <?php  
                 $var_x=0; // variable pour affiche une fois a la ligne 50 dans le else
                    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');$bdd->exec("SET NAMES 'utf8'");
                ?>
                     <!-- mettre sont email et sont mot de passe  -->
                        <form method="post" action="reini_motdepasse.php"> 
                                 Entrez votre adresse e-mail:   
                                 <?php    echo  "</br>"; ?>
                             <input type="text" name="tata"style="width:200px;height:30px;font-size:20px" />
                             <?php    echo  "</br>"; ?>
                             Entrez votre nouveau mot de passe:   
                             <?php    echo  "</br>"; ?>
                            <input  type="password" name="titi"style="width:200px;height:30px;font-size:20px" />
                            <?php    echo  "</br>"; ?>
                            <input type ="submit" name="toto"value="Valider"style=";height:30px;font-size:20px" />
                        </form>            
                      <form method="post" action="connexion.php">
                        <input type ="submit"value="Retour"style=";height:30px;font-size:20px" />
                  </form>     
                <?php

        if(isset($_POST['toto']))// si toto existe 
            {

                    if($_POST['toto']=='Valider')// si on clik sur le bouton Valider
                        {       $req=$bdd->query("SELECT* FROM utilisateur ");    
                                 while ($ligne= $req->fetch())// verification du motdepasse et de e_mail 
                                         { 

                                                if( $_POST['tata']==$ligne['e_mail'])
                                                 {        
                                                     // permet modifier la case que lon veut 
                                                     //ici ces la case mot_de_passe  de e_mail rentré avatn 
                                                        $req = $bdd->prepare('UPDATE utilisateur SET mot_de_passe=:mot WHERE e_mail=:email');
                                                        $req->execute(array(
                                                                'mot' =>$_POST['titi'],
                                                                'email'=>$_POST['tata']
                                                        ));
                                                          echo  "modification réussi";
                                                 }
                                                  else
                                                  {  $var_x=$var_x+1;
                                                   if ($var_x==1)
                                                   {echo  "modification non réussi";}
                                                  }
                                        }   

                        }  
                       
           }  
            
        else
            {
            echo  "";
            }  

                        ?>       

    </body>
    </html>