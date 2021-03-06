.. _resource-order:

L'ordine
========

|head2_descr|
-------------

Un ordine che il :ref:`GAS <resource-gas>`  invia ad un :ref:`fornitore <role-supplier>`: è formato dall'insieme dei prodotti ordinati dai singoli gasisti che hanno preso parte all'ordine, scegliendo tra i prodotti disponibili nel listino del |res_supplier| per quel particolare ordine.
Un ordine è inoltre caratterizzato da:

* il |res_supplier|;
* il :ref:`patto di solidarietà <resource-pact>` tra il |res_gas| e il |res_supplier|;
* la data di apertura e quella di chiusura;
* un appuntamento di consegna, cioè le modalità con cui il |res_supplier| consegna al |res_gas| la merce ordinata;
* un appuntamento di ritiro, cioè le modalità di distribuzione della merce ordinata ai gasisti;
* un eventuale importo minimo, sotto il quale il |res_supplier| non accetta l'ordine. 

La procedura attraverso cui i gasisti ordinano i prodotti è ben definita all'interno del software, e comprende i seguenti passi:

1. un |res_gasmember| con il ruolo di :ref:`referente fornitore <role-gasreferrersupplier>` o :ref:`referente informatico <role-gasreferrertech>` del proprio |res_gas| crea l'ordine su un |res_pds|; a seconda della data di apertura dell'ordine, questo passa allo stato di: 
* preparato, se la data è precedente a quella della creazione;
* aperto, se la data è quella della creazione.
durante questa fase viene anche impostata la data di chiusura se si desidera che l'ordine venga chiuso automaticamente, altrimenti si puo anche scegliere che l'ordine rimanga aperto fino alla chiusura manuale da parte di una delle due figure che possono aprire/preparare l'ordine. 

.. figure:: _static/create_order.png
    :alt: Apertura dell'ordine
    :align: center

    Un |res_gasmember| abilitato apre l'ordine.

2. una volta che l'ordine è aperto, i gasisti possono cominciare a inserire nei propri panieri i prodotti che il |res_supplier| del |res_pds| ha reso disponibili tra quelli nel suo listino.

.. figure:: _static/load_order.png
    :alt: Inserimento dei prodotti nell'ordine
    :align: center

    I gasisti inseriscono nei propri panieri i prodotti che desiderano acquistare.

3. una volta che tutti i gasisti hanno confermato i propri panieri (se il |res_gas| lo richiede) e l'ordine è stato chiuso e consegnato, l'importo reale pagato ai fornitori per i prodotti deve essere registrato nel |res_gas| e decurtato dai conti dei gasisti. 
La registrazione e la decurtazione sono azioni che posson essere intraprese solamente dal referente informatico su qualsiasi ordine chiuso del suo |res_gas|. 
In particolare, durante la decurtazione è possibile includere anche altri gasisti che si sono inseriti successivamente nell'ordine, ad esempio perchè il fornitore ha consegnato dei prodotti in più che sono stati ritirati, appunto, da un altro gasista.

.. figure:: _static/manual_close_order.png
    :align: center
    :alt: Chiusura manuale dell'ordine

    Un |res_gasmember| abilitato chiude l'ordine.

.. figure:: _static/register_order.png
    :alt: Registrazione dell'ordine
    :align: center

    Un |res_gasmember| abilitato registra l'importo reale pagato per l'ordine consegnato

.. figure:: _static/curtail_order.png
    :alt: Decurtazione ai gasisti           
    :align: center

    Un |res_gasmember| abilitato decurta ai gasisti l'importo dovuto per i prodotti ritirati

4. una volta che l'importo dell'ordine è stato decurtato, l'ordine passa nello stato di insoluto e puo essere pagato dal :ref:`referente contabile <role-gasreferrercash>` del |res_gas| utilizzando il conto del |res_pds| su cui l'ordine era stato aperto.  

.. figure:: _static/pay_order.png
    :alt: Pagamento dell'ordine
    :align: center

    Un referente contabile paga l'ordine registrato

5. infine, in seguito al pagamento, l'ordine passa automaticamente nello stato archiviato, per cui non viene piu influenzato da eventuali modifiche applicate ai listini dei prodotti dei fornitori nel |res_des| o nel |res_gas|. È possibile visualizzare gli ordini archiviati sia dalla pagina del |res_pds| che dalla pagina del |res_gas| su cui il |res_pds| stesso è stato attivato.

.. figure:: _static/archived_order.png
    :alt: Ordine archiviato
    :align: center

    Un ordine archiviato.

|head2_terms|
-------------

* Report |res_gasmember|
* Report dell'ordine
* Ritiro
* Consegna

|head2_options|
---------------

Le opzioni di configurazione del |res_gas| che influiscono sull'ordine.

Il software offre un'elevata possibilità di configurazione del |res_gas|; molte delle opzioni che possono essere configurate, inoltre, vanno ad influire sull'ordine che il |res_gas| esegue sul |res_pds|.
Di seguito sono elencate le opzioni riguardanti l'ordine che possono essere configurate nel |res_gas|:

* visualizzazine solo della prossima consegna: rende possibile il filtraggio degli ordini in modo che i gasisti visualizzino solo quelli che condividono il prossimo appuntamento di ritiro;
* selezione di un ordine alla volta: limita la selezione a un solo un ordine aperto alla volta;
* conferma automatica degli ordini dei gasisti: se selezionato, gli ordini dei gasisti vengono automaticamente confermati, altrimenti ogni |res_gasmember| deve confermare manualmente i propri ordini;
* giorno, ora e minuto predefinito di chiusura degli ordini;
* giorno, ora e minuto predefinito della settimana di consegna degli ordini;
* possibilità di cambiare il luogo di consegna ad ogni ordine: se selezionata, rende possibile specificare il luogo della consegna ad ogni ordine. Se non selezioanta, il |res_gas| usa solo il luogo predefinito di consegna nel caso questo sia definito, altrimenti la sede del |res_gas|.
* luogo di consegna predefinito: va specificato se diverso dal luogo di ritiro;
* possibilità di cambiare il luogo di ritiro ad ogni ordine:  se selezionata, è possibile specificare il luogo di ritiro ad ogni ordine. Se non selezionata, il |res_gas| usa solo il luogo predefinito di ritiro nel caso questo sia deinito, altrimenti la sede del |res_gas|.
* luogo di ritiro predefinito: va specificato se è diverso dalla sede;
* giorni di preavviso prima della chiusura dell'ordine: quanti giorni prima si vuole ricevere un promemoria degli ordini di chiusura del |res_gas|.

Nell'immagine seguente è possibile osservare come tutte le opzioni sopra elencate siano effettivamente configurabili:


.. figure:: _static/gas_config.png
    :alt: Schermata di configurazione del |res_gas|
    :align: center

    La schermata di configurazione del |res_gas|, dove è possibile personalizzare le opzioni per l'ordine.


|head2_relations|
-----------------

* |res_pds|
* Ordini dei gasisti
* Referenti


