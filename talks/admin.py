from django.contrib import admin

from talks.models import Category, AudienceSkillLevel
from talks.models import Talk, TimeSlot, Location, TalkType


admin.site.register(Talk)
admin.site.register(TimeSlot)
admin.site.register(Location)
admin.site.register(TalkType)
admin.site.register(Category)
admin.site.register(AudienceSkillLevel)
