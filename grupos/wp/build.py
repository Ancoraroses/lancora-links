#!/usr/bin/env python3
"""Genera las piezas de la página «Grups i celebracions» para WordPress (WPML: ca, es, fr, en, de).

Salida (carpeta out/):
  <lang>-top.html      bloque HTML 1: estilos + portada + ocasiones + cómo funciona
  <lang>-lead.html     bloque HTML 2: texto de la banda azul (a la izquierda del formulario)
  <lang>-bottom.html   bloque HTML 3: ventajas + cierre + botón WhatsApp + datos estructurados
  forms.json           5 formularios Contact Form 7 (uno por idioma)
  pages.json           título, slug y textos auxiliares por idioma

Textos editables: diccionario T. Diseño: variables CSS en STYLE.
"""
import json, os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

PHONE_TXT = "972 25 63 86"
WA = "https://wa.me/34972256386"
SEAL = "https://ancoraroses.com/wp-content/uploads/2026/11/logo-40-aniversario-360.png"
HERO = "https://ancoraroses.com/wp-content/uploads/2023/03/IMG_20221008_145142-1-scaled.jpg"
PRIVACY = "https://ancoraroses.com/privacitat/"
CONDITIONS = "https://ancoraroses.com/condiciones-de-reserva/"
AEPD = "https://www.aepd.es/"

LANGS = ["ca", "es", "fr", "en", "de"]

