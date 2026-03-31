import urllib.request
import time
import threading

URL = "http://localhost:5000/"
NB_REQUETES = 100
NB_CONCURRENT = 10

resultats = []
lock = threading.Lock()

def faire_requete():
    try:
        debut = time.time()
        urllib.request.urlopen(URL)
        fin = time.time()
        with lock:
            resultats.append(fin - debut)
    except Exception as e:
        print(f"Erreur: {e}")

print(f"Test de charge : {NB_REQUETES} requêtes, {NB_CONCURRENT} simultanées")
debut_total = time.time()

threads = []
for i in range(NB_REQUETES):
    t = threading.Thread(target=faire_requete)
    threads.append(t)
    t.start()
    if len(threads) % NB_CONCURRENT == 0:
        for th in threads:
            th.join()
        threads = []

fin_total = time.time()
duree_totale = fin_total - debut_total

print(f"\n=== RÉSULTATS ===")
print(f"Requests/sec : {round(NB_REQUETES / duree_totale, 2)}")
print(f"Average      : {round(sum(resultats) / len(resultats), 4)} secs")
print(f"Fastest      : {round(min(resultats), 4)} secs")
print(f"Slowest      : {round(max(resultats), 4)} secs")
