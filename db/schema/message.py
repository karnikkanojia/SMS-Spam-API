from mongoengine import StringField, IntField, Document, ValidationError

class SpamMessage(Document):
    message = StringField(required=True)
    label = IntField(required=True, min_value=0, max_value=1)

    def __str__(self):
        return f"{self.message}->{self.label}"
    
    def validate(self, clean=True):
        if self.message in (None, '') or self.label is None:
            raise ValidationError("Message field can't be empty")
        return super().validate(clean)