T = {
"ca": dict(
  locale="ca", slug="grups-i-celebracions", title="Grups i celebracions",
  meta="Menús per a grups, sopars d'empresa, aniversaris i celebracions a L'Àncora, a peu de platja a Roses (Costa Brava). Demana el dossier i un pressupost a mida.",
  eyebrow="Celebracions i grups a Roses",
  h1a="On el sabor mediterrani es troba amb", h1b="celebracions inoblidables.",
  sub="Menús per a grups, sopars d'empresa i esdeveniments privats. Arrossos, peix i tapes a peu de platja, amb un equip que cuida cada detall.",
  cta1="Demana el dossier per a grups", cta2="Escriu-nos per WhatsApp",
  tr1="Des del 1986", tr2="A peu de platja", tr3="+1.000 opinions a Google",
  occ_eyebrow="Per a cada ocasió", occ_title="Preparem l'escenari perfecte per a cada ocasió.",
  c=[("Sopars d'empresa","Desconnecteu de l'oficina a tocar del mar. Menús tancats perquè només us hàgiu de preocupar de gaudir, fer equip i brindar."),
     ("Aniversaris i celebracions","Bufeu les espelmes amb el mar de fons. Detalls personalitzats i un tracte que us fa sentir com a casa."),
     ("Amics i família","Perquè no sempre cal una excusa per trobar-se. Arrossos, peix, tapes i sobretaules que s'allarguen.")],
  how_eyebrow="Com funciona", how_title="De la primera consulta a la reserva.",
  s=[("Explica'ns la data i quants sou","Omple el formulari o escriu-nos per WhatsApp. Si ho saps, indica el tipus d'esdeveniment i les restriccions alimentàries."),
     ("T'enviem menús i un pressupost a mida","El nostre equip revisa la teva sol·licitud i et respon amb les propostes de menú i un pressupost segons el grup."),
     ("Confirmem la reserva","Per a grups de més de 8 persones podem demanar confirmació addicional, prepagament parcial o elecció de menú tancat. Un menú tancat s'ha de confirmar almenys 24 hores abans.")],
  cond_link="Consulta les condicions generals de reserva",
  lead_a="Demana el nostre dossier de grups i", lead_b="un brindis de benvinguda de regal.",
  lead_sub="Deixa'ns les teves dades i et farem arribar els menús per a grups amb un pressupost a mida. A més, si reserves l'esdeveniment després de demanar el dossier, convidem tot el grup a la primera ronda de cava o sangria.",
  gift="Promoció subjecta a la confirmació de la reserva i a disponibilitat.",
  why_eyebrow="Per què L'Àncora", why_title="Per què triar L'Àncora.",
  b=[("Cuina mediterrània autèntica","Arrossos, peix fresc i tapes, el que fem des de fa quatre dècades."),
     ("Des del 1986","Quaranta anys de taules compartides a Roses."),
     ("A peu de platja","Celebreu amb el mar al davant."),
     ("Menús de grup tancats","Tries el menú abans del dia i només cal gaudir."),
     ("Sala privada per a grups grans","Espai a la planta de dalt per a celebracions més nombroses, d'ús exclusiu per servei i segons disponibilitat."),
     ("Resposta personal","Et responem nosaltres, per correu electrònic o WhatsApp.")],
  close_title="Preparem la teva celebració?", close_sub="Digue'ns la data i quants sou, i t'ajudem a muntar la vetllada.",
  close_wa="Reserva per WhatsApp", close_call="Truca al",
  wa_tip="Reserva per WhatsApp", wa_msg="Hola L'Àncora! M'agradaria informació sobre menús per a grups.",
  # formulario
  f_name="Nom i cognoms", f_email="Correu electrònic", f_phone="Telèfon / WhatsApp", f_type="Tipus d'esdeveniment",
  f_types=["Empresa","Aniversari","Amics","Altres"], f_date="Data aproximada (opcional)", f_guests="Comensals (opcional)",
  f_msg="Comentaris o al·lèrgies (opcional)",
  f_priv="He llegit i accepto la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">política de privacitat</a>." % PRIVACY,
  f_mkt="Vull rebre ofertes i novetats de L'Àncora per correu electrònic o WhatsApp. Puc retirar el consentiment quan vulgui.",
  f_submit="Demanar dossier i pressupost",
  info=("<strong>Informació bàsica de protecció de dades.</strong> <b>Responsable:</b> Ancora Oci i Hosteleria, S.L. (NIF B55162051). "
        "<b>Finalitat:</b> atendre la teva sol·licitud d'informació i pressupost per a grups i, si ho marques, enviar-te ofertes. "
        "<b>Legitimació:</b> la teva sol·licitud i el teu consentiment. <b>Destinataris:</b> no cedim dades; el nostre proveïdor d'allotjament web i de correu actua com a encarregat del tractament. "
        "<b>Conservació:</b> el temps necessari per gestionar la sol·licitud i, si escau, la reserva; les ofertes, fins que retiris el consentiment. "
        "<b>Drets:</b> accés, rectificació, supressió, oposició, limitació i portabilitat a info@ancoraroses.com; i reclamació davant l'<a href=\"%s\" target=\"_blank\" rel=\"noopener\">AEPD</a>. "
        "Més informació a la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">política de privacitat</a>.") % (AEPD, PRIVACY),
  m_ok="Gràcies! Hem rebut la teva sol·licitud. Et respondrem amb els menús i un pressupost a mida.",
  m_ng="No s'ha pogut enviar la sol·licitud. Torna-ho a provar o escriu-nos per WhatsApp al %s." % PHONE_TXT,
  m_val="Hi ha camps per revisar. Comprova'ls i torna-ho a provar.", m_req="Aquest camp és obligatori.",
  m_terms="Cal acceptar la política de privacitat per poder enviar la sol·licitud.",
  m_email="Introdueix una adreça de correu vàlida.", m_tel="Introdueix un telèfon vàlid.",
  mail_subject="[Grups CA] {name} · {type} · {guests} p.",
  mail_head="Nova sol·licitud de dossier de grups (web, idioma: CA)",
  lab=dict(name="Nom",email="Correu",phone="Telèfon",type="Esdeveniment",date="Data",guests="Comensals",msg="Comentaris",priv="Consentiment privacitat",mkt="Ofertes (consentiment de màrqueting)",page="Pàgina",sent="Enviat"),
  ar_subject="Hem rebut la teva sol·licitud · L'Àncora",
  ar_body=("Hola {name},\n\nGràcies pel teu interès a celebrar amb nosaltres. Hem rebut la teva sol·licitud de menús per a grups.\n"
           "El nostre equip la revisarà i et respondrà amb les propostes de menú i un pressupost a mida.\n\n"
           "Si ho prefereixes, també ens pots escriure per WhatsApp al %s.\n\n"
           "L'equip de L'Àncora\nAvinguda de Rhode 62 · 17480 Roses\n\n--\n"
           "Responsable del tractament: Ancora Oci i Hosteleria, S.L. Pots exercir els teus drets escrivint a info@ancoraroses.com. Més informació: %s") % (PHONE_TXT, PRIVACY),
),
"es": dict(
  locale="es_ES", slug="grupos-y-celebraciones", title="Grupos y celebraciones",
  meta="Menús para grupos, cenas de empresa, cumpleaños y celebraciones en L'Àncora, a pie de playa en Roses (Costa Brava). Pide el dosier y un presupuesto a medida.",
  eyebrow="Celebraciones y grupos en Roses",
  h1a="Donde el sabor mediterráneo se une a", h1b="celebraciones inolvidables.",
  sub="Menús para grupos, cenas de empresa y eventos privados. Arroces, pescado y tapas a pie de playa, con un equipo que cuida cada detalle.",
  cta1="Pide el dosier para grupos", cta2="Escríbenos por WhatsApp",
  tr1="Desde 1986", tr2="A pie de playa", tr3="+1.000 opiniones en Google",
  occ_eyebrow="Para cada ocasión", occ_title="Preparamos el escenario perfecto para cada ocasión.",
  c=[("Cenas de empresa","Desconectad de la oficina junto al mar. Menús cerrados para que solo os preocupéis de disfrutar, hacer equipo y brindar."),
     ("Cumpleaños y aniversarios","Soplad las velas con el mar de fondo. Detalles personalizados y un trato que os hace sentir como en casa."),
     ("Amigos y familia","Porque no siempre hace falta una excusa para juntarse. Arroces, pescado, tapas y sobremesas que se alargan.")],
  how_eyebrow="Cómo funciona", how_title="De la primera consulta a la reserva.",
  s=[("Cuéntanos la fecha y cuántos sois","Rellena el formulario o escríbenos por WhatsApp. Si lo sabes, indica el tipo de evento y las restricciones alimentarias."),
     ("Te enviamos menús y un presupuesto a medida","Nuestro equipo revisa tu solicitud y te responde con las propuestas de menú y un presupuesto según el grupo."),
     ("Confirmamos la reserva","Para grupos de más de 8 personas podemos pedir confirmación adicional, prepago parcial o elección de menú cerrado. Un menú cerrado debe confirmarse al menos 24 horas antes.")],
  cond_link="Consulta las condiciones generales de reserva",
  lead_a="Pide nuestro dosier de grupos y", lead_b="un brindis de bienvenida de regalo.",
  lead_sub="Déjanos tus datos y te haremos llegar los menús para grupos con un presupuesto a medida. Además, si reservas el evento después de pedir el dosier, invitamos a todo el grupo a la primera ronda de cava o sangría.",
  gift="Promoción sujeta a la confirmación de la reserva y a disponibilidad.",
  why_eyebrow="Por qué L'Àncora", why_title="Por qué elegir L'Àncora.",
  b=[("Cocina mediterránea auténtica","Arroces, pescado fresco y tapas, lo que hacemos desde hace cuatro décadas."),
     ("Desde 1986","Cuarenta años de mesas compartidas en Roses."),
     ("A pie de playa","Celebrad con el mar delante."),
     ("Menús de grupo cerrados","Eliges el menú antes del día y solo queda disfrutar."),
     ("Sala privada para grupos grandes","Espacio en la planta de arriba para celebraciones más numerosas, de uso exclusivo por servicio y según disponibilidad."),
     ("Respuesta personal","Te respondemos nosotros, por correo electrónico o WhatsApp.")],
  close_title="¿Preparamos tu celebración?", close_sub="Dinos la fecha y cuántos sois, y te ayudamos a montar la velada.",
  close_wa="Reserva por WhatsApp", close_call="Llama al",
  wa_tip="Reserva por WhatsApp", wa_msg="¡Hola L'Àncora! Me gustaría información sobre menús para grupos.",
  f_name="Nombre y apellidos", f_email="Correo electrónico", f_phone="Teléfono / WhatsApp", f_type="Tipo de evento",
  f_types=["Empresa","Cumpleaños","Amigos","Otro"], f_date="Fecha aproximada (opcional)", f_guests="Comensales (opcional)",
  f_msg="Comentarios o alergias (opcional)",
  f_priv="He leído y acepto la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">política de privacidad</a> (disponible en catalán)." % PRIVACY,
  f_mkt="Quiero recibir ofertas y novedades de L'Àncora por correo electrónico o WhatsApp. Puedo retirar el consentimiento cuando quiera.",
  f_submit="Pedir dosier y presupuesto",
  info=("<strong>Información básica de protección de datos.</strong> <b>Responsable:</b> Ancora Oci i Hosteleria, S.L. (NIF B55162051). "
        "<b>Finalidad:</b> atender tu solicitud de información y presupuesto para grupos y, si lo marcas, enviarte ofertas. "
        "<b>Legitimación:</b> tu solicitud y tu consentimiento. <b>Destinatarios:</b> no cedemos datos; nuestro proveedor de alojamiento web y de correo actúa como encargado del tratamiento. "
        "<b>Conservación:</b> el tiempo necesario para gestionar la solicitud y, en su caso, la reserva; las ofertas, hasta que retires el consentimiento. "
        "<b>Derechos:</b> acceso, rectificación, supresión, oposición, limitación y portabilidad en info@ancoraroses.com; y reclamación ante la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">AEPD</a>. "
        "Más información en la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">política de privacidad</a>.") % (AEPD, PRIVACY),
  m_ok="¡Gracias! Hemos recibido tu solicitud. Te responderemos con los menús y un presupuesto a medida.",
  m_ng="No se ha podido enviar la solicitud. Vuelve a intentarlo o escríbenos por WhatsApp al %s." % PHONE_TXT,
  m_val="Hay campos por revisar. Compruébalos y vuelve a intentarlo.", m_req="Este campo es obligatorio.",
  m_terms="Debes aceptar la política de privacidad para enviar la solicitud.",
  m_email="Introduce una dirección de correo válida.", m_tel="Introduce un teléfono válido.",
  mail_subject="[Grupos ES] {name} · {type} · {guests} p.",
  mail_head="Nueva solicitud de dosier de grupos (web, idioma: ES)",
  lab=dict(name="Nombre",email="Correo",phone="Teléfono",type="Evento",date="Fecha",guests="Comensales",msg="Comentarios",priv="Consentimiento privacidad",mkt="Ofertas (consentimiento de marketing)",page="Página",sent="Enviado"),
  ar_subject="Hemos recibido tu solicitud · L'Àncora",
  ar_body=("Hola {name},\n\nGracias por tu interés en celebrar con nosotros. Hemos recibido tu solicitud de menús para grupos.\n"
           "Nuestro equipo la revisará y te responderá con las propuestas de menú y un presupuesto a medida.\n\n"
           "Si lo prefieres, también puedes escribirnos por WhatsApp al %s.\n\n"
           "El equipo de L'Àncora\nAvinguda de Rhode 62 · 17480 Roses\n\n--\n"
           "Responsable del tratamiento: Ancora Oci i Hosteleria, S.L. Puedes ejercer tus derechos escribiendo a info@ancoraroses.com. Más información: %s") % (PHONE_TXT, PRIVACY),
),
"fr": dict(
  locale="fr_FR", slug="groupes-et-evenements", title="Groupes et événements",
  meta="Menus de groupe, dîners d'entreprise, anniversaires et fêtes à L'Àncora, face à la plage de Roses (Costa Brava). Demandez le dossier et un devis sur mesure.",
  eyebrow="Fêtes et groupes à Roses",
  h1a="Là où la saveur méditerranéenne rencontre", h1b="des célébrations inoubliables.",
  sub="Menus de groupe, dîners d'entreprise et événements privés. Riz, poisson et tapas au bord de la plage, avec une équipe qui soigne chaque détail.",
  cta1="Demander le dossier groupes", cta2="Écrivez-nous sur WhatsApp",
  tr1="Depuis 1986", tr2="Au bord de la plage", tr3="+1 000 avis sur Google",
  occ_eyebrow="Pour chaque occasion", occ_title="Nous préparons le cadre idéal pour chaque occasion.",
  c=[("Dîners d'entreprise","Déconnectez du bureau face à la mer. Des menus fixes pour que vous n'ayez qu'à profiter, souder l'équipe et trinquer."),
     ("Anniversaires et fêtes","Soufflez les bougies avec la mer en toile de fond. Des attentions personnalisées et un accueil qui vous fait sentir chez vous."),
     ("Entre amis et en famille","Parce qu'il n'y a pas toujours besoin d'une excuse pour se retrouver. Riz, poisson, tapas et repas qui s'éternisent.")],
  how_eyebrow="Comment ça marche", how_title="De la première demande à la réservation.",
  s=[("Indiquez-nous la date et le nombre de convives","Remplissez le formulaire ou écrivez-nous sur WhatsApp. Si vous le savez, précisez le type d'événement et les restrictions alimentaires."),
     ("Nous vous envoyons des menus et un devis sur mesure","Notre équipe étudie votre demande et vous répond avec des propositions de menus et un devis adapté au groupe."),
     ("Nous confirmons la réservation","Pour les groupes de plus de 8 personnes, nous pouvons demander une confirmation supplémentaire, un acompte partiel ou le choix d'un menu fixe. Un menu fixe doit être confirmé au moins 24 heures à l'avance.")],
  cond_link="Consulter les conditions générales de réservation",
  lead_a="Demandez notre dossier groupes et", lead_b="un toast de bienvenue offert.",
  lead_sub="Laissez-nous vos coordonnées et nous vous enverrons les menus de groupe avec un devis sur mesure. De plus, si vous réservez l'événement après avoir demandé le dossier, nous offrons à tout le groupe la première tournée de cava ou de sangria.",
  gift="Offre soumise à la confirmation de la réservation et à la disponibilité.",
  why_eyebrow="Pourquoi L'Àncora", why_title="Pourquoi choisir L'Àncora.",
  b=[("Cuisine méditerranéenne authentique","Riz, poisson frais et tapas, ce que nous faisons depuis quarante ans."),
     ("Depuis 1986","Quarante ans de tablées partagées à Roses."),
     ("Au bord de la plage","Fêtez avec la mer devant vous."),
     ("Menus de groupe fixes","Vous choisissez le menu avant le jour J et il ne reste qu'à en profiter."),
     ("Salle privée pour les grands groupes","Un espace à l'étage pour les célébrations plus nombreuses, à usage exclusif par service et selon disponibilité."),
     ("Réponse personnelle","C'est nous qui vous répondons, par e-mail ou WhatsApp.")],
  close_title="On prépare votre fête ?", close_sub="Indiquez-nous la date et le nombre de convives, nous vous aidons à composer la soirée.",
  close_wa="Réserver sur WhatsApp", close_call="Appelez le",
  wa_tip="Réserver sur WhatsApp", wa_msg="Bonjour L'Àncora ! J'aimerais des informations sur les menus de groupe.",
  f_name="Nom et prénom", f_email="E-mail", f_phone="Téléphone / WhatsApp", f_type="Type d'événement",
  f_types=["Entreprise","Anniversaire","Amis","Autre"], f_date="Date approximative (facultatif)", f_guests="Convives (facultatif)",
  f_msg="Commentaires ou allergies (facultatif)",
  f_priv="J'ai lu et j'accepte la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">politique de confidentialité</a> (disponible en catalan)." % PRIVACY,
  f_mkt="Je souhaite recevoir les offres et nouveautés de L'Àncora par e-mail ou WhatsApp. Je peux retirer mon consentement à tout moment.",
  f_submit="Demander le dossier et un devis",
  info=("<strong>Informations de base sur la protection des données.</strong> <b>Responsable :</b> Ancora Oci i Hosteleria, S.L. (NIF B55162051). "
        "<b>Finalité :</b> traiter votre demande d'informations et de devis pour groupes et, si vous cochez la case, vous envoyer des offres. "
        "<b>Base juridique :</b> votre demande et votre consentement. <b>Destinataires :</b> aucune cession de données ; notre hébergeur web et notre prestataire de messagerie agissent comme sous-traitants. "
        "<b>Conservation :</b> le temps nécessaire pour traiter la demande et, le cas échéant, la réservation ; pour les offres, jusqu'au retrait de votre consentement. "
        "<b>Droits :</b> accès, rectification, effacement, opposition, limitation et portabilité à info@ancoraroses.com ; réclamation auprès de l'<a href=\"%s\" target=\"_blank\" rel=\"noopener\">AEPD</a>. "
        "Plus d'informations dans la <a href=\"%s\" target=\"_blank\" rel=\"noopener\">politique de confidentialité</a>.") % (AEPD, PRIVACY),
  m_ok="Merci ! Nous avons bien reçu votre demande. Nous vous répondrons avec les menus et un devis sur mesure.",
  m_ng="La demande n'a pas pu être envoyée. Réessayez ou écrivez-nous sur WhatsApp au %s." % PHONE_TXT,
  m_val="Certains champs sont à vérifier. Contrôlez-les et réessayez.", m_req="Ce champ est obligatoire.",
  m_terms="Vous devez accepter la politique de confidentialité pour envoyer la demande.",
  m_email="Saisissez une adresse e-mail valide.", m_tel="Saisissez un numéro de téléphone valide.",
  mail_subject="[Groupes FR] {name} · {type} · {guests} p.",
  mail_head="Nouvelle demande de dossier groupes (web, langue : FR)",
  lab=dict(name="Nom",email="E-mail",phone="Téléphone",type="Événement",date="Date",guests="Convives",msg="Commentaires",priv="Consentement confidentialité",mkt="Offres (consentement marketing)",page="Page",sent="Envoyé"),
  ar_subject="Nous avons bien reçu votre demande · L'Àncora",
  ar_body=("Bonjour {name},\n\nMerci de votre intérêt pour fêter votre événement chez nous. Nous avons bien reçu votre demande de menus de groupe.\n"
           "Notre équipe l'étudiera et vous répondra avec des propositions de menus et un devis sur mesure.\n\n"
           "Si vous préférez, vous pouvez aussi nous écrire sur WhatsApp au %s.\n\n"
           "L'équipe de L'Àncora\nAvinguda de Rhode 62 · 17480 Roses\n\n--\n"
           "Responsable du traitement : Ancora Oci i Hosteleria, S.L. Vous pouvez exercer vos droits en écrivant à info@ancoraroses.com. Plus d'informations : %s") % (PHONE_TXT, PRIVACY),
),
"en": dict(
  locale="en_US", slug="groups-and-celebrations", title="Groups and celebrations",
  meta="Group menus, company dinners, birthdays and celebrations at L'Àncora, on the beach in Roses (Costa Brava). Request the dossier and a tailored quote.",
  eyebrow="Celebrations and groups in Roses",
  h1a="Where Mediterranean flavour meets", h1b="unforgettable celebrations.",
  sub="Group menus, company dinners and private events. Rice dishes, fish and tapas right on the beach, with a team that looks after every detail.",
  cta1="Request the group dossier", cta2="Message us on WhatsApp",
  tr1="Since 1986", tr2="Right on the beach", tr3="1,000+ Google reviews",
  occ_eyebrow="For every occasion", occ_title="We set the perfect scene for every occasion.",
  c=[("Company dinners","Switch off from the office by the sea. Set menus so all you have to do is enjoy yourselves, bond as a team and raise a glass."),
     ("Birthdays and anniversaries","Blow out the candles with the sea as a backdrop. Personal touches and service that makes you feel at home."),
     ("Friends and family","Because you don't always need an excuse to get together. Rice dishes, fish, tapas and long, lazy afternoons at the table.")],
  how_eyebrow="How it works", how_title="From first enquiry to booking.",
  s=[("Tell us the date and how many you are","Fill in the form or message us on WhatsApp. If you know them, add the type of event and any dietary requirements."),
     ("We send menus and a tailored quote","Our team reviews your request and replies with menu proposals and a quote based on your group."),
     ("We confirm the booking","For groups of more than 8 we may ask for extra confirmation, a partial prepayment or a set menu choice. A set menu must be confirmed at least 24 hours in advance.")],
  cond_link="Read the general booking conditions",
  lead_a="Request our group dossier and get", lead_b="a welcome toast on the house.",
  lead_sub="Leave your details and we will send you our group menus with a tailored quote. And if you book your event after requesting the dossier, we treat the whole group to the first round of cava or sangria.",
  gift="Offer subject to booking confirmation and availability.",
  why_eyebrow="Why L'Àncora", why_title="Why choose L'Àncora.",
  b=[("Authentic Mediterranean cuisine","Rice dishes, fresh fish and tapas, what we have been doing for four decades."),
     ("Since 1986","Forty years of shared tables in Roses."),
     ("Right on the beach","Celebrate with the sea in front of you."),
     ("Set group menus","You choose the menu before the day, so all that is left is to enjoy it."),
     ("Private room for larger groups","Space upstairs for bigger celebrations, for the exclusive use of one group per service, subject to availability."),
     ("A personal reply","You hear back from us, by email or WhatsApp.")],
  close_title="Shall we plan your celebration?", close_sub="Tell us the date and how many you are, and we will help you build the evening.",
  close_wa="Book on WhatsApp", close_call="Call",
  wa_tip="Book via WhatsApp", wa_msg="Hello L'Àncora! I would like information about group menus.",
  f_name="Full name", f_email="Email", f_phone="Phone / WhatsApp", f_type="Event type",
  f_types=["Company","Birthday","Friends","Other"], f_date="Approximate date (optional)", f_guests="Guests (optional)",
  f_msg="Comments or allergies (optional)",
  f_priv="I have read and accept the <a href=\"%s\" target=\"_blank\" rel=\"noopener\">privacy policy</a> (available in Catalan)." % PRIVACY,
  f_mkt="I would like to receive offers and news from L'Àncora by email or WhatsApp. I can withdraw my consent at any time.",
  f_submit="Request dossier and quote",
  info=("<strong>Basic data protection information.</strong> <b>Controller:</b> Ancora Oci i Hosteleria, S.L. (NIF B55162051). "
        "<b>Purpose:</b> to handle your request for information and a group quote and, if you tick the box, to send you offers. "
        "<b>Legal basis:</b> your request and your consent. <b>Recipients:</b> we do not share your data; our web hosting and email providers act as processors. "
        "<b>Retention:</b> as long as needed to handle the request and, if applicable, the booking; for offers, until you withdraw your consent. "
        "<b>Rights:</b> access, rectification, erasure, objection, restriction and portability at info@ancoraroses.com; you may also complain to the <a href=\"%s\" target=\"_blank\" rel=\"noopener\">Spanish data protection authority (AEPD)</a>. "
        "More information in the <a href=\"%s\" target=\"_blank\" rel=\"noopener\">privacy policy</a>.") % (AEPD, PRIVACY),
  m_ok="Thank you! We have received your request. We will reply with the menus and a tailored quote.",
  m_ng="Your request could not be sent. Please try again or message us on WhatsApp at %s." % PHONE_TXT,
  m_val="Some fields need checking. Please review them and try again.", m_req="This field is required.",
  m_terms="You must accept the privacy policy to send the request.",
  m_email="Enter a valid email address.", m_tel="Enter a valid phone number.",
  mail_subject="[Groups EN] {name} · {type} · {guests} p.",
  mail_head="New group dossier request (web, language: EN)",
  lab=dict(name="Name",email="Email",phone="Phone",type="Event",date="Date",guests="Guests",msg="Comments",priv="Privacy consent",mkt="Offers (marketing consent)",page="Page",sent="Sent"),
  ar_subject="We have received your request · L'Àncora",
  ar_body=("Hello {name},\n\nThank you for your interest in celebrating with us. We have received your request for group menus.\n"
           "Our team will review it and reply with menu proposals and a tailored quote.\n\n"
           "If you prefer, you can also message us on WhatsApp at %s.\n\n"
           "The L'Àncora team\nAvinguda de Rhode 62 · 17480 Roses\n\n--\n"
           "Data controller: Ancora Oci i Hosteleria, S.L. You can exercise your rights by writing to info@ancoraroses.com. More information: %s") % (PHONE_TXT, PRIVACY),
),
"de": dict(
  locale="de_DE", slug="gruppen-und-feiern", title="Gruppen und Feiern",
  meta="Gruppenmenüs, Firmenessen, Geburtstage und Feiern im L'Àncora, direkt am Strand von Roses (Costa Brava). Dossier anfordern und ein individuelles Angebot erhalten.",
  eyebrow="Feiern und Gruppen in Roses",
  h1a="Wo mediterraner Geschmack auf", h1b="unvergessliche Feiern trifft.",
  sub="Gruppenmenüs, Firmenessen und private Veranstaltungen. Reisgerichte, Fisch und Tapas direkt am Strand, mit einem Team, das auf jedes Detail achtet.",
  cta1="Gruppendossier anfordern", cta2="Schreiben Sie uns per WhatsApp",
  tr1="Seit 1986", tr2="Direkt am Strand", tr3="Über 1.000 Google-Bewertungen",
  occ_eyebrow="Für jeden Anlass", occ_title="Wir schaffen den passenden Rahmen für jeden Anlass.",
  c=[("Firmenessen","Schalten Sie am Meer vom Büro ab. Feste Menüs, damit Sie nur genießen, als Team zusammenwachsen und anstoßen müssen."),
     ("Geburtstage und Jubiläen","Pusten Sie die Kerzen aus, mit dem Meer im Hintergrund. Persönliche Details und ein Service, bei dem Sie sich wie zu Hause fühlen."),
     ("Freunde und Familie","Denn man braucht nicht immer einen Grund, um zusammenzukommen. Reisgerichte, Fisch, Tapas und lange Gespräche nach dem Essen.")],
  how_eyebrow="So funktioniert es", how_title="Von der ersten Anfrage bis zur Reservierung.",
  s=[("Nennen Sie uns Datum und Personenzahl","Füllen Sie das Formular aus oder schreiben Sie uns per WhatsApp. Wenn möglich, geben Sie die Art der Feier und Unverträglichkeiten an."),
     ("Wir senden Menüs und ein individuelles Angebot","Unser Team prüft Ihre Anfrage und antwortet mit Menüvorschlägen und einem Angebot passend zu Ihrer Gruppe."),
     ("Wir bestätigen die Reservierung","Bei Gruppen über 8 Personen können wir eine zusätzliche Bestätigung, eine Teilvorauszahlung oder die Wahl eines festen Menüs verlangen. Ein festes Menü muss mindestens 24 Stunden vorher bestätigt werden.")],
  cond_link="Allgemeine Reservierungsbedingungen ansehen",
  lead_a="Fordern Sie unser Gruppendossier an und erhalten Sie", lead_b="einen Begrüßungsschluck aufs Haus.",
  lead_sub="Hinterlassen Sie Ihre Daten und wir senden Ihnen unsere Gruppenmenüs mit einem individuellen Angebot. Und wenn Sie Ihre Feier nach der Anfrage des Dossiers buchen, laden wir die ganze Gruppe auf die erste Runde Cava oder Sangria ein.",
  gift="Angebot vorbehaltlich der Reservierungsbestätigung und der Verfügbarkeit.",
  why_eyebrow="Warum L'Àncora", why_title="Warum L'Àncora.",
  b=[("Authentische mediterrane Küche","Reisgerichte, frischer Fisch und Tapas, das machen wir seit vier Jahrzehnten."),
     ("Seit 1986","Vierzig Jahre gemeinsame Tische in Roses."),
     ("Direkt am Strand","Feiern Sie mit dem Meer vor Augen."),
     ("Feste Gruppenmenüs","Sie wählen das Menü vor dem Tag aus und müssen nur noch genießen."),
     ("Privater Raum für größere Gruppen","Platz im Obergeschoss für größere Feiern, zur exklusiven Nutzung durch eine Gruppe pro Service und nach Verfügbarkeit."),
     ("Persönliche Antwort","Sie hören direkt von uns, per E-Mail oder WhatsApp.")],
  close_title="Planen wir Ihre Feier?", close_sub="Nennen Sie uns Datum und Personenzahl, wir helfen Ihnen, den Abend zu gestalten.",
  close_wa="Per WhatsApp reservieren", close_call="Rufen Sie an:",
  wa_tip="Per WhatsApp reservieren", wa_msg="Hallo L'Àncora! Ich hätte gern Informationen zu Gruppenmenüs.",
  f_name="Vor- und Nachname", f_email="E-Mail", f_phone="Telefon / WhatsApp", f_type="Art der Veranstaltung",
  f_types=["Firma","Geburtstag","Freunde","Sonstiges"], f_date="Ungefähres Datum (optional)", f_guests="Personen (optional)",
  f_msg="Anmerkungen oder Allergien (optional)",
  f_priv="Ich habe die <a href=\"%s\" target=\"_blank\" rel=\"noopener\">Datenschutzerklärung</a> gelesen und akzeptiere sie (auf Katalanisch verfügbar)." % PRIVACY,
  f_mkt="Ich möchte Angebote und Neuigkeiten von L'Àncora per E-Mail oder WhatsApp erhalten. Ich kann meine Einwilligung jederzeit widerrufen.",
  f_submit="Dossier und Angebot anfordern",
  info=("<strong>Grundlegende Informationen zum Datenschutz.</strong> <b>Verantwortlicher:</b> Ancora Oci i Hosteleria, S.L. (NIF B55162051). "
        "<b>Zweck:</b> Bearbeitung Ihrer Anfrage nach Informationen und einem Gruppenangebot und, wenn Sie das Kästchen ankreuzen, Zusendung von Angeboten. "
        "<b>Rechtsgrundlage:</b> Ihre Anfrage und Ihre Einwilligung. <b>Empfänger:</b> Wir geben keine Daten weiter; unser Webhosting- und E-Mail-Anbieter handelt als Auftragsverarbeiter. "
        "<b>Speicherdauer:</b> so lange, wie für die Bearbeitung der Anfrage und gegebenenfalls der Reservierung nötig; bei Angeboten bis zum Widerruf Ihrer Einwilligung. "
        "<b>Rechte:</b> Auskunft, Berichtigung, Löschung, Widerspruch, Einschränkung und Übertragbarkeit unter info@ancoraroses.com; Beschwerde bei der spanischen Datenschutzbehörde (<a href=\"%s\" target=\"_blank\" rel=\"noopener\">AEPD</a>). "
        "Weitere Informationen in der <a href=\"%s\" target=\"_blank\" rel=\"noopener\">Datenschutzerklärung</a>.") % (AEPD, PRIVACY),
  m_ok="Vielen Dank! Wir haben Ihre Anfrage erhalten. Wir antworten mit den Menüs und einem individuellen Angebot.",
  m_ng="Die Anfrage konnte nicht gesendet werden. Versuchen Sie es erneut oder schreiben Sie uns per WhatsApp an %s." % PHONE_TXT,
  m_val="Einige Felder müssen überprüft werden. Bitte prüfen Sie diese und versuchen Sie es erneut.", m_req="Dieses Feld ist erforderlich.",
  m_terms="Sie müssen die Datenschutzerklärung akzeptieren, um die Anfrage zu senden.",
  m_email="Geben Sie eine gültige E-Mail-Adresse ein.", m_tel="Geben Sie eine gültige Telefonnummer ein.",
  mail_subject="[Gruppen DE] {name} · {type} · {guests} P.",
  mail_head="Neue Anfrage für das Gruppendossier (Web, Sprache: DE)",
  lab=dict(name="Name",email="E-Mail",phone="Telefon",type="Veranstaltung",date="Datum",guests="Personen",msg="Anmerkungen",priv="Datenschutz-Einwilligung",mkt="Angebote (Marketing-Einwilligung)",page="Seite",sent="Gesendet"),
  ar_subject="Wir haben Ihre Anfrage erhalten · L'Àncora",
  ar_body=("Hallo {name},\n\nvielen Dank für Ihr Interesse, bei uns zu feiern. Wir haben Ihre Anfrage für Gruppenmenüs erhalten.\n"
           "Unser Team prüft sie und antwortet mit Menüvorschlägen und einem individuellen Angebot.\n\n"
           "Wenn Sie möchten, können Sie uns auch per WhatsApp unter %s schreiben.\n\n"
           "Das Team von L'Àncora\nAvinguda de Rhode 62 · 17480 Roses\n\n--\n"
           "Verantwortlicher: Ancora Oci i Hosteleria, S.L. Ihre Rechte können Sie per E-Mail an info@ancoraroses.com ausüben. Weitere Informationen: %s") % (PHONE_TXT, PRIVACY),
),
}

ICONS = {
 "company": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M3 13h18"/>',
 "cake": '<path d="M4 20h16M5 20v-6h14v6M5 14c2 0 2-2 3.5-2s2 2 3.5 2 2-2 3.500-2 1.500 2 3.500 2M12 12V9M12 6.500c.8-.9.8-1.700 0-2.700-.8 1-.8 1.800 0 2.700z"/>',
 "friends": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.300 2.700-6 6-6s6 2.700 6 6"/><circle cx="17" cy="9" r="2.500"/><path d="M16 14.200c2.900.3 5 2.600 5 5.800"/>',
 "fork": '<path d="M7 3v7a2 2 0 0 0 2 2v9M7 3v5M10.500 3v5M17 3c-2 2-2.500 5-2.500 8H17v10"/>',
 "forty": '<circle cx="12" cy="12" r="9"/><path d="M8 8v4h3M11 8v8M14.500 8h2.500v8h-2.500z"/>',
 "wave": '<path d="M2 9c3-4 5-4 8 0s5 4 8 0 3-3 4-2M2 16c3-4 5-4 8 0s5 4 8 0 3-3 4-2"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 15h3"/>',
 "room": '<path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4V5z"/>',
}
def icon(name):
    return '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % ICONS[name]

STYLE = """
<style>
/* L'Àncora · Grups i celebracions. Integrat al disseny del web: Poppins, blau #05273d, crema #F4ECE2, botons pastilla, fotografia a sang. */
.ag{--navy:#05273d;--gold:#F4ECE2;--gold-d:#4F6272;--sand:#F7F2EA;--paper:#FFFFFF;--ink:#05273d;--soft:#4A5560;--line:#E6DFD3;--wa:#146F3A;font-family:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);line-height:1.65;font-size:16px;text-align:left}
.ag *,.ag *::before,.ag *::after{box-sizing:border-box}
.ag a{color:inherit}
.ag .ag-in{max-width:1120px;margin:0 auto;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
.ag .ag-eyebrow{margin:0 0 10px!important;font-size:12.5px!important;font-weight:500!important;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-d)!important}
.ag h1.ag-h1,.ag h2.ag-h2,.ag h3.ag-h3{font-family:inherit!important;color:var(--ink)!important;margin:0!important;line-height:1.14!important;text-transform:none!important;letter-spacing:-.01em;text-wrap:balance}
.ag h2.ag-h2{font-size:clamp(26px,4.2vw,40px)!important;font-weight:500!important}
.ag h3.ag-h3{font-size:19px!important;font-weight:500!important;line-height:1.3!important}
.ag p{font-size:16px;line-height:1.65;margin:0}
.ag .ag-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:48px;padding:13px 26px;border-radius:999px;font:500 15.5px/1.2 Poppins,system-ui,sans-serif;text-decoration:none!important;cursor:pointer;border:1.5px solid var(--navy);transition:background .2s,transform .2s,color .2s}
.ag .ag-btn:focus-visible{outline:3px solid #fff;outline-offset:3px;box-shadow:0 0 0 6px var(--navy)}
.ag .ag-btn.gold{background:var(--gold);border-color:var(--gold);color:var(--navy)!important}
.ag .ag-btn.gold:hover{background:#fff;transform:translateY(-1px)}
.ag .ag-btn.wa{background:var(--wa);border-color:var(--wa);color:#fff!important}
.ag .ag-btn.wa:hover{background:#0F5C2E;transform:translateY(-1px)}
.ag .ag-btn.line{background:transparent;color:#fff!important;border-color:rgba(255,255,255,.7)}
.ag .ag-btn.line:hover{background:rgba(255,255,255,.12)}
.ag .ag-btn.dark{background:transparent;color:var(--navy)!important;border-color:var(--navy)}
.ag .ag-btn.dark:hover{background:var(--navy);color:#fff!important}
/* portada */
.ag-hero{position:relative;color:#fff;background:linear-gradient(180deg,rgba(5,39,61,.72),rgba(5,39,61,.60) 55%,rgba(5,39,61,.86)),url(__HERO__) center/cover no-repeat,var(--navy);overflow:hidden}
.ag-hero .ag-in{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:40px;align-items:center;padding-top:72px;padding-bottom:72px}
.ag-hero .ag-eyebrow{color:#F4ECE2!important}
.ag-hero h1.ag-h1{color:#F4ECE2!important;font-size:clamp(30px,5.2vw,52px)!important;font-weight:500!important}
.ag-hero h1.ag-h1 span{display:block;color:#fff!important}
.ag-hero .ag-sub{margin-top:18px;max-width:58ch;font-size:clamp(16px,2vw,19px);color:#F1EADB}
.ag-hero .ag-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.ag-hero .ag-trust{display:flex;flex-wrap:wrap;gap:8px 26px;margin:28px 0 0;padding:0;list-style:none;font-size:14px;color:#E9E0CE}
.ag-hero .ag-trust li{display:flex;align-items:center;gap:8px}
.ag-hero .ag-trust li::before{content:"";width:6px;height:6px;border-radius:50%;background:#F4ECE2}
.ag-hero .ag-seal{width:110px;height:110px;border-radius:50%;background:rgba(255,255,255,.12);border:1px solid rgba(244,236,226,.35);color:#F4ECE2;display:flex;align-items:center;justify-content:center}
.ag-hero .ag-seal svg{width:54px;height:54px}
.ag-wave{display:block;width:100%;height:auto;color:#F4ECE2;opacity:.45}
/* ocasiones */
.ag-sec{padding:76px 0}
.ag-sec.sand{background:var(--sand)}
.ag-head{max-width:680px;margin-bottom:38px}
.ag-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr));gap:22px}
.ag-card{position:relative;background:var(--navy);color:#F4ECE2;border-radius:24px;padding:32px 28px 30px;overflow:hidden;min-width:0}
.ag-card .ic{width:48px;height:48px;border-radius:50%;background:rgba(244,236,226,.12);color:#F4ECE2;display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.ag-card h3.ag-h3{color:#fff!important;margin-bottom:10px!important}
.ag-card p{color:#DCE3E8;font-size:15.5px}
/* pasos */
.ag-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr));gap:22px;list-style:none;margin:0;padding:0}
.ag-step{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:26px 24px;min-width:0}
.ag-step b{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:var(--navy);color:#F4ECE2;font-size:15px;font-weight:500;margin-bottom:14px}
.ag-step h3.ag-h3{margin-bottom:8px!important}
.ag-step p{color:var(--soft);font-size:15px}
.ag-note{margin-top:22px!important;font-size:14.5px!important}
.ag-note a{font-weight:600;color:var(--navy);text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--navy)}
/* banda de formulario */
.ag-lead-copy{color:#F4ECE2}
.ag-lead-copy h2.ag-h2{color:#fff!important}
.ag-lead-copy h2.ag-h2 span{display:block;color:#fff!important}
.ag-lead-copy .ag-eyebrow{color:#F4ECE2!important}
.ag-lead-copy p{color:#DCE3E8;margin-top:18px;max-width:50ch}
.ag-lead-copy .ag-gift{margin-top:20px;display:flex;gap:12px;align-items:flex-start;background:rgba(255,255,255,.08);border:1px solid rgba(244,236,226,.4);border-radius:16px;padding:14px 16px;font-size:14.5px;color:#F4ECE2}
.ag-lead-copy .ag-gift svg{flex:none;color:#F4ECE2;margin-top:2px}
.ag-lead .wpcf7,.ag-lead .wpcf7 *{box-sizing:border-box}
.ag-lead .wpcf7-form{background:#fff;color:var(--navy);border-radius:24px;padding:30px 28px;font-family:Poppins,system-ui,sans-serif}
.ag-lead .wpcf7-form p{margin:0 0 16px!important;font-size:14.5px!important;line-height:1.5}
.ag-lead .wpcf7-form label{display:block;font-size:13.5px;font-weight:600;color:var(--navy)}
.ag-lead .wpcf7-form input[type=text],.ag-lead .wpcf7-form input[type=email],.ag-lead .wpcf7-form input[type=tel],.ag-lead .wpcf7-form input[type=date],.ag-lead .wpcf7-form input[type=number],.ag-lead .wpcf7-form select,.ag-lead .wpcf7-form textarea{width:100%!important;margin-top:6px;padding:12px 14px!important;font:400 16px/1.4 Poppins,system-ui,sans-serif!important;color:var(--navy)!important;background:#fff!important;border:1.5px solid #C9BFA9!important;border-radius:12px!important;box-shadow:none!important;height:auto}
.ag-lead .wpcf7-form textarea{min-height:92px}
.ag-lead .wpcf7-form input:focus-visible,.ag-lead .wpcf7-form select:focus-visible,.ag-lead .wpcf7-form textarea:focus-visible{outline:3px solid #7FA3BC;outline-offset:1px;border-color:var(--navy)!important}
.ag-lead .ag-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,170px),1fr));gap:0 16px}
.ag-lead .wpcf7-acceptance .wpcf7-list-item{margin:0}
.ag-lead .wpcf7-acceptance label{display:flex;gap:12px;align-items:flex-start;font-weight:400;font-size:14px;line-height:1.5}
.ag-lead .wpcf7-acceptance input{flex:none;width:20px!important;height:20px;margin:2px 0 0!important;accent-color:var(--navy)}
.ag-lead .wpcf7-acceptance a{font-weight:600;text-decoration:underline;text-underline-offset:3px}
.ag-lead .ag-info{font-size:12.5px!important;line-height:1.55!important;color:#4D586B;background:var(--sand);border-radius:12px;padding:12px 14px}
.ag-lead .ag-info a{text-decoration:underline;text-underline-offset:2px;font-weight:600}
.ag-lead .wpcf7-submit{display:block;width:100%;min-height:50px;border:0!important;border-radius:999px!important;background:var(--navy)!important;color:#F4ECE2!important;font:500 16px/1.2 Poppins,system-ui,sans-serif!important;padding:14px 24px!important;cursor:pointer;transition:background .2s}
.ag-lead .wpcf7-submit:hover{background:#0B3A58!important}
.ag-lead .wpcf7-not-valid-tip{font-size:13px;color:#A32A1E;margin-top:4px}
.ag-lead .wpcf7-response-output{margin:16px 0 0!important;padding:12px 14px!important;border-radius:12px;font-size:14.5px;color:var(--navy)}
.ag-lead .wpcf7 form.sent .wpcf7-response-output{border:2px solid #3F7A3A!important;background:#EAF4E6}
.ag-lead .wpcf7 form.invalid .wpcf7-response-output,.ag-lead .wpcf7 form.failed .wpcf7-response-output,.ag-lead .wpcf7 form.unaccepted .wpcf7-response-output{border:2px solid #A32A1E!important;background:#FBEAE7}
/* ventajas */
.ag-ben{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:26px 40px;list-style:none;margin:0;padding:0}
.ag-ben li{display:flex;gap:16px;align-items:flex-start;min-width:0}
.ag-ben .ic{flex:none;width:50px;height:50px;border-radius:50%;background:var(--navy);color:#F4ECE2;display:flex;align-items:center;justify-content:center}
.ag-ben h3.ag-h3{margin-bottom:4px!important;font-size:17px!important}
.ag-ben p{color:var(--soft);font-size:15px}
/* cierre */
.ag-close{background:var(--sand);text-align:center}
.ag-close .ag-in{display:flex;flex-direction:column;align-items:center;gap:16px}
.ag-close p{max-width:52ch;color:var(--soft)}
.ag-close .ag-cta{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:8px}
.ag-close .ag-tel{font-size:15px;color:var(--navy)}
.ag-close .ag-tel a{font-weight:600;text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--navy)}
/* whatsapp flotante */
.ag-wa{position:fixed;z-index:9990;right:calc(16px + env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));display:flex;align-items:center;gap:10px;text-decoration:none!important}
.ag-wa .tip{background:#fff;color:var(--navy);font:600 13.5px/1.2 Poppins,system-ui,sans-serif;padding:9px 14px;border-radius:999px;box-shadow:0 6px 18px rgba(0,0,0,.18);border:1px solid var(--line)}
.ag-wa .dot{width:60px;height:60px;border-radius:50%;background:var(--wa);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 22px rgba(0,0,0,.3);animation:agbob 2.6s ease-in-out infinite}
.ag-wa .dot svg{width:30px;height:30px}
.ag-wa:focus-visible .dot{outline:3px solid var(--navy);outline-offset:3px}
@keyframes agbob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@media (max-width:820px){
 .ag-hero .ag-in{grid-template-columns:minmax(0,1fr);gap:24px;padding-top:44px;padding-bottom:52px}
 .ag-hero .ag-seal{width:112px;height:112px;order:-1}
 .ag-sec{padding:54px 0}
}
@media (max-width:440px){.ag-wa .tip{display:none}.ag-lead .wpcf7-form{padding:24px 18px}}
@media (prefers-reduced-motion:reduce){.ag-wa .dot{animation:none}.ag .ag-btn{transition:none}}
</style>
""".replace("__HERO__", HERO)

WAVE = '<svg class="ag-wave" viewBox="0 0 1200 40" preserveAspectRatio="none" aria-hidden="true"><path d="M0 22c50-18 100-18 150 0s100 18 150 0 100-18 150 0 100 18 150 0 100-18 150 0 100 18 150 0 100-18 150 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.6-5.4A8.4 8.4 0 1 1 21 11.5Z"/><path d="M9 8.8c.3 2.6 2.7 5.2 6 6l1.2-1.3-2-1-.9.7c-.9-.4-1.7-1.200-2.200-2.200l.7-.9-1-2Z" fill="currentColor" stroke="none"/></svg>'
GLASS = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 3h10l-1 7a4 4 0 0 1-8 0L7 3zM12 14v7M8 21h8"/></svg>'

def e(s):
    return html.escape(s, quote=False)

def top(L):
    t = T[L]
    cards = "".join(
        '<article class="ag-card"><div class="ic">%s</div><h3 class="ag-h3">%s</h3><p>%s</p></article>' % (icon(ic), e(h), e(p))
        for ic, (h, p) in zip(["company", "cake", "friends"], t["c"]))
    steps = "".join(
        '<li class="ag-step"><b>%d</b><h3 class="ag-h3">%s</h3><p>%s</p></li>' % (i + 1, e(h), e(p))
        for i, (h, p) in enumerate(t["s"]))
    return ('<div class="ag" lang="%s">' % L + STYLE +
      '<section class="ag-hero" aria-labelledby="ag-h1"><div class="ag-in"><div>'
      '<p class="ag-eyebrow">%s</p><h1 class="ag-h1" id="ag-h1">%s <span>%s</span></h1><p class="ag-sub">%s</p>'
      '<div class="ag-cta"><a class="ag-btn gold" href="#dossier">%s</a><a class="ag-btn line" href="%s?text=%s" target="_blank" rel="noopener">%s</a></div>'
      '<ul class="ag-trust"><li>%s</li><li>%s</li><li>%s</li></ul></div>'
      '<div class="ag-seal" aria-hidden="true">%s</div></div>%s</section>'
      % (e(t["eyebrow"]), e(t["h1a"]), e(t["h1b"]), e(t["sub"]), e(t["cta1"]), WA, __import__("urllib.parse").parse.quote(t["wa_msg"]), e(t["cta2"]),
         e(t["tr1"]), e(t["tr2"]), e(t["tr3"]), icon("wave").replace('width="24" height="24"','width="54" height="54"'), WAVE) +
      '<section class="ag-sec" aria-labelledby="ag-occ"><div class="ag-in"><div class="ag-head"><p class="ag-eyebrow">%s</p><h2 class="ag-h2" id="ag-occ">%s</h2></div><div class="ag-cards">%s</div></div></section>'
      % (e(t["occ_eyebrow"]), e(t["occ_title"]), cards) +
      '<section class="ag-sec sand" aria-labelledby="ag-how"><div class="ag-in"><div class="ag-head"><p class="ag-eyebrow">%s</p><h2 class="ag-h2" id="ag-how">%s</h2></div><ol class="ag-steps">%s</ol>'
      '<p class="ag-note"><a href="%s" target="_blank" rel="noopener">%s</a></p></div></section></div>'
      % (e(t["how_eyebrow"]), e(t["how_title"]), steps, CONDITIONS, e(t["cond_link"])))

def lead(L):
    t = T[L]
    return ('<div class="ag ag-lead-copy" lang="%s" id="dossier"><p class="ag-eyebrow">%s</p><h2 class="ag-h2">%s <span>%s</span></h2><p>%s</p>'
            '<div class="ag-gift">%s<span>%s</span></div></div>'
            % (L, e(t["eyebrow"]), e(t["lead_a"]), e(t["lead_b"]), e(t["lead_sub"]), GLASS, e(t["gift"])))

def bottom(L):
    t = T[L]
    items = "".join(
        '<li><div class="ic">%s</div><div><h3 class="ag-h3">%s</h3><p>%s</p></div></li>' % (icon(ic), e(h), e(p))
        for ic, (h, p) in zip(["fork", "forty", "wave", "calendar", "room", "chat"], t["b"]))
    ld = {
      "@context": "https://schema.org", "@type": "Restaurant", "name": "L'Àncora Bar Restaurant",
      "url": "https://ancoraroses.com/", "telephone": "+34972256386", "foundingDate": "1986",
      "servesCuisine": ["Mediterranean", "Seafood", "Rice dishes", "Tapas"], "acceptsReservations": True,
      "address": {"@type": "PostalAddress", "streetAddress": "Avinguda de Rhode 62", "postalCode": "17480",
                  "addressLocality": "Roses", "addressRegion": "Girona", "addressCountry": "ES"},
      "sameAs": ["https://www.instagram.com/ancoraroses/", "https://www.facebook.com/ancoraroses/"],
    }
    return ('<div class="ag" lang="%s">' % L + STYLE.split("</style>")[0].split("<style>")[0] +
      '<section class="ag-sec" aria-labelledby="ag-why"><div class="ag-in"><div class="ag-head"><p class="ag-eyebrow">%s</p><h2 class="ag-h2" id="ag-why">%s</h2></div><ul class="ag-ben">%s</ul></div></section>'
      % (e(t["why_eyebrow"]), e(t["why_title"]), items) +
      '<section class="ag-sec ag-close"><div class="ag-in"><img src="%s" width="96" height="96" alt="L\'Àncora 1986 – 2026" loading="lazy" decoding="async"><h2 class="ag-h2">%s</h2><p>%s</p><div class="ag-cta"><a class="ag-btn wa" href="%s?text=%s" target="_blank" rel="noopener">%s</a>'
      '<a class="ag-btn dark" href="#dossier">%s</a></div><p class="ag-tel">%s <a href="tel:+34972256386">%s</a> · Avinguda de Rhode 62, 17480 Roses</p></div></section>'
      % (SEAL, e(t["close_title"]), e(t["close_sub"]), WA, __import__("urllib.parse").parse.quote(t["wa_msg"]), e(t["close_wa"]), e(t["cta1"]), e(t["close_call"]), PHONE_TXT) +
      '<a class="ag-wa" href="%s?text=%s" target="_blank" rel="noopener" aria-label="%s"><span class="tip">%s</span><span class="dot">%s</span></a>'
      % (WA, __import__("urllib.parse").parse.quote(t["wa_msg"]), e(t["wa_tip"]), e(t["wa_tip"]), WA_SVG) +
      '<script type="application/ld+json">%s</script></div>' % json.dumps(ld, ensure_ascii=False))

def form(L):
    t = T[L]
    types = " ".join('"%s"' % x for x in t["f_types"])
    labs = t["lab"]
    markup = (
      '<p><label>{name}*<br>[text* your-name autocomplete:name maxlength:80]</label></p>\n'
      '<p><label>{email}*<br>[email* your-email autocomplete:email maxlength:120]</label></p>\n'
      '<p><label>{phone}*<br>[tel* your-phone autocomplete:tel maxlength:30]</label></p>\n'
      '<p><label>{type}<br>[select event-type {types}]</label></p>\n'
      '<div class="ag-row"><p><label>{date}<br>[date event-date]</label></p><p><label>{guests}<br>[number guests min:2 max:300]</label></p></div>\n'
      '<p><label>{msg}<br>[textarea your-message x4 maxlength:600]</label></p>\n'
      '<p>[acceptance consent-privacy]{priv}[/acceptance]</p>\n'
      '<p>[acceptance consent-marketing optional]{mkt}[/acceptance]</p>\n'
      '<p class="ag-info">{info}</p>\n'
      '[submit "{submit}"]'
    ).format(name=t["f_name"], email=t["f_email"], phone=t["f_phone"], type=t["f_type"], types=types, date=t["f_date"],
             guests=t["f_guests"], msg=t["f_msg"], priv=t["f_priv"], mkt=t["f_mkt"], info=t["info"], submit=t["f_submit"])
    body = (t["mail_head"] + "\n\n" +
      "%s: [your-name]\n%s: [your-email]\n%s: [your-phone]\n%s: [event-type]\n%s: [event-date]\n%s: [guests]\n%s: [your-message]\n\n" % (
        labs["name"], labs["email"], labs["phone"], labs["type"], labs["date"], labs["guests"], labs["msg"]) +
      "%s: [consent-privacy]\n%s: [consent-marketing]\n(1 = sí / buit = no)\n\n%s: [_url]\n%s: [_date] [_time]\n" % (
        labs["priv"], labs["mkt"], labs["page"], labs["sent"]))
    subj = t["mail_subject"].replace("{name}", "[your-name]").replace("{type}", "[event-type]").replace("{guests}", "[guests]")
    return {
      "title": "Grups i celebracions - Sol·licitud (%s)" % L.upper(),
      "locale": t["locale"],
      "properties": {
        "form": markup,
        "mail": {"active": True, "subject": subj, "sender": "L'Àncora Web <wordpress@ancoraroses.com>",
                 "recipient": "info@ancoraroses.com", "body": body, "additional_headers": "Reply-To: [your-email]",
                 "attachments": "", "use_html": False, "exclude_blank": True},
        "mail_2": {"active": True, "subject": t["ar_subject"], "sender": "L'Àncora <wordpress@ancoraroses.com>",
                   "recipient": "[your-email]", "body": t["ar_body"].replace("{name}", "[your-name]"),
                   "additional_headers": "Reply-To: info@ancoraroses.com", "attachments": "", "use_html": False, "exclude_blank": True},
        "messages": {"mail_sent_ok": t["m_ok"], "mail_sent_ng": t["m_ng"], "validation_error": t["m_val"], "spam": t["m_ng"],
                     "accept_terms": t["m_terms"], "invalid_required": t["m_req"], "invalid_too_long": t["m_val"], "invalid_too_short": t["m_val"],
                     "invalid_email": t["m_email"], "invalid_tel": t["m_tel"], "invalid_number": t["m_val"], "invalid_date": t["m_val"],
                     "upload_failed": t["m_ng"]},
        "additional_settings": "",
      },
    }

forms, pages = {}, {}
for L in LANGS:
    open(os.path.join(OUT, "%s-top.html" % L), "w", encoding="utf-8").write(top(L))
    open(os.path.join(OUT, "%s-lead.html" % L), "w", encoding="utf-8").write(lead(L))
    open(os.path.join(OUT, "%s-bottom.html" % L), "w", encoding="utf-8").write(bottom(L))
    forms[L] = form(L)
    pages[L] = {"title": T[L]["title"], "slug": T[L]["slug"], "meta": T[L]["meta"]}
json.dump(forms, open(os.path.join(OUT, "forms.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(pages, open(os.path.join(OUT, "pages.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", {L: os.path.getsize(os.path.join(OUT, "%s-top.html" % L)) for L in LANGS})
