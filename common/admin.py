from django.contrib import admin

from common.models import StartsWithIAMModel, SkillModel, PortfolioImagesModel, PortfolioModel, SocialModel, MainModel, \
    ContactModel

admin.site.register(StartsWithIAMModel)
admin.site.register(SkillModel)
admin.site.register(PortfolioImagesModel)
admin.site.register(PortfolioModel)
admin.site.register(SocialModel)
admin.site.register(MainModel)
admin.site.register(ContactModel)