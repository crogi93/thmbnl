import django
import jsonschema

from django.core.validators import BaseValidator


class JSONSchemaValidator(BaseValidator):
    def compare(self, value, schema):
        try:
            jsonschema.validate(value, schema)
        except jsonschema.exceptions.ValidationError:
            raise django.core.exceptions.ValidationError(
                '%(value)s failed JSON schema check', params={'value': value}
            )
