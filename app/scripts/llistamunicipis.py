import pandas as pd
def lmunicipis():
    l=['Alella', "Ametlla del Vallès, l'", 'Arenys de Mar', 'Arenys de Munt', 'Argençola', 'Argentona', 'Avinyonet del Penedès', 'Aiguafreda', 'Badalona', 'Badalona', 'Badalona', 'Badalona', 'Badalona', 'Badalona', 'Badalona', 'Badalona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Begues', 'Berga', 'Bigues i Riells', 'Brull, el', 'Cabrera de Mar', 'Cabrils', 'Caldes de Montbui', 'Calella', 'Calldetenes', 'Campins', 'Canet de Mar', 'Canovelles', 'Cànoves i Samalús', 'Canyelles', 'Cardedeu', 'Cardona', 'Castellar del Vallès', 'Castellbisbal', 'Castellcir', 'Castelldefels', 'Castellet i la Gornal', 'Castellnou de Bages', 'Castellterçol', 'Castellví de la Marca', 'Castellví de Rosanes', 'Centelles', 'Cervelló', 'Cervelló', 'Collbató', 'Corbera de Llobregat', 'Cornellà de Llobregat', 'Esplugues de Llobregat', 'Fogars de Montclús', 'Folgueroles', 'Franqueses del Vallès, les', 'Garriga, la', 'Gavà', 'Gelida', 'Gironella', 'Granera', 'Granollers', 'Gurb', "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", "Hospitalet de Llobregat, l'", 'Igualada', 'Llinars del Vallès', "Lliçà d'Amunt", 'Lliçà de Vall', 'Lluçà', 'Malgrat de Mar', 'Malla', 'Manlleu', 'Manresa', 'Martorelles', 'Masnou, el', 'Matadepera', 'Mataró', 'Mataró', 'Mataró', 'Mataró', 'Molins de Rei', 'Mollet del Vallès', 'Montcada i Reixac', 'Montgat', 'Montesquiu', 'Montmaneu', 'Montseny', 'Moià', 'Òdena', 'Olesa de Montserrat', 'Olivella', 'Olost', 'Pacs del Penedès', 'Palau-solità i Plegamans', 'Pallejà', 'Papiol, el', 'Parets del Vallès', 'Perafita', 'Piera', 'Pineda de Mar', 'Prat de Llobregat, el', 'Premià de Mar', 'Pujalt', 'Ripollet', 'Roca del Vallès, la', 'Rubí', 'Sabadell', 'Sabadell', 'Sabadell', 'Sabadell', 'Sabadell', 'Sabadell', 'Sabadell', 'Sallent', 'Santpedor', 'Sant Iscle de Vallalta', 'Sant Adrià de Besòs', 'Sant Agustí de Lluçanès', 'Sant Andreu de la Barca', 'Sant Andreu de Llavaneres', 'Sant Antoni de Vilamajor', 'Sant Bartomeu del Grau', 'Sant Boi de Llobregat', 'Sant Boi de Lluçanès', 'Sant Celoni', 'Sant Climent de Llobregat', 'Sant Cugat del Vallès', 'Sant Cugat del Vallès', 'Sant Cugat del Vallès', 'Sant Cugat del Vallès', 'Sant Cugat del Vallès', 'Sant Cugat Sesgarrigues', 'Sant Esteve de Palautordera', 'Sant Esteve Sesrovires', 'Sant Fost de Campsentelles', 'Sant Feliu de Codines', 'Sant Feliu de Llobregat', 'Sant Fruitós de Bages', 'Vilassar de Dalt', 'Sant Hipòlit de Voltregà', 'Sant Joan Despí', 'Vilassar de Mar', 'Sant Julià de Vilatorta', 'Sant Just Desvern', 'Sant Martí Sarroca', 'Sant Martí Sesgueioles', 'Premià de Dalt', 'Sant Pere de Ribes', 'Sant Pere de Riudebitlles', 'Sant Pere de Torelló', 'Sant Pere de Vilamajor', 'Sant Pol de Mar', 'Sant Quintí de Mediona', 'Sant Quirze del Vallès', 'Sant Quirze Safaja', "Sant Sadurní d'Anoia", "Sant Sadurní d'Osormort", 'Santa Coloma de Cervelló', 'Santa Coloma de Gramenet', 'Santa Coloma de Gramenet', 'Santa Coloma de Gramenet', 'Santa Coloma de Gramenet', 'Santa Eugènia de Berga', 'Santa Eulàlia de Ronçana', 'Santa Maria de Besora', 'Santa Maria de Palautordera', 'Santa Perpètua de Mogoda', 'Santa Susanna', 'Sant Vicenç dels Horts', 'Sant Vicenç de Montalt', 'Sant Vicenç de Torelló', 'Cerdanyola del Vallès', 'Cerdanyola del Vallès', 'Seva', 'Sitges', 'Sitges', 'Sobremunt', 'Sora', 'Subirats', 'Súria', 'Tavèrnoles', 'Taradell', 'Terrassa', 'Terrassa', 'Teià', 'Tiana', 'Tona', 'Tordera', 'Torelló', 'Torrelles de Llobregat', 'Vallgorguina', 'Vallirana', 'Vallromanes', 'Vic', 'Viladecans', 'Vilanova de Sau', 'Vilafranca del Penedès', 'Vilanova i la Geltrú', 'Palma de Cervelló, la', "Far d'Empordà, el", 'Anglès', 'Arbúcies', 'Avinyonet de Puigventós', 'Banyoles', "Bisbal d'Empordà, la", 'Blanes', 'Breda', 'Camós', 'Campdevànol', 'Campelles', 'Queralbs', 'Cassà de la Selva', 'Siurana', "Escala, l'", 'Figueres', 'Fontanilles', 'Fornells de la Selva', 'Fortià', 'Girona', 'Girona', 'Girona', 'Girona', 'Girona', 'Girona', 'Gualta', 'Llívia', 'Lloret de Mar', 'Maçanet de la Selva', 'Navata', 'Olot', 'Ordis', 'Palafrugell', 'Palamós', 'Pardines', 'Pau', 'Porqueres', 'Puigcerdà', 'Quart', 'Ribes de Freser', 'Ripoll', 'Riumors', 'Roses', 'Sant Joan de les Abadesses', "Santa Cristina d'Aro", 'Sant Joan les Fonts', "Tallada d'Empordà, la", 'Torroella de Montgrí', 'Torroella de Montgrí', 'Tossa de Mar', "Vall d'en Bas, la", 'Vilablareix', 'Viladrau', 'Vilamalla', "Cruïlles, Monells i Sant Sadurní de l'Heura", 'Forallac', 'Agramunt', 'Alguaire', 'Almacelles', 'Alpicat', 'Arbeca', 'Artesa de Segre', 'Sentiu de Sió, la', 'Aitona', 'Balaguer', 'Borges Blanques, les', 'Castellserà', 'Cervera', 'Cervera', 'Estaràs', 'Golmés', 'Gósol', 'Guissona', 'Guixers', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Lleida', 'Linyola', 'Navès', 'Odèn', 'Oliana', 'Olius', 'Olius', 'Oluges, les', 'Conca de Dalt', 'Penelles', 'Peramola', 'Pinell de Solsonès', 'Pobla de Segur, la', 'Ponts', 'Pont de Suert, el', 'Rosselló', 'Sant Llorenç de Morunys', "Seu d'Urgell, la", 'Sidamon', 'Solsona', 'Sort', 'Sudanell', 'Talavera', 'Tàrrega', 'Torrefarrera', 'Torres de Segre', 'Tremp', 'Vallfogona de Balaguer', 'Vielha e Mijaran', 'Albinyana', 'Alcanar', 'Alió', 'Altafulla', 'Amposta', 'Ascó', 'Benissanet', 'Borges del Camp, les', 'Calafell', 'Calafell', 'Cambrils', 'Castellvell del Camp', 'Cunit', 'Fatarella, la', 'Flix', 'Horta de Sant Joan', 'Masdenverge', 'Miravet', 'Montblanc', 'Montbrió del Camp', 'Mont-roig del Camp', "Móra d'Ebre", 'Reus', 'Reus', 'Reus', 'Reus', 'Reus', 'Reus', 'Riudoms', 'Santa Coloma de Queralt', 'Tarragona', 'Tarragona', 'Tarragona', 'Tarragona', 'Tarragona', 'Tarragona', 'Tarragona', 'Tivissa', 'Tortosa', 'Tortosa', 'Tortosa', 'Ulldecona', 'Valls', 'Valls', "Vandellòs i l'Hospitalet de l'Infant", 'Vendrell, el', 'Vila-seca', 'Vimbodí i Poblet', 'Vinyols i els Arcs', 'Deltebre', 'Salou']
    l2=set(l)
    l3=list(l2)
    return l3