from abc import (
    ABCMeta, abstractmethod
)


class SSOSessionCookieInterface(metaclass=ABCMeta):

    # Stages of session
    SSO_SESSION_STAGE_NOT_INITIALIZED = 0

    SSO_SESSION_STAGE_LOGIN_STARTED = 1

    SSO_SESSION_STAGE_PROVIDER_CHOSE = 2

    SSO_SESSION_STAGE_PROVIDER_EXECUTION = 3

    SSO_SESSION_STAGE_LOGGED_IN = 4

    @classmethod
    @abstractmethod
    def deserialize(cls, s, key_retrieval_func):
        pass

    @classmethod
    @abstractmethod
    def serialize(cls, cookie, keyid, key_retrieval_func):
        pass

    @classmethod
    @abstractmethod
    def get_key_id(cls, s):
        pass

    @property
    @abstractmethod
    def tenant_id(self):
        pass

    @tenant_id.setter
    @abstractmethod
    def tenant_id(self, tid):
        pass

    # User id getter and setter
    @property
    @abstractmethod
    def user_id(self):
        pass

    @user_id.setter
    @abstractmethod
    def user_id(self, uid):
        pass

    @property
    @abstractmethod
    def provider_id(self):
        pass

    @provider_id.setter
    @abstractmethod
    def provider_id(self, pid):
        pass

    @property
    @abstractmethod
    def user_data_pointer(self):
        pass

    @user_data_pointer.setter
    @abstractmethod
    def user_data_pointer(self, pointer):
        pass

    # session id getter and setter
    @property
    @abstractmethod
    def sso_session_id(self):
        pass

    @sso_session_id.setter
    @abstractmethod
    def sso_session_id(self, sid):
        pass

    # Token type getter and setter
    @property
    @abstractmethod
    def sso_session_type(self):
        pass

    @sso_session_type.setter
    @abstractmethod
    def sso_session_type(self, stp):
        pass

    @property
    @abstractmethod
    def sso_session_stage(self):
        pass

    @sso_session_stage.setter
    @abstractmethod
    def sso_session_stage(self, stg):
        pass

    @property
    @abstractmethod
    def sso_session_meta_data_pointer(self):
        pass

    @sso_session_meta_data_pointer.setter
    @abstractmethod
    def sso_session_meta_data_pointer(self, stg):
        pass

    # logout token getter and setter
    @property
    @abstractmethod
    def logout_token(self):
        pass

    @logout_token.setter
    @abstractmethod
    def logout_token(self, lt):
        pass

    # is impersonated getter and setter
    @property
    @abstractmethod
    def impersonation_info(self):
        pass

    @impersonation_info.setter
    @abstractmethod
    def impersonation_info(self, info):
        pass

    @property
    @abstractmethod
    def is_impersonated(self):
        pass

    @is_impersonated.setter
    @abstractmethod
    def is_impersonated(self, v):
        pass

    @property
    @abstractmethod
    def is_web(self):
        pass

    @is_web.setter
    @abstractmethod
    def is_web(self, v):
        pass

    @property
    @abstractmethod
    def is_mobile(self):
        pass

    @is_mobile.setter
    @abstractmethod
    def is_mobile(self, v):
        pass

    @abstractmethod
    def is_initialized(self):
        pass

    @abstractmethod
    def is_choosing_provider(self):
        pass

    @abstractmethod
    def is_executing_provider(self):
        pass

    @abstractmethod
    def is_user_logged_in(self):
        pass

    @abstractmethod
    def is_login_started(self):
        pass

    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
