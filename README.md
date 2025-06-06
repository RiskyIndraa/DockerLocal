# Testing Docker Lokal Data Siswa

Ini adalah project mini untuk testing Docker container aplikasi data siswa di local sebelum push ke cloud.

## Langkah

1. Build image  
   `docker build -t data-siswa-app .`

2. Run container  
   `docker run -p 5000:5000 data-siswa-app`

3. Cek aplikasi di `http://localhost:5000`

4. Debug jika perlu dengan `docker ps`, `docker logs`, `docker stop`

5. Tag image sebelum push  
   `docker tag data-siswa-app:latest <username>/data-siswa-app:latest`
