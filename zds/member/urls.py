from django.contrib.auth.views import LogoutView
from django.urls import re_path, path

from zds.member.views import MemberList
from zds.member.views.profile import (
    UpdateMember,
    UpdateGitHubToken,
    remove_github_token,
    UpdateAvatarMember,
    UpdatePasswordMember,
    UpdateUsernameEmailMember,
    redirect_old_profile_to_new,
)
from zds.member.views.moderation import (
    modify_karma,
    settings_mini_profile,
    member_from_ip,
    modify_profile,
)
from zds.member.views.login import LoginView
from zds.member.views.hats import (
    HatsSettings,
    RequestedHatsList,
    HatRequestDetail,
    add_hat,
    remove_hat,
    solve_hat_request,
    HatsList,
    HatDetail,
    SolvedHatRequestsList,
)
from zds.member.views.emailproviders import (
    BannedEmailProvidersList,
    NewEmailProvidersList,
    AddBannedEmailProvider,
    remove_banned_email_provider,
    check_new_email_provider,
    MembersWithProviderList,
)
from zds.member.views.register import (
    RegisterView,
    SendValidationEmailView,
    unregister,
    warning_unregister,
    activate_account,
    generate_token_account,
)
from zds.member.views.password_recovery import forgot_password, new_password
from zds.member.views.admin import settings_promote
from zds.member.views.reports import CreateProfileReportView, SolveProfileReportView


urlpatterns = [
    # list
    re_path(r"^$", MemberList.as_view(), name="member-list"),
    # details
    path("voir/<str:user_name>/", redirect_old_profile_to_new, name="member-detail-redirect"),
    # modification
    re_path(r"^parametres/profil/$", UpdateMember.as_view(), name="update-member"),
    re_path(r"^parametres/github/$", UpdateGitHubToken.as_view(), name="update-github"),
    re_path(r"^parametres/github/supprimer/$", remove_github_token, name="remove-github"),
    re_path(r"^parametres/profil/maj_avatar/$", UpdateAvatarMember.as_view(), name="update-avatar-member"),
    re_path(r"^parametres/compte/$", UpdatePasswordMember.as_view(), name="update-password-member"),
    re_path(r"^parametres/user/$", UpdateUsernameEmailMember.as_view(), name="update-username-email-member"),
    # moderation
    re_path(r"^profil/signaler/(?P<profile_pk>\d+)/$", CreateProfileReportView.as_view(), name="report-profile"),
    re_path(r"^profil/resoudre/(?P<alert_pk>\d+)/$", SolveProfileReportView.as_view(), name="solve-profile-alert"),
    re_path(r"^profil/karmatiser/$", modify_karma, name="member-modify-karma"),
    re_path(r"^profil/modifier/(?P<user_pk>\d+)/$", modify_profile, name="member-modify-profile"),
    re_path(r"^parametres/mini_profil/(?P<user_name>.+)/$", settings_mini_profile, name="member-settings-mini-profile"),
    re_path(r"^profil/multi/(?P<ip_address>.+)/$", member_from_ip, name="member-from-ip"),
    # email providers
    re_path(r"^fournisseurs-email/nouveaux/$", NewEmailProvidersList.as_view(), name="new-email-providers"),
    re_path(
        r"^fournisseurs-email/nouveaux/verifier/(?P<provider_pk>\d+)/$",
        check_new_email_provider,
        name="check-new-email-provider",
    ),
    re_path(r"^fournisseurs-email/bannis/$", BannedEmailProvidersList.as_view(), name="banned-email-providers"),
    re_path(
        r"^fournisseurs-email/bannis/ajouter/$", AddBannedEmailProvider.as_view(), name="add-banned-email-provider"
    ),
    re_path(
        r"^fournisseurs-email/bannis/rechercher/(?P<provider_pk>\d+)/$",
        MembersWithProviderList.as_view(),
        name="members-with-provider",
    ),
    re_path(
        r"^fournisseurs-email/bannis/supprimer/(?P<provider_pk>\d+)/$",
        remove_banned_email_provider,
        name="remove-banned-email-provider",
    ),
    # user rights
    re_path(r"^profil/promouvoir/(?P<user_pk>\d+)/$", settings_promote, name="member-settings-promote"),
    # hats
    re_path(r"^casquettes/$", HatsList.as_view(), name="hats-list"),
    re_path(r"^casquettes/(?P<pk>\d+)/$", HatDetail.as_view(), name="hat-detail"),
    re_path(r"^parametres/casquettes/$", HatsSettings.as_view(), name="hats-settings"),
    re_path(r"^casquettes/demandes/$", RequestedHatsList.as_view(), name="requested-hats"),
    re_path(r"^casquettes/demandes/archives/$", SolvedHatRequestsList.as_view(), name="solved-hat-requests"),
    re_path(r"^casquettes/demandes/(?P<pk>\d+)/$", HatRequestDetail.as_view(), name="hat-request"),
    re_path(r"^casquettes/demandes/(?P<request_pk>\d+)/resoudre/$", solve_hat_request, name="solve-hat-request"),
    re_path(r"^casquettes/ajouter/(?P<user_pk>\d+)/$", add_hat, name="add-hat"),
    re_path(r"^casquettes/retirer/(?P<user_pk>\d+)/(?P<hat_pk>\d+)/$", remove_hat, name="remove-hat"),
    # membership
    re_path(r"^connexion/$", LoginView.as_view(), name="member-login"),
    re_path(r"^deconnexion/$", LogoutView.as_view(), name="member-logout"),
    re_path(r"^inscription/$", RegisterView.as_view(), name="register-member"),
    re_path(r"^reinitialisation/$", forgot_password, name="member-forgot-password"),
    re_path(r"^validation/$", SendValidationEmailView.as_view(), name="send-validation-email"),
    re_path(r"^new_password/$", new_password, name="member-new-password"),
    re_path(r"^activation/$", activate_account, name="member-active-account"),
    re_path(r"^envoi_jeton/$", generate_token_account, name="member-generate-token-account"),
    re_path(r"^desinscrire/valider/$", unregister, name="member-unregister"),
    re_path(r"^desinscrire/avertissement/$", warning_unregister, name="member-warning-unregister"),
]
