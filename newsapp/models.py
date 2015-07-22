from django.db import models
import time

class Country(models.Model):
    country_code=models.CharField(max_length=5,blank=True)
    country_name=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return str(self.country_name)    
    class Meta:
        managed=True
        #app_label='newsapp'

CAT_CHOICES=(
        ("GN","General"),
        ("ENT","Entertainment"),
        ("SPT","Sport"),
        ("FSN","Fashion"),
        ("S&T","Science and Technology")
        )
class Website(models.Model):
    
    #site_num=models.IntegerField(default=0)
    #site_ID=models.CharField(max_length=100,default=str(time.time()))
    site_name=models.CharField(max_length=100,blank=True)
    site_url=models.CharField(max_length=100,blank=True)
    category=models.CharField(max_length=50,choices=CAT_CHOICES,default="GN")
    country=models.ForeignKey(Country)

    def __str__(self):
        return str(self.site_name)

    class Meta:
        managed=True
        #app_label='newsapp'

    #def save(self, *args,**kwargs):
        #self.site_num=website.objects.count()+1
        #self.site_ID=str(self.site_num)+"_"+self.site_name+"_"+self.country_id
        
        #super(website,self).save(*args,**kwargs)




class Channel(models.Model):
    MORE_CAT_CHOICES=CAT_CHOICES+(
        ("WH","Weather"),
        ("CY","Currency"),
        ("ST","Stock"),
        ("Bus","Business"),
        ("FN","Financial"),
        ("LC","Local News"),
        ("WN","World News"),
        ("MC","Miscellaneous"),
        )
    channel_title=models.CharField(max_length=200,blank=True)
    feed_url=models.URLField()
    site=models.ForeignKey(Website)
    country=models.ForeignKey(Country)
    category=models.CharField(max_length=50,choices=MORE_CAT_CHOICES)

    def __str__(self):
        return str(self.feed_url)

    #def save(self, *args,**kwargs):
        
    #    self.channel_id=str(self.category)+"_"+str(self.site_id)
        
#        super(Channel,self).save(*args,**kwargs)


class Post(models.Model):
    #post_id=models.CharField(max_length=100,primary_key=True,default=str(time.time()))
    pub_date=models.DateField()
    title=models.CharField(max_length=200)
    summary=models.TextField()
    content=models.TextField()
    thumbnail=models.URLField()
    feed_url=models.ForeignKey(Channel)
    post_url=models.URLField(blank=True)
    site=models.CharField(max_length=200,blank=True)

    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        self.site=self.feed_url.site.site_name
        return super().save(force_insert, force_update, using, update_fields)