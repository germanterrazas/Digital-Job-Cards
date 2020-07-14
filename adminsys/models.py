from django.db import models

# Create your models here.

class Cad(models.Model):
    filepath = models.CharField(max_length=100, db_column='FilePath')  # Field name made lowercase.
    cadid = models.AutoField(primary_key=True, db_column='CADID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'CAD'
    def __str__(self):
        return self.filepath


class Group(models.Model):
    groupid = models.AutoField(primary_key=True, db_column='GroupID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    name = models.CharField(max_length=100, db_column='Name')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Group'
    def __str__(self):
        return u"%s" % self.name


class Inspectedby(models.Model):
   inspectedbyid = models.AutoField(primary_key=True, db_column='InspectedByID')  # Field name made lowercase.
   inspectionid = models.ForeignKey('Inspection', models.DO_NOTHING, db_column='InspectionID')  # Field name made lowercase.
   operationid = models.ForeignKey('Operation', models.DO_NOTHING, db_column='OperationID')  # Field name made lowercase.
   class Meta:
       managed = False
       db_table = u'InspectedBy'
   def __str__(self):
       return u"Inspection: %s -- Operation: %s" % (self.inspectionid, self.operationid)


class Inspection(models.Model):
    inspectionid = models.AutoField(primary_key=True, db_column='InspectionID')  # Field name made lowercase.
    comment = models.CharField(max_length=500, db_column='Comment')  # Field name made lowercase.
    result = models.IntegerField(db_column='Result')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Inspection'
    def __str__(self):
        return u"%s" % self.comment


class Job(models.Model):
    jobid = models.AutoField(primary_key=True, db_column='JobID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    orderid = models.ForeignKey('Order', models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Job'
    def __str__(self):
        return u"%s" % self.description


class Jobcard(models.Model):
    jobcardid = models.AutoField(primary_key=True, db_column='JobCardID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    jobid = models.ForeignKey(Job, models.DO_NOTHING, db_column='JobID')  # Field name made lowercase.
    cadid = models.ForeignKey(Cad, models.DO_NOTHING, db_column='CADID')  # Field name made lowercase.
    barcode = models.CharField(max_length=500, db_column='BarCode')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'JobCard'
    def __str__(self):
        return u"%s" % self.description


class Material(models.Model):
    stockid = models.AutoField(primary_key=True, db_column='StockID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    jobcard = models.ManyToManyField(Jobcard, through='Uses')
    code = models.CharField(max_length=100, db_column='Code')  # Field name made lowercase.
    uom = models.CharField(max_length=100, db_column='UOM')  # Field name made lowercase.
    location = models.CharField(max_length=100, db_column='Location')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Material'
    def __str__(self):
        return u"%s" % self.description


class Operation(models.Model):
    operationid = models.AutoField(primary_key=True, db_column='OperationID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    number = models.CharField(max_length=100, db_column='Number')  # Field name made lowercase.
    jobcardid = models.ForeignKey(Jobcard, models.DO_NOTHING, db_column='JobCardID')  # Field name made lowercase.
    userdid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Operation'
    def __str__(self):
        return u"%s" % self.description


class Order(models.Model):
    orderid = models.AutoField(primary_key=True, db_column='OrderID')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    partnumber = models.IntegerField(db_column='PartNumber')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Order'
    def __str__(self):
        return u"%s" % self.description


class Permissions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    read = models.IntegerField(db_column='Read')  # Field name made lowercase.
    write = models.IntegerField(db_column='Write')  # Field name made lowercase.
    delete = models.IntegerField(db_column='Delete')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Permissions'


class Realisedby(models.Model):
    realisedbyid = models.AutoField(primary_key=True, db_column='RealisedByID')  # Field name made lowercase.
    start = models.DateField(db_column='Start')  # Field name made lowercase.
    end = models.DateField(db_column='End')  # Field name made lowercase.
    operationid = models.ForeignKey(Operation, models.DO_NOTHING, db_column='OperationID')  # Field name made lowercase.
    wsid = models.ForeignKey('Workstation', models.DO_NOTHING, db_column='WSID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'RealisedBy'
    def __str__(self):
        return u"Station: %s -- Operation: %s" % (self.wsid, self.operationid)


class User(models.Model):
    userid = models.AutoField(primary_key=True, db_column='UserID')  # Field name made lowercase.
    name = models.CharField(max_length=100, db_column='Name')  # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description')  # Field name made lowercase.
    groupid = models.ForeignKey("Group", models.DO_NOTHING, db_column='GroupID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'User'
    def __str__(self):
        return u"%s (%s)" % (self.name, self.groupid)


class Uses(models.Model):
    usesid = models.AutoField(primary_key=True, db_column='UsesID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase. This field type is a guess.
    jobcardid = models.ForeignKey(Jobcard, models.DO_NOTHING, db_column='JobCardID')  # Field name made lowercase.
    stockid = models.ForeignKey(Material, models.DO_NOTHING, db_column='StockID')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'Uses'
        unique_together = ('jobcardid', 'stockid')
    def __str__(self):
        return u"Job card: %s -- Material: %s" % (self.jobcardid, self.stockid)


class Workstation(models.Model):
    wsid = models.AutoField(primary_key=True, db_column='WSID')  # Field name made lowercase.
    name = models.CharField(max_length=100, db_column='Name')  # Field name made lowercase.
    location = models.CharField(max_length=100, db_column='Location')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = u'WorkStation'
    def __str__(self):
        return u"%s" % self.name




#class Material(models.Model):
#	Description = models.CharField(max_length=500)
#
#	def __str__(self):
#		return self.Description