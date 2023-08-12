from datetime import datetime

class Configurations:
    allow_unprivileged_device_configuration: bool
    allow_unprivileged_device_management: bool
    default_client_allowed_ips: list
    default_client_dns: list
    default_client_endpoint: str
    default_client_mtu: int
    default_client_persistent_keepalive: int
    disable_vpn_on_oidc_error: bool
    id: str
    inserted_at: datetime
    local_auth_enabled: bool
    logo: dict
    openid_connect_providers: list
    saml_identity_providers: list
    updated_at: datetime
    vpn_session_duration: int

    @staticmethod
    def __init_from_dict__(data: dict) -> 'Configurations':
        configurations = Configurations()
        configurations.__dict__.update(data)
        return configurations
    
    @staticmethod
    def get(client, *args, **kwargs) -> 'Configurations':
        return Configurations.__init_from_dict__(client.__get__("/configuration")["data"])

    def patch(self, client):
        data = {
            "configuration": {
                "allow_unprivileged_device_configuration": self.allow_unprivileged_device_configuration,
                "allow_unprivileged_device_management": self.allow_unprivileged_device_management,
                "default_client_allowed_ips": self.default_client_allowed_ips,
                "default_client_dns": self.default_client_dns,
                "default_client_endpoint": self.default_client_endpoint,
                "default_client_mtu": self.default_client_mtu,
                "default_client_persistent_keepalive": self.default_client_persistent_keepalive,
                "disable_vpn_on_oidc_error": self.disable_vpn_on_oidc_error,
                "local_auth_enabled": self.local_auth_enabled,
                "openid_connect_providers": self.openid_connect_providers,
                "saml_identity_providers": self.saml_identity_providers,
                "vpn_session_duration": self.vpn_session_duration
            }
        }
        client.__patch__("/configuration", data)
