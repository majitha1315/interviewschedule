from rest_framework import serializers


from API.models import User, InterviewSlot


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
class UserSerializer(serializers.ModelSerializer):

    candidate = serializers.BooleanField(source='is_candidate')
    interviewer = serializers.BooleanField(source='is_interviewer')

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'candidate', 'interviewer')


class InterviewSlotSerializer(serializers.ModelSerializer):
    slot = ChoiceField(choices=InterviewSlot.SLOT_CHOICES)
    class Meta:
        model = InterviewSlot
        fields = ('id', 'date', 'slot')

    class Meta:
        model = InterviewSlot
        fields = ('id', 'date', 'slot')

    def create(self, validated_data):


        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)