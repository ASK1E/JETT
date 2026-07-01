# JETT - Job Explore Top Talent

Platform job portal berbasis web yang menghubungkan pencari kerja dengan perusahaan. JETT memfasilitasi seluruh proses rekrutmen secara online mulai dari pendaftaran, pencarian lowongan, hingga melamar pekerjaan.

---

## Tim Pengembang

| Nama | NIM |
|------|-----|
| Syafiq Adi Kurniawan | 4332401013 |
| Syahdan Arief S | 4332401006 |
| Muhammad Reza Pahlevi | 4332401020 |
| Helena Yolanda Amelia | 4332401027 |

**Mata Kuliah:** PBL RKS 321

---

## Fitur Utama

### Job Seeker
- Registrasi dan verifikasi email
- Kelengkapan profil dengan data terenkripsi
- Pencarian dan filter lowongan kerja
- Melamar pekerjaan secara online
- Melacak status lamaran

### Company
- Registrasi perusahaan
- Manajemen profil perusahaan
- Pembuatan dan pengelolaan lowongan kerja
- Melihat daftar pelamar

### Keamanan
- Multi-Factor Authentication (TOTP)
- Enkripsi data sensitif (alamat, nomor telepon, tanggal lahir)
- Rate limiting untuk mencegah brute force
- Email verification wajib
- Password reset dengan token kedaluwarsa

---

## Teknologi

### Backend
- **Django 5+** - Web framework
- **Python 3.10+** - Bahasa pemrograman
- **MySQL 8** - Database
- **Docker** - Containerization

### Frontend
- **HTML5 / CSS3 / JavaScript**

### Libraries
- `django-axes` - Rate limiting dan account lockout
- `cryptography` - Enkripsi data sensitif
- `pyotp` - TOTP-based MFA
- `qrcode` - QR code generation untuk MFA
- `Pillow` - Image processing
- `PyMySQL` - MySQL driver

---

## Distribusi Kode

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│    ████████████████████████████████████████  CSS (38.0%)            │
│    ██████████████████████████████████  Python (33.2%)               │
│    ████████████████████████  HTML (25.2%)                           │
│    ███  JavaScript (3.6%)                                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Total: 6.687 baris kode
```

| Bahasa | Baris Kode | Persentase |
|--------|-----------|------------|
| CSS | 2.541 | 38.0% |
| Python | 2.219 | 33.2% |
| HTML | 1.684 | 25.2% |
| JavaScript | 243 | 3.6% |

---

## Struktur Proyek

```
jett/
├── accounts/          # Autentikasi, profil user, MFA
├── applications/      # Sistem lamaran kerja
├── jobs/              # Manajemen lowongan
├── landing/           # Halaman utama
├── jett/              # Konfigurasi Django
├── static/            # File statis global
├── templates/         # Template base dan error pages
├── logs/              # Log aplikasi
└── media/             # Upload user (logo perusahaan)
```

---

## Instalasi dan Menjalankan

### Prasyarat
- Python 3.10+
- Docker dan Docker Compose
- pip

### Langkah Instalasi

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd jett
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan MySQL dengan Docker**
   ```bash
   docker compose up -d
   ```

5. **Verifikasi container berjalan**
   ```bash
   docker ps
   ```

6. **Lakukan migrasi database**
   ```bash
   python manage.py migrate
   ```

7. **Jalankan server**
   ```bash
   python manage.py runserver
   ```

8. **Akses aplikasi**
   Buka browser dan navigasi ke `http://127.0.0.1:8000`

---

## Konfigurasi Environment

Buat file `.env` di root proyek dengan format:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=jett
DB_USER=jett_user
DB_PASSWORD=jett_password
DB_HOST=localhost
DB_PORT=3306

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

---

## Keamanan Data

JETT mengimplementasikan standar keamanan berikut:

| Fitur | Deskripsi |
|-------|-----------|
| Enkripsi Field | Data sensitif dienkripsi menggunakan Fernet symmetric encryption |
| Password Hashing | Menggunakan PBKDF2 dengan SHA256 |
| Rate Limiting | Memblokir akun setelah 5x percobaan gagal dalam 1 jam |
| MFA | TOTP-based 2FA menggunakan aplikasi authenticator |
| Token Expiry | Token verifikasi dan reset password memiliki masa berlaku terbatas |
| Session Security | Session cookies dengan pengaturan secure dan age limit |

---

## Lisensi

Proyek ini dikembangkan untuk keperluan akademik mata kuliah PBL RKS 321.
