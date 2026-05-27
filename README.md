# REST API Manajemen Data Mahasiswa Menggunakan Flask dan MySQL

## Deskripsi
Project ini merupakan REST API sederhana menggunakan Flask dan MySQL untuk mengelola data mahasiswa. API mendukung operasi CRUD (Create, Read, Update, Delete) menggunakan metode HTTP.

## Fitur
- Menampilkan seluruh data mahasiswa
- Menampilkan data mahasiswa berdasarkan NPM
- Menambahkan data mahasiswa
- Menghapus data mahasiswa
- Mengubah seluruh data mahasiswa (PUT)
- Mengubah sebagian data mahasiswa (PATCH)
- Validasi input data

## Teknologi yang Digunakan
- Python
- Flask
- MySQL
- PyMySQL
- JSON

## Struktur Database

Nama database:

```sql
mhs
```

Tabel:

```sql
CREATE TABLE mhs (
    npm VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(100),
    angkatan INT,
    prodi VARCHAR(100),
    jenis_kelamin VARCHAR(20),
    email VARCHAR(100)
);
```

## Instalasi

### 1. Clone repository

```bash
git clone https://github.com/username/nama-project.git
```

### 2. Masuk ke folder project

```bash
cd nama-project
```

### 3. Install dependency

```bash
pip install flask pymysql
```

### 4. Buat database MySQL

Import atau jalankan query:

```sql
CREATE DATABASE mhs;
```

Lalu buat tabel:

```sql
CREATE TABLE mhs (
    npm VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(100),
    angkatan INT,
    prodi VARCHAR(100),
    jenis_kelamin VARCHAR(20),
    email VARCHAR(100)
);
```

### 5. Jalankan aplikasi

```bash
python app.py
```

Server berjalan pada:

```bash
http://127.0.0.1:5000
```

---

## Endpoint API

### Menampilkan semua data

```http
GET /mhs
```

Response:

```json
[
  {
    "npm":"230001",
    "nama":"Budi",
    "angkatan":2023,
    "prodi":"Informatika",
    "jenis_kelamin":"Laki-laki",
    "email":"budi@gmail.com"
  }
]
```

---

### Menampilkan data berdasarkan NPM

```http
GET /mhs/230001
```

---

### Menambahkan data

```http
POST /mhs
```

Body:

```json
{
    "npm":"230001",
    "nama":"Budi",
    "angkatan":2023,
    "prodi":"Informatika",
    "jenis_kelamin":"Laki-laki",
    "email":"budi@gmail.com"
}
```

---

### Mengubah seluruh data

```http
PUT /mhs/230001
```

---

### Mengubah sebagian data

```http
PATCH /mhs/230001
```

Contoh:

```json
{
    "nama":"Budi Santoso",
    "email":"budibaru@gmail.com"
}
```

---

### Menghapus data

```http
DELETE /mhs/230001
```

## Catatan
- Menggunakan koneksi MySQL lokal (localhost).
- Database menggunakan PyMySQL.
- API dibuat untuk pembelajaran dasar REST API dan CRUD menggunakan Flask.
