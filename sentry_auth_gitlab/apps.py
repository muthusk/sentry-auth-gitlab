from __future__ import absolute_import

from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry_auth_gitlab"

    def ready(self):
        from sentry.auth import register

        from .provider import GitLabOAuth2Provider

        register('gitlab', GitLabOAuth2Provider)