    <!-- premere page du QCM 
    on clik sur fomration puis le theme et enfin connexion 
    ou crée un compte si on n'en pas un  -->

 <!-- bgcolor="00FF00 " -->

    <!DOCTYPE html>
    <html>
            <body>
                    <!-- bouton formation  -->
                        <form method="post" action="index.php">
                            <input type ="submit" name="toto"value="Formation" />
                        </form>
                <?php

        if(isset($_POST['toto']))
            {
                    if($_POST['toto']=='Formation')
                        {
                ?>
                                <!--  bouton conexionutilisateur-->
                                    <form method="post" action="connexion.php">
                                        <input type ="submit" value="Connexion UTILISATEUR" />
                                    </form>
                                        <!--  bouton conexion formateur-->
                                        <form method="post" action="connexionfor.php">
                                        <input type ="submit" value="Connexion FORMATEUR" />
                                        </form>
                                    <!-- bouton création du compte -->
                                    <form method="post" action="creation_dun_compte.php">
                                        <input type ="submit" value="Créer son compte utilisateur " />
                                    </form>
                            <?php
                        }  
            }    
        else
            {
            echo  "";
            }
                        ?>
    </body>
    </html>