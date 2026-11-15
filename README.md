Végh Bence, VS117G, visszajelzés alapján a program teljesen átalakításra került.
Az új program egy 6 bútorból álló előre meghatározott méretű listából iterálhatunk bútorokat, majd a szoba méretét és a kívánt szabad hely százalékát kiválasztva kiszámolja, elférnek-e a bútorok a szobában

Az indítás a main.py file futtatásával történik, nem szükséges telepíteni semmi egyebet

a sajat_modul_VB.py fileban találhatóak a bútor főosztály és ennek az útód-osztályai, ezenfelül minden olyan függvény amely a szoba- a bútorok és a szellősséget felelősek kiszámolni itt találhatóak 

a main.py tartalmazza a grafikai felület definiálását és itt történik a bútorok példányosítása is, egy grid segítségével a bútorok fel vannak sorolva, a felhasználó itt képes megadni, hogy melyik és mennyi bútor lesz a szobában
a program ezután bekéri a szoba méretét méterben megadva, majd egy csúszka vezérlővel azt is megkérdezi mekkora legyen a szabad padló hely %-ban
Ha a felhasználó mindent helyesen megadott, akkor a a program alján található "Elfér-e? Számítás" gombra kattintva a program kiírja a számítás eredményét, amelyben megjeleníti a szabad padló-felületet, a tényleges szellőséget, és a beállított elvárt szellőséget
illetve felsorolja, melyik bútorból mennyi szerepel a szobában
