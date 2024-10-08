from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")
    host: str = "127.0.0.1"
    port: int = 6379


class KeycloakSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="IDP_KEYCLOAK_")
    url: str = ""
    client: str = ""
    secret: str = ""


class JaegerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="JAEGER_")
    host: str
    port: int
    enable_tracer: bool = False


class VKSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="VK_")
    client_id: str = ""
    client_secret: str = ""

    # Bad idea but works for MVP w/o UI
    redirect_uri: str = "http://localhost/api/v1/auth/vk/endpoint"
