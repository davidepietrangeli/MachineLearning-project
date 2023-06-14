# Programma di Machine Learning
Programa che prende dati clinici anonimizzati, svolge feature extraction-selection tramite la PCA ed applica il modello di Support Vector Machines per andare a predire un'etichetta binaria per la classificazione della recidività di un tumore.

Programma svolto per il corso di Intelligenza Artificiale per l'Università Campus Bio-Medico di Roma.

## Task
L’obiettivo del progetto consiste nell’analizzare dati che provengono da 79 pazienti anonimizzati dai
quali sono state acquisite immagini TAC del distretto anatomico dell’addome.

A tutti i 79 pazienti è stata inizialmente diagnosticata una neoplasia maligna alla prostata e si sono
sottoposti ad una prostatectomia radicale.
Successivamente, durante un esame di “controllo” nel quale sono state raccolte le TAC in analisi, in
45 dei pazienti è stata riscontrata una recidiva del tumore.

Si chiede di sviluppare un sistema in IA che, utilizzando il dato acquisito in questa visita di controllo,
predica la presenza di recidiva del tumore.

Il task consiste quindi nel predire l’etichetta binaria Recidiva/Non_Recidiva per ogni paziente.

## DataSet
I dati a disposizione consistono in un dataset tabulare composto da attributi clinici associati ai pazienti
e da feature quantitative estratte direttamente dai volumi 3D del distretto anatomico dell’addome:

• cliniche raccolte dai medici (7):

• Epoca_TC: se la TAC è stata acquisita prima della prostatectomia radicale o dopo, durante la radioterapia;

• Area_grasso_periviscerale: volume del grasso periviscerale;

• Area_grasso_sottocutaneo: volume del grasso sottocutaneo;

• Istologia: risultato istologico del tessuto analizziato;

• GS_alla_diagnosi: Gleason Score alla diagnosi;

• TNM_alla_diagnosi: Estensione del tumore;

• Eta_alla_RP: Età del paziente alla prostatectomia radicale;

• feature estratte dai VOI:

• 12 estratte dall’istogramma del I ordine dell’immagine;

• 182 estratte dalle matrici GLCM 3D (istogrammi del II ordine), come 7 feature dalle matrici calcolate da 26 direzioni differenti;

• 48 estratte dall’istogramma del I ordine delle trasformazioni TOP-LBP, come 12 feature da 4 differenti varianti della trasformazione.

L’ultima colonna del dataset infine rappresenta la classe binaria da predire Recidiva/Non_Recidiva
per ogni paziente.

 # Autore
 Codice scritto da:
 Davide Pietrangeli
 -  
