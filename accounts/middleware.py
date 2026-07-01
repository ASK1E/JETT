from django.shortcuts import redirect
from django.urls import reverse


# URL yang diizinkan diakses meskipun profil belum lengkap
EXEMPT_URLS = [
    "/accounts/mfa/setup/",
    "/accounts/mfa/verify/",
    "/accounts/mfa/disable/",
    "/accounts/logout/",
    "/accounts/delete/",
    "/accounts/seeker/profile/setup/",
    "/accounts/company/profile/setup/",
    "/static/",
    "/media/",
]


def _is_seeker_profile_complete(user):
    """
    Cek apakah profil seeker sudah lengkap.
    Semua field wajib diisi.
    """
    try:
        profile = user.seeker_profile
        return all([
            profile.date_of_birth,
            profile.address,
            profile.phone,
            profile.education,
        ])
    except Exception:
        return False


def _is_company_profile_complete(user):
    """
    Cek apakah profil company sudah lengkap.
    Semua field wajib diisi.
    """
    try:
        profile = user.company_profile
        return all([
            profile.owner_name,
            profile.address,
            profile.phone,
            profile.industry,
            profile.description,
        ])
    except Exception:
        return False


class ProfileCompletionMiddleware:
    """
    Middleware yang memaksa user melengkapi profil
    sebelum bisa mengakses halaman manapun.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip kalau user belum login
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Skip untuk URL yang dikecualikan
        path = request.path
        for exempt in EXEMPT_URLS:
            if path.startswith(exempt):
                return self.get_response(request)

        # Cek profil sesuai role
        if request.user.role == "seeker":
            setup_url = reverse("accounts:seeker_profile_setup")
            if path == setup_url:
                return self.get_response(request)
            if not _is_seeker_profile_complete(request.user):
                return redirect("accounts:seeker_profile_setup")

        elif request.user.role == "company":
            setup_url = reverse("accounts:company_profile_setup")
            if path == setup_url:
                return self.get_response(request)
            if not _is_company_profile_complete(request.user):
                return redirect("accounts:company_profile_setup")

        return self.get_response(request)