from conecta_dbs import ConectaPostgre as CP

conectaPost = CP()
conecta = conectaPost.connect_bd()

if conecta:
    
    conectaPost.encerra_connect()
