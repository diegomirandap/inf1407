from django.db import models
class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name made
    mpg = models.FloatField(db_column='MPG') # Field name made
    acyl = models.IntegerField(db_column='CYL') # Field name made
    disp = models.FloatField(db_column='DISP') # Field name made
    hp = models.IntegerField(db_column='HP') # Field name made
    wt = models.FloatField(db_column='WT') # Field name made
    qsec = models.FloatField(db_column='QSEC') # Field name made
    vs = models.IntegerField(db_column='VS') # Field name made
    am = models.IntegerField(db_column='AM') # Field name made
    gear = models.IntegerField(db_column='GEAR') # Field name made
    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']
    def __str__(self):
        return self.name
